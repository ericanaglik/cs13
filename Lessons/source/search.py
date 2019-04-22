#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


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
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left = 0
    right = len(array) - 1
    index = int(len(array)/2)
    while array[index] != item:
        if array[index] > item: 
            right = index
        else:
            left = index
        index = int((right+left)/2)
    return index
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # left = 0
    # right = len(array) - 1
    # index = int(len(array)/2)
    # while array[index] != item:
    #     if array[index] > item: 
    #         right = index
    #     else:
    #         left = index
    #     index = int((right+left)/2)
    # return index
    # return binary_search_recursive(array, item, left, right)
    if left == None:
        left = 0
    if right == None:
        right = len(array) - 1
    index = (right+left)/2
    if array[index] == item:
        return index
    else:
        if array[index] > item:
            right = index
        else:
            left = index
        return binary_search_recursive(array, item, left, right)
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

if __name__ == '__main__':
    print(binary_search_iterative([1,2,3,4,5,6,7,8,9,10], 4))
    
