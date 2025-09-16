from dataclasses import dataclass
from logic.models.enums.entry_type import EntryType
from logic.models.enums.loci_type import LociType
from logic.models.enums.relation_type import RelationType
import uuid

# Rule: boolean
# Heuristic: non boolean
# perhaps add, RuleComposition for programming and logical convenience, e.g. intra voice mvmt of tritone or major 6th or 2nd species movement


@dataclass(frozen=True)
class Entry:
    Guid: uuid.UUID
    Text: str
    Note: str
    PageNumberFrom: int
    PageNumberTo: int
    EntryType: EntryType
    LociType: LociType
    RelationType: RelationType
