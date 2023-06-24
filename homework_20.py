import random
import requests


#task 1


websites = [
    'http://google.com',
    'http://facebook.com',
    'http://twitter.com',
    'http://amazon.com',
    'http://apple.com'
]

random_website = random.choice(websites)

response = requests.get(random_website)

status_code = response.status_code
website_name = random_website.split("//")[-1]
html_length = len(response.text)

print('Статус-код:', status_code)
print('Назва сайту:', website_name)
print('Довжина HTML-коду:', html_length)


#task 2

def get_city_coordinates(city):
    geocoding_url = "https://api.open-meteo.com/v1/geocode"
    params = {"query": city}
    response = requests.get(geocoding_url, params=params)
    data = response.json()

    if "latitude" in data and "longitude" in data:
        latitude = data["latitude"]
        longitude = data["longitude"]
        return latitude, longitude

    return None
def get_weather_data(latitude, longitude):
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
    response = requests.get(weather_url)
    data = response.json()
    current_weather = data["current_weather"]
    return current_weather
city = input("Введіть назву міста: ")
coordinates = get_city_coordinates(city)
if coordinates is None:
    print("Неможливо знайти координати для вказаного міста.")
else:
    latitude, longitude = coordinates
    weather_data = get_weather_data(latitude, longitude)
    print("Поточні показники погоди:")
    print("Температура:", weather_data["temperature"], "°C")
    print("Вологість:", weather_data["humidity"], "%")
    print("Швидкість вітру:", weather_data["wind_speed"], "м/с")
    print("Стан неба:", weather_data["weather_description"])