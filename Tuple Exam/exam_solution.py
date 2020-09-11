# Create an empty tuple
my_tuple = tuple()
print(my_tuple)

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Felix', 'Iroms', 'Junior', 'Mike')
sisters = ('Joy', 'Florence', 'Nkeshi')

# Join brothers and sisters tuples and assign it to siblings
combine_tuple = brothers + sisters
print(combine_tuple)

# How many siblings do you have?
print(len(combine_tuple))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Webber', 'Angella')
family_members = combine_tuple + parents

# Unpack siblings and parents from family_members
*children, father, mother = family_members
del parents
parents = []
parents.append(father)
parents.append(mother)
print(children)
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('mango', 'guava', 'apple', 'strawberry')
vegetables = ('cucumber', 'broccoli', 'cauliflower')
animal_product = ('corned-beef', 'hot dog')
food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_tp[len(food_stuff_tp) // 2 :])

# Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_tp[:3]
last_three = food_stuff_tp[-3:]
print(first_three)
print(last_three)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
print(f"{'Yes, Estonia is a nordic country' if 'Estonia' in nordic_countries else 'No, Estonia is not a nordic country'}")

# Check if 'Iceland' is a nordic country
print(f"{'Yes, Iceland is a nordic country' if 'Iceland' in nordic_countries else 'No, Iceland is not a nordic country'}")
