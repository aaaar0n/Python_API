import requests
from unidecode import unidecode
country_dict = {}


def get_population(type_name='common'):
    """
    Returns the list of countries with population.
    """
    countries = requests.get('https://restcountries.com/v3.1/all').json()
    for country in countries:
        cleaned_name = unidecode(country['name'][type_name])
        population = country['population']
        country_dict[cleaned_name] = population
    return country_dict

def sort_top_10(population_dict): # Returns the list of countries with population in ascending order.
    sorted_asc = sorted(population_dict.items(), key=lambda x: x[1])
    return sorted_asc


def sort_least_10(population_dict): # Returns the list of countries with population in descending order.
    sorted_desc = sorted(population_dict.items(), key=lambda x: x[1], reverse = True)
    return sorted_desc



if __name__ == '__main__':
    country_population = get_population(type_name='common')
    #print(country_population)
    sorted_population_asc = sort_top_10(country_population)
    print(sorted_population_asc)
    sorted_population_desc = sort_least_10(country_population)
    #print(sorted_population_desc)




# Assignment:
"""
1. make a function {'country_name': population} return dict
2. make a function total (countries passed on parameter)
3. make a function list top 10 biggest area, least 10
"""
