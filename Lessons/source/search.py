#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if array[index] == item:
        return index # found
    else:
        return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_iterative(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    first = 0
    last = len(array) - 1
    position = None
    found = False

    while not found and first <= last:
        midpoint = (first + last) // 2
        if array[midpoint] == item:
            found = True
            position = midpoint
        elif item < array[midpoint]:
            last = midpoint - 1
        elif item > array[midpoint]:
            first = midpoint + 1
    return position 
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if right >= left:
        midpoint = (right + left) // 2
        if array[midpoint] == item:
            return midpoint
        elif array[midpoint] > item:
            return binary_search_recursive(array, item, left, midpoint - 1)
        else:
            return binary_search_recursive(array, item, midpoint + 1, right)
    else:
        return None
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

if __name__ == '__main__':
    main()
    
