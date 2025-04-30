#include <stdio.h> // Needed for printf

/**
 * @brief Recursively calculates the sum of an integer array segment.
 * @param arr Pointer to the current element.
 * @param count Number of elements remaining from arr onwards.
 * @return The sum of the array segment.
 */
int sum_recursive(int *arr, int count) {
    // Base Case: The condition that stops the recursion.
    // If there are no elements left (count is 0 or less), the sum is 0.
    if (count <= 0) {
        return 0;
    }

    // Recursive Step: The function calls itself with a smaller problem.
    // It adds the current element (*arr) to the result of calling
    // itself on the rest of the array (starting at the next element 'arr + 1'
    // with one less element 'count - 1').
    return *arr + sum_recursive(arr + 1, count - 1);
}

int main() {
    int numbers[] = {1, 2, 7, 9};
    int size = sizeof(numbers) / sizeof(numbers[0]); // Calculate array size

    // Initial call to the recursive function
    int total_sum = sum_recursive(numbers, size);

    printf("The sum is: %d\n", total_sum);

    return 0; // Indicate successful execution
}