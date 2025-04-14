#include <stdio.h>
#include <stdbool.h>

// Recursive binary search function
// Returns true if the target is found, otherwise false
bool recursive_binary_search(int arr[], int low, int high, int target) {
    if (low > high) {
        return false; // Base case: target not found
    }

    int mid = (low + high) / 2;

    if (arr[mid] == target) {
        return true; // Target found
    } else if (arr[mid] < target) {
        return recursive_binary_search(arr, mid + 1, high, target); // Search in the right half
    } else {
        return recursive_binary_search(arr, low, mid - 1, target); // Search in the left half
    }
}

// Verifies and prints the result of the search
void verify(bool result) {
    printf("Target found: %s\n", result ? "true" : "false");
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    // Test case 1: Target not in the array
    bool result = recursive_binary_search(numbers, 0, size - 1, 12);
    verify(result);

    // Test case 2: Target in the array
    result = recursive_binary_search(numbers, 0, size - 1, 6);
    verify(result);

    return 0;
}
