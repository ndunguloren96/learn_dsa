#  A function that calls itself


def sum(numbers):
    total = 0
    for number in numbers:
        total += number
        return total


print(sum([1, 2, 7, 9]))
