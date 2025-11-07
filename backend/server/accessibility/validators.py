import os
from enum import Enum

import pikepdf
from pikepdf import PdfError, PasswordError

from .models import ValidationResult


class ValidationStatus(Enum):
    VALID = "valid"
    INVALID = "invalid"
    ENCRYPTED = "encrypted"
    WARNING = "warning"


def validate_pdf_file(file_path):
    result = ValidationResult(
        status=ValidationStatus.VALID.value,
        can_proceed=True,
        file_size_bytes=0,
        is_valid_pdf=False,
        is_encrypted=False
    )

    result.file_size_bytes = os.path.getsize(file_path)

    if result.file_size_bytes > 10 * 1024 * 1024:
        result.warnings.append(f"Large file ({result.file_size_bytes // 1024 // 1024}MB) may take longer")
        result.status = ValidationStatus.WARNING.value

    if result.file_size_bytes > 50 * 1024 * 1024:
        result.warnings.append("Very large file - extraction may timeout")

    try:
        pdf = pikepdf.Pdf.open(file_path)
        result.is_valid_pdf = True

        if pdf.is_encrypted:
            result.is_encrypted = True
            result.status = ValidationStatus.ENCRYPTED.value
            result.can_proceed = False
            result.errors.append("PDF is encrypted. Please decrypt before uploading.")

        pdf.close()

    except PasswordError:
        result.is_encrypted = True
        result.status = ValidationStatus.ENCRYPTED.value
        result.can_proceed = False
        result.errors.append("PDF is password-protected. Please decrypt before uploading.")

    except PdfError as e:
        result.is_valid_pdf = False
        result.status = ValidationStatus.INVALID.value
        result.can_proceed = False
        result.errors.append(f"Invalid PDF: {str(e)}")

    return result
