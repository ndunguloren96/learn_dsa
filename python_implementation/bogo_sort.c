#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

// Function to check if the array is sorted
bool is_sorted(int *arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            return false;
        }
    }
    return true;
}

// Function to shuffle the array
void shuffle(int *arr, int n) {
    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

// Bogo sort implementation
void bogo_sort(int *arr, int n) {
    int attempts = 0;
    while (!is_sorted(arr, n)) {
        printf("Attempt %d: ", attempts);
        for (int i = 0; i < n; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n");
        shuffle(arr, n);
        attempts++;
    }
}

// Helper function to load numbers from stdin
int load_numbers(int *arr, int max_n) {
    int n = 0;
    while (n < max_n && scanf("%d", &arr[n]) == 1) {
        n++;
    }
    return n;
}

int main() {
    srand((unsigned int)time(NULL));
    int arr[100];
    printf("Enter numbers separated by spaces (end with non-number):\n");
    int n = load_numbers(arr, 100);
    printf("Initial list: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    bogo_sort(arr, n);
    printf("Sorted list: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
