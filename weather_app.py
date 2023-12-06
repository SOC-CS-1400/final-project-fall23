"""
Weather App to check the current weather based on zip code
"""
from city_weather import CityWeather
import requests
# from pprint import pprint as pp

#Set your API Key
API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # TODO: Update with your API key
# Base URL for OpenWeatherMap
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'


def pull_weather_data(zip_code):
    api_url = BASE_URL + 'zip=' + str(zip_code) + ',us' \
        + '&units=metric' + '&appid=' + API_KEY 
    # TODO: Call the API and store the response
    # return the JSON response
    pass


def find_hottest_city(weather_zips):
    # TODO: Find the hottest city
    pass


def find_coldest_city(weather_zips):
    # TODO: Find the coldest city
    pass


def main():
    """My main function driver
    """
    #TODO: Read zipcodes from file
    zip_file = 'zip_codes.txt'
            # TODO: Call pull_weather_data for each zip code
            
            # TODO: Store data in a CityWeather object
    # TODO: Compare the current temperture of all objects
    # TODO: print the hotest and coldest

    

if __name__ == '__main__':
    main()
