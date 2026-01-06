# 카드 덱의 크기는 무제한입니다.
# 조커 카드는 사용하지 않습니다.
# Jack/Queen/King은 모두 10으로 계산됩니다.
# Ace는 11 또는 1로 계산될 수 있습니다.
# 다음 리스트를 카드 덱으로 사용하세요:

# 리스트의 카드들은 동일한 확률로 선택됩니다.
# 뽑힌 카드는 덱에서 제거되지 않습니다.
# 컴퓨터가 딜러 역할을 합니다.

"""
1. 딜러(컴퓨터)는 번갈아가며 플레이어와 자신에게 카드를 나눠준다.
2. 플레이어는 받은 카드를 확인하고 카드를 더 받던지 멈출 수 있다.
3. 21이 넘어가면 자동으로 패배이며, 딜러의 카드 합 보다, 플레이어의 카드 합이 더 커야 이기는 게임이다.
"""

import random
import art
print(art.logo)

""" card를 뽑는 함수 """
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

""" 카드의 합을 계산하는 함수 """
def calculate_cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

""" 카드를 비교하는 함수(결과) """
def compared(c_point, u_point):
    if c_point == u_point:
        return "무승부!"
    elif c_point == 0:
        return "딜러 블랙잭!.. 패배"
    elif u_point == 0:
        return "블랙잭! 승리!"
    elif u_point > 21:
        return "21을 넘었어요 ㅠ 패배!"
    elif c_point > 21:
        return "딜러가 21을 넘겼어요! 승리!"
    elif u_point > c_point:
        return "승리!"
    else:
        return "패배!"

def play_game():
    player_cards = []
    computer_cards = []
    sum_player_cards = -1
    sum_computer_cards = -1
    game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        sum_player_cards = calculate_cards(player_cards)
        sum_computer_cards = calculate_cards(computer_cards)
        print(f"플레이어 카드의 합은 {sum_player_cards} 입니다")
        print(f"딜러의 첫 번째 카드는 {computer_cards[0]} 입니다")

        if sum_player_cards == 0 or sum_computer_cards == 0 or sum_player_cards > 21:
            game_over = True
        else:
            deal_continue = input("카드를 더 받으시겠습니까? 'y' or 'n' : ")
            if deal_continue == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

    while sum_computer_cards != 0 and sum_computer_cards < 17:
        computer_cards.append(deal_card())
        sum_computer_cards = calculate_cards(computer_cards)

    print(f"final user card : {sum_player_cards}")
    print(f"final computer card : {sum_computer_cards}")
    print(f"result : {compared(sum_computer_cards, sum_player_cards)}")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
