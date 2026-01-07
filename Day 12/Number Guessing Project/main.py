import art
import random

# 정답을 전역 상수로 설정
ANSWER = random.randint(0,100)
life = 0

def guess():
    global life
    game_over = False
    if input("choose a difficulty. Type 'easy' or 'hard' : ") == 'easy':
        life = 10
    else:
        life = 5

    while not game_over:
        if life < 1:
            game_over = True
            print("You've run out of guess. Refresh the page to run again")
        else:
            print(f"You have {life} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess :"))
            if guess_number < ANSWER:
                life -= 1
                if life > 0:
                    print("Too low\nGuess again")

            elif guess_number > ANSWER:
                life -= 1
                if life > 0:
                    print("Too high\nGuess again")

            else:
                game_over = True
                print(f"You got it! The answer was {ANSWER}")

print(art.logo)
guess()



