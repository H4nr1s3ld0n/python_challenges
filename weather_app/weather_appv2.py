import requests
import json
import sys

API_key = 'YOUR_KEY_HERE'

# Insert country names here 

city_name = 'Paris'
country_code = 'France'

# Resolves the name of the place to the lat and long

response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={API_key}')

# Retrieves data as JSON

response.text
response_data = json.loads(response.text)

lat = json.loads(response.text)[0]['lat']
lon = json.loads(response.text)[0]['lon']

# Makes a second request with the latitude and longitude 

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
response_data = json.loads(response.text)

# Retrieves the data and stores it in variables

f_temp = response_data['main']['temp']
feels_temp = response_data['main']['feels_like']
desc = response_data['weather'][0]['description']

# Converts the temperature to C°

celsius_temp = round(f_temp - 273.15, 1)
celsius_feel = round(feels_temp - 273.15, 1)

# Prints information

print(f"It's {celsius_temp} ° in {city_name}, {country_code}")
print(f"It feels like {celsius_feel}")
print(f"There is a {desc}")
