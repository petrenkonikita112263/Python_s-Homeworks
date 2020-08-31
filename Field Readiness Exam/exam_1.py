from typing import List

print('''
Task 1
Open the exam.txt file with Python and with only read permission and 
store the contents in a list called exam_lines

!!!['Welcome to your First Exam Recruit.\n', 'Only the best recruits can become agents.\n', 
'Do you have what it takes?\n', 'We will test your knowledge with this field readiness exam.\n',
'It should be pretty simple, since you only know the basics so far.\n', "Let's get started.\n", 
'Best of luck recruit.']''')

print('''
# Task 2
# How many lines does this file have?

!!!Your output should look something like this: 7''')

def count_lines(some_text: List) -> int:
    total = sum(1 for line in some_text)
    return total

print('''
Task 3
Print out the 5th line of the text file.

!!!Your output should look something like this: It should be pretty simple, 
since you only know the basics so far.''')
def find_line(some_text: List, i: int) -> None:
    print(some_text[i - 1])

with open('Python Exam\'s Task\Field Readiness Exam\exam.txt', 'r') as file:
    exam_lines = file.readlines()
    print(exam_lines)
    print(count_lines(exam_lines))
    find_line(exam_lines, 5)

    print('''
    Task 4
    Grab the last line of the text file and save it to a variable called last.

    !!!Your output should look something like this: 'Best of luck recruit.''')
    last_line = exam_lines[len(exam_lines) - 1]
    print(last_line)

    print('''
    Task 5
    Use indexing to grab the letter 'o' from the last line of the file.

    !!!Your output should look something like this: 'o'.''')
    letter = [word for word in last_line if 'o' in word]
    print(letter)

    print('''
    Task 6
    How could you use Python to count how many words there are in the last line? 

    !!!Your output should look something like this: 4''')
    total_words = sum(1 for word in last_line.split())
    print(total_words)

print('''
Task 8
Let's check how well you understand indexing and key calls. 
Here we present to you a set of dictionaries and lists that are nested inside a single dictionary d. 
this is an unrealistic representation of how you would use these data types in the field, 
this is just for practice:

!!!Your task is to retrieve the string "get me please" from the dictionary with stacked index and key calls.
''')

d = {"levelone":[1,2,{'leveltwo':[5,6,[1,['get me please']]]}]}
first_key = d['levelone']
print(first_key)
second_key = first_key[2]
print(second_key)
first_result = d['levelone'][2]
print(first_result)
second_result = first_result['leveltwo']
print(second_result)
third_result = second_result[2]
print(third_result)
last_result = third_result[1][0]
print(last_result)
# final command d['levelone'][2]['leveltwo'][2][1][0]

print('''
Bonus Task
How many unique integers are in this list? 
(You will need to use a casting method we haven't shown you yet)
Your output should look something like this: 12''')

mylist = [1,2,3,4,5,6,4,3,2,1,2,3,4,5,6,6,7,8,5,6,7,8,9,8,9,8,9,7,10,123,1,2,2,3,1,3,2,4,1,4,4,1,2,2,22,3,4,1,4,1]
my_set = set(mylist)
print(my_set)
my_result = sum(1 for i in my_set)
print(my_result)