import requests
import threading

API_URL = 'https://api.open-meteo.com/v1/forecast'

def get_weather(latitude, longitude, city_name):
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'hourly': 'temperature_2m'
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    temperatures = data['hourly']['temperature_2m']
    average_temperature = sum(temperatures) / len(temperatures)
    return city_name, average_temperature


cities = [
    {'name': 'London', 'latitude': 51.51, 'longitude': -0.13},
    {'name': 'Paris', 'latitude': 48.86, 'longitude': 2.35},
    {'name': 'Berlin', 'latitude': 52.52, 'longitude': 13.40},
    {'name': 'Rome', 'latitude': 41.89, 'longitude': 12.49},
    {'name': 'Madrid', 'latitude': 40.42, 'longitude': -3.70}
]


threads = []
results = []


for city in cities:
    thread = threading.Thread(target=lambda: results.append(get_weather(city['latitude'], city['longitude'], city['name'])))
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()


max_city, max_temperature = max(results, key=lambda x: x[1])


print(f"City with the highest average temperature: {max_city} - {round(max_temperature, 2)}°C")