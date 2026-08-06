"""Determine whether the given sides form a triangle and whether the triangle is equilateral, isosceles, or scalene."""


def equilateral(sides):
    """Return True if the triangle has three sides of equal length."""
    if is_triangle(sides):
        if sides[0] == sides[1] == sides[2]:
            return True
    return False


def isosceles(sides):
    """Return True if the triangle has at least two sides of equal length."""
    if is_triangle(sides):
        if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            return True
    return False


def scalene(sides):
    """Return True if the triangle has three sides of different lengths."""
    if is_triangle(sides):
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
            return True
    return False


def is_triangle(sides):
    """Return True if the given side lengths can form a valid triangle."""
    if (3 > len(sides) > 3) or (sides[0] == sides[1] == sides[2] == 0):
        return False
    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        return False
    return True
