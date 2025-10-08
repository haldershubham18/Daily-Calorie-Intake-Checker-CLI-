# tracker.py

#Name : Shubham Halder
#Roll No. : 2501410002
#Course : B.tech CSE CyberSecurity 2025-2029
#Date : 08-10-2025
#Title: Daily calorie Tracker CLI Program 


print("Hello! Welcome to the Calorie Tracker!")
print("This program helps you track your daily calories.")
print()

# Making empty lists for meals and calories
meals = []
calories = []

# Asking how many meals
num_meals = input("How many meals did you eat today? ")

# Checking if input is a number
is_number = True
for char in num_meals:
    if char not in "0123456789":
        is_number = False
        break

if is_number and num_meals != "":
    num_meals = int(num_meals)
else:
    print("That's not a number of times one can eat! I'll set it to default 3 meals.")
    num_meals = 3

print()

# Getting meal information
count = 0
while count < num_meals:
    count = count + 1
    
    meal_name = input(f"What was meal #{count} called? ")
    meals.append(meal_name)
    
    calorie_input = input(f"How many calories in {meal_name}? ")
    
# Checking if calorie input is a number
    is_calorie_number = True
    has_decimal = False
    for char in calorie_input:
        if char not in "0123456789.":
            is_calorie_number = False
            break
        if char == ".":
            if has_decimal:
                is_calorie_number = False
                break
            else:
                has_decimal = True
    
    if is_calorie_number and calorie_input != "":
        if has_decimal:
            calorie_float = float(calorie_input)
        else:
            calorie_float = float(calorie_input)
        calories.append(calorie_float)
        print(f"Okay,I have added {meal_name} with {calorie_float} calories.")
    else:
        print("That's not a valid number! Using 0 calories.")
        calories.append(0)
    
    print()

# Calculating totals
total = 0
i = 0
while i < len(calories):
    total = total + calories[i]
    i = i + 1

if len(calories) > 0:
    average = total / len(calories)
else:
    average = 0

# Getting daily limit
limit_input = input("What is your daily calorie limit? ")

# Checking if limit input is a number
is_limit_number = True
has_decimal_limit = False
for char in limit_input:
    if char not in "0123456789.":
        is_limit_number = False
        break
    if char == ".":
        if has_decimal_limit:
            is_limit_number = False
            break
        else:
            has_decimal_limit = True

if is_limit_number and limit_input != "":
    if has_decimal_limit:
        limit = float(limit_input)
    else:
        limit = float(limit_input)
else:
    print("I didn't understand that. Using 2000 as default.")
    limit = 2000

print()
print("=== YOUR CALORIE SUMMARY ===")
print()

# Showing all meals
print("Your meals today:")
print("Meal\t\tCalories")
print("----\t\t--------")

j = 0
while j < len(meals):
    print(f"{meals[j]}\t\t{calories[j]}")
    j = j + 1

print()
print(f"TOTAL CALORIES: {total}")
print(f"AVERAGE PER MEAL: {average}")
print(f"YOUR DAILY LIMIT: {limit}")
print()

# Checking if over limit
if total > limit:
    over = total - limit
    print(f"WARNING! You are over your limit by {over} calories!")
    print("Maybe eat less tomorrow!")
else:
    if total == limit:
        print("Perfect! You hit your limit exactly!")
    else:
        under = limit - total
        print(f"Good job! You are under your limit by {under} calories!")
        print("You can have a small snack!")

print()

# Asking about saving to file
save = input("Do you want to save this to a file? (yes/no) ")

if save == "yes" or save == "y" or save == "Yes" or save == "Y":
# Get current date
    import datetime
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    
    date_string = f"{year}-{month}-{day} {hour}:{minute}"
    
# Create filename
    filename = "my_calorie_log.txt"
    
# Write to file
    file = open(filename, "w")
    
    file.write("MY CALORIE DIARY\n")
    file.write("================\n")
    file.write(f"Date: {date_string}\n")
    file.write(f"Daily limit: {limit}\n")
    file.write("\n")
    file.write("MEALS:\n")
    file.write("------\n")
    
    k = 0
    while k < len(meals):
        file.write(f"{meals[k]}: {calories[k]} calories\n")
        k = k + 1
    
    file.write("\n")
    file.write(f"TOTAL: {total} calories\n")
    file.write(f"AVERAGE: {average} calories per meal\n")
    file.write("\n")
    
    if total > limit:
        file.write("STATUS: OVER LIMIT\n")
    else:
        if total == limit:
            file.write("STATUS: AT LIMIT\n")
        else:
            file.write("STATUS: UNDER LIMIT\n")
    
    file.write("================\n")
    file.close()
    
    print(f"Saved to {filename}!")
    print("You can find this file in the same folder as this program.")
else:
    print("Okay, not saving to file.")

print()
print("=== THANK YOU FOR USING CALORIE TRACKER! ===")
print("Come back tomorrow!")
