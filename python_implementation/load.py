def load_numbers(filename):
    """
    Load numbers from a file into a list.
    Each number should be on a new line in the file.
    """
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line.strip()))
    return numbers
