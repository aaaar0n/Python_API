import requests
from unidecode import unidecode


def get_countries(type_name='common', is_reverse=False):
    """
    Returns the list of countries.
    """
    country_list = []
    countries = requests.get('https://restcountries.com/v3.1/all').json()
    for country in countries:
        import pdb; pdb.set_trace()
        cleaned_name = unidecode(country['name'][type_name])
        country_list.append(cleaned_name)
    return sorted(country_list, reverse=is_reverse)


if __name__ == '__main__':
    countries = get_countries(type_name='common', is_reverse=True)
    print(countries)


# Assignment:
"""
1. make a function {'country_name': population} return dict
2. make a function total (countries passed on parameter)
3. make a function list top 10 biggest area, least 10
"""