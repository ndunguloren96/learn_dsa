#include <stdio.h>

// Function to print the elements of an array
void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int new_list[] = {1, 2, 3};
    int size = 3;

    // Accessing elements
    printf("First element: %d\n", new_list[0]);
    printf("Last element: %d\n\n", new_list[size - 1]);

    // Searching for an element
    printf("Searching for 1: %s\n", (new_list[0] == 1) ? "Found it!" : "Not found");
    printf("\n");

    // Inserting elements
    printf("Original list: ");
    print_array(new_list, size);

    // Append operation (manually extended array for demonstration)
    int extended_list[] = {1, 2, 3, 4};
    size = 4;
    printf("After appending 4: ");
    print_array(extended_list, size);

    return 0;
}
