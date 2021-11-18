# CHALLENGE 1

# Write a function named `addOne` that takes an array of numbers, and returns a new array of the numbers, incremented by 1.

# Use `forEach` to loop over the input array and work with each value.  Push the new value into a local array. Return the local array;

def add_one(array):
    new_array = []

    for number in array:
        new_array.append(number + 1)

    return new_array

# print(add_one([1, 2, 3, 4, 5]))


# CHALLENGE 2

# Write a function named `addExclamation` that takes an array of strings, and returns a new array of the same strings with an "!" added to the end.

# Use `forEach` to loop over the input array. Modify each string, and add the updated value into a local array. Return the local array;

def add_exclamation(array):
    new_array = []

    for string in array:
        new_array.append(string + '!')

    return new_array

# print(add_exclamation(['hello', 'world', 'now', 'in', 'python']))



# CHALLENGE 3

# Write a function named `allUpperCase` that takes an array of strings, and returns a new array of the strings converted to upper case.

# Use `forEach` to loop over the input array. The modified strings should each be added into a local array. Return that local array.

def all_upper_case(array):
    new_array = []

    for string in array:
        new_array.append(string.upper())
    
    return new_array

print(all_upper_case(['hello', 'world', 'now', 'in', 'python']))


# CHALLENGE 4

# Write a function named `greeting` that takes in a single string and returns the string in all uppercase letters, and followed by an "!".

# Then, write a function named `speaker` that takes in an array of strings and a callback function. 

# Use `forEach` to build a new array of strings, each string modified by the callback. Return the new array. 




# CHALLENGE 5

# Write a function named addValues that takes in an array and a value and pushes the value into the array. This function does not need a return statement.

# Then, write a function named addNumbers that takes in four arguments:
#   - A number to be added to an array
#   - An array into which the number should be added
#   - The number of times the number should be added
#   - A callback function to use to add the numbers to the array (Hint: you already defined it)

# Within the addNumbers function, invoke the callback function as many times as necessary, based on the third argument of the addNumbers function.

# Return the modified array.




# CHALLENGE 6

# Write a function named createList that takes in an array of the current store intentory.

# The inventory is formatted like this:
# [
#   { name: 'apples', available: true },
#   { name: 'pears', available: true },
#   { name: 'oranges', available: false },
#   { name: 'bananas', available: true },
#   { name: 'blueberries', available: false }
# ]

# This function should use forEach to populate your grocery list based on the store's inventory. If the item is available, add it to your list. Return the final list.




# STRETCH - CHALLENGE 7

# Write a function named fizzbuzz that takes in an array of numbers.

# Iterate over the array using forEach to determine the output based on several rules:
#   - If a number is divisible by 3, add the word "Fizz" to the output array.
#   - If the number is divisible by 5, add the word "Buzz" to the output array.
#   - If the number is divisible by both 3 and 5, add the phrase "Fizz Buzz" to the output array.
#   - Otherwise, add the number to the output array.

# Return the resulting output array.

