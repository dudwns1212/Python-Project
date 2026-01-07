파이썬은 블록 범위(block scope)를 가지지 않는다는 점에서 다른 프로그래밍 언어와 조금 다릅니다.

즉, for 루프, if 문, while 루프 등과 같은 다른 코드 블록 내부에서 생성된 변수는 로컬 범위를 갖지 않습니다. 해당 변수가 함수 내부에 있다면 함수 범위(function scope)를 가지며, 함수 외부라면 전역 범위(global scope)를 가지게 됩니다.

예:

```
# 어디에서나 접근 가능
my_global_var = 1

def my_function():
    # my_function() 내부에서만 접근 가능
    my_local_var = 2
    
for _ in range(10):
    # 어디에서나 접근 가능
    my_block_var = 3