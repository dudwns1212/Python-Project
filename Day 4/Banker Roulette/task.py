friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# import random으로 0~4(index)를 랜덤으로 뽑는 변수를 생성
import random
rand_num_index = random.randint(0, len(friends)-1)

print(friends[rand_num_index])

#random.py 안에 choice 라는 함수도 존재함, 리스트 내에서 랜덤의 값을 뽑아주는 함수
print(random.choice(friends)) # 위의 함수와 동일하게 작동함

