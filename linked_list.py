class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """
    def __init__(self, data):
        self.data = data          # Assign data when a new node is created
        self.next_node = None     # This points to the next node in the list

    def __repr__(self):
        return "<Node data: %s>" % self.data  # Display node in a readable format


class LinkedList:
    # Singly linked list

    def __init__(self):
        self.head = None
        self.__count = 0           # Keep track of number of nodes for O(1) size

    def is_empty(self):
        # This checks if head = None (i.e. if the list is empty)
        return self.head is None

    def size(self):
        """
        Returns the number of nodes in the list.
        Takes O(1) time due to tracking with __count.
        """
        return self.__count

    def add(self, data):
        """
        Adds new node containing data at head.
        Takes O(1) time.
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        self.__count += 1

    def search(self, key):
        """
        Search for the first node containing data that matches the key.
        Returns the node or `None` if not found.
        Takes O(n) time.
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position.
        Insertion takes O(1) time but finding node at insertion point takes
        O(n) time. Overall O(n).
        """
        if index > self.__count or index < 0:
            raise IndexError('Index out of range')

        if index == 0:
            self.add(data)
            return

        new_node = Node(data)
        current = self.head
        position = 0

        # Traverse to node just before the insertion point
        while position < index - 1:
            current = current.next_node
            position += 1

        new_node.next_node = current.next_node
        current.next_node = new_node

        self.__count += 1

    def node_at_index(self, index):
        """
        Returns the Node at specified index.
        Takes O(n) time.
        """
        if index >= self.__count or index < 0:
            raise IndexError('Index out of range')

        current = self.head
        position = 0

        while position < index:
            current = current.next_node
            position += 1

        return current

    def remove(self, key):
        """
        Removes Node containing data that matches the key.
        Returns the node or `None` if key doesn't exist.
        Takes O(n) time.
        """
        current = self.head
        previous = None

        while current:
            if current.data == key:
                if previous is None:  # Node to remove is head
                    self.head = current.next_node
                else:
                    previous.next_node = current.next_node
                self.__count -= 1
                return current
            previous = current
            current = current.next_node

        return None

    def remove_at_index(self, index):
        """
        Removes Node at specified index.
        Takes O(n) time.
        """
        if index >= self.__count or index < 0:
            raise IndexError('Index out of range')

        current = self.head

        if index == 0:
            self.head = current.next_node
            self.__count -= 1
            return current

        position = 0
        previous = None

        while position < index:
            previous = current
            current = current.next_node
            position += 1

        previous.next_node = current.next_node
        self.__count -= 1

        return current

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next_node

    def __repr__(self):
        """
        Returns a string representation of the list.
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return ' -> '.join(nodes)


# Example usage:
if __name__ == "__main__":
    l = LinkedList()  # create a new list

    print("Is the list empty?", l.is_empty())  # expected: True
    print("Size of the list:", l.size())       # expected: 0

    l.add(5)
    print("Is the list empty?", l.is_empty())  # expected: False
    print("Size of the list:", l.size())       # expected: 1
    print("List:", l)

    l.add(10)
    l.add(15)
    print("List after adding 10 and 15:", l)

    n = l.search(10)
    print("Search for 10:", n)

    l.insert(7, 1)
    print("List after inserting 7 at index 1:", l)

    removed_node = l.remove(15)
    print("Removed node with data 15:", removed_node)
    print("List after removal:", l)

    removed_at_index = l.remove_at_index(1)
    print("Removed node at index 1:", removed_at_index)
    print("List after removing at index 1:", l)

    print("Iterating through list:")
    for node in l:
        print(node)
