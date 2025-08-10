def binary_search(arr, x):
    """
    Returns the index of the element x in the sorted list arr,
    or -1 if x is not present in the list.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_first_occurrence(arr, x):
    """
    Returns the index of the first occurrence of the element x in the sorted list arr,
    or -1 if x is not present in the list.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid - 1] < x:
                return mid
            else:
                right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    print(binary_search([3,6,90,2,1,67], 90))