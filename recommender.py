from menu import get_menu
from reviews import get_reviews
from weather import get_weather
from local_time import get_local_time as get_time
from dotenv import dotenv_values, load_dotenv

load_dotenv() 
dotenv_values() 

def get_recommendations():
    menu_results = get_menu()
    review_results = get_reviews()
    weather = get_weather(dotenv_values()["city"], dotenv_values()["weather_api"])
    time_of_day = get_time()

    recommendations = {
        "menu": menu_results,
        "reviews": review_results,
        "weather": weather,
        "time_of_day": time_of_day
    }

    return recommendations

print(get_recommendations())