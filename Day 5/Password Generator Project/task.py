letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#랜덤의 글, 숫자, 기호를 활용해야 하므로 random을 불러온다
import random

#반복문과 range 함수를 활용해서 사용자가 고른 수만큼 반복하여 랜덤의 문자를 출력
password = []
for user_letter in range(nr_letters):
    rand_letter = random.randint(0, len(letters) - 1)
    password.append(letters[rand_letter])
for user_number in range(nr_numbers):
    rand_number = random.randint(0, len(numbers) - 1)
    password.append(numbers[rand_number])
for user_symbol in range(nr_symbols):
    rand_symbol = random.randint(0, len(symbols) - 1)
    password.append(symbols[rand_symbol])
random.shuffle(password)
for pw in password:
    print(pw, end="")

