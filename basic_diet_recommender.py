# Step 1: Calculate BMR (example values)
def calculate_bmr(weight, height, age, gender):
    if gender == "male":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)


# Step 2: Compute daily caloric intake (example activity factor)
def compute_daily_caloric_intake(bmr, activity_factor):
    return bmr * activity_factor


# Example user data
weight = 70  # kg
height = 175  # cm
age = 30
gender = "male"
activity_factor = 1.55  # moderately active

bmr = calculate_bmr(weight, height, age, gender)
daily_caloric_intake = compute_daily_caloric_intake(bmr, activity_factor)
remaining_intake = daily_caloric_intake

# Step 3-7: Meal scheduling and menu selection
meals = ["breakfast", "lunch", "dinner"]
menu = {
    "breakfast": {"oatmeal": 300, "eggs": 200},
    "lunch": {"salad": 400, "sandwich": 500},
    "dinner": {"chicken": 600, "pasta": 700},
}

nutrition_intake = {"calories": 0, "proteins": 0, "fats": 0, "carbs": 0}

for meal in meals:
    print(f"Select your {meal} menu:")
    for item, calories in menu[meal].items():
        print(f"{item}: {calories} calories")

    choice = input(f"Enter your choice for {meal}: ")
    if choice in menu[meal]:
        remaining_intake -= menu[meal][choice]
        nutrition_intake["calories"] += menu[meal][choice]
        print(f"Remaining intake: {remaining_intake} calories")
    else:
        print("Invalid choice")

print("Daily nutrition intake:", nutrition_intake)


####
# Calculate BMR (example values)
def calculate_bmr(weight, height, age, gender):
    if gender == "male":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)


# Compute daily caloric intake (example activity factor)
def compute_daily_caloric_intake(bmr, activity_factor):
    return bmr * activity_factor


# Example user data
weight = 70  # kg
height = 175  # cm
age = 30
gender = "male"
activity_factor = 1.55  # moderately active

# Calculate BMR and daily caloric intake
bmr = calculate_bmr(weight, height, age, gender)
daily_caloric_intake = compute_daily_caloric_intake(bmr, activity_factor)

# Initialize remaining intake
remaining_intake = daily_caloric_intake

print(f"Initial remaining intake: {remaining_intake} calories")
