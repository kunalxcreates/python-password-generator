import random
import string

def generate_password(length, use_symbols, use_numbers):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    characters = letters

    if use_numbers:
        characters += numbers

    if use_symbols:
        characters += symbols

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("=== Password Generator ===")

length = int(input("Enter password length: "))

symbols_choice = input("Include symbols? (yes/no): ").lower()
numbers_choice = input("Include numbers? (yes/no): ").lower()

use_symbols = symbols_choice == "yes"
use_numbers = numbers_choice == "yes"

password = generate_password(length, use_symbols, use_numbers)

print("\nGenerated Password:")
print(password)
