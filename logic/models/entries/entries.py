from dataclasses import dataclass
from typing import Optional
from logic.models.enums.loci_type import LociType
from logic.models.enums.relation_type import RelationType
from logic.models.enums.fux import NVoices, Species
import uuid

# Rule: boolean
# Heuristic: non boolean
# perhaps add, RuleComposition for programming and logical convenience, e.g. intra voice mvmt of tritone or major 6th or 2nd species movement


@dataclass(frozen=True)
class Text:
    Text: str
    AuthorsNote: str
    Note: str


@dataclass(frozen=True)
class PageNumbers:
    PageNumberFrom: int
    PageNumberTo: int


@dataclass(frozen=True)
class FuxDetails:
    NVoice: NVoices
    Species: Species


@dataclass(frozen=True)
class Entry:
    Guid: uuid.UUID
    FuxDetails: FuxDetails
    Text: Text
    PageNumbers: PageNumbers
    LociType: LociType


@dataclass(frozen=True)
class Fact(Entry):
    RelationType: RelationType


@dataclass(frozen=True)
class Rule(Entry):
    RelationType: RelationType


@dataclass(frozen=True)
class Heuristic(Entry):
    RelationType: Optional[RelationType]


@dataclass(frozen=True)
class Suggestion(Entry):
    RelationType: Optional[RelationType]
