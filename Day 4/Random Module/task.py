import random # 모듈, .py파일을 생성하여 모듈을 생성, import 키 워드를 사용해 해당 파일의 변수나 함수를 가져올 수 있음
rand_num = random.randint(1, 10)
print(rand_num) # 랜덤한 숫자 1~10

rand_num_0_to_1 = random.random()
print(rand_num_0_to_1) # random() -> 0.0~<1.0

#만약 5.0 전 까지만 뽑고싶다?
rand_num_0_to_5 = random.random()*5
print(rand_num_0_to_5)

rand_num = random.randint(0,1)

if rand_num == 1:
    print("앞")
else:
    print("뒤")