class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def calculate_daily_nutrition(food_list):
    total_cal = 0
    total_pro = 0
    total_car = 0
    total_fat = 0

    for food in food_list:
        total_cal += food.calories
        total_pro += food.protein
        total_car += food.carbs
        total_fat += food.fat

    print("24 hours nutrition data tracker")
    print(f"total calories:{total_cal} kcal")
    print(f"total proteins:{total_pro} g")
    print(f"total carbohydrate:{total_car} g")
    print(f"total fat:{total_fat} g")

    warning = []
    if total_cal > 2500:
        warning.append("calories are over 2500 kcal!")
    if total_fat > 90:
        warning.append("fat is over 90 g!")

    if warning:
        print("\n warning:" + " ".join(warning))
    else:
        print("\nnurtrition is okay!")

    return total_cal, total_pro, total_car, total_fat


if __name__ == "__main__":
    apple = food_item("apple", 60, 0.3, 15, 0.5)
    purplr_sweet_potato = food_item("purple sweet potato", 80, 1.2, 30, 0.2)
    chicken_leg = food_item("chicken leg", 160, 19, 0, 7.2)
    pizza = food_item("pizza", 300, 12, 36, 10)

    daily_food = [apple, purplr_sweet_potato, chicken_leg, pizza, pizza]
    calculate_daily_nutrition(daily_food)