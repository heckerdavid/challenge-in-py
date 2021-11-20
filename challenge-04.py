# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 1 - Review

# Write a function named addAnimal that takes in array of animals (strings) and some callback function.

# This function should first create a new array. Then iterate over the input array and modify each value based on the callback function provided.

# Push each updated animal string into the new array. Return the new array.

# HINT: Look at the tests to see how the callback functions are used.

# ------------------------------------------------------------------------------------------------ */

def add_animal(array, callback):
    new_array = []

    for item in array:
        new_array.append(callback(item))

    return new_array



# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 2

# Write a function called sortNames that takes an array of names and sorts them alphabetically. Capital letters should come before lowercase letters.

# For example: 'Cat' would come before 'apple'
# ------------------------------------------------------------------------------------------------ */

def sort_names(array):

    array.sort()

    return array


# print(sort_names(['cat', 'Cat', 'bat', 'apple', 'zoo']))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 3

# Write a function called sortNumbers that takes an array of numbers and sorts them from smallest to largest.


# ------------------------------------------------------------------------------------------------ */

def sort_numbers(array):
    array.sort()

    return array


# print(sort_numbers([1,2,8,6,4,2,6,8,9,3,2]))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 4

# Write a function named sortBackwards that takes in an array of numbers and returns the same array, with the numbers sorted, largest to smallest.

# HINT: Do it with a custom sort callback, not with using `.reverse()`. ;)
# ------------------------------------------------------------------------------------------------ */

def sort_backwards(array):
    array.sort(reverse=True)

    return array


# print(sort_backwards([0,45,2,1,6,7,9,32,1,4,67,1]))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 5

# Write a function named alphabetize that takes in an array of strings and returns the same array with the strings sorted alphabetically.

# In this alphabetization, capital letters come before lower case letters.

# For example, ['Alphabet', 'Zebra', 'alphabet', 'carrot'] is correctly sorted.
# ------------------------------------------------------------------------------------------------ */

def alphabetize(array):

    array.sort()

    return array


# print(alphabetize(['alphabet', 'Zebra', 'Alphabet', 'carrot']))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 6

# Write a function named sortByPrice that takes in an array of objects, each of which has a 'price' property, and sorts those objects by price, lowest to highest, returning the same array.

# Here is an example of the input:
# [
#   {name: 'Sweatshirt', price: 45},
#   {name: 'Bookmark', price: 2.50},
#   {name: 'Tote bag', price: 15}
# ];
# ------------------------------------------------------------------------------------------------ */

def sort_by_price(array):
    array.sort(key = lambda n : n['price'])

    return array


# print(sort_by_price([
#   {'name': 'Sweatshirt', 'price': 45},
#   {'name': 'Bookmark', 'price': 2.50},
#   {'name': 'Tote bag', 'price': 15}
# ]))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 7 - Stretch Goal

# Write a function named alphabetizeBetter that takes in an array of strings and returns the same array, with the strings sorted alphabetically. Capitalization should not change the sort order of two strings.

# For example, ['Alphabet', 'alphabet', 'carrot', 'Zebra'] is correctly sorted, and so is ['alphabet', 'Alphabet', 'carrot', 'Zebra'].
# ------------------------------------------------------------------------------------------------ */

def alphabetize_better(array):

    array.sort(key = lambda n : n.lower())

    return array


# print(alphabetize_better(['alphabet', 'Zebra', 'Alphabet', 'carrot']))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 8 - Stretch Goal

# Write a function named sortByLength that takes in an array of strings and returns the same array, with the strings sorted by their length, lowest to highest.
# ------------------------------------------------------------------------------------------------ */

def sort_by_length(array):

    array.sort(key = lambda n : len(n))

    return array


print(sort_by_length(['alphabet', 'Zebra', 'Alphabet', 'carrot', 'dog', 'paradimethalaminobynzaldihyde']))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 9 - Stretch Goal

# Write a function named sortNumbersByLength that takes in an array of numbers and sorts those numbers by their length.

# For example, [1, 14, 0.2, -281, 54782] is only correctly sorted in that order.
# ------------------------------------------------------------------------------------------------ */



# /*-----------------------------------------------------------------------------------------------
# CHALLENGE 10 - Stretch Goal

# Write a function named sortPeople that takes in an array of Person objects, each of which has firstName, lastName, and age properties, and sorts those people by their last names. Do not worry about capitalization or first names.
# ------------------------------------------------------------------------------------------------ */

# function Person(firstName, lastName, age) {
#   this.firstName = firstName;
#   this.lastName = lastName;
#   this.age = age;
# }

# const people = [
#   new Person('Wes', 'Washington', 25),
#   new Person('Casey', 'Codefellow', 38),
#   new Person('Stan', 'Seattle', 67),
# ];

# const sortPeople = (arr) => {
#   // Solution code here...
# };

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 11 - Stretch Goal

# Write a function named sortPeopleBetter that takes in an array of Person objects, each of which has firstName, lastName, and age properties, and sorts those people by their last names.

# If two people share the same last name, alphabetize on their first name.

# If two people have the same full name, the younger one should come first. Do not worry about capitalization.
# ------------------------------------------------------------------------------------------------ */



# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 12 - Stretch Goal

# Write a function named sortMeetingsByDay that takes in an array of objects, each of which represents a meeting happening a particular day of the week, with a particular start time and end time.

# Sort the meetings by the day on which they happen, Monday-Friday. It does not matter which order meetings come in on a particular day. For example, if there are two meetings on Monday, it does not matter which comes first.
# ------------------------------------------------------------------------------------------------ */

# function Meeting(dayOfWeek, start, end) {
#   this.dayOfWeek = dayOfWeek;
#   this.start = start;
#   this.end = end;
# }
# const meetings = [
#   new Meeting('Monday', '0900', '1000'),
#   new Meeting('Wednesday', '1300', '1500'),
#   new Meeting('Tuesday', '1145', '1315'),
#   new Meeting('Wednesday', '0930', '1000'),
#   new Meeting('Monday', '0900', '0945'),
#   new Meeting('Friday', '1200', '1345'),
# ];



# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 13 - Stretch Goal

# This challenge should use the array of meetings from challenge 9, above.

# Sort the meetings in the order that they start. If two meetings start at the same time on the same day, the shorter meeting should come first.

# You DO NOT need to use your solution to Challenge 9 in completing Challenge 10.
# ------------------------------------------------------------------------------------------------ */
