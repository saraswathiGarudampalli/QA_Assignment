import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=" + API_KEY

def get_weather_data():
    date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
    url = BASE_URL
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        for data in weather_data['list']:
            if data['dt_txt'] == date:
                print(f"Temperature at {date}: {data['main']['temp']} Kelvin")
                return
        print("Weather data not found for the given date.")
    else:
        print("Failed to fetch weather data.")

def get_wind_speed_data():
    date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
    url = BASE_URL
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        for data in weather_data['list']:
            if data['dt_txt'] == date:
                print(f"Wind Speed at {date}: {data['wind']['speed']} m/s")
                return
        print("Wind speed data not found for the given date.")
    else:
        print("Failed to fetch weather data.")

def get_pressure_data():
    date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
    url = BASE_URL
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        for data in weather_data['list']:
            if data['dt_txt'] == date:
                print(f"Pressure at {date}: {data['main']['pressure']} hPa")
                return
        print("Pressure data not found for the given date.")
    else:
        print("Failed to fetch weather data.")

