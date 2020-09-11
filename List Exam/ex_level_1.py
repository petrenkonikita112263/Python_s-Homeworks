# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
weeksdays_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Find the length of your list
len(weeksdays_list)

# Get the first item, the middle item and the last item of the list
first_item = weeksdays_list[0]
middle_item = weeksdays_list[len(weeksdays_list) // 2]
last_item = weeksdays_list[len(weeksdays_list) - 1]
print(f'First item of list {first_item}, middle item - {middle_item} and last item is {last_item}')

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Marty', 32, 67.21, False, 'San Francisco']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(f'Number of companies in the list is {len(it_companies)}')

# Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[len(it_companies) - 1]
print(f'First company in the list - {first_company}, middle company - {middle_company} and last company is {last_company}')

# Print the list after modifying one of the companies
it_companies[len(it_companies) - 1] = 'eBay'
print(f'List of companies after modification {it_companies}')

# Add an IT company to it_companies
it_companies.append('Netcrecker')

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Ali Express')

# Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies)
print(it_companies[-2].upper())

# Join the it_companies with a string '#;  '
joined_list = '#; '.join(it_companies)
print(joined_list)

# Check if a certain company exists in the it_companies list.
print(f"Is Netcrecker in the list? {'Yes' if 'Netcrecker' in it_companies else 'No'}")

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies[:] = it_companies[::-1]
print(it_companies)

'''it_companies.reverse()
print(it_companies)'''

# Slice out the first 3 companies from the list
print(it_companies[:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
print(it_companies[len(it_companies) // 2 : - len(it_companies) // 2 + 1])

# Remove the first IT company from the list
print(it_companies)
it_companies.remove('eBay')

# Remove the middle IT company or companies from the list
it_companies.remove(it_companies[len(it_companies) // 2])

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_list = front_end + back_end
print(full_list)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
i = full_list.index('Redux')
copy_list = full_list[:]
copy_list.insert(i + 1, 'Python')
copy_list.insert(i + 1, 'SQL')
print(copy_list)
print(full_list)
