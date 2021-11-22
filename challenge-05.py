
# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 1 - Review

# Write a function that iterates over an array of people objects
# and creates a new list of each person's full name using the array method 'map'.
# Each object will have the shape {firstName:string, lastName:string}
# E.g. [ { firstName:"Jane", lastName:"Doe" }, { firstName:"James", lastName:"Bond"}]
# should convert to ["Jane Doe", "James Bond"]
# Note the space in between first and last names.
# You can assume that neither firstName nor lastName will be blank
# ------------------------------------------------------------------------------------------------ */

def print_names(array):
    new_array = []

    for person in array:
        new_array.append(f"{person['first_name']} {person['last_name']}")

    return new_array


# print(print_names([{ 'first_name':"Jane", 'last_name':"Doe" }, { 'first_name':"James", 'last_name':"Bond"}]))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 2

# Write a function named addValues that, given an array of numbers as input, uses reduce to add the values in the array.

# ------------------------------------------------------------------------------------------------ */

def add_values(array):
    return sum(array)


print(add_values([1, 2, 3, 4, 5]))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 3

# Write a function named addPurchases that, given an array of objects as input, uses reduce to find the total amount purchased. Each object contains the keys `item` and `purchasePrice` like the example.

# {
#   item: 'switch'
#   purchasePrice: 399
# }

# ------------------------------------------------------------------------------------------------ */

# const addPurchases = arr => arr.reduce((acc, item) => acc + item.purchasePrice, 0);

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 4

# Write a function named countNumberOfElements that, given an array as input, uses reduce to count the number of elements in the array.

# Note: You may not use the array's built-in length property.
# ------------------------------------------------------------------------------------------------ */



# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 5

# Write a function named returnNames that, given the Star Wars data, below, uses reduce to return an array containing the names of the characters.
# ------------------------------------------------------------------------------------------------ */

# let starWarsData = [{
#   name: 'Luke Skywalker',
#   height: '172',
#   mass: '77',
#   hair_color: 'blond',
#   skin_color: 'fair',
#   eye_color: 'blue',
#   birth_year: '19BBY',
#   gender: 'male',
# },
# {
#   name: 'C-3PO',
#   height: '167',
#   mass: '75',
#   hair_color: 'n/a',
#   skin_color: 'gold',
#   eye_color: 'yellow',
#   birth_year: '112BBY',
#   gender: 'n/a'},
# {
#   name: 'R2-D2',
#   height: '96',
#   mass: '32',
#   hair_color: 'n/a',
#   skin_color: 'white, blue',
#   eye_color: 'red',
#   birth_year: '33BBY',
#   gender: 'n/a'
# },
# {
#   name: 'Darth Vader',
#   height: '202',
#   mass: '136',
#   hair_color: 'none',
#   skin_color: 'white',
#   eye_color: 'yellow',
#   birth_year: '41.9BBY',
#   gender: 'male'
# },
# {
#   name: 'Leia Organa',
#   height: '150',
#   mass: '49',
#   hair_color: 'brown',
#   skin_color: 'light',
#   eye_color: 'brown',
#   birth_year: '19BBY',
#   gender: 'female'
# }];



# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 6

# Write a function named reversedString that takes in a string and returns a string with the letters in reverse order.

# Note: You must use reduce for this challenge. You may not use the built-in .reverse() string method.
# ------------------------------------------------------------------------------------------------ */



# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 7 - Stretch Goal

# Write a function named countNumberOfChildren that, given the array of characters, below, uses reduce to return the total number of children in the data set.
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
# CHALLENGE 8 - Stretch Goal

# Write a function that, given an array of numbers as input, uses reduce to calculate the array's average value.

# Hint: The accumulator should begin as { count: 0, sum: 0 }
# ------------------------------------------------------------------------------------------------ */



# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 9 - Stretch Goal

# Write a function named countPrimeNumbers that, given an array elements as input, uses reduce to count the number of elements that are prime numbers.

# You are welcome to use the provided isPrime function.
# ------------------------------------------------------------------------------------------------ */

# const isPrime = (value) => {
#   for (let i = 2; i < value; i++) {
#     if (value % i === 0) {
#       return false;
#     }
#   }
#   return value > 1;
# };



# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 10 - Stretch Goal

# Write a function named extractState that, given the snorlaxData, below, uses reduce to return the object whose 'name' property matches the given string.

# If the input array does not have a stat with that specific name, the function should return null.
# ------------------------------------------------------------------------------------------------ */

# const snorlaxData = {
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


# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 11 - Stretch Goal

# Write a function named extractChildren that, given the array of characters from challenge 4, accomplishes the following:

# 1) Uses filter to return an array of the characters that contain the letter 'a' in their name

# 2) Then, uses reduce to return an array of all the children's names in the filtered array
# ------------------------------------------------------------------------------------------------ */


