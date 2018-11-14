#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from random import shuffle
from typing import Tuple, List, Optional, Dict
from enum import Enum

Point = Tuple[int, int]
Entity = Tuple[int, int, int]


def __find_next_points(point: Point) -> List[Point]:
    l = [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)]
    shuffle(l)
    return l


def get_border_with_obstacles(obstacles: List[Point], doors: List[Point] = []) -> List[Point]:
    copy = list(obstacles)

    for y in (0, 8):
        for x in range(0, 13):
            if (x, y) in doors:
                # These are additional obstacles behind the doors.
                # They prevent enemies from leaving the room.
                if y == 0:
                    copy.append((x, -1))
                else:
                    copy.append((x, 9))
                continue
            copy.append((x, y))

    for x in (0, 12):
        for y in range(0, 9):
            if (x, y) in doors:
                # These are additional obstacles behind the doors.
                # They prevent enemies from leaving the room.
                if x == 0:
                    copy.append((-1, y))
                else:
                    copy.append((13, y))
                continue
            copy.append((x, y))

    # print(copy)

    return copy


def find_path(source: Entity, target: Point, obstacles: List[Point], distance: int = 0) -> Optional[List['Action']]:
    while distance >= 0:
        p = find_path_internal(source, target, obstacles, distance)

        if p is not None:
            return p
        distance -= 1

    return None


def find_path_internal(source: Entity, target: Point, obstacles: List[Point], distance: int = 0) -> Optional[
    List['Action']]:
    source_point = source[0], source[1]
    real_target: Point = target

    parent: Dict[Point, Point] = {source_point: None}

    change = True
    found = False
    while not found and change:
        change = False
        keys = list(parent.keys())
        new = []

        if len(keys) == 1:
            new.append(keys[0])

        for p in keys:
            for n in __find_next_points(p):
                if n not in parent and n not in obstacles and n not in new:
                    change = True
                    parent[n] = p
                    new.append(n)

        shuffle(new)

        for n in new:
            if n[0] == target[0] and abs(n[1] - target[1]) == distance:
                target = n
                found = True
                break
            elif n[1] == target[1] and abs(n[0] - target[0]) == distance:
                target = n
                found = True
                break

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

    if len(result) == 0:
        next_facing = 0
        if current[0] > real_target[0]:
            next_facing = 3
        elif current[0] < real_target[0]:
            next_facing = 1
        elif current[1] > real_target[1]:
            next_facing = 0
        elif current[1] < real_target[1]:
            next_facing = 2

        if current[2] != next_facing:
            result.append(Action(ActionType.TURN, next_facing))

    return result


class Action:
    def __init__(self, action_type: 'ActionType', direction: Optional[int] = None):
        self.type = action_type
        self.direction = direction


class ActionType(Enum):
    MOVE = 0
    TURN = 1


if __name__ == "__main__":
    source = 1, 1, 1
    target = 4, 1

    with_border = get_border_with_obstacles([])
    path = find_path(source, target, with_border, 3)

    print("----------")

    if path is None:
        print("No path found")
    else:
        for action in path:
            print(str(action.type) + " " + str(action.direction))
