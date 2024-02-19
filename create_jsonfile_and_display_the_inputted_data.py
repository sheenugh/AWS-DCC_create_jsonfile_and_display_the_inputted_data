# ========= IMPORTS/S =========
import json

# ========= PSUEDO CODE =========
# - Ask user his/her name, age, fav food
ask_user_name = input("Enter your name:")
ask_user_age = int(input("Enter your age:"))
ask_user_fav_food = input("Enter your favorite food/s:")

# - Code for storing the user's inputted data
data = {
    "Name" : ask_user_name,
    "Age" : ask_user_age,
    "Favorite Food/s" : ask_user_fav_food
}

# - Code for storing the json data
json_data = json.dumps(data, indent=2)
print(json_data)

# - Coed for creating a new json file
with open('output.json', 'w') as file:
    file.write(json_data)

print("\n")
# - Printing the "Data has been saved to "
print("Thank you for filling up. Your data has been saved to out.json")
