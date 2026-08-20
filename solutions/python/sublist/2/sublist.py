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

    if len_one == 0:
        if len_two == 0:
            return EQUAL
        return SUBLIST
    if len_two == 0:
        return SUPERLIST

    if len_one <= len_two:
        if list_one == list_two:
            return EQUAL

        for start in range(0, len_two - len_one + 1):
            if list_one == list_two[start : len_one + start]:
                return SUBLIST
    else:
        for start in range(0, len_one - len_two + 1):
            if list_two == list_one[start : len_two + start]:
                return SUPERLIST

    return UNEQUAL
