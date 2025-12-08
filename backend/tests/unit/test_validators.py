import sys
import types
import importlib.util


# Ensure a pikepdf module exists for import-time safety when tests run
if importlib.util.find_spec("pikepdf") is None:
    fake = types.SimpleNamespace()

    class _FakePdf:
        def __init__(self):
            self.is_encrypted = False

        def close(self):
            # no-op for fake
            pass

        @staticmethod
        def open(path):
            return _FakePdf()

    fake.Pdf = _FakePdf
    fake.PdfError = Exception
    fake.PasswordError = Exception
    sys.modules["pikepdf"] = fake


import os
import server.accessibility.validators as validators


def test_validate_pdf_file_small_valid(monkeypatch, tmp_path):
    f = tmp_path / "small.pdf"
    f.write_bytes(b"pdf")

    # small size
    monkeypatch.setattr(validators.os.path, "getsize", lambda p: 1024)

    class FakePdfObj:
        is_encrypted = False

        def close(self):
            # no-op for fake
            pass

    monkeypatch.setattr(validators.pikepdf.Pdf, "open", lambda p: FakePdfObj(), raising=False)

    res = validators.validate_pdf_file(str(f))
    assert res.is_valid_pdf is True
    assert res.status == validators.ValidationStatus.VALID.value


def test_validate_pdf_file_large_warns(monkeypatch, tmp_path):
    f = tmp_path / "large.pdf"
    f.write_bytes(b"x")

    # 12 MB -> warning
    monkeypatch.setattr(validators.os.path, "getsize", lambda p: 12 * 1024 * 1024)

    class FakePdfObj:
        is_encrypted = False

        def close(self):
            # no-op for fake
            pass

    monkeypatch.setattr(validators.pikepdf.Pdf, "open", lambda p: FakePdfObj(), raising=False)

    res = validators.validate_pdf_file(str(f))
    assert res.status == validators.ValidationStatus.WARNING.value
    assert any("Large file" in w for w in res.warnings)


def test_validate_pdf_file_password_error(monkeypatch, tmp_path):
    f = tmp_path / "pw.pdf"
    f.write_bytes(b"x")

    monkeypatch.setattr(validators.os.path, "getsize", lambda p: 1024)

    def raise_pw(path):
        raise validators.PasswordError("password")

    monkeypatch.setattr(validators.pikepdf.Pdf, "open", raise_pw, raising=False)

    res = validators.validate_pdf_file(str(f))
    assert res.is_encrypted is True
    assert res.status == validators.ValidationStatus.ENCRYPTED.value
    assert res.can_proceed is False


def test_validate_pdf_file_invalid_pdf(monkeypatch, tmp_path):
    f = tmp_path / "bad.pdf"
    f.write_bytes(b"x")

    monkeypatch.setattr(validators.os.path, "getsize", lambda p: 1024)

    def raise_bad(path):
        raise validators.PdfError("corrupt")

    monkeypatch.setattr(validators.pikepdf.Pdf, "open", raise_bad, raising=False)

    res = validators.validate_pdf_file(str(f))
    assert res.is_valid_pdf is False
    assert res.status == validators.ValidationStatus.INVALID.value
    assert res.can_proceed is False
