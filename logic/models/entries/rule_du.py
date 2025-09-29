from __future__ import annotations
from dataclasses import dataclass
from typing import Literal, Union


# --- define the cases (like F# DU cases) ---
@dataclass(frozen=True)
class RuleBase:
    kind: Literal["RuleBase"] = "RuleBase"
    radius: float = 0.0


@dataclass(frozen=True)
class RuleAuthor:
    kind: Literal["RuleAuthor"] = "RuleAuthor"
    width: float = 0.0
    height: float = 0.0


@dataclass(frozen=True)
class RuleRelaxing:
    kind: Literal["RuleRelaxing"] = "RuleRelaxing"
    x: float = 0.0
    y: float = 0.0


Rule = Union[RuleBase, RuleAuthor, RuleRelaxing]  # the DU type alias


def RuleType(s: Rule) -> float:
    match s:
        case RuleBase(radius=r):
            return 3.1415926535 * r * r
        case RuleAuthor(width=w, height=h):
            return w * h
        case RuleRelaxing():
            return 0.0
