def recursive_binary_search(list, target):
    """
    Performs a recursive binary search on a sorted list.
    Returns True if the target is found, otherwise False.
    """
    if len(list) == 0:
        return False  # Base case: empty list

    midpoint = len(list) // 2

    if list[midpoint] == target:
        return True  # Target found
    elif list[midpoint] < target:
        return recursive_binary_search(
            list[midpoint + 1 :], target
        )  # Search in the right half
    else:
        return recursive_binary_search(
            list[:midpoint], target
        )  # Search in the left half


def verify(result):
    """Prints whether the target was found."""
    print("Target found: ", result)


# Test cases
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(numbers, 12)  # Target not in the list
verify(result)

result = recursive_binary_search(numbers, 6)  # Target in the list
verify(result)
