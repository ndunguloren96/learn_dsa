#include <stdio.h>

// Linear search function
// Returns the index of the target if found, otherwise -1
int linear_search(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i; // Target found
        }
    }
    return -1; // Target not found
}

// Verifies and prints the result of the search
void verify(int index) {
    if (index != -1) {
        printf("Target found at index: %d\n", index);
    } else {
        printf("Target not found in the list\n");
    }
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    printf("Enter a target number to search through the list: ");
    int target;
    scanf("%d", &target);

    // Perform linear search and verify the result
    int result = linear_search(numbers, size, target);
    verify(result);

    return 0;
}
