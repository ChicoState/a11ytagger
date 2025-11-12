import os
import io
from datetime import datetime, timedelta

import pikepdf
from pikepdf import PdfError, PasswordError

from .models import ExtractionResult, ImageReference, StructureElement


def extract_structure_tree(pdf, struct_tree_root):
    if not struct_tree_root:
        return None

    children = struct_tree_root.get('/K')
    if not children:
        return None

    elements = traverse_element(children, depth=0, reading_order=[0])

    if not elements:
        return None

    if len(elements) == 1:
        return elements[0]

    root = StructureElement(
        element_type='Root',
        depth=0,
        reading_order_index=0,
        children=elements
    )
    return root


def traverse_element(elem, depth, reading_order, max_depth=20):
    if depth > max_depth:
        return []

    if isinstance(elem, list) or (hasattr(elem, '__iter__') and not hasattr(elem, 'get')):
        results = []
        for item in elem:
            results.extend(traverse_element(item, depth, reading_order, max_depth))
        return results

    if not hasattr(elem, 'get'):
        return []

    element_type = elem.get('/S')
    if not element_type:
        children = elem.get('/K')
        if children:
            return traverse_element(children, depth, reading_order, max_depth)
        return []

    reading_order[0] += 1
    current_index = reading_order[0]

    structure_elem = StructureElement(
        element_type=str(element_type),
        depth=depth,
        reading_order_index=current_index,
        alt_text=str(elem.get('/Alt')) if elem.get('/Alt') else None,
        actual_text=str(elem.get('/ActualText')) if elem.get('/ActualText') else None,
        title=str(elem.get('/T')) if elem.get('/T') else None,
        lang=str(elem.get('/Lang')) if elem.get('/Lang') else None,
        children=[]
    )

    children = elem.get('/K')
    if children:
        structure_elem.children = traverse_element(children, depth + 1, reading_order, max_depth)
        for child in structure_elem.children:
            child.parent_type = structure_elem.element_type

    return [structure_elem]


def extract_images_from_tree(structure_tree):
    if not structure_tree:
        return []

    images = []
    _collect_images_recursive(structure_tree, images, page_number=1)
    return images


def _collect_images_recursive(element, images, page_number):
    if element.element_type == 'Figure' or element.element_type == '/Figure':
        image = ImageReference(
            page_number=page_number,
            alt_text=element.alt_text,
            actual_text=element.actual_text,
            has_alt_text=bool(element.alt_text and element.alt_text.strip())
        )
        images.append(image)

    for child in element.children:
        _collect_images_recursive(child, images, page_number)


def get_metadata(pdf):
    metadata = {}

    lang = pdf.Root.get('/Lang')
    metadata['language'] = str(lang) if lang else None

    title = pdf.docinfo.get('/Title') if hasattr(pdf, 'docinfo') and pdf.docinfo else None
    metadata['title'] = str(title) if title else None

    return metadata


def extract_all_images(pdf_path):
    images = []
    
    try:
        pdf = pikepdf.Pdf.open(pdf_path)
        
        image_id = 0
        for page_num, page in enumerate(pdf.pages, start=1):
            for obj_name, obj in page.images.items():
                try:
                    raw_image = obj
                    
                    if raw_image.Subtype == '/Image':
                        pil_image = pikepdf.PdfImage(raw_image).as_pil_image()
                        
                        img_buffer = io.BytesIO()
                        pil_image.save(img_buffer, format='PNG')
                        img_data = img_buffer.getvalue()
                        
                        images.append({
                            'id': image_id,
                            'page_number': page_num,
                            'width': pil_image.width,
                            'height': pil_image.height,
                            'format': pil_image.format or 'PNG',
                            'data': img_data
                        })
                        image_id += 1
                        
                except Exception as e:
                    continue
        
        pdf.close()
        
    except Exception as e:
        pass
    
    return images


def get_image_by_id(pdf_path, image_id):
    images = extract_all_images(pdf_path)
    
    for img in images:
        if img['id'] == image_id:
            return img
    
    return None


def tag_image_with_alt_text(pdf_path, image_id, alt_text):
    import traceback
    
    try:
        print(f"[DEBUG] Opening PDF: {pdf_path}")
        pdf = pikepdf.Pdf.open(pdf_path, allow_overwriting_input=True)
        
        current_id = 0
        target_image_obj = None
        target_page = None
        target_obj_name = None
        
        print(f"[DEBUG] Searching for image with ID: {image_id}")
        for page_num, page in enumerate(pdf.pages, start=1):
            for obj_name, obj in page.images.items():
                try:
                    if obj.Subtype == '/Image':
                        if current_id == image_id:
                            target_image_obj = obj
                            target_page = page
                            target_obj_name = obj_name
                            print(f"[DEBUG] Found target image on page {page_num}, object: {obj_name}")
                            break
                        current_id += 1
                except Exception as e:
                    print(f"[DEBUG] Error checking image on page {page_num}: {e}")
                    continue
            if target_image_obj:
                break
        
        if not target_image_obj:
            print(f"[ERROR] Image with ID {image_id} not found (total images found: {current_id})")
            pdf.close()
            return False
        
        print(f"[DEBUG] Getting/creating structure tree root")
        struct_tree_root = pdf.Root.get('/StructTreeRoot')
        if not struct_tree_root:
            print(f"[DEBUG] Creating new structure tree root")
            struct_tree_root = pdf.make_indirect(pikepdf.Dictionary(
                Type=pikepdf.Name('/StructTreeRoot'),
                K=pikepdf.Array([])
            ))
            pdf.Root.StructTreeRoot = struct_tree_root
        
        if '/K' not in struct_tree_root:
            print(f"[DEBUG] Adding /K array to structure tree root")
            struct_tree_root.K = pikepdf.Array([])
        
        print(f"[DEBUG] Creating figure element with alt text: {alt_text}")
        figure_elem = pdf.make_indirect(pikepdf.Dictionary(
            Type=pikepdf.Name('/StructElem'),
            S=pikepdf.Name('/Figure'),
            P=struct_tree_root,
            Alt=alt_text
        ))
        
        print(f"[DEBUG] Adding figure element to structure tree")
        if isinstance(struct_tree_root.K, list):
            struct_tree_root.K.append(figure_elem)
        else:
            struct_tree_root.K = pikepdf.Array([struct_tree_root.K, figure_elem])
        
        print(f"[DEBUG] Setting MarkInfo")
        mark_info = pdf.Root.get('/MarkInfo')
        if not mark_info:
            pdf.Root.MarkInfo = pikepdf.Dictionary(Marked=True)
        else:
            mark_info.Marked = True
        
        print(f"[DEBUG] Saving PDF to: {pdf_path}")
        pdf.save(pdf_path)
        pdf.close()
        
        print(f"[DEBUG] Successfully tagged image {image_id}")
        return True
        
    except Exception as e:
        error_msg = f"{type(e).__name__}: {str(e)}"
        traceback_str = traceback.format_exc()
        print(f"[ERROR] Exception in tag_image_with_alt_text: {error_msg}")
        print(f"[ERROR] Traceback:\n{traceback_str}")
        return False


def extract_accessibility_info(pdf_path, filename):
    result = ExtractionResult(
        pdf_filename=filename,
        extraction_timestamp=datetime.now(),
        cache_key="",
        expires_at=datetime.now() + timedelta(hours=1),
        page_count=0,
        file_size_bytes=os.path.getsize(pdf_path),
        pdf_version="",
        success=False,
        has_structure_tree=False,
        is_tagged=False
    )

    try:
        pdf = pikepdf.Pdf.open(pdf_path)

        result.page_count = len(pdf.pages)
        result.pdf_version = pdf.pdf_version

        if pdf.is_encrypted:
            result.is_encrypted = True
            result.errors.append("PDF is encrypted")
            pdf.close()
            return result

        struct_tree_root = pdf.Root.get('/StructTreeRoot')
        result.has_structure_tree = struct_tree_root is not None

        mark_info = pdf.Root.get('/MarkInfo')
        result.is_tagged = bool(mark_info and mark_info.get('/Marked'))

        metadata = get_metadata(pdf)
        result.document_language = metadata.get('language')
        result.document_title = metadata.get('title')

        if struct_tree_root:
            try:
                result.structure_tree = extract_structure_tree(pdf, struct_tree_root)
                result.images = extract_images_from_tree(result.structure_tree)
            except Exception as e:
                result.warnings.append(f"Partial extraction - corrupted tags: {str(e)}")

        result.success = True
        pdf.close()

    except PasswordError:
        result.is_encrypted = True
        result.errors.append("PDF is password-protected")

    except PdfError as e:
        result.errors.append(f"PDF parsing error: {str(e)}")

    except Exception as e:
        result.errors.append(f"Unexpected error: {str(e)}")

    return result
