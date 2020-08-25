# Use a for loop and indexing to print out only the words that start with an s in this sentence:
# Answer:
''' Secret
    super
    staying'''

mystring = "Secret agents are super good at staying hidden."
first_task = [word for word in mystring.split() if word.lower().startswith('s')]
print(first_task)

# old variant
'''for word in mystring.split():
    first_letter = word.lower()[0]
    if first_letter == 's':
        print(word)'''

# Using the same string as previously used:
# Use a for loop to only print out the words with an even number of characters/letters.
# Answer: 
''' Secret
    agents
    good
    at'''

second_task = [word for word in mystring.split() if len(word) % 2 == 0]
print(second_task) 

# old variant
'''for word in mystring.split():
    if len(word) % 2 == 0:
        print(word)'''

# Use a list comprehension to create a list of every first letter in this string
# Answer: ['S', 'a', 'a', 's', 'g', 'a', 's', 'h']

third_task = [word[0] for word in mystring.split()]
print(third_task)

# Use list comprehension to create a list of all the even numbers from 0 to 10.
# Answer: [0, 2, 4, 6, 8, 10]

fourth_task = [i for i in range(0, 10 + 1) if i % 2 == 0]
print(fourth_task)

# Use the range function to create a list of all the even numbers from 0 to 10.
# Answer: [0, 2, 4, 6, 8, 10]

fifth_task = list(range(0, 10 + 1, 2))
print(fifth_task)

# Create a for loop that uses the random library to create a list of 10 random numbers.
# Answer: [95, 69, 33, 40, 92, 65, 9, 69, 91, 94, 85] but every time it will be others

import random
six_task = [random.randint(0, 10) for i in range(0, 10 + 1)]
print(six_task)

# Old variant
'''six_task = []
for i in range(0, 10 + 1):
    six_task.append(random.randint(0, 10))
print(six_task)'''

# Create a while loop that will ask the user to input an even number. 
# It should keep repeating the request until an even integer is provided. 
# You should only need to expect integers to be passed in, if the user provides a string or something else 
# that can't be transformed to an integer with int(), then the loop should break with an error.

while True:
    try:
        user_number = int(input('Type the even number: '))
    except ValueError:
        print('You shall input int. Try again.')
        user_number = int(input('Type the number: '))
    else:
        if (user_number % 2 == 0):
            print('Thank you')
            break
        else:
            print('Please provide an even number')
            continue
