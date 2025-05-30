#include <stdio.h>

// Function to perform binary search
// Returns the index of the target if found, else returns -1
int binary_search(int arr[], int size, int target) {
    int first = 0;
    int last = size - 1;

    while (first <= last) {
        int midpoint = (first + last) / 2;

        if (arr[midpoint] == target) {
            return midpoint;  // Target found
        } else if (arr[midpoint] < target) {
            first = midpoint + 1;  // Search in right half
        } else {
            last = midpoint - 1;  // Search in left half
        }
    }

    return -1;  // Target not found
}

// Function to verify and print the result
void verify(int index) {
    if (index != -1) {
        printf("Target found at index: %d\n", index);
    } else {
        printf("Target not found in list\n");
    }
}

int main() {
    // Sorted list (important for binary search)
    int numbers[] = {1,2,3,4,5,6,7,8,9,10};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    // Test with target not in list
    int result = binary_search(numbers, size, 23);
    verify(result);

    // Test with target in list
    result = binary_search(numbers, size, 7);
    verify(result);

    return 0;
}

/*
Expected output
Target no found in list
Target found at index: 6 
*/
/*
Space Complexity
for any value of n, the space complexity is constant (O(1))
*/