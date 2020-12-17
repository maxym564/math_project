"""
Tests for iter_tools module
"""

import iter_tools

def count_test(start: int, step: int, limit: int) -> list:
    """
    Return a sequence from a start number
    to limit with certain step.

    >>> len(count_test(1, 1, 10**6))
    1000000
    >>> len(count_test(1, 1, 10**2))
    100
    >>> count_test(0, 10, 100)
    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    >>> count_test(0, 1, 10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> count_test(0, 0, 0)
    [0]
    """
    num_list = []

    for num in iter_tools.count(start, step):
        if num <= limit:
            num_list.append(num)
        else:
            break
    return num_list

def cycle_test(iterable, limit: int) -> list:
    """
    Return a sequence with limited length.

    >>> cycle_test('ABC', 9)
    ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
    >>> cycle_test(['A', 'B', 'C'], 9)
    ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
    >>> cycle_test(['A', 'B', 'C'], 3)
    ['A', 'B', 'C']
    >>> cycle_test('ITERABLE', 8)
    ['I', 'T', 'E', 'R', 'A', 'B', 'L', 'E']
    >>> cycle_test('', 1)
    []
    """
    sequence = []

    for value in iter_tools.cycle(iterable):
        if len(sequence) < limit:
            sequence.append(value)
        else:
            break
    return sequence

def repeat_test(value, repeats: int) -> list:
    """
    Return a sequence with n-time
    repeated value.

    >>> len(repeat_test('ABC', 1000))
    1000
    >>> repeat_test('ABC', 3)
    ['ABC', 'ABC', 'ABC']
    >>> repeat_test('aBcDhIj', 5)
    ['aBcDhIj', 'aBcDhIj', 'aBcDhIj', 'aBcDhIj', 'aBcDhIj']
    >>> repeat_test('test', 0)
    []
    >>> repeat_test('', 1)
    ['']
    """
    sequence = []

    for value in iter_tools.repeat(value, repeats):
        sequence.append(value)
    return sequence

def product_test(*iterable, limit: int) -> list:
    """

    """
    pass

def permutations_test(iterable, limit: int) -> list:
    """

    """
    pass

def combinations_test(iterable, limit: int) -> list:
    """

    """
    pass

def combinations_with_replacement_test(iterable, limit: int) -> list:
    """

    """
    pass


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())