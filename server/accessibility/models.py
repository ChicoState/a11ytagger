from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class ImageReference:
    page_number: int
    alt_text: Optional[str]
    actual_text: Optional[str]
    has_alt_text: bool
    position_x: Optional[float] = None
    position_y: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None


@dataclass
class StructureElement:
    element_type: str
    depth: int
    reading_order_index: int
    alt_text: Optional[str] = None
    actual_text: Optional[str] = None
    title: Optional[str] = None
    lang: Optional[str] = None
    children: List['StructureElement'] = field(default_factory=list)
    parent_type: Optional[str] = None


@dataclass
class ExtractionResult:
    pdf_filename: str
    extraction_timestamp: datetime
    cache_key: str
    expires_at: datetime
    page_count: int
    file_size_bytes: int
    pdf_version: str
    success: bool
    has_structure_tree: bool
    is_tagged: bool
    is_encrypted: bool = False
    timed_out: bool = False
    document_language: Optional[str] = None
    document_title: Optional[str] = None
    structure_tree: Optional[StructureElement] = None
    images: List[ImageReference] = field(default_factory=list)
    total_images: int = 0
    images_with_alt_text: int = 0
    images_without_alt_text: int = 0
    structure_types_found: List[str] = field(default_factory=list)
    max_heading_level: Optional[int] = None
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.total_images = len(self.images)
        self.images_with_alt_text = sum(1 for img in self.images if img.has_alt_text)
        self.images_without_alt_text = self.total_images - self.images_with_alt_text

        if self.structure_tree:
            self.structure_types_found = self._collect_unique_types(self.structure_tree)
            self.max_heading_level = self._find_max_heading_level(self.structure_tree)

    def _collect_unique_types(self, element: StructureElement) -> List[str]:
        types = {element.element_type}
        for child in element.children:
            types.update(self._collect_unique_types(child))
        return sorted(list(types))

    def _find_max_heading_level(self, element: StructureElement) -> Optional[int]:
        max_level = None

        if element.element_type.startswith('H'):
            try:
                level = int(element.element_type[1:]) if len(element.element_type) > 1 else 1
                max_level = level
            except ValueError:
                pass

        for child in element.children:
            child_max = self._find_max_heading_level(child)
            if child_max is not None:
                max_level = max(max_level or 0, child_max)

        return max_level


@dataclass
class ValidationResult:
    status: str
    can_proceed: bool
    file_size_bytes: int
    is_valid_pdf: bool
    is_encrypted: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
