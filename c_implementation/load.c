#include <stdio.h>  // For file operations (fopen, fgets, fclose)
#include <stdlib.h> // For memory allocation (malloc, realloc, free) and string conversion (atoi)
#include <string.h> // For string functions if needed (though atoi handles basic conversion)

#define INITIAL_CAPACITY 10 // Initial size guess for the array
#define LINE_BUFFER_SIZE 256 // Max expected length of a line in the file

/**
 * @brief Loads integers from a file into a dynamically allocated array.
 * @param filename The path to the file containing numbers, one per line.
 * @param count_out Pointer to an integer where the number of loaded elements will be stored.
 * @return Pointer to the dynamically allocated array of integers, or NULL on failure.
 * The caller is responsible for freeing this memory using free().
 */
int *load_numbers(const char *filename, int *count_out) {
    FILE *file = fopen(filename, "r"); // Open file for reading
    if (file == NULL) {
        perror("Error opening file"); // Print system error message
        *count_out = 0;
        return NULL; // Indicate failure
    }

    int *numbers = NULL;         // Pointer to our dynamic array
    int count = 0;               // Number of elements currently stored
    int capacity = 0;            // Current allocated capacity of the array
    char line[LINE_BUFFER_SIZE]; // Buffer to read each line

    // Read file line by line
    while (fgets(line, sizeof(line), file) != NULL) {
        // Check if we need more space in the array
        if (count >= capacity) {
            // Calculate new capacity (double it, or start with INITIAL_CAPACITY)
            int new_capacity = (capacity == 0) ? INITIAL_CAPACITY : capacity * 2;
            // Attempt to resize the array
            int *temp = realloc(numbers, new_capacity * sizeof(int));
            if (temp == NULL) {
                perror("Error reallocating memory");
                fclose(file);
                free(numbers); // Free what we had before failing
                *count_out = 0;
                return NULL; // Indicate failure
            }
            numbers = temp;     // Update pointer to the new memory block
            capacity = new_capacity; // Update capacity
        }

        // Convert line to integer (basic conversion, ignores potential errors)
        numbers[count] = atoi(line);
        count++; // Increment the number of elements stored
    }

    fclose(file); // Close the file

    // Optional: Shrink array to exact size (can save memory if much was overallocated)
    // int *final_numbers = realloc(numbers, count * sizeof(int));
    // if (final_numbers != NULL || count == 0) { // Check if realloc worked or if count is 0
    //     numbers = final_numbers;
    // } // If realloc fails here, we just keep the slightly larger array

    *count_out = count; // Set the output parameter with the final count
    return numbers;     // Return the pointer to the loaded numbers
}

// --- Example Usage ---
int main() {
    // 1. Create a dummy file for testing
    const char *test_filename = "numbers.txt";
    FILE *outfile = fopen(test_filename, "w");
    if (!outfile) {
        perror("Failed to create test file");
        return 1;
    }
    fprintf(outfile, "10\n");
    fprintf(outfile, "-5\n");
    fprintf(outfile, "100\n");
    fprintf(outfile, "0\n");
    fprintf(outfile, "999\n");
    fclose(outfile);

    // 2. Load the numbers
    int num_count = 0;
    int *loaded_data = load_numbers(test_filename, &num_count);

    // 3. Check if loading was successful
    if (loaded_data == NULL) {
        printf("Failed to load numbers from %s\n", test_filename);
        // No need to free loaded_data if it's NULL
        return 1; // Exit with error code
    }

    // 4. Print the loaded numbers
    printf("Loaded %d numbers:\n", num_count);
    for (int i = 0; i < num_count; i++) {
        printf("%d\n", loaded_data[i]);
    }

    // 5. IMPORTANT: Free the dynamically allocated memory
    free(loaded_data);

    // Optional: Clean up the test file
    // remove(test_filename);

    return 0; // Indicate successful execution
}
