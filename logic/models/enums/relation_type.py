from enum import IntEnum


class RelationType(IntEnum):
    INTRA_VOICE_MOVEMENT = 0
    INTER_VOICE_MOVEMENT = 1
    CONFIG = 2


class InterVoiceMovementTypes(IntEnum):
    DEFAULT = 0  # both intra and inter
    INTRA_MEASURE = 1
    INTER_MEASURE = 2


class ConfigTypes(IntEnum):
    CONFIG_LOCI = 0
    CONFIG_RELAIIONS = 1
