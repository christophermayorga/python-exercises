#Define a function named is_two. It should accept one input and return True if the passed input 
# is either the number or the string 2, False otherwise.

def is_two(n):
    return n == '2' or n == 2

#Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(str):
    if str in 'aeiouAEIOU':
        return True
    else:
        return False

#Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(str):
    if is_vowel(str) == True:
        return False
    else:
        return True

#Define a function that accepts a string that is a word. The function should capitalize the first 
# letter of the word if the word starts with a consonant.
def capitalize_first(str):
    if is_consonant(str[0]) == True:
        return str.capitalize()
    else:
        return str

#Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.
def calculate_tip(tip, total):
    if tip > 0 and tip < 1:
        return tip * total

#Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.
def apply_discount(original, discount):
    if discount > 0 and discount < 1:
        new_price = original - (original * discount)
        return new_price

#Define a function named handle_commas. It should accept a string that is a number that contains commas 
# in it as input, and return a number as output.
def handle_commas(str):
    return int(str.replace(',', ''))

#Define a function named get_letter_grade. It should accept a number and return the 
# letter grade associated with that number (A-F).
def get_letter_grade(num):
    if num >= 0 and num < 60:
        return ("F")
    if num >= 60 and num < 70:
        return ("D")
    if num >= 70 and num < 80:
        return ("C")
    if num >= 80 and num < 90:
        return ("B")
    if num >= 90:
        return ("A")

#Define a function named remove_vowels that accepts a string and returns a string with all 
# the vowels removed.
def remove_vowels(word):
    vowels = "aeiouAEIOU"
    for char in vowels:
        word = word.replace(char, "")
    return word

#Define a function named normalize_name. It should accept a string and return a
#  valid python identifier, that is:
def normalize_name(string):
    string = string.lower()
    string = string.strip()
    string = string.replace(" ", "_")
    for i in string:
        if i.isdigit() == True or i.isalpha() == True or i == "_":
            continue
        else:
            string = string.replace(i, "")
    return string

#Write a function named cumulative_sum that accepts a list of numbers and returns a list 
# that is the cumulative sum of the numbers in the list.
def cumulative_sum(numbers):
    new_numbers = []
    sums = []
    for num in numbers:
        new_numbers.append(num)
        sums.append(sum(new_numbers))
    return sums

#Create a function named twelveto24. It should accept a string in the format 10:45am or 
# 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.

def twelveto24(time):
    single_numbers = ("2, 3, 4, 5, 6, 7, 8, 9")
    tuple_single_numbers = tuple(map(str, single_numbers.split(', ')))
    if time.endswith("am"):
        if time.startswith("12"):
            time = time.replace(time[-1], "").replace(time[-2], "").replace("12", "00", 1)
            return time
        if time.startswith("1"):
            if time.startswith("10") or time.startswith("11"):
                time = time.replace(time[-1], "").replace(time[-2], "")
                return time
            else:
                time = time.replace(time[-2], "").replace(time[-1], "").replace(time[0], "0"+time[0], 1)
                return time
        if time.startswith(tuple_single_numbers):
            time = time.replace(time[-2], "").replace(time[-1], "").replace(time[0], "0"+time[0], 1)
            return time
    if time.endswith("pm"):
        if time.startswith("1"):
            if time.startswith("12"):
                time = time.replace(time[-1], "", 1).replace(time[-2], "", 1)
                return time
            if time.startswith("10") or time.startswith("11"):
                time = time.replace(time[0:2], str(int(time[0:2]) + 12), 1).replace(time[-1], "").replace(time[-2], "")
                return time
            if time.startswith("1"):
                time = time.replace(time[-2], "").replace(time[-1], "").replace(time[0], str(int(time[0]) + 12),1)
                return time
        if time.startswith(tuple_single_numbers):
            time = time.replace(time[-2], "").replace(time[-1], "").replace(time[0], str(int(time[0]) + 12),1)
            return time