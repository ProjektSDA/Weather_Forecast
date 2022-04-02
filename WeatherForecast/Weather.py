import json
from dataclasses import dataclass

import requests


@dataclass
class Weather:
    city: str
    description: str
    temperature: float
    precipitation: float
    pressure: int
    wind_direction: str
    wind_speed: int
    humidity: float


# def get_temperature_in(city: str) -> float:
#     response = requests.get(f"https://wttr.in/{city}?format=j1")
#     json_response = response.json()
#     return float(json_response['current_condition'][0]['temp_C'])

def check_weather_in(city: str):
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    json_response = response.json()
    shortened_response = json_response['current_condition'][0]


    Weather.city = city
    Weather.temperature = float(shortened_response['temp_C'])
    Weather.humidity = shortened_response['humidity']
    Weather.precipitation = float(shortened_response['precipMM'])
    Weather.pressure = shortened_response['pressure']
    Weather.description = shortened_response['weatherDesc'][0].get('value')
    Weather.wind_direction = shortened_response['winddir16Point']
    Weather.wind_speed = shortened_response['windspeedKmph']

    # current_weather = {'city': {Weather.city}, 'description': {Weather.description}, 'temperature': {Weather.temperature}, 'humidity': {Weather.humidity}, 'precipitation': {Weather.precipitation}, 'pressure': {Weather.pressure}, 'wind_direction': {Weather.wind_direction}, 'wind_speed': {Weather.wind_speed}}
    print (f"{Weather.city},temperature: {Weather.temperature}, {Weather.description},humidity: {Weather.humidity}, precipitation: {Weather.precipitation}, pressure(hPa): {Weather.pressure}, wind direction: {Weather.wind_direction}, wind speed(km/h): {Weather.wind_speed}")
    # print(current_weather)
    # return float(json_response['current_condition'][0]['temp_C'])


check_weather_in('Lublin')