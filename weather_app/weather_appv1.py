import requests
import json
import sys

API_key = 'ENTER_YOUR_API_KEY' # Create your account and retrieve key there => https://openweathermap.org

if len(sys.argv) < 2:    
  print("Usage: python3 weather_app.py <City_name> (Format : Paris) <country_code> (format : FR)")    
  sys.exit(1)

city_name = sys.argv[1]
country_code = sys.argv[2]

response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={API_key}')

response.text
response_data = json.loads(response.text)
#print(response_data)

response_data[0]['lat']
response_data[0]['lon']

lat = json.loads(response.text)[0]['lat']
lon = json.loads(response.text)[0]['lon']

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
response_data = json.loads(response.text)
#print(response_data)

f_temp = response_data['main']['temp']
feels_temp = response_data['main']['feels_like']

celsius_temp = round(f_temp - 273.15, 1)
celsius_feel = round(feels_temp - 273.15, 1)

print(f"It's {celsius_temp} ° in {country_code}")
print(f"It feels like {celsius_feel}")
