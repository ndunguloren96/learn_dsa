def linear_search(list, target):
    """
    Returns the index position of the target if found, else return None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


# testing
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in the list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List:", numbers)

result = linear_search(
    numbers, int(input("Enter a target number to search through list: "))
)
verify(result)

# Test data       : Expected Output
# 1               : Target found at index:  0
# 5               : Target found at index:  4
# 10              : Target found at index:  9
# 11              : Target not found in the list
# 0               : Target not found in the list
