import random
import sys
from load import load_numbers


def is_sorted(values):
    """Check if the list is sorted"""
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True


def bogo_sort(values):
    """Sort the list using bogo sort algorithm"""
    attempts = 0
    while not is_sorted(values):
        print(f"Attempt {attempts}: {values}")
        random.shuffle(values)
        attempts += 1
    return values


if __name__ == "__main__":
    numbers = load_numbers(sys.argv[1])
    print("Initial list:", numbers)
    sorted_numbers = bogo_sort(numbers.copy())
    print("Sorted list:", sorted_numbers)
