from dataclasses import dataclass
from typing import Optional
from uuid import UUID
from logic.models.entries.entries import LociType, RelationType


@dataclass(frozen=True)
class CompositeRule:
    Logic: str
    Note: Optional[str]
    Guid: UUID
    LociType: LociType
    RelationType: RelationType
    AbstractedGuids: list[UUID]
