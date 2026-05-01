"""
Module providing function to chek if a year is a leap year 
"""
def leap_year(year):
    """
    :param year: integer - year to check
    :return: bool - true if year is a leap year else false

    :description:
    This function evaluates if a year is a leap year
    A leap year (in the Gregorian calendar) occurs:

    In every year that is evenly divisible by 4.
    Unless the year is evenly divisible by 100,
    in which case it's only a leap year if the year is also
    evenly divisible by 400.

    """
    leap = False
    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0

    if divisible_by_4:
        if divisible_by_100:
            leap = divisible_by_400
        else:
            leap = divisible_by_4
    else:
        leap = divisible_by_4
    return leap