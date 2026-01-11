from contextlib import nullcontext

import art
import game_data
import random

data_len = len(game_data.data)
a = random.randint(0, data_len-1)
def choice_b(choice_a):
    bb = random.randint(0, data_len-1)
    while bb == choice_a:
        bb = random.randint(0, data_len-1)
    return bb
b = choice_b(a)

def compare_follower(input_answer, compare_a, against_b):
    global a
    if input_answer == 'A':
        if compare_a > against_b:
            a = b
            return True
        return False
    elif input_answer == 'B':
        if compare_a < against_b:
            a = b
            return True
        return False
    return False

total_score = 0

while True:
    print(art.logo)
    if total_score > 0:
        b = choice_b(a)
        print(f"You're right! Current score: {total_score}.")
    print(f'Compare A: {game_data.data[a]['name']}, a {game_data.data[a]['description']}, from {game_data.data[a]['country']}')
    print(art.vs)
    print(f'Against B: {game_data.data[b]['name']}, a {game_data.data[b]['description']}, from {game_data.data[b]['country']}')

    answer = input("Who has more followers? Type 'A' or 'B': ")
    correct = compare_follower(answer, game_data.data[a]['follower_count'], game_data.data[b]['follower_count'])
    if correct:
        total_score += 1
        print('\n' * 20)
    else:
        print('\n' * 20)
        print(art.logo,f"\nSorry, that's wrong. Final score: {total_score}")
        break
