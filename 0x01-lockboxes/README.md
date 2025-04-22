# 0x01. Lockboxes

## Description
This project contains a Python algorithm to solve the lockboxes problem: given n number of locked boxes, each potentially containing keys to other boxes, determine if all boxes can be opened, starting with box 0 already unlocked.

## Requirements
* All files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
* All files should end with a new line
* First line of all files should be exactly `#!/usr/bin/python3`
* Code should use PEP 8 style (version 1.7.x)
* All files must be executable

## Task
### 0. Lockboxes
Write a method that determines if all the boxes can be opened.

* Prototype: `def canUnlockAll(boxes)`
* `boxes` is a list of lists
* A key with the same number as a box opens that box
* You can assume all keys will be positive integers
* There can be keys that do not have boxes
* The first box `boxes[0]` is unlocked
* Return `True` if all boxes can be opened, else return `False`

## File
* `0-lockboxes.py` - Implementation of the canUnlockAll function