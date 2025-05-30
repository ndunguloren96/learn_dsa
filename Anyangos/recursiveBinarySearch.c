/*A recursive function such as this one calls itself multiple times until the target value is reached
*/

#include <stdio.h>
#include <stdbool.h>

// Recursive binary search returning true if found, false otherwise
bool recursive_binary_search(int arr[], int low, int high, int target) {
    if (low > high) {
        return false;  // Base case: not found
    }

    int mid = (low + high) / 2;

    if (arr[mid] == target) {
        return true;  // Target found
    } else if (arr[mid] < target) {
        return recursive_binary_search(arr, mid + 1, high, target);  // Search right
    } else {
        return recursive_binary_search(arr, low, mid - 1, target);  // Search left
    }
}

// Function to verify and print result
void verify(bool result) {
    if (result) {
        printf("Target found: true\n");
    } else {
        printf("Target found: false\n");
    }
}

int main() {
    int numbers[] = {1,2,3,4,5,6,7,8};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    // Test with target not in list
    bool result = recursive_binary_search(numbers, 0, size - 1, 12);
    verify(result);

    // Test with target in list
    result = recursive_binary_search(numbers, 0, size - 1, 5);
    verify(result);

    return 0;
}


/*
expected output:
Target found: false
Target found: true

Space Complexity: O (log n)

*/