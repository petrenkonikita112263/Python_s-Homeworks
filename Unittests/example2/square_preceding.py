"""
Main module to be tested.
"""


def square_preceding(values):
    """ (list of number) -> NoneType
    Replace each item in the list with square the value of the
    preceding item, and replace the first item with 0.
    >>> L = [1, 2, 3]
    >>> square_preceding(L)
    >>> L
    [0, 1, 4]
    """
    temp = values[0]
    if values != []:
        values[0] = 0
    for i in range(1, len(values)):
        values[i], temp = temp ** 2, values[i]
    return values
