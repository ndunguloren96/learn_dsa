# Approach/step 1: Top-down Design and writing a code scaffold.

# ---How it is done---
# 1. You first outline the structure, main features, and steps (sometimes with comments or docstrings).
# 2. Then fill in the actual logic.
# 3. This helps clarify your thinking and makes the code easier to implement and maintain.


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
