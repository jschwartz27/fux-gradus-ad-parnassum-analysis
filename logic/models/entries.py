from dataclasses import dataclass
from logic.models.enums.entry_type import EntryType
from logic.models.enums.loci_type import LociType
from logic.models.enums.relation_type import RelationType
from logic.models.enums.fux import NVoices, Species
import uuid

# Rule: boolean
# Heuristic: non boolean
# perhaps add, RuleComposition for programming and logical convenience, e.g. intra voice mvmt of tritone or major 6th or 2nd species movement


@dataclass(frozen=True)
class Entry:
    Guid: uuid.UUID
    NVoice: NVoices
    Species: Species
    Text: str
    AuthorsNote: str
    Note: str
    PageNumberFrom: int
    PageNumberTo: int
    EntryType: EntryType
    LociType: LociType
    RelationType: RelationType
