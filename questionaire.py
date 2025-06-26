def get_user_inputs():
    mood = input("What's your mood/craving? (adventurous, comfort, spicy, cheesy, etc): ")
    diet = input("Dietary preference? (vegetarian, vegan, chicken, no preference): ")
    meal = input("Meal size? (snack, full meal, drink/dessert): ")
    spice = input("Spice level? (not spicy, mild, spicy, very spicy): ")
    budget = input("Budget? (press Enter to skip): ")
    # time_of_day, weather, etc. can be fetched here
    return {
        "mood": mood,
        "diet": diet,
        "meal": meal,
        "spice": spice,
        "budget": budget or None,
    }

user_profile = get_user_inputs()
print(user_profile)
