import json
import requests
import pycountry
import random
import emoji

def json_file_maker(countries, file_name): # funtion to create a json file of pokemon using .dump
    with open(f"{file_name}", "w") as jsonfile:
        json.dump(countries, jsonfile)

def countries_get(field) -> dict:
    countries_req = requests.get(f"https://restcountries.com/v3.1/{field}")
    countries = countries_req.json()
    json_file_maker(countries, f"{field}.json")

# countries_get('all')


def country_info(json_file: str) -> list:
    with open(json_file, "r") as read_file:
        data = json.load(read_file)
        countries = []
        for country_data in data:
            common_name = country_data.get('name', {}).get('common', None)
            if common_name:
                countries.append(common_name)
        return countries


# Open and load the JSON file
with open('all.json', 'r') as info:
    info2 = json.load(info)

countries = []

for country_data in info2:
    country_name_dict = country_data.get('name', {})  # Extract the 'name' dictionary
    country_name = country_name_dict.get('common', 'Unknown')  # Extract the 'common' key or use 'Unknown' as a default
    population = country_data.get('population', None)  # Set to None if 'population' is missing
    currency_names = []
    currencies_data = country_data.get('currencies', {})
    for currency_code, currency_info in currencies_data.items():
        currency_name = currency_info.get('name', 'Unknown')
        currency_names.append(currency_name)
    subregion = country_data.get('subregion', None)
    capital_list = country_data.get('capital', [])
    if capital_list:
        capital = capital_list[0]
    else:
        capital = None
    flag = country_data.get('flag', None)
    if country_name and population is not None:
        country_info = {
            'country': country_name,
            'population': population,
            'currency': currency_name,
            'subregion': subregion,
            'capital': capital,
            'country_code': flag
        }
        countries.append(country_info)


random.shuffle(countries)


for country_data in countries:
    revealed_info = []  # Store the revealed information step by step
    for info_key in ['population', 'subregion', 'capital', 'country_code', 'currency']:
        revealed_info.append(info_key)
        print("Revealed Info:")
        for key in revealed_info:
            print(f"{key}: {country_data[key]}")

        user_guess = input(f"Guess a Country!").strip()

        if user_guess.lower() == country_data['country'].lower():
            print("Congratulations! You guessed the country correctly.")
            break
        elif user_guess.lower() == 'quit':
            print("You gave up. The correct country was:", country_data['country'])
            break  # Break out of the loop if the user quits
        else:
            print("Incorrect guess. Keep guessing...")

    else:
        print("All information revealed. The correct country was:", country_data['country'])
        next_action = input("Press Enter to move on to the next country or type 'quit' to exit: ").strip()
        if next_action.lower() == 'quit':
            break  # Break out of the loop if the user quits

print("Game over. You've gone through all countries.")



