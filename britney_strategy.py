def find_number_binary_simple_with_value():
    """
    Finds a target number using a simplified binary search strategy, showing the guessed value.
    """

    start_range = int(input("Enter the starting range: "))
    end_range = int(input("Enter the ending range: "))
    target_number = int(input("Enter the target number: "))

    number_list = list(range(start_range, end_range + 1))

    if target_number not in number_list:
        print("Target number not found in the specified range.")
        return

    low = 0
    high = len(number_list) - 1
    tries = 0

    while low <= high:
        tries += 1
        mid = (low + high) // 2
        guess = number_list[mid]

        if guess == target_number:
            print(f"Target number {target_number} found in {tries} tries.")
            return
        elif guess < target_number:
            print(f"{guess} is too low.")
            low = mid + 1
        else:
            print(f"{guess} is too high.")
            high = mid - 1

    # This line should not be reached if the number is in the list.
    print("Error: Target number not found (shouldn't happen).")


# Example usage
find_number_binary_simple_with_value()
