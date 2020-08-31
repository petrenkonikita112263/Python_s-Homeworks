from typing import List

print('''
Task 1
Create a function that takes in two integers and returns True if their sum is 10, 
False if their sum is something else.
''')

def check_ten(n1: int, n2: int) -> bool:
    return n1 + n2 == 10

print(check_ten(10, 0))                        # True
print(check_ten(5, 5))                         # True
print(check_ten(2, 7))                         # False

print('''
Task 2
Create a function that takes in two integers and returns True if their sum is 10, otherwise, 
return the actual sum value.
''')

def check_ten_sum(n1: int, n2: int) :
    return True if n1 + n2 == 10 else n1 + n2

print(check_ten_sum(10,0))                     # True
print(check_ten_sum(2,7))                      # 9

print('''
Task 3
Create a function that takes in a string 
and returns back the first character of that string in upper case.
''')


def first_upper(mystring: str) -> str:
    return mystring[0].upper()

print(first_upper('hello'))                    # 'H'
print(first_upper('agent'))                    # 'A'

print('''
Task 4
Create a function that takes in a string and returns the last two characters. 
If there are less than two chracters, return the string: "Error".
''')

def last_two(mystring: str) -> str:
    return mystring[-2:] if len(mystring) >= 2 else 'Error'

print(last_two('hello'))                       # 'lo'
print(last_two('hi'))                          # 'hi'
print(last_two('a'))                           # 'Error'

print('''
Task 5
Given a list of integers, return True if the sequence [1,2,3] 
is somewhere in the list. Hint: Use slicing and a for loop.
''')

def seq_check(nums: List) -> bool:
    # modern solution
    return any([1,2,3] == nums[i:i+3] for i in range(len(nums)))

    # old variant
    '''for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False'''

print(seq_check([1,2,3]))                      # True
print(seq_check([7,7,7,1,2,3,7,7,7]))          # True
print(seq_check([3,2,1,3,2,1,1,1,2,2,3,3,3]))  # False

print('''
Task 6
Given a 2 strings, create a function that returns the difference in length between them. 
This difference in length should always be a positive number (or just 0). Hint: Absolute Value.
''')

def compare_len(s1: str, s2: str) -> int:
    return abs(len(s1) - len(s2))


print(compare_len('aa','aa'))                  # 0
print(compare_len('a','bb'))                   # 1
print(compare_len('bb','a'))                   # 1

print('''
Task 7
Given a list of integers, if the length of the list is an even number, 
return the sum of the list. If the length of the list is odd, return the max value in that list.
''')

def sum_or_max(mylist: List) -> int:
    return sum(mylist) if len(mylist) % 2 == 0 else max(mylist)

print(sum_or_max([1,2,3]))                     # 3
print(sum_or_max([0,1,2,3]))                   # 6

print('''
Task 8
Agents in the field sometimes need to speak in code. 
Create a function that takes in a string name (e.g. "James", "Cindy", etc...) 
and replaces all vowels with the letter x. 
For our purposes, consider these letters as vowels: [a,e,i,o,u]. 
Then switch the position of the first and last letters.

This task is challenging, break it down into multiple pieces.
''')

vowel_list = ['a','e','i','o','u']
def replace_and_switch(name: str) -> str:
    spy_name = list(name)
    for index, letter in enumerate(name):
        if letter in vowel_list:
            spy_name[index] = 'x'
        else:
            spy_name[index] = letter
    spy_name[0], spy_name[-1] = spy_name[-1], spy_name[0]
    return ''.join(spy_name)

print(replace_and_switch('James'))             # 'sxmxJ'
print(replace_and_switch('Cindy'))             # 'yxndC'
print(replace_and_switch('Alfred'))            # 'dlfrxx'

print('Excellent work! You\'r not nebwnie!')