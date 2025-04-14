# John's strategy = sequential search
def find_number_sequentially():  # define the function find_number_sequentially
    """
    Finds a target number in a list using sequential search.
    """
    # variables
    start_range = int(input("Enter the starting range: "))
    end_range = int(input("Enter the ending range: "))  # variables
    target_number = int(input("Enter the target number: "))

    number_list = list(range(start_range, end_range + 1))

    if target_number not in number_list:
        print("Target number not found in the specified range.")
        # print("The target number is in the specified range of value.")
        return

    tries = 0
    for number in number_list:
        tries += 1  # tries = tries + 1
        if number == target_number:
            print(f"Target number {target_number} found in {tries} tries.")
            return


# Example usage
find_number_sequentially()
