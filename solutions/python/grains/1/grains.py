def square(number):
    if number >= 1 and number <=64 :
        return 2 ** (number-1)
    else:
        raise ValueError("square must be between 1 and 64")

def total():
    square_numbers = list(range(1,65))
    resultat0 = list(map(square,square_numbers))
    return sum(resultat0)
