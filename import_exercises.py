import json
import itertools as it
from statistics import mean

#Import and test 3 of the functions from your functions exercise file. Import each function in a different way:

#import the module and refer to the function with the . syntax

#use from to import the function directly

#use from and give the function a different name

from function_exercises import calculate_tip as ct
print(r"A total of 30 and tip of 15% gives you a tip of:", ct(.15, 30))

#How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
print("Total combinations: ", len(list(it.permutations(it.product('abc', '123'),1))))

#How many different combinations are there of 2 letters from "abcd"?
print("Total combinations: ", len(list(it.combinations('ABCD',2))))

#How many different permutations are there of 2 letters from "abcd"?
print("Total permutations: ", len(list(it.permutations('ABCD',2))))

profiles = json.load(open('profiles.json'))

#Total number of users
print("Total number of users: ", len(profiles))

#Number of active users
print("Number of active users: ", len([profile for profile in profiles if profile['isActive'] == True]))

#Number of inactive users
print("Number of inactive users: ", len([profile for profile in profiles if profile['isActive'] == False]))

#Grand total of balances for all users
print(f"Grand total of balances for all users: ${sum([float(profile['balance'].replace('$', '').replace(',', '')) for profile in profiles])}")

#Average balance per user
print("Average balance: ", mean([float(profile['balance'].replace('$', '').replace(',', '')) for profile in profiles]))

#User with the lowest balance
min_bal = min([float(profile['balance'].replace('$', '').replace(',', '')) for profile in profiles])
min_bal_user = {}
for profile in profiles:
    if float(profile['balance'].replace('$', '').replace(',', '')) == min_bal:
        min_bal_user = profile
print("User with the lowest balance: ", min_bal_user['name'])
#User with the highest balance
max_bal = max([float(profile['balance'].replace('$', '').replace(',', '')) for profile in profiles])
max_bal_user = {}
for profile in profiles:
    if float(profile['balance'].replace('$', '').replace(',', '')) == max_bal:
        max_bal_user = profile
print("User with the highest balance: ", max_bal_user['name'])
#Most common favorite fruit
print("Most common favorite fruit: ", max([profile['favoriteFruit'] for profile in profiles]))

#Least common favorite fruit
print("Least common favorite fruit: ", min([profile['favoriteFruit'] for profile in profiles]))

#Total number of unread messages for all users
messages = []
for profile in profiles:
    greeting = profile['greeting']
    for char in profile['greeting']:
        if char.isdigit() == False:
            greeting = greeting.replace(char, "")
    greeting.strip()
    messages.append(int(greeting))
print("Total number of unread messages for all users: ", sum(messages))