""" Transform legacy data into new format """
def transform(legacy_data):
    """Create a dict that tracks value of each lower letter from the legacy data.

    Parameters:
        legacy_data (dict): The legacy data, one key is the point value and the value is a list of letters that have that point value.

    Returns:
        dict: data new format with lower letters as keys and their corresponding points as values.
    """
    letters_to_points={}
    for point, point_to_letters in legacy_data.items():
        for letter in point_to_letters:
            letters_to_points[letter.lower()]=point
    return letters_to_points