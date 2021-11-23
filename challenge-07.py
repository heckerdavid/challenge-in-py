
# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 1 - Review

# Write a function called sortStarWarsCharacters that sorts the characters in the starWarsPeople array by height from tallest to shortest.
# ------------------------------------------------------------------------------------------------ */

starWarsPeople = [
  {
    "name": "C-3PO",
    "height": "167",
    "eye_color": "yellow"
  },
  {
    "name": "Luke Skywalker",
    "height": "172",
    "eye_color": "blue"
  },
  {
    "name": "R2-D2",
    "height": "96",
    "eye_color": "red"
  }
];

# const sortStarWarsCharacters = starWarsArr => starWarsArr.sort((a, b) => b.height - a.height);

def sort_star_wars_characters(array):

    array.sort(key = lambda n : int(n['height']))

    return array


print(sort_star_wars_characters(starWarsPeople))

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 2

# Write a function named removeThree that takes an index and an array. The function should removes three items in the array starting with the value at the index. 
# ------------------------------------------------------------------------------------------------ */

# const removeThree = (idx, arr) => {
#   arr.splice(idx, 3);
#   return arr;
# };

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 3

# Write a function named joinArray that takes an array and joins all of the elements together in one string on a space.
# ------------------------------------------------------------------------------------------------ */

# const joinArray = arr => arr.join(' ');

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 4

# Write a function named howMuchPencil that takes in a string, as written on the side of a pencil.

# As you sharpen the pencil, the string will become shorter and shorter, starting by removing the first letter.

# Your function should use slice within a loop and return an array of each successive string result from losing letters to the sharpener, until nothing is left.

# For example, if the input is 'Welcome', the output will be:
# ['Welcome', 'elcome', 'lcome', 'come', 'ome', 'me', 'e', ''].
# ------------------------------------------------------------------------------------------------ */

# const howMuchPencil = (str) => {
#   let result = [];
#   result.push(str);
#   for (let i = 0; i < str.length; i) {
#     str = str.slice(1);
#     result.push(str);
#   }
#   return result;
# };

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 5

# Write a function name wordsToCharList that, given a string as input, returns a new array where every element is a character of the input string.

# For example, wordsToCharList('gregor') returns ['g','r','e','g','o','r'].
# ------------------------------------------------------------------------------------------------ */

# const wordsToCharList = arr => arr.split('');


# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 6

# You are making a grocery list for ingredients needed in the gruffalo crumble recipe, below. Rather than taking the entire recipe, you only want a list of the item names.

# Write a function named listFoods that takes in the recipe and returns a new array of the food items without any amount or units. Just the name. For example, '1 cup flour' will return 'flour'.

# Use slice for this function, maybe more than once. The Array.indexOf() method may also be helpful.

# Do not use split for this function.
# ------------------------------------------------------------------------------------------------ */

# const gruffaloCrumble = {
#   name: 'How to make a Gruffalo Crumble',
#   ingredients: [
#     '1 medium-sized Gruffalo',
#     '8 pounds oats',
#     '2 pounds brown sugar',
#     '4 pounds flour',
#     '2 gallons pure maple syrup',
#     '16 cups chopped nuts',
#     '1 pound baking soda',
#     '1 pound baking powder',
#     '1 pound cinnamon',
#     '6 gallons melted butter',
#     '2 gallons fresh water',
#   ],
#   steps: [
#     'Pre-heat a large oven to 375',
#     'De-prickle the gruffalo',
#     'Sprinkle with cinnamon, sugar, flour, and nuts',
#     'Mix until evenly distributed',
#     'Grease a 3-foot x 3-foot casserole dish',
#     'Combine gruffalo compote with water to maintain moisture in the oven',
#     'Fold together remaining ingredients to make the crisp',
#     'Spread the crisp evenly over the gruffalo mixture',
#     'Bake for 12-15 hours',
#   ]
# };


# const listFoods = recipe => recipe.ingredients.map((str) => str.replace(/\d+ \w+ |\d+ \w+.\w+ /g, ''));

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 7 - Stretch Goal

# Write a function named splitFoods that uses split to produce the same output as Challenge 3.

# You may also use other string or array methods.
# ------------------------------------------------------------------------------------------------ */

# const splitFoods = (recipe) => {
#   let result = [];
#   // Solution code here...
#   return result;
# };

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 8 - Stretch Goal

# Use the same recipe from Challenge 3, above.

# Write a function named stepAction that takes in the recipe and extracts the action verbs from the steps. Fortunate for you, the action verbs are the first word of each action.

# Return a new array containing just the verbs. For example, ['Mix until evenly distributed'] returns ['Mix'].
# ------------------------------------------------------------------------------------------------ */

# const stepActions = (recipe) => {
#   let result = [];
#   // Solution code here...
#   return result;
# };

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 9 - Stretch Goal

# Write a function named removeEvenValues that, given an array of integers as input, deletes all even values from the array, leaving no 'gaps' behind.

# The array should be modified in-place.

# For example:
#   const integers = [1, 2, 3, 4, 5, 6];
#   removeEvenValues(integers);
#   console.log(integers) will print [1, 3, 5]
# ------------------------------------------------------------------------------------------------ */

# const removeEvenValues = (arr) => {
#   // Solution code here...
# };

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 10 - Stretch Goal

# Write a function named removeLastCharacters that takes in a string and a number. The numberOfCharacters argument determines how many characters will be removed from the end of the string. Return the resulting string.

# If the numberOfCharacters argument is greater than the length of the input string, the function should return an empty string.

# If the numberOfCharacters argument input is a negative number, the function should return the input string without any changes.

# For example:
# removeLastCharacters('Gregor', 2) returns 'Greg'
# removeLastCharacters('Gregor', -2) returns 'Gregor'
# removeLastCharacters('Gregor', 9) returns ''
# ------------------------------------------------------------------------------------------------ */

# const removeLastCharacters = (str, numberOfCharacters) => {
#   // Solution code here...
# };


# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 11 - Stretch Goal

# Write a function named totalSumCSV that, given a string of comma-separated values (CSV) as input. (e.g. "1,2,3"), returns the total sum of the numeric values (e.g. 6).
# ------------------------------------------------------------------------------------------------ */

# const totalSumCSV = (str) => {
#   let total = 0;
#   // Solution code here...
#   return total;
# };


# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 12 - Stretch Goal

# Write a function named removeVowels that takes in a string and returns a new string where all the vowels of the original string have been removed.

# For example, removeVowels('gregor') returns 'grgr'.
# ------------------------------------------------------------------------------------------------ */

# const removeVowels = (str) => {
#   // Solution code here...
# };

# /* ------------------------------------------------------------------------------------------------
# CHALLENGE 13 - Stretch Goal

# Write a function named extractVowels that takes in a string and returns an array where the first element is the original string with all the vowels removed, and the second element is a string of all the vowels that were removed, in alphabetical order.

# For example, extractVowels('gregor') returns ['grgr', 'eo'].

# Similarly, extractVowels('The quick brown fox') returns ['Th qck brwn fx', 'eioou']
# ------------------------------------------------------------------------------------------------ */

# const extractVowels = (str) => {
#   // Solution code here...
# };
