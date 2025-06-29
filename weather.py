import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }
    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code != 200:
        print("API error:", data.get("message", "Unknown error"))
        return None
    weather_desc = data["weather"][0]["description"] 
    temp = data["main"]["temp"]  
    print(f"Weather: {weather_desc}, Temperature: {temp}°C")
    return {
        "weather": weather_desc,
        "temperature": temp,
        "city": data["name"]
    }
