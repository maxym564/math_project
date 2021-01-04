"""
Alternative for a library itertools
Available functions: count(), cycle(),
repeat(), product(), permutations(),
combinations(), combinations_with_replacement()
"""
from typing import Generator, Iterator, Iterable


def count(start=0, step=1) -> Iterator:
    """
    Returns iterable object of endless cycle.

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


def cycle(iterable: Iterable) -> Iterator:
    """
    Returns endless iterator with values
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


def repeat(value, repeats=1) -> Iterator:
    """
    Returns endless iterator with
    values which are repeated a 
    certain number of times.

    Usage:
    repeat(3, 3) -> 3, 3, 3
    repeat('A', 5) -> A, A, A, A, A
    repeat(0) -> 0
    """
    depth=0

    while depth != repeats:
        yield value
        depth += 1


def product(*iterables: Iterable, repeat=2) -> Generator:
    """
    Returns generator of Cartesian product
    of all elements.

    Usage:
    product(*[1, 2]) -> (1, 1), (1, 2), (2, 1), (2, 2)
    product(*(1, 2)) -> (1, 1), (1, 2), (2, 1), (2, 2)
    product(*'AB') -> ('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')
    """
    el_lst = []
    counter = 2

    if repeat < 2:
        for el in iterables:
            yield tuple(str(el))
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

    el_lst = sorted(el_lst)

    for el in el_lst:
        yield tuple(el)


def permutations(iterable: Iterable, r= None) -> Generator:
    """
    Returns all permutations of iterable.
    Order of elements is important.

    Usage:
    permutations('abc', 2) -> ab, ba, ac, ca, bc, cb
    """
    r = len(iterable) if r == None else r
    pos_comb = combinations(iterable,r)

    for area in pos_comb:
        n = len(area)
        run = True
        variants = list(range(n))

        yield tuple(area[i] for i in variants)

        while run:
            for j in range(n-2,-1,-1):
                if variants[j] < variants[j + 1]:
                    break
            else:
                run = False
                break
            k = n -1
            while variants[j] > variants[k]:
                k -= 1
            variants[k],variants[j] = variants[j],variants[k]
            r = n-1
            s = j+1

            while r > s:
                variants[r],variants[s] = variants[s],variants[r]
                r -= 1
                s += 1
            yield tuple(area[i] for i in variants)


def combinations(iterable: Iterable, r: int) -> Generator:
    """
    Returns the generator with all possible combinations
    without repetitions from elements of an array on r.
    Order is not important.

    Usage:
    combinations('abc', 2) -> ab, ac, bc
    """
    area = tuple(iterable)
    n = len(area)
    variants = list(range(r))

    if r > n:
        return None

    yield tuple(area[i] for i in range(r))

    while True:
        for i in reversed(range(r)):
            if variants[i] != n - r + i:
                break
        else:
            return None

        variants[i] = variants[i] + 1

        for j in range(i+1, r):
            variants[j] = variants[j-1] + 1

        yield tuple(area[i] for i in variants)


def combinations_with_replacement(iterable: Iterable, n: int) -> Generator:
    """
    Returns all combinations of iterable with n elements.
    Elements could be repeated.
    Elements are sorted.
    Order is not important.

    Usage:
    combinations_with_replacement(list(range(2)), 2) -> (0, 0), (0, 1), (1, 1)
    """
    if n == 0:
        return []

    replacement_lst = list(product(*iterable, repeat=n))
    replacement_lst = list(map(sorted, sorted(replacement_lst)))

    for item in reversed(replacement_lst):
        if replacement_lst.count(item) > 1:
            replacement_lst.remove(item)

    for el in sorted(replacement_lst):
        yield tuple(el)