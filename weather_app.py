"""
Weather App to check the current weather based on zip code
"""
from city_weather import CityWeather
import requests
from pprint import pprint as pp

#Set your API Key
API_KEY = 'af4f939501ebb649537e015196aedc70'
# Base URL for OpenWeatherMap
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'


def pull_weather_data(zip_code):
    """Pull weather data from openweathermap.org
    """
    api_url = BASE_URL + 'zip=' + str(zip_code) + ',us' \
        + '&units=metric' + '&appid=' + API_KEY 
    # TODO: Add a try, except for this call
    try:
        # Connect to API
        weather_data = requests.get(api_url).json()
        # Response 200 is good
        if weather_data['cod'] != 200:
            raise ValueError
    except ValueError:
        print('Bad response from API')
    return weather_data

def find_hottest_city(weather_zips):
    """Find the hottest city in the list based on the temp attribute"""
    hottest = None
    for city in weather_zips:
        if hottest is None:
            hottest = city
        elif city > hottest:
            hottest = city
    return hottest


def find_coldest_city(weather_zips):
    """Find the coldest city in the list based on the temp attribute"""
    coldest = None
    for city in weather_zips:
        if coldest is None:
            coldest = city
        elif city < coldest:
            coldest = city
    return coldest


def main():
    """My main function driver
    """
    #TODO: Read zipcodes from file
    zip_file = 'zip_codes.txt'
    weather_zips = []
    with open(zip_file, 'r') as data_file:
        zip_codes = data_file.readlines()
        for zip_code in zip_codes:
            zip_code = zip_code.strip()
            print(f'Pulling data for zip code: {zip_code}')
            weather_data = pull_weather_data(zip_code)
            city_name = weather_data['name']
            print(f'Retreive information from:[{city_name}] city')
            # TODO: Store data in a CityWeather object
            city_weather = CityWeather(weather_data['main']['humidity'],
                            weather_data['main']['temp'],
                            weather_data['main']['temp_max'],
                            weather_data['main']['temp_min'],
                            weather_data['name'])
            weather_zips.append(city_weather)
    # TODO: Compare the current temperture of all objects
    # TODO: print the hotest and coldest
    hottest = find_hottest_city(weather_zips)
    print(f'The hottest city is {hottest.get_city_name()} with a current conditions {hottest}')
    coldest = find_coldest_city(weather_zips)
    print(f'The coldest city is {coldest.get_city_name()} with a current conditions {coldest}')

    

if __name__ == '__main__':
    main()

# Connect to openweathermap.org api to read the 16 day forcast 