# Go to the data folder and access the countries_data.py file.

# Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.

from countries_data import wordList

def most_spoken_languages(user_dict: dict) -> None:
    """Print 10 most spoken languages in the world in descending order

    Args:
        user_dict (dict): take dictionary with info about countries
    """

    # initial variables
    language_list = []
    temp_dict = {}

    # create list that holds all languages
    for elem in user_dict:
        language_list += elem['languages']

    # fill dictionary with key language and value how many it appears in the list
    for item in language_list:
        temp_dict[item] = temp_dict.get(item, 0) + 1

    # sort dictionary by value in reverse order
    sorted_dict = {k: v for k, v in sorted(temp_dict.items(), key=lambda item: item[1], reverse=True)}

    # print first ten most spoken languages
    for lang in list(sorted_dict) [0:10 + 1]:
        print(f'Langueage {lang} speaks in {sorted_dict[lang]} countries')

print(most_spoken_languages(wordList))
print()

def most_populated_countries(user_dict: dict) -> None:
    """Print 10 most populated countries in the world in descending order

    Args:
        user_dict (dict): take dictionary with info about countries
    """

    # initial variable
    country_list = []
    population_list = []

    # save country name and population into lists
    for element in user_dict:
        country_list += [element['name']]
        population_list += [element['population']]
    
    # create dict from two lists and sorted it by values in reverse order
    new_dict = dict(zip(country_list, population_list))
    sorted_dict = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1], reverse=True)}

    # print first ten most populated countries
    for country in list(sorted_dict) [0:10 + 1]:
        print(f'Country {country} has population {sorted_dict[country]}')

print(most_populated_countries(wordList))
