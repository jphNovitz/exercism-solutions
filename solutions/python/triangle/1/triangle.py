def equilateral(sides):
    if isTriangle(sides):
        if sides[0] == sides[1] == sides[2]:
            return True
    return False


def isosceles(sides):
    if isTriangle(sides):
        if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            return True
    return False


def scalene(sides):
    if isTriangle(sides):
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
            return True
    return False


def isTriangle(sides):
    if (3 > len(sides) > 3) or (sides[0] == sides[1] == sides[2] == 0):
        return False
    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        return False
    return True
