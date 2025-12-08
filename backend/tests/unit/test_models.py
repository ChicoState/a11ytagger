from datetime import datetime

from server.accessibility.models import (
    ImageReference,
    StructureElement,
    ExtractionResult,
)


def test_extraction_result_computes_image_counts_and_structure():
    images = [
        ImageReference(page_number=1, alt_text="An image", actual_text=None, has_alt_text=True),
        ImageReference(page_number=2, alt_text=None, actual_text=None, has_alt_text=False),
    ]

    child = StructureElement(element_type="H2", depth=1, reading_order_index=2, children=[])
    root = StructureElement(element_type="H1", depth=0, reading_order_index=1, children=[child])

    er = ExtractionResult(
        pdf_filename="doc.pdf",
        extraction_timestamp=datetime.now(),
        cache_key="k",
        expires_at=datetime.now(),
        page_count=2,
        file_size_bytes=1024,
        pdf_version="1.4",
        success=True,
        has_structure_tree=True,
        is_tagged=False,
        structure_tree=root,
        images=images,
    )

    assert er.total_images == 2
    assert er.images_with_alt_text == 1
    assert er.images_without_alt_text == 1
    assert "H1" in er.structure_types_found and "H2" in er.structure_types_found
    assert er.max_heading_level == 2
