#include <stdio.h>
#include <stdlib.h>

// Function to swap two integer values
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Selection Sort function (in-place)
void selection_sort(int arr[], int n) {
    int i, j, min_idx;

    // One by one move boundary of unsorted subarray
    for (i = 0; i < n - 1; i++) {
        // Find the minimum element in unsorted array
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }

        // Swap the found minimum element with the first element
        if (min_idx != i) { // Avoid swapping element with itself
             swap(&arr[min_idx], &arr[i]);
        }
    }
}

// Function to print an array
void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Function to load numbers from a file
// Returns the number of integers read, or -1 on error
// Updates the pointer `arr_ptr` to point to the allocated array
int load_numbers(const char* filename, int** arr_ptr) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file");
        return -1;
    }

    int capacity = 10; // Initial capacity
    int count = 0;
    *arr_ptr = (int*)malloc(capacity * sizeof(int));
    if (*arr_ptr == NULL) {
        perror("Memory allocation failed");
        fclose(file);
        return -1;
    }

    int num;
    while (fscanf(file, "%d", &num) == 1) {
        if (count >= capacity) {
            capacity *= 2; // Double the capacity
            int* temp = (int*)realloc(*arr_ptr, capacity * sizeof(int));
            if (temp == NULL) {
                perror("Memory reallocation failed");
                free(*arr_ptr);
                fclose(file);
                return -1;
            }
            *arr_ptr = temp;
        }
        (*arr_ptr)[count++] = num;
    }

    fclose(file);

    // Optional: Shrink array to actual size
    int* final_arr = (int*)realloc(*arr_ptr, count * sizeof(int));
     if (final_arr == NULL && count > 0) { // Check if realloc failed but we had elements
        perror("Memory shrink failed, using original size");
        // Keep the larger allocated block (*arr_ptr)
    } else if (count > 0) {
         *arr_ptr = final_arr; // Update pointer only if realloc succeeded or count is 0
     } else if (count == 0) { // If no numbers were read
         free(*arr_ptr);
         *arr_ptr = NULL;
     }

    return count;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1; // Indicate error
    }

    int* numbers = NULL;
    int n = load_numbers(argv[1], &numbers);

    if (n < 0) {
        return 1; // Error loading numbers
    }
     if (n == 0) {
        printf("No numbers found in file or file is empty.\n");
        return 0; // Not an error, but nothing to sort
    }


    selection_sort(numbers, n);

    // printf("Sorted array: \n"); // You can uncomment this if needed
    print_array(numbers, n);

    free(numbers); // Free the allocated memory

    return 0; // Indicate successful execution
}
