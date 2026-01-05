# 카드 덱의 크기는 무제한입니다.
# 조커 카드는 사용하지 않습니다.
# Jack/Queen/King은 모두 10으로 계산됩니다.
# Ace는 11 또는 1로 계산될 수 있습니다.
# 다음 리스트를 카드 덱으로 사용하세요:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

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

player_cards = []
computer_cards = []

is_continue_player = True
is_continue_computer = True
sum_card_computer = 0

first_second = input("먼저 받으시겠습니까?(y/n) : ")
for card in range(2):
    if first_second == "y":
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    else:
        computer_cards.append(random.choice(cards))
        player_cards.append(random.choice(cards))
""" 마지막 딜러가 카드를 뽑는 함수, 17보다 커지면 return """
def computer_last(sums):
    global is_continue_computer
    while is_continue_computer:
        for c_card in computer_cards:
            if 11 in computer_cards:
                if sums + c_card > 21:
                    c_card = 1
                    computer_cards[computer_cards.index(11)] = 1
            sums += c_card
            if sums < 17:
                print(f"딜러 카드의 합->{sums}, 카드를 뽑습니다.")
                computer_cards.append(random.choice(cards))
            else:
                is_continue_computer = False
                break
    return sums


while is_continue_player:
    sum_card_player = 0
    now_status = ""
    for p_card in player_cards:
        if 11 in player_cards:
            if sum_card_player + p_card > 21:
                p_card = 1
                player_cards[player_cards.index(11)] = 1
        sum_card_player += p_card

        if sum_card_player > 21:
            print(f"BOOM!! {sum_card_player}, 21이 넘었어요, 패배!")
            now_status = 'boom'
    if now_status == 'boom':
        break

    print(f"당신의 카드 합은 {sum_card_player} 입니다!")
    more = input("카드를 더 받으시겠습니까?(y/n) : ")
    if more != "y":
        print("-----------------------------")
        is_continue_player = False
        sum_card_computer = computer_last(sum_card_computer)
        if sum_card_computer > 21:
            print(f"{sum_card_computer}, 딜러의 카드가 21을 넘겼습니다, 승리!!")
        elif sum_card_player > sum_card_computer:
            print(f"딜러 카드 합->{sum_card_computer}, 승리!")
        elif sum_card_player < sum_card_computer:
            print(f"딜러 카드 합->{sum_card_computer}, 패배..")
        else:
            print(f"딜러 카드 합 -> {sum_card_computer}, 같은 합 입니다. 비겼습니다")
    else:
        player_cards.append(random.choice(cards))