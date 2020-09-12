# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['ID Software', 'SDO', 'LGR'])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.discard('SDO')
print(it_companies)

# What is the difference between remove and discard
'''
Discard: 
The function deletes the specified element from the set and if the element is not present in the set, it does not return any error.

Remove:
This function is similar to discard() but the difference is that it throws an error when the specified element to delete is not found in the set.
'''

# Join A and B
print(A.union(B))

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
print(A.union(B))
print(B.union(A))

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del it_companies

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_of_age = set(age)
print(f'Length of age list = {len(age)} and length of age set = {len(set_of_age)}')

# Explain the difference between the following data types: string, list, tuple and set
'''
String:
A single character or a sequence of characters identify, the primitive data structures in Python. Immutable

List:
A collection which is ordered and changeable. Allows duplicate members.

Tuple:
A collection which is ordered and unchangeable. Allows duplicate members.

Set:
A collection which is unordered and unindexed. No duplicate members.
'''

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? You did not learn loops yet you can do it manually.
default_sentence = 'I am a teacher and I love to inspire and teach people'
word_list = default_sentence.split(' ')
print(word_list)
print(set(word_list))
print(f'There are = {len(set(word_list))} unique words in the sentence')
