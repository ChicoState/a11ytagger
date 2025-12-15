import io
from types import SimpleNamespace

import server.accessibility.extractor as extractor


def test_get_metadata_returns_title_and_language():
    pdf = SimpleNamespace()
    pdf.Root = SimpleNamespace(get=lambda k: "en" if k == "/Lang" else None)
    pdf.docinfo = {"/Title": "My Title"}

    md = extractor.get_metadata(pdf)
    assert md.get("language") == "en"
    assert md.get("title") == "My Title"


def test_extract_all_images_and_get_image_by_id(monkeypatch, tmp_path):
    # Create fake PIL-like object
    class FakePil:
        def __init__(self):
            self.width = 10
            self.height = 20
            self.format = "PNG"

        def save(self, buffer, format=None):
            buffer.write(b"PNGDATA")

    # Fake PdfImage wrapper
    class FakePdfImage:
        def __init__(self, raw):
            self.raw = raw

        def as_pil_image(self):
            return FakePil()

    # Fake raw image object
    class RawImg:
        Subtype = "/Image"

    # Fake page with images mapping
    page = SimpleNamespace(images={"Im1": RawImg()})

    class FakePdf:
        def __init__(self):
            self.pages = [page]

        def close(self):
            pass

    monkeypatch.setattr(extractor.pikepdf.Pdf, "open", lambda p: FakePdf(), raising=False)
    monkeypatch.setattr(extractor.pikepdf, "PdfImage", FakePdfImage, raising=False)

    images = extractor.extract_all_images("dummy.pdf")
    assert len(images) == 1
    img = images[0]
    assert img["page_number"] == 1
    assert img["width"] == 10
    assert img["height"] == 20

    # get_image_by_id uses extract_all_images internally; monkeypatch to reuse
    monkeypatch.setattr(extractor, "extract_all_images", lambda path: images)
    found = extractor.get_image_by_id("dummy.pdf", 0)
    assert found is not None and found["id"] == 0


def test_tag_image_with_alt_text_image_not_found(monkeypatch):
    # Fake pdf with no images
    class FakePdf:
        def __init__(self):
            self.pages = [SimpleNamespace(images={})]

        def close(self):
            pass

    monkeypatch.setattr(extractor.pikepdf.Pdf, "open", lambda p, allow_overwriting_input=False: FakePdf(), raising=False)

    res = extractor.tag_image_with_alt_text("dummy.pdf", 0, "alt text")
    assert res is False


def test_extract_accessibility_info_encrypted_and_password_error(monkeypatch, tmp_path):
    # Encrypted pdf early-return
    class EncryptedPdf:
        is_encrypted = True
        pdf_version = "1.7"

        def __init__(self):
            self.pages = []

        def close(self):
            pass

    f = tmp_path / "enc.pdf"
    f.write_bytes(b"x")
    monkeypatch.setattr(extractor.os.path, "getsize", lambda p: 1024)
    monkeypatch.setattr(extractor.pikepdf.Pdf, "open", lambda p: EncryptedPdf(), raising=False)

    res = extractor.extract_accessibility_info(str(f), "enc.pdf")
    assert res.is_encrypted is True
    assert any("PDF is encrypted" in e for e in res.errors)

    # PasswordError handling
    def raise_pw(path):
        raise extractor.PasswordError("pw")

    monkeypatch.setattr(extractor.pikepdf.Pdf, "open", raise_pw, raising=False)
    res2 = extractor.extract_accessibility_info(str(f), "enc.pdf")
    assert res2.is_encrypted is True
    assert any("password" in e.lower() for e in res2.errors)


def test_extract_accessibility_info_corrupt_pdf(monkeypatch, tmp_path):
    # Simulate pikepdf failing to open a corrupt PDF
    def raise_corrupt(path):
        raise Exception("corrupt pdf")

    monkeypatch.setattr(extractor.pikepdf.Pdf, "open", raise_corrupt, raising=False)
    monkeypatch.setattr(extractor.os.path, "getsize", lambda p: 1024)

    f = tmp_path / "corrupt.pdf"
    f.write_bytes(b"x")

    res = extractor.extract_accessibility_info(str(f), "corrupt.pdf")

    # ExtractionResult doesn't have can_proceed; validate via errors
    assert res.is_encrypted is False
    assert res.errors
    assert any("unexpected" in e.lower() or "error" in e.lower() or "corrupt" in e.lower() for e in res.errors)

