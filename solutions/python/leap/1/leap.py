def leap_year(year):
    leap = False
    divisible_by_4 = (year % 4 == 0)
    divisible_by_100 = (year % 100 == 0)
    divisible_by_400 = (year % 400 == 0)

    if divisible_by_4:
        if divisible_by_100:
            leap = divisible_by_400
        else:
            leap = divisible_by_4
    else:
        leap = divisible_by_4
    return leap


