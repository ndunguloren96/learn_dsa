def merge_sort(lst):
    """
    Sorts a list in ascending order using the merge sort algorithm.
    """
    if len(lst) <= 1:
        return lst  # A list of 0 or 1 elements is already sorted

    left_half, right_half = split(lst)  # Divide step
    left = merge_sort(left_half)       # Recursively sort left half
    right = merge_sort(right_half)     # Recursively sort right half

    return merge(left, right)          # Combine step


def split(lst):
    """
    Splits a list into two halves.
    """
    mid = len(lst) // 2
    return lst[:mid], lst[mid:]


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    """
    result = []
    i = j = 0

    # Merge elements from both lists in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result += left[i:]
    result += right[j:]

    return result

def verify_sorted(list):
    n = len(list)

    # A list with 0 or 1 elements is trivially sorted
    if n == 0 or n == 1:
        return True

    # Check if the first element is less than the second
    # and recursively verify the rest of the list
    return list[0] < list[1] and verify_sorted(list[1:])

# Example usage
alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
sorted_list = merge_sort(alist)
print(verify_sorted(alist))  #Expected: False (as alist is not sorted)
print(verify_sorted(sorted_list)) #Expected: True(sorte_list is sorted)

