
# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 1 - Review

# Write a function called addTwo that takes in an array and adds two to every value using a for loop. Place the new value in a new array. Return the new array.
# ------------------------------------------------------------------------------------------------ */

def add_two(array):
    new_array = []

    for num in array:
        new_array.append(num + 2)

    return new_array

# print(add_two([1, 2, 3, 4, 5]))


# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 2

# Write a function named typeNum that, given an array as input, uses filter to return an array containing only the numbers.

# For example, typeNum([1, 'bob' ,3]) returns [1,3].
# ------------------------------------------------------------------------------------------------ */

def type_num(array):
    return list(filter(lambda n : isinstance(n, int), array))


# print(type_num([3, 'bob', 1]))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 3

# Write a function named containsAnd that, given an array of strings as input, uses filter to return an array containing only strings that contain 'and' within the string.

# For example, containsAnd(['panda', 'ran', 'and']) returns ['panda', 'and'].
# ------------------------------------------------------------------------------------------------ */

def contains_and(array):

    return list(filter(lambda n : 'and' in n, array))


# print(contains_and(['panda', 'ran', 'and']))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 4

# Write a function named oddValues that, given an array of integers as input, uses filter to return an array containing only the odd integers.

# For example, oddValues([1,2,3]) returns [1,3].
# ------------------------------------------------------------------------------------------------ */

def odd_values(array):

    return list(filter(lambda n : n % 2 != 0, array))


# print(odd_values([1,2,3]))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 5

# Write a function named notInFirstArray that, given two arrays as input, uses filter to return an array of all the elements in the second array that are not included in the first array.

# For example, notInFirstArray([1,2,3], [1,2,3,4]) returns [4].
# ------------------------------------------------------------------------------------------------ */

def not_in_first_array(array1, array2):

    return list(filter(lambda n : n not in array1, array2))


# print(not_in_first_array([1, 2 ,3], [1,2,3,4]))


# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 6 - Stretch Goal

# Write a function named getBaseStatGreaterThan that, given the snorlaxData, below, and an integer as input, uses filter to return an array containing all stats with a baseStat greater than the integer.

# For example, getBaseStatGreaterThan(snorlaxData.stats, 50) will return an array containing the 'special-defense' and 'special-attack' objects.
# ------------------------------------------------------------------------------------------------ */

snorlax_data = {
  'stats': [
    {
      'stat': {
        'url': 'https://pokeapi.co/api/v2/stat/6/',
        'name': 'speed',
      },
      'effort': 5,
      'baseStat': 30,
    },
    {
      'stat': {
        'url': 'https://pokeapi.co/api/v2/stat/5/',
        'name': 'special-defense',
      },
      'effort': 2,
      'baseStat': 110,
    },
    {
      'stat': {
        'url': 'https://pokeapi.co/api/v2/stat/4/',
        'name': 'special-attack',
      },
      'effort': 9,
      'baseStat': 65,
    },
  ],
  'name': 'snorlax',
  'weight': 4600,
};

def get_base_stat_greater_than(array, num):

    return list(filter(lambda n : n['stat'] if n['baseStat'] > num else False, array))


# print(get_base_stat_greater_than(snorlax_data['stats'], 50))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 7 - Stretch Goal

# Write a function named getStatName that is an extension of your getBaseStatGreaterThan function from challenge 7. For this function, extend your solution from challenge 7 to only return the name of the stat, rather than the entire stat object.

# For example, getStatName(snorlaxData.stats, 50) will return ['special-defense', 'special-attack'].
# ------------------------------------------------------------------------------------------------ */

def get_base_stat_name(array, num):

    return list(filter(lambda n : n['stat'] if n['baseStat'] > num else False, array))


# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 8 - Stretch Goal

# Write a function named getCharactersWithoutChildren that, given the array of characters, below, uses filter to return an array of all characters without children.
# ------------------------------------------------------------------------------------------------ */

# const characters = [
#   {
#     name: 'Eddard',
#     spouse: 'Catelyn',
#     children: ['Robb', 'Sansa', 'Arya', 'Bran', 'Rickon'],
#     house: 'Stark',
#   },
#   {
#     name: 'Jon',
#     spouse: 'Lysa',
#     children: ['Robin'],
#     house: 'Arryn',
#   },
#   {
#     name: 'Cersei',
#     spouse: 'Robert',
#     children: ['Joffrey', 'Myrcella', 'Tommen'],
#     house: 'Lannister',
#   },
#   {
#     name: 'Daenarys',
#     spouse: 'Khal Drogo',
#     children: ['Drogon', 'Rhaegal', 'Viserion'],
#     house: 'Targaryen',
#   },
#   {
#     name: 'Mace',
#     spouse: 'Alerie',
#     children: ['Margaery', 'Loras'],
#     house: 'Tyrell',
#   },
#   {
#     name: 'Sansa',
#     spouse: 'Tyrion',
#     house: 'Stark',
#   },
#   {
#     name: 'Jon',
#     spouse: null,
#     house: 'Snow',
#   },
# ];



# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 9 - Stretch Goal

# Write a function named evenOddNumericValues that, given an array as input, uses filter to remove any non-numeric values, then uses map to generate a new array containing the string 'even' or 'odd', depending on the original value.

# For example: evenOddNumericValues(['Gregor', 2, 4, 1]) returns ['even', 'even', 'odd'].
# ------------------------------------------------------------------------------------------------ */

