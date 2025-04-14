#include <stdio.h>

// Function to find a target number using binary search
void find_number_binary_simple_with_value() {
    int start_range, end_range, target_number;

    // Input the range and target number
    printf("Enter the starting range: ");
    scanf("%d", &start_range);
    printf("Enter the ending range: ");
    scanf("%d", &end_range);
    printf("Enter the target number: ");
    scanf("%d", &target_number);

    int low = start_range;
    int high = end_range;
    int tries = 0;

    while (low <= high) {
        tries++;
        int mid = (low + high) / 2;

        if (mid == target_number) {
            printf("Target number %d found in %d tries.\n", target_number, tries);
            return;
        } else if (mid < target_number) {
            printf("%d is too low.\n", mid);
            low = mid + 1;
        } else {
            printf("%d is too high.\n", mid);
            high = mid - 1;
        }
    }

    // If the loop completes, the target was not found
    printf("Target number not found in the specified range.\n");
}

int main() {
    find_number_binary_simple_with_value();
    return 0;
}
