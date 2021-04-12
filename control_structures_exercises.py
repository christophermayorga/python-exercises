#prompt the user for a day of the week, print out whether the day is Monday or not
day_of_week = ''
day_of_week = input('Please input a day of week: ')
if day_of_week.lower() ==  'monday':
    print('That\'s Monday')
else:
    print('That\'s not Monday')

#prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day_of_week = ''
day_of_week = input('Input a day of week: ')
if day_of_week.lower().startswith('s'):
    print('weekend')
else:
    print('weekday')

#create variables and make up values for

#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. 
#You get paid time and a half if you work more than 40 hours
hours_worked = 45
hourly_rate = 20
paycheck = 0
if hours_worked <= 40:
    paycheck = hours_worked * hourly_rate
    print(paycheck)
if hours_worked > 40:
    paycheck = (40 * hourly_rate) + ((hours_worked - 40) * (hourly_rate * 1.5))
    print(paycheck)
else:
    pass

#While

#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i < 16:
    print(i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.

i = 0
while i < 101:
    print(i)
    i += 2

#Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5

#Create a while loop that starts at 2, and displays the number squared on each line while the 
# number is less than 1,000,000.
i = 2
while i < 1000000:
    print(i)
    i **= 2

#Write a loop that uses print to create the output shown below.
i = 100
while i != 0:
    print(i)
    i -= 5

#For Loops
#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

num = input('Enter a number ')
num = int(num)
for i in range(1, 11):
    print (num, 'x', i, '=', num*i)

#Create a for loop that uses print to create the output shown below
for i in range(1,10):
    print(str(i) * i)

#2c
while True:
    posited_num = input('Please insert an odd number between 1 and 50: ')
    if posited_num.isdigit():
        if int(posited_num) % 2 == 1 and int(posited_num) <= 50:
            break

posited_num = int(posited_num)
for num in range(1, 50, 2):
    if num == posited_num:
        print('Yikes! Skipping number: ', num)
    else:
        print('Here is an odd number: ', num)

#2d

while True:
    posited_num = input('Please insert a positive integer: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
posited_num = int(posited_num)        
for num in range(0, posited_num + 1):
    print(num)

#2e
while True:
    posited_num = input('Please insert a positive integer: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
posited_num = int(posited_num)        
for num in range(posited_num, 0, -1):
    print(num)

#3
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

#4
while True:
    posited_num = input('Please insert a positive integer: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
proceed = input('Do you want to continue and print a table of powers? :')
if proceed.lower().startswith('y'):
    posited_num = int(posited_num)
    print()
    print('number  |  squared  |  cubed')
    print('------  |  -------  |  -----')
    for i in range(1, posited_num + 1):
        i_squared = i ** 2
        i_cubed = i ** 3
        print(f'{i: 6}  |  {i_squared: 7}  |  {i_cubed: 5}')

#5
while True:
    user_number = input("Please enter a numerical between 0 and 100")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number < 0 or user_number > 100:
            continue
        break

grade = user_number
if grade in range(60):
    grade = 'F'
elif grade in range(60,67):
    grade = 'D'
elif grade in range(67,80):
    grade = 'C'
elif grade in range(80,88):
    grade = 'B'
else:
    grade = 'A'

#6
bookshelf = [
    {'title': 'The Lightning Thief',
    'author': 'Rick Riordan',
    'genre': 'fantasy adventure'},
    {'title': 'Parable of the Sower',
    'author': 'Octavia Butler',
    'genre': 'science fiction'},
    {'title': 'The Hunger Games',
    'author': 'Suzanne Collins',
    'genre': 'young adult dystopian'},
    {'title': 'Divergent',
    'author': 'Veronica Roth',
    'genre': 'young adult dystopian'}
]

for book in bookshelf:
    [print(key,': ', book[key]) for key in book]
    print('---------')

picked_genre = input('Please pick a genre and I will return the titles we have on the shelf: ')

matches = []
for book in bookshelf:
    if book['genre'].lower() == picked_genre.lower():
        matches.append(book['title'])
if matches == []:
    print("No books in that genre right now. Please check back later!")
else:
    print(f'I have the following titles in the genre {picked_genre}')