from enum import IntEnum


class EntryType(IntEnum):
    FACT = 0
    RULE = 1
    HEURISTIC = 2
    SUGGESTION = 3
    AUTHORS_RULE = 4
