from dataclasses import dataclass
from typing import Optional
from uuid import UUID

# from logic.models.entries.entries import LociType, RelationType


@dataclass(frozen=True)
class CompositeText:
    Logic: str
    Note: Optional[str]


@dataclass(frozen=True)
class CompositeRule:
    Text: CompositeText
    Guid: UUID
    # LociType: LociType
    # RelationType: RelationType
    AbstractedGuids: list[UUID]
