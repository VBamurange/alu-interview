#!/usr/bin/python3
""" rain
"""

def rain(walls):
    if not walls:
        return 0

    left, right = 0, 1
    left_max, right_max = 0, 0
    total_water = 0


    while right < len(walls):
        if walls[left] <= walls[right]:
            if walls[left] > left_max:
                left_max = walls[left]
            else:
                total_water += (left_max - walls[left])
            left += 1
        else:
            if walls[right] > right_max:
                right_max = walls[right]
            else:
                total_water += (right_max - walls[right])
            right += 1

    return total_water
