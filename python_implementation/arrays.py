new_list = [1, 2, 3]

# 1. Accessing elements in a list
result = new_list[0]
print(result)  # Output: 1
print(new_list[-1])
print()


# 2. Searching for an element in a list.
# i. Using in in if statement to search for an element in a list
print(1 in new_list)  # Output: True
print(2 in new_list)  # Output: True
print(4 in new_list)  # Output: False
print()

# ii. Using for loop to search for an element in a list
for n in new_list:
    if n == 1:
        print("Found it!\n")
        break


# 3. Inserting an element in a list
print(new_list)
# i. Using append() method to insert an element at the end of a list
new_list.append(4)
print(new_list)  # Output: [1, 2, 3, 4]

# ii. Using insert() method to insert an element at a specific index in a list
new_list.insert(1, 5)
print(new_list)  # Output: [1, 5, 2, 3, 4]

# iii. Using extend() method to insert multiple elements at the end of a list
# used to add a list to another list.
new_list.extend([6, 7])
print(new_list)  # Output: [1, 5, 2, 3, 4, 6, 7]

# iv. Using + operator to insert multiple elements at the end of a list
new_list += [8, 9]
print(new_list)  # Output: [1, 5, 2, 3, 4, 6, 7, 8, 9]
