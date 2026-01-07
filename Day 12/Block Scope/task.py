my_global_var = 1

def my_function():
    my_local_var = 2

for _ in range(1):
    my_block_var = 3

print("전역 변수를 출력 : ", my_global_var)
print("지역 변수는 출력이 안돼요")
print("블록 범위 안의 변수는? : ", my_block_var)