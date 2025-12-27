rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# 리스트를 만들고
rock_paper_scissors = [rock, paper, scissors]
# 랜덤 숫자 0~2를 뽑아주는 random 함수를 뽑거나 choice 함수 활용
import random
computer_chose = random.randint(0,2)
player_chose =  int(input('what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print(rock_paper_scissors[player_chose])
print('\nComputer chose:\n')
print(rock_paper_scissors[computer_chose])
print('\n')

if player_chose == 0:
    if computer_chose == 1:
        print('You lose')
    elif computer_chose == 2:
        print('You win!')
    else:
        print("It's a draw")
elif player_chose == 1:
    if computer_chose == 0:
        print('You win!')
    elif computer_chose == 2:
        print('You lose')
    else:
        print("It's a draw")
else:
    if computer_chose == 0:
        print('You lose')
    elif computer_chose == 1:
        print('You win!')
    else:
        print("It's a draw")