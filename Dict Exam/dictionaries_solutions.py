# Create an empty dictionary called dog
dog = dict()
print(dog)

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Cadbury'
dog['color'] = 'Grey'
dog['breed'] = 'Hound Group'
dog['legs'] = 4
dog['age'] = 5
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Duckie',
    'last_name': 'Turkey',
    'gender': 'Male',
    'age': 35,
    'martial status': 'Single',
    'skills': ['sculpting', 'foraging', 'cooking'],
    'country': 'Texas',
    'city': 'Amarillo',
    'address': '2391 Smithfield Avenue'
}
print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(type(student['skills']))

# Modify the skills values by adding one or two skills
update_skills = {'skills': ['sorcery', 'signing']}
student.update(update_skills)
print(student)

# Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
student.popitem()
print(student)

dog.pop('legs')
print(dog)

# Delete one of the dictionaries
del dog
