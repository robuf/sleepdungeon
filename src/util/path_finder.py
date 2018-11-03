from typing import Tuple, List, Set, Optional
from enum import Enum

from ..base.game_constants import Facing

Point = Tuple[int, int]
Entity = Tuple[int, int,]


def find_path(source: Entity, target: Point, obstacles: Set[Point], distance: int = 0) -> Optional[List['Action']]:
    return None


class Action:
    def __init__(self, action_type: 'ActionType', direction: Optional[Facing] = None):
        self.type = action_type
        self.direction = direction


class ActionType(Enum):
    MOVE = 0
    TURN = 1
