import random

nicknames = ["Luna","Hammer","Happy","Bean","Dropout","Bubbles","Gummy Pop","Superman"
            ,"Captain","Janitor","Chicken Legs","Dimples"]

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("+"*50)


print(f"Hello {first_name} {random.choice(nicknames)} {last_name}")
