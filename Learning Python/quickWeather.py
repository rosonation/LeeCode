import json
import requests
import sys

# Compute location from command line arguments
if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()
http://api.openweathermap.org/data/2.5/forecast/daily?q=San Francisco, CA&cnt=3
http://openweathermap.org/data/2.5/forecast/daily?q="San Francisco, CA"&cnt=3
location = ' '.join(sys.argv[1:])
# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % location
response = requests.get(url)
print(response.status_code)
# response.raise_for_status()

# load JSON data into a python variable.
weatherData = json.loads(response.text)
# print weather description.
w = weatherData['list']
print('Current weather in %s:' % location)


