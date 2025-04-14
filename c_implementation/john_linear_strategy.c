#include <stdio.h>

// Function to find a target number using sequential search
void find_number_sequentially() {
    int start_range, end_range, target_number;

    // Input the range and target number
    printf("Enter the starting range: ");
    scanf("%d", &start_range);
    printf("Enter the ending range: ");
    scanf("%d", &end_range);
    printf("Enter the target number: ");
    scanf("%d", &target_number);

    int tries = 0;
    for (int i = start_range; i <= end_range; i++) {
        tries++;
        if (i == target_number) {
            printf("Target number %d found in %d tries.\n", target_number, tries);
            return;
        }
    }

    // If the loop completes, the target was not found
    printf("Target number not found in the specified range.\n");
}

int main() {
    find_number_sequentially();
    return 0;
}
