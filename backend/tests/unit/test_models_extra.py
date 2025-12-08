from datetime import datetime
from typing import Any, Dict

from server.accessibility.models import (
    ExtractionResult,
    StructureElement,
)


def _base_er_kwargs(structure_tree=None, images=None) -> Dict[str, Any]:
    """Return a dict of keyword args suitable for ExtractionResult construction."""
    return dict(
        pdf_filename="doc.pdf",
        extraction_timestamp=datetime.now(),
        cache_key="k",
        expires_at=datetime.now(),
        page_count=0,
        file_size_bytes=0,
        pdf_version="1.4",
        success=True,
        has_structure_tree=bool(structure_tree),
        is_tagged=False,
        structure_tree=structure_tree,
        images=images or [],
    )


def test_extraction_result_no_structure_tree_defaults():
    er = ExtractionResult(**_base_er_kwargs(structure_tree=None, images=[]))
    assert er.total_images == 0
    assert er.images_with_alt_text == 0
    assert er.images_without_alt_text == 0
    assert er.structure_types_found == []
    assert er.max_heading_level is None


def test_find_max_heading_level_variants():
    # H (no number) should be treated as level 1
    child_h = StructureElement(element_type="H", depth=1, reading_order_index=1, children=[])
    # H2a should be ignored for numeric parsing
    child_h2a = StructureElement(element_type="H2a", depth=1, reading_order_index=2, children=[])
    # H3 should be detected as level 3
    child_h3 = StructureElement(element_type="H3", depth=1, reading_order_index=3, children=[])

    root = StructureElement(element_type="Root", depth=0, reading_order_index=0, children=[child_h, child_h2a, child_h3])

    er = ExtractionResult(**_base_er_kwargs(structure_tree=root, images=[]))
    assert "H" in er.structure_types_found
    assert "H2a" in er.structure_types_found
    assert "H3" in er.structure_types_found
    assert er.max_heading_level == 3