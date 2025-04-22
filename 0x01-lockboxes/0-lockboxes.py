#!/usr/bin/python3
"""
0-lockboxes module
Contains a method that determines if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
        boxes (list of lists): A list of lists where each inner list
                              contains keys (integers) to other boxes

    Returns:
        bool: True if all boxes can be opened, else False

    Note:
        - Box 0 is initially unlocked
        - A key with the same number as a box opens that box
    """
    if not boxes or type(boxes) is not list:
        return False

    n = len(boxes)
    if n == 0:
        return True

    # Keep track of which boxes are unlocked
    unlocked = [False] * n
    unlocked[0] = True  # First box is already unlocked

    # Keep track of keys we have
    keys = set(boxes[0])

    # While we have keys to unopened boxes
    while keys:
        key = keys.pop()
        
        # If the key is valid and the box hasn't been unlocked yet
        if key < n and not unlocked[key]:
            # Unlock the box
            unlocked[key] = True
            # Add new keys to our set, but only if we haven't seen them yet
            for new_key in boxes[key]:
                if new_key < n and not unlocked[new_key]:
                    keys.add(new_key)

    # Check if all boxes are unlocked
    return all(unlocked)