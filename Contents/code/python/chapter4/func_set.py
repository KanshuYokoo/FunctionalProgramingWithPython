"""
Purely Functional Sets as Characteristic Functions.
Inspired by Martin Odersky's course: Functional Programming Principles in Scala (EPFL).
"""

from typing import Callable

# A FunSet is a characteristic function: Int -> Bool
FunSet = Callable[[int], bool]


def contains(s: FunSet, elem: int) -> bool:
    """Check if elem is a member of set s."""
    return s(elem)


def singleton_set(elem: int) -> FunSet:
    """Set containing exactly one element."""
    return lambda x: x == elem


def union(s: FunSet, t: FunSet) -> FunSet:
    """Union of sets s and t: elements in s OR t."""
    return lambda x: s(x) or t(x)


def intersect(s: FunSet, t: FunSet) -> FunSet:
    """Intersection of sets s and t: elements in s AND t."""
    return lambda x: s(x) and t(x)


def diff(s: FunSet, t: FunSet) -> FunSet:
    """Difference of sets s and t: elements in s AND NOT in t."""
    return lambda x: s(x) and not t(x)


def filter_set(s: FunSet, p: Callable[[int], bool]) -> FunSet:
    """Filter set s with predicate p: elements of s satisfying p."""
    return lambda x: s(x) and p(x)


def forall(s: FunSet, p: Callable[[int], bool], bound: int = 1000) -> bool:
    """Check if all elements in s satisfy predicate p within [-bound, bound]."""
    for a in range(-bound, bound + 1):
        if contains(s, a) and not p(a):
            return False
    return True


def exists(s: FunSet, p: Callable[[int], bool], bound: int = 1000) -> bool:
    """Check if at least one element in s satisfies predicate p."""
    return not forall(s, lambda x: not p(x), bound)


def map_set(s: FunSet, f: Callable[[int], int], bound: int = 1000) -> FunSet:
    """Transform set s by applying function f: {f(x) | x in s}."""
    return lambda y: exists(s, lambda x: f(x) == y, bound)


if __name__ == "__main__":
    s1 = singleton_set(1)
    s2 = singleton_set(2)
    s3 = singleton_set(3)

    s_1_2 = union(s1, s2)
    s_1_2_3 = union(s_1_2, s3)

    assert contains(s_1_2_3, 1) is True
    assert contains(s_1_2_3, 2) is True
    assert contains(s_1_2_3, 4) is False

    s_even = filter_set(s_1_2_3, lambda x: x % 2 == 0)
    assert contains(s_even, 2) is True
    assert contains(s_even, 1) is False

    s_doubled = map_set(s_1_2_3, lambda x: x * 2)
    assert contains(s_doubled, 2) is True
    assert contains(s_doubled, 4) is True
    assert contains(s_doubled, 6) is True
    assert contains(s_doubled, 3) is False

    print("All functional set assertions passed successfully!")
