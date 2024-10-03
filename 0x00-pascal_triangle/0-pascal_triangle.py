#!/usr/bin/python3
"""Learning about the pascal triangle dsa"""


def pascal_triangle(n):
    """pascal triangle func"""

    if n <= 0:
        return []
    """This means the first row"""
    res = [[1]]

    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        """so we have padded the row"""
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res
