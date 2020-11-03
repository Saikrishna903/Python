#Calling an api using requests library.
import requests
location = input("Enter your location to find temperature: ")
url = "http://api.openweathermap.org/data/2.5/find?appid=d12cf8c5c3c40febafd1dca5750f7eb1&units=metric&q=" + location
response = requests.get(url)
weather_info = response.json()
temp_from_weather_info = weather_info['list'][0]['main']['temp']
print("Temperature is : " + str (temp_from_weather_info) + chr(176) + "C")