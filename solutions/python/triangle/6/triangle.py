"""Determine whether the given sides form a triangle and whether the triangle is equilateral, isosceles, or scalene."""


def equilateral(sides):
    """Return True if the triangle has three sides of equal length."""
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    """Return True if the triangle has at least two sides of equal length."""
    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    """Return True if the triangle has three sides of different lengths."""
    return is_triangle(sides) and len(set(sides)) == 3


def is_triangle(sides):
    """Return True if the given side lengths can form a valid triangle."""
    if len(sides) != 3:
        return False

    a_side, b_side, c_side = sorted(sides)
    if a_side <= 0:
        return False
    if a_side + b_side <= c_side:
        return False
    return True
