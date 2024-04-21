#!/usr/bin/python3
"""
Algorithm question:
A method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes can be opened.
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
        - There can be keys that do not have boxes
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """
    all_keys = set([0])
    n = len(boxes)

    new_keys = set()
    first_box = [x for x in boxes[0] if x < n]
    new_keys.update(first_box)
    all_keys.update(new_keys)

    while (new_keys):
        nxt_keys = set()
        for key in new_keys:
            nxt_box = [x for x in boxes[key] if x < n]
            nxt_keys.update(nxt_box)

        nxt_keys = nxt_keys - all_keys - new_keys

        new_keys.clear()
        new_keys.update(nxt_keys)
        all_keys.update(new_keys)

    return len(all_keys) == n
