import requests
import json
from datetime import datetime, timedelta

# API Key for weather data
API_KEY = "fc7e8247cce6cbe387a0716c3f774382"

def fetch_weather_data(city):
    """
    Fetches current weather data for a given city using the OpenWeatherMap API.
    Returns a dictionary containing the weather data.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def fetch_historical_weather_data(city):
    """
    Fetches historical weather data for the last seven days for a given city using the OpenWeatherMap API.
    Returns a list of dictionaries containing the historical weather data for each day.
    """
    historical_data = []
    for i in range(7):
        date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={date}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        historical_data.append(data)
    return historical_data

def calculate_statistics(temperature_data):
    """
    Calculates average, median, and mode of the historical temperature data.
    Returns a dictionary containing the statistics.
    """
    # Perform calculations for average, median, and mode here
    return statistics

def save_to_file(data, filename):
    """
    Saves the fetched data and statistical analysis results to a file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def main():
    city = input("Enter the name of the city: ")
    
    # Fetch current weather data
    current_weather = fetch_weather_data(city)
    
    # Fetch historical weather data
    historical_weather = fetch_historical_weather_data(city)
    
    # Calculate statistics
    statistics = calculate_statistics(historical_weather)
    
    # Save data to a file
    save_to_file({"current_weather": current_weather, "historical_weather": historical_weather, "statistics": statistics}, "weather_data.json")
    
    print("Weather data fetched and saved successfully!")

if __name__ == "__main__":
    main()
