[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=526669888)

# CS 1400 Final Project

## Overview
In this final project, you will utilize a weather API to retrieve current weather conditions based on zip codes.

## Task 1: Iterate Over Zip Codes
Your initial objective is to create a loop that iterates over the content of the zip_codes.txt file, accessing each zip code listed.

### Sample Output Task 1
```bash
Pulling data for zip code: 84403
Pulling data for zip code: 33101
Pulling data for zip code: 84321
Pulling data for zip code: 78023
Pulling data for zip code: 55458
```

## Task 2: Retrieve Data from Weather API
Your next task is to implement a function named pull_weather_data, which takes a zip code as its only input parameter. To achieve this, follow these steps:

1. Obtain an API key from openweathermap.org, if you don't have one already.

2. Set your API key in your Python script as follows:
```python
#Set your API Key
API_KEY = 'xxxxxxxxxxxx' # get your own key
```
3. The API supports various calls, but for this task, use the following base URL:
```python
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
```
4. Construct the final API URL based on the input zip code:
```python
    api_url = BASE_URL + 'zip=' + str(zip_code) + ',us' \
        + '&units=metric' + '&appid=' + API_KEY 
```
5. Utilize the requests Python module to send a request to the server:
```python
        # Connect to API
        weather_data = requests.get(api_url).json()
```
Ensure your function returns the JSON object obtained from the API.

### Sample output Task 2
```
Pulling data for zip code: 84403
Retreive information from:[Ogden] city

Pulling data for zip code: 33101
Retreive information from:[Miami] city

Pulling data for zip code: 84321
Retreive information from:[Logan] city

Pulling data for zip code: 78023
Retreive information from:[Helotes] city

Pulling data for zip code: 55458
Retreive information from:[Minneapolis] city
```

## Taks 3: Define CityWeather Class
Your next task is to define a new class called CityWeather with the following characteristics:

- Implement a constructor `__init__` that takes `humidity, temp, temp_max, temp_min, and city_name` as parameters and initializes the corresponding attributes.

- Implement "getters" methods for each of these attributes to retrieve their values.

- Implement the following operator overloads: `__gt__` (greater than), `__lt__` (less than), and `__eq__` (equal) operators. These operators should allow for comparisons between CityWeather objects based on their humidity values.

- Implement the `__str__` method to provide a string representation of the object's information.

Here's a basic outline to get you started:
```python
class CityWeather:
    def __init__(self, humidity, temp, temp_max, temp_min, city_name):
        # Initialize attributes here

    # Define "getters" methods for each attribute

    # Implement operator overloads (__gt__, __lt__, __eq__)

    def __str__(self):
        # Provide a string representation of the object's information
        # You can format it as per your preference

# Example usage:
# city1 = CityWeather(65, 25, 30, 20, "Example City")
# print(city1)
```

## Task 4: Store Weather Objects
Your next task is to create `CityWeather` objects and store them in a collections. You have the flexibility to choose any type of collection to hold this data -- whether it be a list, dictionary, or any other suitable data structure. Make sure to organize the stored information in a way that allows for easy retrieval and manipulation in subsequent tasks.

## Task 5: Calculate the Hottest and Coldest Temperature
Now, using the collection you created in the previous task, create functions to calculate the hottest and coldest city. Your function should take the collection of CityWeather objects, and it should return the names of the hottest and coldest cities.

Here's an outline for the functions:

```python
def calculate_hottest_city(city_weather_objects):
    # Implement the logic to find the hottest city based on temperature
    # Return the name of the hottest city

def calculate_coldest_city(city_weather_objects):
    # Implement the logic to find the coldest city based on temperature
    # Return the name of the coldest city

# Example usage:
# hottest_city = calculate_hottest_city(city_objects_collection)
# coldest_city = calculate_coldest_city(city_objects_collection)
# print(f"The hottest city is: {hottest_city}")
# print(f"The coldest city is: {coldest_city}")
```

You can choose to implement this as one or two functions, as mentioned in the task. The logic should involve iterating through the collection and comparing temperature values.

### Sample output Task 5:
```
Pulling data for zip code: 84403
Retreive information from:[Ogden] city

Pulling data for zip code: 33101
Retreive information from:[Miami] city

Pulling data for zip code: 84321
Retreive information from:[Logan] city

Pulling data for zip code: 78023
Retreive information from:[Helotes] city

Pulling data for zip code: 55458
Retreive information from:[Minneapolis] city

The hottest city is Miami with a current conditions Miami has a temperature of 22.15
        with a humidity of 52
        a max temp of 23 and a min temp of 18.99

The coldest city is Minneapolis with a current conditions Minneapolis has a temperature of -3.35
        with a humidity of 87
        a max temp of -0.99 and a min temp of -5.92
```