def main():
    import random

    numbers = "0123456789"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    capital_alphabets = "ABCDEFGHIJKLMNOPQRST"
    signs = "!@#$%^&*()_+-=*/?|.><,"
    characters = numbers + alphabet + capital_alphabets + signs

    print("Welcome to Password Generator!")
    length = int(input("Please Enter the length of the password: "))
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    print("*" * 50)
    print(f"Your password is: {password}")