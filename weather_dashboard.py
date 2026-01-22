"""
Project: Weather Forecast Visualization System
Description: Fetches weather data from OpenWeatherMap API and visualizes it
Author: Team Project - Internship
"""

import requests
import matplotlib.pyplot as plt




API_KEY = "PASTE_YOUR_API_KEY_HERE"  
CITY_NAME = "Delhi"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
UNIT_SYSTEM = "metric"
FORECAST_LIMIT = 8   




def get_weather_data():
    params = {
        "q": CITY_NAME,
        "appid": API_KEY,
        "units": UNIT_SYSTEM
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as error:
        print("Error while fetching weather data:", error)
        return None




def extract_weather_details(weather_json):
    temperatures = []
    humidities = []
    timestamps = []

    for record in weather_json["list"][:FORECAST_LIMIT]:
        temperatures.append(record["main"]["temp"])
        humidities.append(record["main"]["humidity"])
        timestamps.append(record["dt_txt"])

    return temperatures, humidities, timestamps




def display_weather_dashboard(times, temps, hums):
    plt.figure(figsize=(10, 5))

    plt.plot(times, temps, marker='o', label="Temperature (°C)")
    plt.plot(times, hums, marker='x', label="Humidity (%)")

    plt.title(f"Weather Forecast Dashboard - {CITY_NAME}")
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



def main():
    print("Connecting to weather service...")
    weather_data = get_weather_data()

    if weather_data is None:
        print("Unable to retrieve weather data.")
        return

    temp_list, hum_list, time_list = extract_weather_details(weather_data)

    print("Rendering visualization...")
    display_weather_dashboard(time_list, temp_list, hum_list)


if __name__ == "__main__":
    main()
