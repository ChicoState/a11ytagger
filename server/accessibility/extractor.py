import signal
from contextlib import contextmanager
from datetime import datetime, timedelta

import pikepdf
from pikepdf import PdfError, PasswordError

from .models import ExtractionResult, ImageReference, StructureElement


class ExtractionTimeout(Exception):
    pass


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


@contextmanager
def timeout(seconds):
    def handler(signum, frame):
        raise ExtractionTimeout("Extraction exceeded timeout")

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


def extract_accessibility_info(pdf_path, filename, timeout_seconds=10):
    import os

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
        with timeout(timeout_seconds):
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

    except ExtractionTimeout:
        result.timed_out = True
        result.errors.append("Extraction timed out - PDF too complex for processing")

    except PasswordError:
        result.is_encrypted = True
        result.errors.append("PDF is password-protected")

    except PdfError as e:
        result.errors.append(f"PDF parsing error: {str(e)}")

    except Exception as e:
        result.errors.append(f"Unexpected error: {str(e)}")

    return result
