# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######

total = 0
rows = range(1, 8)
for i in rows:
    total = '#' * i
    print(total, end = '\n')

# Same thing but instead of # print numbers
try:
    rows = int(input("Please, enter the number of rows: "))
except ValueError as error:
    print('Wrong value', error, '/nTry again')
    rows = int(input("Please, enter the number of rows: "))
else:
    print('Right Triangle Pattern Of Numbers-', rows)
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(i, end = ' ')
        print(' ')

# Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(1, 9):
    print('# ' * 8)

# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(0, 11):
    print(f'{i} * {i} = {i * i}')


from typing import List

def reverse_list(user_list: List) -> List:
    """Function that revers the list

    Args:
        user_list (List): input list

    Returns:
        [List]: the reverse of the array
    """
    return user_list[::-1]

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]

def capitalize_list_items(user_list: List) -> List:
    """Function that capitalizes each element in list

    Args:
        user_list (List): input list

    Returns:
        List: a capitalized list of items
    """
    return [item.upper() for item in user_list]

print(capitalize_list_items(['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']))

def add_item(user_list: List, element: object):
    """Function that adds item to the end of the list

    Args:
        user_list (List): input list
        element (object): item that will add to the list

    Returns:
        [type]: a list with the item added at the end
    """
    user_list.append(element)
    return user_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))     # [2, 3, 7, 9, 5]

def remove_item(user_list: List, element: object):
    """Function that removes item from the list

    Args:
        user_list (List): input list
        element (object): item that will remove from the list

    Returns:
        [type]: a list after remove operation
    """
    user_list.remove(element)
    return user_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]


def sum_all_numbers(num: int) -> int:
    """Adds all the numbers

    Args:
        num (int): natural number

    Returns:
        int: sum of first num natural numbers
    """
    return num * (num + 1) // 2

print(sum_all_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050


'''Write different functions which take lists. 
They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, 
calculate_std (standard deviation).'''

# simple way - use statistics module to solve it

import statistics
import numpy

def stat_calc(user_list: List) -> None:
    calc_mean = statistics.mean(num_list)
    calc_median = statistics.median(num_list)
    calc_mode = statistics.mode(num_list)
    calc_range = numpy.ptp(num_list)
    calc_variance = statistics.pvariance(num_list)
    calc_std = statistics.pstdev(num_list)
    print('The mean is', calc_mean, ' median = ', calc_median, ' mode = ', calc_mode, ' range = ', calc_range, ' variance = ', calc_variance, ' std = ', calc_std)

num_list = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]
print(stat_calc(num_list))