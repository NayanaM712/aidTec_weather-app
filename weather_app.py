import requests

API_KEY = "6bf5f89f327e1e2af6cfb1889f5cf4d9"

def get_weather_data(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data
# def display_current_weather(data):
#     print(data)


def display_current_weather(data):
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    weather_condition = data["weather"][0]["description"]

    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Weather Condition: {weather_condition}")

def display_forecast(location):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    print(f"\nForecast for {location}:")
    for forecast in data["list"]:
        date = forecast["dt_txt"].split()[0]
        temperature = forecast["main"]["temp"]
        weather_condition = forecast["weather"][0]["description"]
        print(f"Date: {date}\tTemperature: {temperature}°C\tWeather Condition: {weather_condition}")

def main():
    print("Welcome to the Weather App!")
    while True:
        location = input("Enter a location (or 'q' to quit): ")
        if location.lower() == 'q':
            break

        weather_data = get_weather_data(location)
        if weather_data["cod"] == "404":
            print("Invalid location. Please try again.")
            continue

        display_current_weather(weather_data)

        choice = input("\nDo you want to view the forecast for the next few days? (y/n): ")
        if choice.lower() == 'y':
            display_forecast(location)

    print("Thank you for using the Weather App!")

if __name__ == "__main__":
    main()
