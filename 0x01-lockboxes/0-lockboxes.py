#!/usr/bin/python3
"""
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1 and each box
    may contain keys to the other boxes.
    Write a method that determines if all the boxes can be opened.
"""
import copy


def canUnlockAll(boxes):
    """
        canUnlockAll
    """
    copied_boxes = copy.deepcopy(boxes)
    openBox(copied_boxes, 0)
    for ele in copied_boxes:
        if not ele or ele[0] != -1:
            return False
    return True


def openBox(boxes, index):
    """
        openBox
    """
    if index == -1 or index > len(boxes):
        return
    if not boxes[index]:
        boxes[index].append(-1)
    if len(boxes[index]) == 1:
        key = boxes[index][0]
        boxes[index][0] = -1
        openBox(boxes, key)
    elif len(boxes[index]) > 1:
        target = 0
        for element in boxes[index]:
            newKey = element
            boxes[index][target] = -1
            openBox(boxes, newKey)
            target += 1
