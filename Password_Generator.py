import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

passwordR = []

print("Welcome to the PyPassword Generator!")
letters_user_choice = int(input("How many letters would you like in your password?\n"))
for a in range(letters_user_choice):
    passwordR.append(random.choice(letters))

symbols_user_choice = int(input("\n"f"How many symbols would you like?\n"))
for b in range(symbols_user_choice):
    passwordR.append(random.choice(symbols))


numbers_user_choice = int(input("\n"f"How many numbers would you like?\n"))
for c in range(numbers_user_choice):
    passwordR.append(random.choice(numbers))

print(passwordR)
random.shuffle(passwordR)
print(passwordR)

print(f"your password is:{passwordR}")
print(f"Your password is: {''.join(passwordR)}")
