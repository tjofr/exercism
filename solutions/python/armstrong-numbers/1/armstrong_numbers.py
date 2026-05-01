
def count_digits(number):
    """
    Returns the number of digits in an integer.

    Parameters:
    n (int): The input integer.

    Returns:
    int: The number of digits in the input integer.

    Description:
    This function works by converting the absolute value of the input integer `n` to a string, which will have as many
    characters as there are digits. The built-in `len()` function is then used to count the number of characters in
    the string, effectively giving us the number of digits.
    """
    # Convert the integer to a string and return its length
    return len(str(abs(number)))


def is_armstrong_number(number):
    # computes amstrong formula
    candidate = 0
    power = count_digits(number)
    for char in str(abs(number)):
        candidate += int(char) ** power
    return candidate == number