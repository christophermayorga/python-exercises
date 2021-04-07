# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = []
for fruit in fruits:
    uppercased_fruits.append(fruit.upper())
uppercased_fruits
# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = []
for fruit in fruits:
    capitalized_fruits.append(fruit.title())
capitalized_fruits
# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
def count_vowels(x):
    count = 0
    vowel = set ('aeiouAEIOU')
    for element in x:
        if element in vowel:
            count += 1
    return count

[fruit for fruit in fruits if count_vowels(fruit) > 2]
# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
[fruit for fruit in fruits if count_vowels(fruit) == 2]

# Exercise 5 - make a list that contains each fruit with more than 5 characters
[fruit for fruit in fruits if len(fruit) > 5]

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
[fruit for fruit in fruits if len(fruit) == 5]

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
[fruit for fruit in fruits if len(fruit) < 5]

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
[len(fruit) for fruit in fruits]

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
def has_a(name):
    name.lower()
    a = name.count('a')
    if a>0:
        return True
    else:
        return False
fruits_with_letter_a = [fruit for fruit in fruits if has_a(fruit) == True]

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
def is_even(number):
    remainder=number%2
    if remainder==0:
        return True
    else:
        return False
even_numbers = [num for num in numbers if is_even(num) == True]

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
def is_odd(number):
    remainder=number%2
    if remainder==0:
        return False
    else:
        return True
odd_numbers = [num for num in numbers if is_odd(num) == True]

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
def is_positive(number):
    if number > 0:
        return True
    else:
        return False
positive_numbers = [num for num in numbers if is_positive(num) == True]

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
def is_negative(number):
    if number < 0:
        return True
    else:
        return False
negative_numbers = [num for num in numbers if is_negative(num) == True]

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
[number for number in numbers if number >= 10 or number <= -10]

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
[num ** 2 for num in numbers]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
def is_negative_odd(number):
    remainder=number%2
    if number<0 and remainder>0:
        return True
    else:
        return False
odd_negative_numbers = [num for num in numbers if is_negative_odd(num) == True]

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [num + 5 for num in numbers]

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
def is_prime(n):
   if n <= 1:
      return False
   else:
      for i in range(2, n):
         # checking for factor
         if n % i == 0:
            # return False
            return False
      # returning True
   return True
primes = [num for num in numbers if is_prime(num) == True]