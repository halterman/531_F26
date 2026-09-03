"""
Implements the merge sort algorithm.
"""

MAXIMUM_INT = 1_000_000_000

def merge(a: list[int], p: int, q: int, r: int) -> None:
    # Make new lists containing the left and right halves of a.
    left = [a[p + i] for i in range(0, q - p + 1)]        # n + 1 time
    right = [a[q + j + 1] for j in range(0, r - q)]       # n + 1 time

    # Append sentinel values to simplify the merge logic.
    left.append(MAXIMUM_INT)                              # 
    right.append(MAXIMUM_INT)                             # c time
    i = j = 0                                             # 

    # Merge the two halves.
    for k in range(p, r + 1):                             #
        if left[i] <= right[j]:                           #
            a[k] = left[i]                                #
            i += 1                                        # n time
        else:                                             #
            a[k] = right[j]                               #
            j += 1                                        #


def merge_rec(a: list[int], p: int, r: int) -> None:
    """ The core of the merge sort algorithm. """
    if p < r:
        q = (p + r) // 2       # Compute middle index.
        merge_rec(a, p, q)     # Sort the front half.
        merge_rec(a, q + 1, r) # Sort the last half.
        merge(a, p, q, r)      # Merge the two halves.


def merge_sort(a: list[int]) -> None:
    """ Merge sort: call the recursive function. """
    merge_rec(a, 0, len(a) - 1)


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
    merge_sort(lst)
    print(lst)
    