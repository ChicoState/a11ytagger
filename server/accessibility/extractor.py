import signal
from contextlib import contextmanager
from datetime import datetime, timedelta

import pikepdf
from pikepdf import PdfError, PasswordError

from .models import ExtractionResult, ImageReference, StructureElement


class ExtractionTimeout(Exception):
    pass


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
    result = ExtractionResult(
        pdf_filename=filename,
        extraction_timestamp=datetime.now(),
        cache_key="",
        expires_at=datetime.now() + timedelta(hours=1),
        page_count=0,
        file_size_bytes=0,
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
