from server.accessibility.extractor import (
    traverse_element,
    extract_structure_tree,
    extract_images_from_tree,
)
from server.accessibility.models import StructureElement


class FakeElem:
    def __init__(self, mapping):
        self._m = mapping

    def get(self, key):
        return self._m.get(key)


def test_traverse_element_single():
    elem = FakeElem({"/S": "H1", "/K": None, "/Alt": None, "/ActualText": None, "/T": None, "/Lang": None})
    results = traverse_element(elem, depth=0, reading_order=[0])
    assert isinstance(results, list)
    assert len(results) == 1
    se = results[0]
    assert se.element_type == "H1"
    assert se.depth == 0
    assert se.children == []


def test_extract_structure_tree_creates_root_for_multiple_children():
    child1 = FakeElem({"/S": "P", "/K": None})
    child2 = FakeElem({"/S": "P", "/K": None})
    struct_root = FakeElem({"/K": [child1, child2]})

    root = extract_structure_tree(None, struct_root)
    assert isinstance(root, StructureElement)
    assert root.element_type == "Root"
    assert len(root.children) == 2


def test_extract_images_from_tree_finds_figures():
    fig = StructureElement(element_type="Figure", depth=1, reading_order_index=1, alt_text="an alt", actual_text=None, children=[])
    other = StructureElement(element_type="P", depth=1, reading_order_index=2, children=[])
    root = StructureElement(element_type="Root", depth=0, reading_order_index=0, children=[fig, other])

    images = extract_images_from_tree(root)
    assert len(images) == 1
    img = images[0]
    assert img.has_alt_text is True
    assert img.alt_text == "an alt"
