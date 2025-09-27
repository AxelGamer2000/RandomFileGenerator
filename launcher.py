user_input = int(input("1. ui, 2. helper, 3. settings\n> "))

if user_input == 1:
    with open("main_ui.py", "r") as file:
        exec(file.read())
elif user_input == 2:
    with open("helper.py", "r") as file:
        exec(file.read())
elif user_input == 3:
    with open("settings_ui.py", "r") as file:
        exec(file.read())