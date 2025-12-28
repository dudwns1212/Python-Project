루프는 컴퓨터에게 반복적인 코드를 작성하지 않고도 동작을 반복하도록 지시할 수 있게 해줍니다. 만약 컴퓨터가 1부터 100까지 출력하도록 만들고 싶다면, 각 숫자에 대해 print 문을 작성하거나, 1부터 100까지 모든 숫자를 직접 입력하는 것은 매우 번거로울 것입니다. 루프를 사용하면 규칙을 하나 정의하여 컴퓨터가 이를 따라 반복 작업을 수행할 수 있습니다.

### 구문

```
for <각 항목의 변수 이름> in <리스트>:
    <무언가 하기>
    <다른 일 하기>
```

### PAUSE 1 - 컴퓨터처럼 생각하기  
아래 코드가 출력할 내용을 예측해 보세요:  

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```

### 들여쓰기  
들여쓰기는 Python 프로그래밍에서 매우 중요합니다. 매번 `:` 기호가 사용될 때, 그 뒤에 오는 들여쓰기에 주의해야 합니다.

예: 이 코드는 매우 다르게 동작합니다.  

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print("Hello")
```

이 코드와 비교하면:  

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello")