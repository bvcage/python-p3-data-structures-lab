spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food.get("name") for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level") > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name")
        cuisine = food.get("cuisine")
        spices = "🌶" * food.get("heat_level")
        print(f"{name} ({cuisine}) | Heat Level: {spices}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food for food in spicy_foods if food.get("cuisine") == cuisine][0]

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    heat_levels = [food.get("heat_level") for food in spicy_foods]
    return sum(heat_levels) / len(heat_levels)

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]
