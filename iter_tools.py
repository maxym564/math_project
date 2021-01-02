"""
Alternative for a library itertools
Available functions: count(), cycle(),
repeat(), product(), permutations(),
combinations(), combinations_with_replacement()
"""

def count(start=0, step=1):
    """
    Return iterable object of endless cycle.

    Usage:
    count() -> 0, 1, 2, ...
    count(10, 3) -> 10, 13, 16, ...
    count(0, 0) -> 0, 0, 0, ...
    """
    yield start

    if step == 0:
        return start
    else:
        while True:
            yield start + step
            start += step


def cycle(iterable):
    """
    Return endless iterator with values
    which are in iterable object.

    Usage:
    cycle(['A', 'B', 'C']) -> A, B, C, A, B, C, ...
    cycle(['ABC']) -> A, B, C, A, B, C, ...
    cycle(('A')) -> A, A, A, ...
    """
    if len(iterable) == 0:
        return iterable
    else:
        while True:
            for item in iterable:
                yield item


def repeat(value, repeats=1, depth=0):
    """
    Return endless iterator with
    values which are repeated a 
    certain number of times.

    Usage:
    repeat(3, 3) -> 3, 3, 3
    repeat('A', 5) -> A, A, A, A, A
    repeat(0) -> 0
    """
    while depth != repeats:
        yield value
        depth += 1


def product(*iterables, repeat=2):
    """
    Return generator of Cartesian product
    of all elements.

    Usage:
    product(*[1, 2]) -> [(1, 1), (1, 2), (2, 1), (2, 2)]
    product(*(1, 2)) -> [(1, 1), (1, 2), (2, 1), (2, 2)]
    product(*'AB') -> [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
    """
    el_lst = []
    counter = 2

    if repeat < 2:
        for el in iterables:
            yield tuple(el)
        return None

    for el in iterables:
        for subel in iterables:
            el_lst.append([el, subel])

    while counter != repeat:
        new_lst = []
        for subel in iterables:
            for ind in range(len(el_lst)):
                new_lst.append(el_lst[ind] + [subel])

        el_lst = new_lst
        counter += 1

    el_lst = sorted(el_lst, key=lambda lst: lst)

    for el in el_lst:
        yield tuple(el)


def permutations(iterable, length=None):
    """
    Return all permutations of iterable.
    Order of elements is important.

    Usage:
    ...
    """
    pass


def combinations(iterable, n: int):
    """
    Return all combinations of iterable with n elements.
    No matter what order of elements it is.
    Elements are sorted.

    Usage:
    ...
    """
    pass


def combinations_with_replacement(iterable, n: int):
    """
    Return all combinations of iterable with n elements.
    Elements could be repeated.
    Elements are sorted.

    Usage:
    ...
    """
    pass