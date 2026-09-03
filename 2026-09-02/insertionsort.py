"""
Implements the insertion sort algorithm.
"""


def insertion_sort(a: list[int]) -> None:
    """ Implements the insertion sort algorithm. """
    n = len(a)
    for j in range(1, n):
        key = a[j]
        # Insert a[j] into the sorted sequence a[0]...a[j - 1]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key


def make_random_list(n: int, max_size: int) -> list[int]:
    """ Creates a list of n random integers. All the
        elements are in the range 0...max_size - 1. """ 
    from random import randrange
    result: list[int] = []
    while n:
        result.append(randrange(max_size))
        n -= 1
    return result


if __name__ == '__main__':
    lst = make_random_list(10, 500)
    print(lst)
    insertion_sort(lst)
    print(lst)
    