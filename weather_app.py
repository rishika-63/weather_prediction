import requests

API_KEY = "0ce487c137159734c0bd0ac117e5e3b6" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(location):
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric" 
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"].capitalize()
            }
        elif data.get("message"):
            print(f"Error: {data['message'].capitalize()}")
        else:
            print("Error: Unable to fetch weather data.")
    except Exception as e:
        print(f"Exception occurred: {e}")
    return None

def main():
    print("=== Weather App ===")
    location = input("Enter city name or ZIP code: ").strip()

    if not location:
        print("❌ Invalid input. Please enter a location.")
        return

    weather = get_weather_data(location)
    if weather:
        print(f"\n📍 Location: {weather['city']}")
        print(f"🌡️ Temperature: {weather['temperature']} °C")
        print(f"💧 Humidity: {weather['humidity']}%")
        print(f"🌤️ Condition: {weather['description']}\n")

if __name__ == "__main__":
    main()
