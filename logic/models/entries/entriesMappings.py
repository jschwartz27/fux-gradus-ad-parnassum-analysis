from typing import Any
from uuid import UUID
from logic.models.entries.compositeRule import CompositeRule, CompositeText
from logic.models.entries.entries import (
    AuthorsRule,
    Entry,
    Fact,
    FuxDetails,
    Heuristic,
    PageNumbers,
    Rule,
    Suggestion,
    Text,
)
from logic.models.enums.entry_type import EntryType
from logic.models.enums.fux import NVoices, Species
from logic.models.enums.loci_type import LociType
from logic.models.enums.relation_type import RelationType


class EntryRawToDataclass:

    @staticmethod
    def transformToCompositeRule(raw_entry: dict[str, Any]) -> CompositeRule:
        # return CompositeRule(
        #     Logic=raw_entry["Logic"],
        #     Note=raw_entry["Note"],
        #     Guid=UUID(raw_entry["Guid"]),
        #     LociType=LociType(raw_entry["LociType"]),
        #     RelationType=RelationType(raw_entry["RelationType"]),
        #     AbstractedGuids=list(map(lambda g: UUID(g), raw_entry["AbstractedGuids"])),
        # )
        return CompositeRule(
            Text=CompositeText(Logic=raw_entry["Logic"], Note=raw_entry["Note"]),
            Guid=UUID(raw_entry["Guid"]),
            AbstractedGuids=list(map(lambda g: UUID(g), raw_entry["AbstractedGuids"])),
        )

    @staticmethod
    def transformToEntity(raw_entry: dict[str, Any]) -> Entry:
        match EntryType(raw_entry["EntryType"]):
            case EntryType.FACT:
                return Fact(
                    Guid=raw_entry["Guid"],
                    FuxDetails=FuxDetails(
                        NVoice=NVoices(raw_entry["NVocies"]),
                        Species=Species(raw_entry["SpeciesType"]),
                    ),
                    Text=Text(
                        Text=raw_entry["Text"],
                        AuthorsNote=raw_entry["AuthorsNote"],
                        Note=raw_entry["Note"],
                    ),
                    PageNumbers=PageNumbers(
                        PageNumberFrom=raw_entry["PageNumberFrom"],
                        PageNumberTo=raw_entry["PageNumberFrom"],
                    ),
                    # LociType=LociType(raw_entry["LociType"]),
                    RelationType=RelationType(raw_entry["RelationType"]),
                )
            case EntryType.RULE:
                return Rule(
                    Guid=raw_entry["Guid"],
                    FuxDetails=FuxDetails(
                        NVoice=NVoices(raw_entry["NVocies"]),
                        Species=Species(raw_entry["SpeciesType"]),
                    ),
                    Text=Text(
                        Text=raw_entry["Text"],
                        AuthorsNote=raw_entry["AuthorsNote"],
                        Note=raw_entry["Note"],
                    ),
                    PageNumbers=PageNumbers(
                        PageNumberFrom=raw_entry["PageNumberFrom"],
                        PageNumberTo=raw_entry["PageNumberFrom"],
                    ),
                    LociType=LociType(raw_entry["LociType"]),
                    RelationType=RelationType(raw_entry["RelationType"]),
                    Logic=raw_entry["Logic"],
                )
            case EntryType.HEURISTIC:
                return Heuristic(
                    Guid=raw_entry["Guid"],
                    FuxDetails=FuxDetails(
                        NVoice=NVoices(raw_entry["NVocies"]),
                        Species=Species(raw_entry["SpeciesType"]),
                    ),
                    Text=Text(
                        Text=raw_entry["Text"],
                        AuthorsNote=raw_entry["AuthorsNote"],
                        Note=raw_entry["Note"],
                    ),
                    PageNumbers=PageNumbers(
                        PageNumberFrom=raw_entry["PageNumberFrom"],
                        PageNumberTo=raw_entry["PageNumberFrom"],
                    ),
                    LociType=LociType(raw_entry["LociType"]),
                    RelationType=RelationType(raw_entry["RelationType"]),
                )
            case EntryType.SUGGESTION:
                return Suggestion(
                    Guid=raw_entry["Guid"],
                    FuxDetails=FuxDetails(
                        NVoice=NVoices(raw_entry["NVocies"]),
                        Species=Species(raw_entry["SpeciesType"]),
                    ),
                    Text=Text(
                        Text=raw_entry["Text"],
                        AuthorsNote=raw_entry["AuthorsNote"],
                        Note=raw_entry["Note"],
                    ),
                    PageNumbers=PageNumbers(
                        PageNumberFrom=raw_entry["PageNumberFrom"],
                        PageNumberTo=raw_entry["PageNumberFrom"],
                    ),
                    LociType=LociType(raw_entry["LociType"]),
                    RelationType=RelationType(raw_entry["RelationType"]),
                )
            case EntryType.AUTHORS_RULE:
                return AuthorsRule(
                    Guid=raw_entry["Guid"],
                    FuxDetails=FuxDetails(
                        NVoice=NVoices(raw_entry["NVocies"]),
                        Species=Species(raw_entry["SpeciesType"]),
                    ),
                    Text=Text(
                        Text=raw_entry["Text"],
                        AuthorsNote=raw_entry["AuthorsNote"],
                        Note=raw_entry["Note"],
                    ),
                    PageNumbers=PageNumbers(
                        PageNumberFrom=raw_entry["PageNumberFrom"],
                        PageNumberTo=raw_entry["PageNumberFrom"],
                    ),
                    LociType=LociType(raw_entry["LociType"]),
                    RelationType=RelationType(raw_entry["RelationType"]),
                    Logic=raw_entry["Logic"],
                )
