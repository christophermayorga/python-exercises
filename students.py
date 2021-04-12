from statistics import mean
from collections import Counter
students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

#How many students are there?

print("There are", len(students), "students.")

#How many students prefer light coffee? For each type of coffee roast?
prefer_light = []
for student in students:
    if student["coffee_preference"] == "light":
        prefer_light.append(student)
    else:
        continue
print(len(prefer_light), "students prefer light coffee.")

prefer_light = []
prefer_medium = []
prefer_dark = []
for student in students:
    if student["coffee_preference"] == "light":
        prefer_light.append(student)
    if student["coffee_preference"] == "medium":
        prefer_medium.append(student)
    if student["coffee_preference"] == "dark":
        prefer_dark.append(student)
    else:
        continue
print(len(prefer_light), "students prefer light coffee.")
print(len(prefer_medium), "students prefer medium coffee.")
print(len(prefer_dark), "students prefer dark coffee.")

#How many types of each pet are there?
horses = []
dogs = []
cats = []
for student in students:
    pets = student["pets"]
    for species in pets:
        pet_species = species['species']
        if pet_species == 'horse':
            horses.append(pet_species)
        if pet_species == 'dog':
            dogs.append(pet_species)
        if pet_species == 'cat':
            cats.append(pet_species)

print((f'Number of horses: {len(horses)}'))
print((f'Number of dogs: {len(dogs)}'))
print((f'Number of cats: {len(cats)}'))

#How many grades does each student have? Do they all have the same number of grades?
for student in students:
    number_of_grades = len(student["grades"])
    print(f"{student['student']} has {number_of_grades} grade(s)")
print("All students have 4 grades.")

#What is each student's grade average?
for student in students:
    avg_grade = sum(student["grades"])/len(student["grades"])
    print(f"{student['student']}'s average grade is {avg_grade}")

#How many pets does each student have?
for student in students:
    number_of_pets = len(student["pets"])
    print(f"{student['student']} has {number_of_pets} pet(s)")

#How many students are in web development? data science?
web_dev_students = []
ds_students = []
for student in students:
    course = student["course"]
    if course == "web development":
        web_dev_students.append(student)
    if course == "data science":
        ds_students.append(student)
print("There are", len(web_dev_students), "in the web development course.")
print("There are", len(ds_students), "in the data science course.")

#What is the average number of pets for students in web development?
web = 0
pets = 0
for student in students:
    if student['course'] == 'web development':
        web += 1
        pets += len(student['pets'])
print('Web Development students have an average of', (pets / web), 'pets.')

#What is the average pet age for students in data science?
total_age = 0
number_pets = 0
for student in students:
    if student['course'] == 'data science':
        pets = student['pets']
        for pet in pets:
            total_age += pet['age']
            number_pets += 1
average_age = (total_age / number_pets)            
print(f'The average pet age for students in Data Science is {average_age}.')

#What is most frequent coffee preference for data science students?
light = 0
medium = 0
dark = 0

for student in students:
    if student['course'] == 'data science':
        if student['coffee_preference'] == 'light':
            light += 1
        if student['coffee_preference'] == 'medium':
            medium += 1
        if student['coffee_preference'] == 'dark':
            dark += 1
coffee_choices = dict(light = light, medium = medium, dark = dark)
coffee_preference = max(coffee_choices, key=coffee_choices.get)    
print("The most common coffee preference for data science students is", coffee_preference)


#What is the least frequent coffee preference for web development students?
coffee_prefs_wd = []
for c in students:
    if c['course'] != 'web development':
        continue
    else:
        coffee_prefs_wd.append(c['coffee_preference'])
pref_counts_wd = Counter(coffee_prefs_wd)
least_common_list = pref_counts_wd.most_common()[:-2-1:-1]
leastcommonwd1, lcwdcounter1 = least_common_list[0]
leastcommonwd2, lcwdcounter2 = least_common_list[1]
print('The least common preferences for the web development are',
    leastcommonwd1, 'and', leastcommonwd2)

#What is the average grade for students with at least 2 pets?
grades_total = 0
number_grades = 0
for student in students:
    if len(student['pets']) > 1:
        grades_total += sum(student['grades'])
        number_grades += len(student['grades'])
print('The average grade for students with at least 2 pets is:', (grades_total / number_grades))

#How many students have 3 pets?
have_three_pets = []
for student in students:
    if len(student['pets']) == 3:
        have_three_pets.append(student)
print(len(have_three_pets), 'student has three pets.')

#What is the average grade for students with 0 pets?
grades_total = 0
number_grades = 0
for student in students:
    if len(student['pets']) == 0:
        grades_total += sum(student['grades'])
        number_grades += len(student['grades'])
print('The average grade for students with at 0 pets is:', (grades_total / number_grades))

#What is the average grade for web development students? data science students?
web_dev_students = []
ds_students = []
web_dev_grades = []
ds_grades = []
for student in students:
    if student['course'] == 'data science':
        ds_students.append(student)
    if student['course'] == 'web development':
        web_dev_students.append(student)
    else:
        continue
for student in web_dev_students:
    avg_grade = mean(student['grades'])
    web_dev_grades.append(avg_grade)
print(f"Web development's average grade is {mean(web_dev_grades)}")
for student in ds_students:
    avg_grade = mean(student['grades'])
    ds_grades.append(avg_grade)
print(f"Data science's average grade is {mean(ds_grades)}")

#What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
dark_coffee_drinkers = []
ranges = []
for student in students:
    if student['coffee_preference'] == "dark":
        dark_coffee_drinkers.append(student)
for student in dark_coffee_drinkers:
    rng = max(student['grades']) - min(student['grades'])
    ranges.append(rng)
print(f"The average grade range for dark coffee drinkers is {mean(ranges)}")

#What is the average number of pets for medium coffee drinkers?
medium_coffee_drinkers = []
number_of_pets = []
for student in students:
    if student['coffee_preference'] == 'medium':
        medium_coffee_drinkers.append(student)
for student in medium_coffee_drinkers:
    num_pets = len(student['pets'])
    number_of_pets.append(num_pets)
print(f'The average number of pets for medium coffee drinkers is {mean(number_of_pets)}')

#What is the most common type of pet for web development students?
cat = 0
dog = 0
horse = 0
all_pets = []
types_of_pets = []
for student in web_dev_students:
    all_pets.append(student['pets'])
for item in all_pets:
    if len(item) == 1:
        types_of_pets.append(item[0])
    if len(item) > 1:
        for animals in item:
            types_of_pets.append(animals)
for pet in types_of_pets:
    if pet['species'] == 'horse':
        horse += 1
    if pet['species'] == 'cat':
        cat += 1
    if pet['species'] == 'dog':
        dog += 1
pet_prefs = dict(cat = cat, dog = dog, horse = horse)
most_common_pet = max(pet_prefs, key=pet_prefs.get)
print("The most common pet type for web development students is", most_common_pet)

#What is the average name length?
lengths = []
for student in students:
    lengths.append(len(student['student']))
print("The average name length is", mean(lengths), "characters.")

#What is the highest pet age for light coffee drinkers?
light_coffee_drinkers = []
all_pets = []
types_of_pets = []
pet_ages = []
for student in students:
    if student['coffee_preference'] == 'light':
        light_coffee_drinkers.append(student)
for student in light_coffee_drinkers:
    all_pets.append(student['pets'])
for item in all_pets:
    types_of_pets.append(item[0])
for pet in types_of_pets:
    pet_ages.append(pet.get('age'))
print("The highest pet age for light coffee drinkers is", max(pet_ages))