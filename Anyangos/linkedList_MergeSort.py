# Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

# LinkedList class with essential methods
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count

    def node_at_index(self, index):
        current = self.head
        for _ in range(index):
            if current:
                current = current.next_node
            else:
                return None
        return current

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next_node
        return result

    def print_list(self):
        print(" -> ".join(map(str, self.to_list())))

# Merge sort for linked lists
def merge_sort(linked_list):
    if linked_list.size() == 1 or linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    if linked_list == None or linked_list.head == None:
        return linked_list, None

    size = linked_list.size()
    mid = size // 2
    mid_node = linked_list.node_at_index(mid - 1)

    left_half = linked_list
    right_half = LinkedList()
    right_half.head = mid_node.next_node
    mid_node.next_node = None

    return left_half, right_half

def merge(left, right):
    merged = LinkedList()
    merged.add(0)  # Temporary dummy node
    current = merged.head

    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            break
        elif right_head is None:
            current.next_node = left_head
            break
        else:
            if left_head.data < right_head.data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node

    merged.head = merged.head.next_node  # Remove dummy node
    return merged

# create linked list from Python list
def create_linked_list_from_list(lst):
    ll = LinkedList()
    for value in reversed(lst):
        ll.add(value)
    return ll

# === TEST CASES ===
test_cases = [
    [4, 2, 7, 1, 3],
    [],
    [10],
    [5, 5, 5, 5],
    [9, 7, 5, 3, 1],
    [1, 2, 3, 4, 5]
]

for i, case in enumerate(test_cases, 1):
    print(f"\nTest Case {i}: {case}")
    ll = create_linked_list_from_list(case)
    print("Original List:")
    ll.print_list()

    sorted_ll = merge_sort(ll)
    print("Sorted List:")
    sorted_ll.print_list()
