def leap_year(year):
    """Return whether the given year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False
