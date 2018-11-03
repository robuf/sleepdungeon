from typing import Tuple, List, Set, Optional, Dict
from enum import Enum

Point = Tuple[int, int]
Entity = Tuple[int, int, int]


def find_path(source: Entity, target: Point, obstacles: Set[Point], distance: int = 0) -> Optional[List['Action']]:
    found = {}
    return None


class Action:
    def __init__(self, action_type: 'ActionType', direction: Optional[int] = None):
        self.type = action_type
        self.direction = direction


class ActionType(Enum):
    MOVE = 0
    TURN = 1


if __name__ == "__main__":
    source = 1, 1, 0
    target = 4, 3

    path = find_path(source, target, set(), 0)

    if path is None:
        print("No path found")
    else:
        for action in path:
            print(str(action.type) + str(action.direction))
