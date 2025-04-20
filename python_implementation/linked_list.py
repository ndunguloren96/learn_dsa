class Node:
    """
    An object for storing a single node of a linked list.
    The node contains 2 attributes: data stored in the node and a reference to the next node in the list.
    """

    def __init__(self, data):
        self.data = data
        self.next_node = None  # Initialize next_node to None for each instance

    def __repr__(self):
        return "<Node data: %s>" % self.data


# Text data
# bash: python -i linked_list.py
# >>> N1 = Node(10)
# >>> N1
# <Node data: 10>
# >>> N2 = Node(20)
# >>> N1.next_node = N2
# >>> N1.next_node
# <Node data: 20>
# >>> N2.next_node = None
# >>> N1.next_node
# <Node data: None>


class LinkedList:
    """
    Sigly Linked List
    """

    def __init__(self):
        self.head = None  # Initialize the head of the list to None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Return the number of nodes in the list
        Tale 0(n) time
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds new Node cntaining data at head of the list
        Takes 0(1) time (constatnt time)
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first  node containing data that matches the key
        Return the node or None if not found

        Take 0(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertion takes 0(1) time but finding the node at the
        insertion point takes 0(n) time

        Take 0(n) time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes node containing data that matches the key
        Returns the node or None if key does not exist
        Takes 0(n) time
        """
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current.data if found else None

    def __repr__(self):
        """
        Returns a string representation of the list.
        Takes 0(n) time
        """

        node = []
        current = self.head
        # Iterate through the list, starting from the head node
        while current:
            # Check if we're at the head node
            if current is self.head:
                # Append a string representation of the head node to the list
                node.append("[Head: %s]" % current.data)
            # Check if we're at the tail node (i.e., the last node in the list)
            elif current.next_node is None:
                # Append a string representation of the tail node to the list
                node.append("[Tail: %s]" % current.data)
            else:
                # Append a string representation of a regular node to the list
                node.append("[%s]" % current.data)
            # Move to the next node in the list
            current = current.next_node
        # Join all the node representations together with '-> ' in between
        return "-> ".join(node)
