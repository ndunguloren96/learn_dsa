from linked_list import Node, LinkedList


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively merge the linked list into sublists containign a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains.
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)  # Sort the left half
    right = merge_sort(right_half)  # Sort the right half
    return merge(left, right)  # Merge the sorted halves


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2
