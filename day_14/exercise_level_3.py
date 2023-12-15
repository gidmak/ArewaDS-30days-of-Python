import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Sort countries by name, by capital, by population
from collections import Counter
from operator import itemgetter

from countries_data import countries_data as countries 

def sort_countries_by_name(countries_list):
    return sorted(countries_list, key=lambda country: country['name'])

def sort_countries_by_capital(countries_list):
    return sorted(countries_list, key=lambda country: country['capital'])

def sort_countries_by_population(countries_list):
    return sorted(countries_list, key=lambda country: country['population'])

sorted_by_name = sort_countries_by_name(countries)
sorted_by_capital = sort_countries_by_capital(countries)
sorted_by_population = sort_countries_by_population(countries)

# Print the sorted lists
print("Sorted by Name:")
for country in sorted_by_name:
    print(country['name'])

print("\nSorted by Capital:")
for country in sorted_by_capital:
    print(country['capital'])

print("\nSorted by Population:")
for country in sorted_by_population:
    print(country['population'])

# Sort out the ten most spoken languages by location.
from countries_data import countries_data
def most_languages_spoken():
    lang = {}
    for country in countries_data:
        for language in country['languages']:
            lang[language] = lang.get(language, 0) + 1
    sorted_lang = sorted(lang.items(), key=lambda x: x[1], reverse=True)[:10]
    return sorted_lang
print(most_languages_spoken())

def get_most_spoken_languages(countries_list, num_languages=10):
    languages_counter = Counter()
    
    for country in countries_list:
        languages = country.get('languages', [])
        languages_counter.update(languages)

    most_spoken_languages = languages_counter.most_common(num_languages)
    return most_spoken_languages

# Get the ten most spoken languages
most_spoken_languages = get_most_spoken_languages(countries, num_languages=10)

# Print the result
print("Ten most spoken languages by location:")
for language, count in most_spoken_languages:
    print(f"{language}: {count} countries")

# Sort countries by population in descending order to get 10 most populous countries
sorted_by_population = sorted(countries, key=lambda country: country['population'], reverse=True)

# Get the top ten most populated countries
top_ten_most_populated = sorted_by_population[:10]

# Print the result
print("Top Ten Most Populated Countries:")
for country in top_ten_most_populated:
    print(f"{country['name']:30}Population: {country['population']:15,}")