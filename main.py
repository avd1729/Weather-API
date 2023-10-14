import requests


def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API request
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # You can change the units to 'imperial' for Fahrenheit
    }

    try:
        # Make a GET request to the API
        response = requests.get(base_url, params=params)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            data = response.json()
            # Extract relevant weather information from the response
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            # Print the weather information
            print(f"Weather in {city_name}: {weather}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(
                f"Error: Unable to fetch weather data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Replace with your OpenWeatherMap API key
    api_key = ""
    city_name = "New Delhi"   # Replace with the city name you want to fetch weather data for
    get_weather(api_key, city_name)
