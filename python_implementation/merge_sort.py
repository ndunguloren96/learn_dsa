# Merge Sort Implementation in Python
def merge_sort(list):
    """
    Merge Sort Algorithm
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    Stable Sort: Yes
    In-place Sort: No
    """

    """
    Sort a list in ascending order
    Returns a new sorted list
    The algorithm is a recursive divide-and-conquer algorithm

    Divide: Find the midpoint of the list and divide it into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in the previous step
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at the midpoint into sublists
    Returns two lists - the left and right sublists
    """

    mid = len(list) // 2
    left = list[:mid]  # does not include mid
    right = list[mid:]  # includes mid
    return left, right


def merge(left, right):
    """
    Merge two lists (arrays), sorting them in the process.
    Returns a new merged sorted list.
    """

    l = []  # Resultant merged list
    i = 0  # Pointer for left list
    j = 0  # Pointer for right list

    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # Compare current elements
            l.append(left[i])  # Append smaller element from left
            i += 1
        else:
            l.append(right[j])  # Append smaller element from right
            j += 1

    # Append any remaining elements from left list
    while i < len(left):
        l.append(left[i])
        i += 1

    # Append any remaining elements from right list
    while j < len(right):
        l.append(right[j])
        j += 1

    return l  # Return the merged sorted list
