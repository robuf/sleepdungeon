from typing import Tuple, List, Optional, Dict
from enum import Enum

Point = Tuple[int, int]
Entity = Tuple[int, int, int]


def __find_next_points(point: Point) -> List[Point]:
    return [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)]


def get_border_with_obstacles(obstacles: List[Point]) -> List[Point]:
    copy = list(obstacles)

    for x in range(0, 13):
        copy.append((x, 0))
        copy.append((x, 8))

    for y in range(0, 9):
        copy.append((0, y))
        copy.append((12, y))

    return copy


def find_path(source: Entity, target: Point, obstacles: List[Point], distance: int = 0) -> Optional[List['Action']]:
    source_point = source[0], source[1]

    parent: Dict[Point, Point] = {source_point: None}

    change = True
    found = False
    while not found and change:
        change = False
        keys = list(parent.keys())
        new = list()
        for p in keys:
            for n in __find_next_points(p):
                if n not in parent and n not in obstacles:
                    change = True
                    parent[n] = p
                    new.append(p)

            for n in new:
                if n[0] == target[0] and abs(n[1] - target[1]) == distance:
                    target = n
                    found = True
                if n[1] == target[1] and abs(n[0] - target[0]) == distance:
                    target = n
                    found = True

    if not found:
        return None

    path = []

    prev = target

    while prev is not None and prev != source_point:
        path.append(prev)
        prev = parent[prev]

    result = []

    current = source

    path.reverse()
    for item in path:
        next_facing = 0
        if current[0] > item[0]:
            next_facing = 3
        elif current[0] < item[0]:
            next_facing = 1
        elif current[1] > item[1]:
            next_facing = 0
        elif current[1] < item[1]:
            next_facing = 2

        if current[2] != next_facing:
            result.append(Action(ActionType.TURN, next_facing))

        result.append(Action(ActionType.MOVE))

        current = item[0], item[1], next_facing

    return result


class Action:
    def __init__(self, action_type: 'ActionType', direction: Optional[int] = None):
        self.type = action_type
        self.direction = direction


class ActionType(Enum):
    MOVE = 0
    TURN = 1


if __name__ == "__main__":
    source = 1, 1, 0
    target = 4, 5

    obstacles = [(3, y) for y in range(1, 8)]
    path = find_path(source, target, get_border_with_obstacles(obstacles), 0)

    print("----------")

    if path is None:
        print("No path found")
    else:
        for action in path:
            print(str(action.type) + " " + str(action.direction))
