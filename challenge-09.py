
# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 1 - Review

# Write a function that finds the maximum value in an array
# using the 'reduce' method.

# E.g. [4,2,7,5,9,2] -> 9
# ------------------------------------------------------------------------------------------------ */
# const maxInArray = arr => arr.reduce((a, b) => a < b ? b : a);
def max_in_array(array):
    array.sort()

    return array[-1]


# print(max_in_array([1,4,6,3,2,4,67,78,4,2,3,4,6]))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 2

# Write a function named getCourseKeys that takes in the courseInfo object and returns an array containing the keys for the courseInfo object.

# For example: (['name', 'duration', 'topics', 'finalExam']).
# ------------------------------------------------------------------------------------------------ */
courseInfo = { 'name': 'Code 301', 'duration': { 'dayTrack': '4 weeks', 'eveningTrack': '8 weeks'},
  'topics': ['SMACSS', 'APIs', 'NodeJS', 'SQL', 'jQuery', 'functional programming'],
  'finalExam': True
};

# const getCourseKeys = obj => Object.keys(obj);
def get_course_keys(array):

    return array.keys()


# print(get_course_keys(courseInfo))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 3

# Write a function named checkValues that takes in an object and a value and returns true if the value is in the object.


# ------------------------------------------------------------------------------------------------ */

# const checkValues = (obj, value) => Object.values(obj).includes(value);

def check_values(obj, value):
    return value in obj.values()


# print(check_values(courseInfo, 'Code 301'))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 4

# You are given an object with names and their coresponding phone numbers that looks like this:
data = {
  'Grace Hopper': '222-303-5938',
  'Ada Lovelace': '222-349-9842',
  'Alan Turing': '222-853-5933'
}

# HR has asked you to change the data to make it easier to print so that it looks like this:
# [
#   'Grace Hopper: 222-303-5938',
#   'Ada Lovelace: 222-349-9842',
#   'Alan Turing: 222-853-5933'
# ]

# ------------------------------------------------------------------------------------------------ */

# const updateNumbers = obj => {
#   let arr = [];
#   for (const pair of Object.entries(obj)) {
#     arr.push(`${pair[0]}: ${pair[1]}`);
#   }
#   return arr;
# };4.""

def update_numbers(obj):
    new_arr = []
    keys = list(obj.keys())
    values = list(obj.values())
    for i in range(len(keys)):
        new_arr.append(f'{keys[i]}: {values[i]}')

    return new_arr


# print(update_numbers(data))



# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 5

# Write a function named getHouses that returns a new array containing the names of all of the houses in the data set.
# ------------------------------------------------------------------------------------------------ */

characters = [
  {
    'name': 'Eddard',
    'spouse': 'Catelyn',
    'children': ['Robb', 'Sansa', 'Arya', 'Bran', 'Rickon'],
    'house': 'Stark',
  },
  {
    'name': 'Jon',
    'spouse': 'Lysa',
    'children': ['Robin'],
    'house': 'Arryn',
  },
  {
    'name': 'Cersei',
    'spouse': 'Robert',
    'children': ['Joffrey', 'Myrcella', 'Tommen'],
    'house': 'Lannister',
  },
  {
    'name': 'Daenarys',
    'spouse': 'Khal Drogo',
    'children': ['Drogon', 'Rhaegal', 'Viserion'],
    'house': 'Targaryen',
  },
  {
    'name': 'Mace',
    'spouse': 'Alerie',
    'children': ['Margaery', 'Loras'],
    'house': 'Tyrell',
  },
  {
    'name': 'Sansa',
    'spouse': 'Tyrion',
    'house': 'Stark',
  },
  {
    'name': 'Jon',
    'spouse': False,
    'house': 'Snow',
  },
];

# const getHouses = arr => {
#   let houses = [];
#   for (const family of arr) {
#     houses.push(family.house);
#   }
#   return houses;
# };

def get_houses(array):
    new_array = []

    for person in array:
        new_array.append(person['house'])

    return new_array

print(get_houses(characters))

# /*------------------------------------------------------------------------------------------------
# CHALLENGE 6

# Write a function named hasChildrenValues that uses Object.values to determine if any given character in the data set has 'children'.

# This function should take in an array of data and a character name and return a Boolean.

# For example:
# hasChildrenValues(characters, 'Cersei') will return true
# hasChildrenValues(characters, 'Sansa') will return false
# ------------------------------------------------------------------------------------------------ */

# const hasChildrenValues = (arr, character) => {
#   let characterSelected = Object.values(arr).filter(value => value.name === character);
#   if( characterSelected[0].children) {
#     return true;
#   } else {
#     return false;
#   }
# };

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 7 - Stretch Goal

# Write a function named hasChildrenEntries that is similar to your hasChildrenValues function from challenge 4, but uses the data's entries instead of its values.

# The input and output of this function are the same as the input and output from challenge 3.
# ------------------------------------------------------------------------------------------------ */

# const hasChildrenEntries = (arr, character) => {
#   // Solution code here...
# };

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 8 - Stretch Goal

# Write a function named totalCharacters that takes in an array and returns the number of characters in the array.
# ------------------------------------------------------------------------------------------------ */

# const totalCharacters = (arr) => {
#   // Solution code here...
# };

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 9 - Stretch Goal

# Write a function named houseSize that takes in the array of characters and creates an object for each house containing the name of the house and the number of members.

# All of these objects should be added to an array named "sizes". Return the "sizes" array from the function.

# For example: [{ house: 'Stark', members: 7 }, { house: 'Arryn', members: 3 }, ... ].
# ------------------------------------------------------------------------------------------------ */

# const houseSize = (arr) => {
#   const sizes = [];
#   // Solution code here...
#   return sizes;
# };

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 10 - Stretch Goal

# As fans are well aware, "When you play the game of thrones, you win or you die. There is no middle ground."

# We will assume that Alerie Tyrell is deceased. She missed her daughter's wedding. Twice.

# Write a function named houseSurvivors. You may modify your houseSize function from challenge 6 to use as the basis of this function.

# This function should create an object for each house containing the name of the house and the number of members. If the spouse is deceased, do not include him/her in the total number of family members.

# All of these objects should be added to an array named "survivors". Return the "survivors" array from the function.

# For example: [ { house: 'Stark', members: 6 }, { house: 'Arryn', members: 2 }, ... ].
# ------------------------------------------------------------------------------------------------ */

# const deceasedSpouses = ['Catelyn', 'Lysa', 'Robert', 'Khal Drogo', 'Alerie'];

# const houseSurvivors = (arr) => {
#   const survivors = [];
#   // Solution code here...
#   return survivors;
# };

# /* ------------------------------------------------------------------------------------------------
