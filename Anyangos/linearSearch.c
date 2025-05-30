#include <stdio.h>

// Function to perform linear search
// Returns the index of the target if found, otherwise returns -1
int linear_search(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i;  // Target found, return index
        }
    }
    return -1;  // Target not found
}

// Function to verify and display search result
void verify(int index) {
    if (index != -1) {
        printf("Target found at index: %d\n", index);
    } else {
        printf("Target not found in list\n");
    }
}

int main() {
    // Define the array and its size
    int numbers[] = {1,2,3,4,5,6,7,8,9,10};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    // Search with target not in list
    int result = linear_search(numbers, size, 12);
    verify(result);

    // Search with target in list
    result = linear_search(numbers, size, 6);
    verify(result);

    return 0;
}

/*
Expected output
Target not found in list
Target found at index 5
*/
