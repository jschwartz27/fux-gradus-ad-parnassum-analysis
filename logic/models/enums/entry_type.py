from enum import Enum


class EntryType(Enum):
    FACT = 0
    RULE = 1
    HEURISTIC = 2
    SUGGESTION = 3
    AuthorRule = 4
    CompositeRule = 5
