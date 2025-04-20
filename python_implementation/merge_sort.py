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

left_half, right_half = split(merge_sort)
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
