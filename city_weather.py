"""
Class to model city weather
"""


class CityWeather:
    # TODO: Set constructor with the following attributes:
    # humidity, temp, temp_max, temp_min, city_name
    def __init__(self, humidity, temp, temp_max, temp_min, city_name):
        self._humidity = humidity
        self._temp = temp
        self._temp_max = temp_max
        self._temp_min = temp_min
        self._city_name = city_name
    # TODO: Set all your "getters"
    def get_humidity(self):
        return self._humidity
    
    def get_temp(self):
        return self._temp

    def get_temp_max(self):
        return self._temp_max

    def get_temp_min(self):
        return self._temp_min
    
    def get_city_name(self):
        return self._city_name

    # TODO: Set your __gt__, __lt__, and __eq__ operators
    # based on the temp attribute
    def __gt__(self, other):
        return self._temp > other._temp

    def __lt__(self, other):
        return self._temp < other._temp

    def __eq__(self, other):
        return self._temp == other._temp

    # TODO: Set your __str__ operator which should display
    # all the attributes
    def __str__(self):
        return f'''{self._city_name} has a temperature of {self._temp}
        with a humidity of {self._humidity}
        a max temp of {self._temp_max} and a min temp of {self._temp_min}'''


def main():
    """My main function driver
    """
    print('Ready to code')
    

if __name__ == '__main__':
    main()