"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    """Determine the relationship between two lists.

    Return whether one is a sublist, superlist, equal, or unequal.
    """

    len_one = len(list_one)
    len_two = len(list_two)

    if list_one == list_two:
        return EQUAL

    if len_one == 0:
        return SUBLIST

    if len_two == 0:
        return SUPERLIST

    if len_one <= len_two:
        if is_sublist(list_one, list_two):
            return SUBLIST
    else:
        if is_sublist(list_two, list_one):
            return SUPERLIST

    return UNEQUAL


def is_sublist(smaller, larger):
    """Return True if smaller is a consecutive sublist of larger."""
    len_smaller = len(smaller)
    len_larger = len(larger)

    for start in range(0, len_larger - len_smaller + 1):
        if smaller == larger[start : len_smaller + start]:
            return True
    return False
