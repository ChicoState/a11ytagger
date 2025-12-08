import types

import server.accessibility.validators as validators


def test_validate_pdf_file_pdf_object_is_encrypted(monkeypatch, tmp_path):
    f = tmp_path / "enc.pdf"
    f.write_bytes(b"x")

    # small size
    monkeypatch.setattr(validators.os.path, "getsize", lambda p: 1024)

    class FakePdfObj:
        is_encrypted = True

        def close(self):
            pass

    monkeypatch.setattr(validators.pikepdf.Pdf, "open", lambda p: FakePdfObj(), raising=False)

    res = validators.validate_pdf_file(str(f))
    assert res.is_encrypted is True
    assert res.status == validators.ValidationStatus.ENCRYPTED.value
    assert res.can_proceed is False
    assert any("encrypt" in e.lower() or "decrypt" in e.lower() for e in res.errors)


def test_validate_pdf_file_very_large_warns(monkeypatch, tmp_path):
    f = tmp_path / "huge.pdf"
    f.write_bytes(b"x")

    # 60 MB -> both warnings
    monkeypatch.setattr(validators.os.path, "getsize", lambda p: 60 * 1024 * 1024)

    class FakePdfObj:
        is_encrypted = False

        def close(self):
            pass

    monkeypatch.setattr(validators.pikepdf.Pdf, "open", lambda p: FakePdfObj(), raising=False)

    res = validators.validate_pdf_file(str(f))
    assert any("Very large file" in w for w in res.warnings)
    assert any("Large file" in w for w in res.warnings)
    assert res.status == validators.ValidationStatus.WARNING.value