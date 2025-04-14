#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Node structure representing each element in the linked list
typedef struct Node {
    int data;              // Data stored in the node
    struct Node* next;     // Pointer to the next node
} Node;

// LinkedList structure representing the linked list
typedef struct LinkedList {
    Node* head;            // Pointer to the head node
} LinkedList;

// Creates and initializes a new linked list
LinkedList* create_linked_list() {
    LinkedList* list = (LinkedList*)malloc(sizeof(LinkedList));
    list->head = NULL; // Initialize head to NULL
    return list;
}

// Checks if the linked list is empty
bool is_empty(LinkedList* list) {
    return list->head == NULL;
}

// Returns the size (number of nodes) of the linked list
int size(LinkedList* list) {
    int count = 0;
    Node* current = list->head;
    while (current != NULL) {
        count++;
        current = current->next;
    }
    return count;
}

// Adds a new node with the given data at the head of the list
void add(LinkedList* list, int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = list->head;
    list->head = new_node;
}

// Searches for a node with the given key and returns it
Node* search(LinkedList* list, int key) {
    Node* current = list->head;
    while (current != NULL) {
        if (current->data == key) {
            return current; // Return the node if found
        }
        current = current->next;
    }
    return NULL; // Return NULL if not found
}

// Inserts a new node with the given data at the specified index
void insert(LinkedList* list, int data, int index) {
    if (index == 0) {
        add(list, data); // Add at the head if index is 0
        return;
    }

    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;

    Node* current = list->head;
    for (int i = 0; i < index - 1 && current != NULL; i++) {
        current = current->next;
    }

    if (current == NULL) {
        printf("Index out of bounds\n");
        free(new_node);
        return;
    }

    new_node->next = current->next;
    current->next = new_node;
}

// Removes the node with the given key and returns its data
int remove_node(LinkedList* list, int key) {
    Node* current = list->head;
    Node* previous = NULL;

    while (current != NULL) {
        if (current->data == key) {
            if (previous == NULL) {
                list->head = current->next; // Update head if removing the first node
            } else {
                previous->next = current->next;
            }
            int data = current->data;
            free(current);
            return data; // Return the data of the removed node
        }
        previous = current;
        current = current->next;
    }
    return -1; // Return -1 if key not found
}

// Prints the linked list in a readable format
void print_list(LinkedList* list) {
    Node* current = list->head;
    while (current != NULL) {
        printf("[%d] -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    LinkedList* list = create_linked_list();

    // Add nodes to the list
    add(list, 10);
    add(list, 20);
    add(list, 30);

    printf("List: ");
    print_list(list);

    printf("Size: %d\n", size(list));

    // Search for a node
    Node* found = search(list, 20);
    if (found) {
        printf("Found: %d\n", found->data);
    } else {
        printf("Not found\n");
    }

    // Insert a node at index 1
    insert(list, 25, 1);
    printf("After insertion: ");
    print_list(list);

    // Remove a node with key 20
    remove_node(list, 20);
    printf("After removal: ");
    print_list(list);

    return 0;
}
