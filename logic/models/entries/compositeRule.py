from dataclasses import dataclass
from typing import Optional
from uuid import UUID


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
