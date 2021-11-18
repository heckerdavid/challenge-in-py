
# /* ------------------------------------------------------------------------------------------------

# CHALLENGE 1 - Review

# Write a function named raisedToTheThird that takes in an array of numbers and returns a new array of each of those numbers raised to the 3rd power (hint: look up Math.pow()). Use forEach to solve this problem.

# ------------------------------------------------------------------------------------------------ */

def raised_to_the_third(array):
    new_array = []

    for number in array:
        new_array.append(pow(number, 3))
    
    return new_array

# print(raised_to_the_third([1, 2, 3, 4, 5]))


# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 2

# Write a function named addOne that, given an array of numbers, uses map to return a new array with each value simply incremented by 1. 
# ------------------------------------------------------------------------------------------------ */

def add_one(array):

    return list(map(lambda n : n + 1, array))


# print(add_one([1, 2, 3, 4, 5]))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 3

# Write a function named addQuestion that, given an array of strings, uses map to return a new array containing each string followed by a question mark character.
# ------------------------------------------------------------------------------------------------ */

def add_question(array):

    return list(map(lambda string : string + '?', array))

# print(add_question(['hello', 'world', 'now', 'in', 'python']))


# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 4

# Write a function named forLoopTwoToThe that, given an array of integers as input, iterates over the array and returns a new array. The returned array should contain the result of raising 2 to the power of the original input element.

# You may choose to complete this challenge using a for loop, for...in syntax, or for...of syntax.

# For example, twoToThe([1,2,3]) returns [2,4,8] because 2 ^ 1 = 2, 2 ^ 2 = 4, and 2 ^ 3 = 8.
# ------------------------------------------------------------------------------------------------ */

def for_loop_two_to_the(array):

    return list(map(lambda n : 2 ** n, array))

# print(for_loop_two_to_the([1, 2, 3, 4, 5]))




# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 5

# Write a function named forEachTwoToThe that produces the same output as your forLoopTwoToThe function from challenge 4, but uses forEach instead of a for loop.
# ------------------------------------------------------------------------------------------------ */

def for_each_two_to_the(array):

    return list(map(lambda n : 2 ** n, array))

# print(for_each_two_to_the([1, 2, 3, 4, 5]))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 6

# Write a function named mapTwoToThe that produces the same output as your forLoopTwoToThe function from challenge 4 and your forEachTwoToThe function from challenge 5, but uses map instead of a for loop or forEach.
# ------------------------------------------------------------------------------------------------ */

def for_each_two_to_the(array):

    return list(map(lambda n : 2 ** n, array))

# print(for_each_two_to_the([1, 2, 3, 4, 5]))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 7 - Stretch Goal

# Write a function named charCode that, given an array of letters as an input, uses map to return a new array where each element is the result of the `charCodeAt` method on the original array element.

# Read the MDN documentation on String.charCodeAt() if necessary.

# For example: charCode(['h','i']) returns [104, 105].
# ------------------------------------------------------------------------------------------------ */

def char_code(array):

    return list(map(lambda n : ord(n), array))


# print(char_code(['a', 'b', 'c', 'd', 'h', 'i']))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 8 - Stretch Goal

# Write a function that, given an array of numbers as input, uses map to return a new array where each element is either the string "even" or the string "odd", based on each value.

# If any element in the array is not a number, the resulting array should have the string "N/A" in its place.

# For example: evenOdd([1,2,3]) returns ['odd','even','odd'].
# ------------------------------------------------------------------------------------------------ */

def even_odd(array):

    return list(map(lambda n : 'even' if n % 2 == 0 else 'odd', array ))


# print(even_odd([1, 2, 3]))


# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 9 - Stretch Goal

# Use the snorlaxAbilities data, below, for this challenge.

# Write a function named extractAbilities that, given the array of abilities, uses map to create an array containing only the ability name.

# Note: Because this function is expecting the array of abilities, it will be invoked as:
# extractAbilities(snorlaxAbilities.abilities)
# ------------------------------------------------------------------------------------------------ */

snorlax_abilities = {
  'abilities': [
    {
      'slot': 3,
      'is_hidden': True,
      'ability': {
        'url': 'https://pokeapi.co/api/v2/ability/82/',
        'name': 'gluttony',
      },
    },
    {
      'slot': 2,
      'is_hidden': False,
      'ability': {
        'url': 'https://pokeapi.co/api/v2/ability/56/',
        'name': 'cute charm',
      },
    },
    {
      'slot': 1,
      'is_hidden': False,
      'ability': {
        'url': 'https://pokeapi.co/api/v2/ability/17/',
        'name': 'immunity',
      },
    },
  ],
  'name': 'snorlax',
  'weight': 4600,
};

def extract_abilities(array):
     
    return list(map(lambda item : item['ability']['name'], array))


print(extract_abilities(snorlax_abilities['abilities']))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 10 - Stretch Goal

# Use the snorlaxStats data, below, for this challenge.

# Write a function named extractStats that, given an array of stats, uses map to return an array of objects containing the stat name and the total.

# The total should be the sum of the effort and the baseStat.

# Here is an example of a single array element: { name: 'speed', total: 35 }
# ------------------------------------------------------------------------------------------------ */

# const snorlaxStats = {
#   stats: [
#     {
#       stat: {
#         url: 'https://pokeapi.co/api/v2/stat/6/',
#         name: 'speed',
#       },
#       effort: 5,
#       baseStat: 30,
#     },
#     {
#       stat: {
#         url: 'https://pokeapi.co/api/v2/stat/5/',
#         name: 'special-defense',
#       },
#       effort: 2,
#       baseStat: 110,
#     },
#     {
#       stat: {
#         url: 'https://pokeapi.co/api/v2/stat/4/',
#         name: 'special-attack',
#       },
#       effort: 9,
#       baseStat: 65,
#     },
#   ],
#   name: 'snorlax',
#   weight: 4600,
# };

