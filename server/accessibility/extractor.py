from datetime import datetime, timedelta

import pikepdf
from pikepdf import PdfError, PasswordError

from .models import ExtractionResult, ImageReference, StructureElement


class ExtractionTimeout(Exception):
    pass


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
