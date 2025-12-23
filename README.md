# Python-Project
파이썬 공부 100일

## 1일차
약속

- 매일 강의 1개 이상
- Notion에 배운 코드 정리
- 강의와 코딩을 함께하기 + 매일 코딩 연습 30분

### 출력

print(”여기에 쓰고싶은 문구를 작성”) → 

C:\Users\ernmq\AppData\Local\Python\pythoncore-3.14-64\python.exe "C:\Users\ernmq\PycharmProjects\100 Days of Code - The Complete Python Pro Bootcamp\Day 1\task\[task.py](http://task.py/)"  → 실행한 파일의 위치 
Hello world!  → 컴퓨터에서 내린 명령의 결과

종료 코드 0(으)로 완료된 프로세스  → 프로세스의 결과를 나타냄

괄호 안에 큰 따옴표 혹은 작은 따옴표를 넣는 이유는  컴퓨터에게 따옴표 사이에 있는 것이 코드가 아니라는 것을 알리기 위해서임.

이러한 텍스트를 프로그래밍 용어로 String이라 한다.

만약에 따옴표를 넣지 않고 실행을 하면 

```python
File "C:\Users\ernmq\PycharmProjects\100 Days of Code - The Complete Python Pro Bootcamp\Day 1\task\task.py", line 1
    print("Hello world!)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

이렇게 SyntaxError가 발생함

이렇게 오류가 발생하면 아래의 빨간 부분을 복사하여 구글에 붙여넣으면 됨

### 문자열 조작

\n : 줄바꿈

\t : 공백

### 들여쓰기 오류(IndentationError)

“” 안에 말고 코드에서 

```python
이부분 print("hello")
```

이런식으로 코드를 작성했을 때, 들여쓰기 오류가 발생함, 따라서 공백이나, tab을 상황에 맞게 써야

### input() 함수

input() : 터미널에 글자를 입력하여 변수로 활용할 수 있음

```python
myName = input("Hello Name!")
print("Hello " + myName + "!")
print("My name is" + " " + "Angela")
```

입력값 → Angela 

Hello Name!Angela
Hello Angela!
My name is Angela

참고로 input() 괄호 안에 글자 안넣어도 됨

```python
print(”Hello ” + input(”What is your name?”))
```

위의 코드의 경우에는 input함수가 먼저 실행이됨, 왜? print 함수가 Hello까지 읽고 뒤에 input() 함수를 읽기 때문에 먼저 실행하는 것 처럼 보이는거

따라서 터미널에는

What is your name?고영준

Hello 고영준

### 변수

프로그래밍에서 데이터를 참조하거나 참조할 수 있도록 데이터를 특정 이름으로 지정할 수 있게 해주는 개념

len() 과 input()을 활용하여 내 이름의 길이를 나타내는 프로그램

```python
name = input("What is your name?")
print(len(name))
```

입력 → 고영준

What is your name?고영준
3

모든 내용을 변수로 나누기 → 위의 문제를 모두 변수로 나타내서 해결해보기

```python
username = input()
length = len(name)

print(username, length)
```

똑같이 고영준을 입력

고영준
고영준 3

### 변수 이름의 규칙

1. 변수 이름은 설명적이어야 합니다
2. 단어 사이에 공백을 사용하지 마세요
3. 숫자로 시작하지 마세요
4. print나 input 같은 특별한 단어를 사용하지 마세요
5. 오타가 날 가능성이 적은 간단한 단어를 선택하세요
6. 회사에서 일을 시작한다면 회사 스타일 가이드를 확인하세요

### 1일차 프로젝트(밴드 이름 생성기 프로젝트)

1. 프로그램의 인사말을 만들어 보세요.
2. 사용자가 자란 도시 이름을 입력받고 그것을 변수에 저장하세요.
3. 사용자가 반려동물의 이름을 입력받고 그것을 변수에 저장하세요.
4. 도시 이름과 반려동물의 이름을 결합하여 그들에게 밴드 이름을 보여주세요.

```python
print("밴드 이름을 고민중이신가요?\n제가 도와드릴게요!")
country = input("어디에서 태어나고 자랐나요?\n입력하세요 : ")
print("확인했습니다.")
pet = input("반려동물의 이름이 무엇인가요? 없다면 소중한 것의 이름이 무엇인가요?\n입력하세요 : ")
print("밴드명 : " + country + " " + pet)
```

⇒

밴드 이름을 고민중이신가요?
제가 도와드릴게요!
어디에서 태어나고 자랐나요?
입력하세요 : Sky
확인했습니다.
반려동물의 이름이 무엇인가요? 없다면 소중한 것의 이름이 무엇인가요?
입력하세요 : boom
밴드명 : Sky boom

간단하게 인사말을 포함해서 2줄로도 가능함



```python
print("밴드 이름을 고민중이신가요?\n제가 도와드릴게요!")
print("밴드명 : " + input("어디서 태어나셨나요?\n->" + " " + input("pet의 이름은?\n->")))

```

## 2일차

## 파이썬의 기본 데이터 형식

### String

`print("Hello"[0])` → [index]를 하면 index번째의 단어를 출력해준다.

0부터 시작하며 음수로도 표현이 가능하다(-1이 마지막 즉, -5가 H가 됨) 
`print("123" + "456")` → 숫자가 아닌 문자열임 ⇒ 123456

### Integer

숫자만 입력하면 됨
`print(123 + 456)` → 579로 연산을 하게 됨

또한 큰 숫자 123456789를 미국에서는 3자리마다 ,로 구분을하는데 123,456,789

이 구분을 코딩에서는 _ 로 구분할 수 있음 → `print(123_456_789)` → 123456789

### Float

소수점이 존재하는 숫자 → 부동 소수점 데이터 타입(Float)

3.141592

### Boolean

True, False

## 형식 오류와 형식 확인, 그리고 형 변환

### 형식 오류

len() → String Type을 받음, int를 넣게 되면 형식 오류가 발생함

len(123) ⇒ TypeError: object of type 'int' has no len()

### 타입 확인

Python에서 값이나 변수의 데이터 타입을 확인하려면 type() 함수를 사용할 수 있다.
`print(type("Hello"))` ⇒ <class 'str'>
`print(type(123))` ⇒ <class 'int'>
`print(type(123.45))` ⇒ <class 'float'>
`print(type(True))` ⇒ <class 'bool'>

### 타입 변환

특정 함수를 사용하여 데이터를 다른 데이터 타입으로 변환할 수 있다. 

float(), int(), str()
`print("123" + "456")`  위에서 이 경우가 123456이 출력되는 것을 보았다, 이것을 형 변환을 통해 int 타입으로 바꿔 연산을 하여 579를 출력하려 한다
`print(int("123") + int("456"))` ⇒ 579
`print(int(123.456))` ⇒ 123 이 출력되며 이를 통해 뒤의 소수점이 떨어지고 정수형으로 변한 것을 확인

** int(”abc”) ⇒ 이런건 안된다

문제 : 아래 코드를 오류 없이 실행되도록 수정하세요

print("Number of letters in your name: " + len(input("Enter your name")))

→ 문자열 + 문자열이어야 하는데 갑자기 len() 함수로 정수가 더해져버림 → 문자열 + 정수 ⇒ 오류 발생

따라서 str(len(input(”Enter your name”))) 으로 형변환을 시켜줘야함

## 파이썬의 수학 연산

`print(123 + 456)`  덧셈

`print(7 - 3)`  뺄셈

`print(6 / 3)`  나눗셈 ⇒ 2.0

`print(3 * 2)`  곱셈
`print(6//3)`  ⇒ 2 , 위의 /의 경우는 Float로, //는 정수로 결과가 출력되는 것을 볼 수 있음
`print(2**3)` ⇒ 8 , 연산에서 제곱임

곱셈이나 나눗셈이 최우선 연산이 되고 그 다음 덧셈과 나눗셈이 실행됨

() → ** → * → / → + → -  ⇒ 연산 우선 순위

실제로는 곱셈과 나눗셈은 왼쪽에 있는것이 우선순위가 됨

`print(3 * 3 + 3 / 3 - 3)`

⇒ `9 + 1.0 - 3 = 7.0`

`print(3 * 3 + 3 / 3 -3)`

`# 다음의 출력이 3이 되게 하시오`

⇒ `print(3 * (3 + 3) // 3 - 3)` = 3

문제 : **BMI 계산기**

height = 1.65
weight = 84

bmi = weight / height**2

print(bmi)

⇒ 30.~~~~~

print(int(bmi)) ⇒ 30

## 파이썬의 숫자 처리 및 F-String

### 반올림

round()를 활용하여 소수점을 반올림하여 정수로 표현할 수 있다.

`bmi = 84 / 1.65 ** 2`

`print(bmi)`

`print(round(bmi))`

⇒30.85399449035813, 31

단순히 끝을 잘라내는 int 형 변환보다 수학적인 계산이 가능함

round는 2개의 변수를 받을 수 있다, 올리고자 하는 변수와 자리수를 입력할 수 있음
`print(round(bmi,2))` ⇒ 30.85

### 할당 연산자

`score = 0`

`#User Score A point`

`score += 1`

`print(score)`

⇒ 1

이런것을 할당 연산자라 하며 +=, -=, *=, /= 가 있다

### F-String

`score = 0`

`print("Your score is " + str(score)) # -> 번거로움`

`print(f"Your score is = {score}") # f가 큰 따옴표나 작음 따옴표 앞에 와야함`

⇒

Your score is 0
Your score is = 0

항상 형 변환을 하기에는 귀찮음, 따라서 F-String을 통해서 문자열 안에서 중괄호로 변수를 사용할 수 있음

## 팁 계산기 프로젝트

우리는 팁 계산기를 만들어 볼 것입니다.

만약 계산서 금액이 $150.00이고, 5명이 나누며, 팁이 12%인 경우:

각 사람이 지불해야 할 금액은:

(150.00 / 5) * 1.12 = 33.6

결과를 소수점 둘째 자리까지 포맷팅한 후 = 33.60

⇒

`print("Welcome to the tip calculator!")`

`bill = float(input("What was the total bill? $"))`

`tip = int(input("What percentage tip would you like to give? 10 12 15 "))`

`people = int(input("How many people to split the bill? "))`

`print(round(bill * (tip/100) / people, 2))` ⇒ tip.xx

⇒

Welcome to the tip calculator!
What was the total bill? $2587
What percentage tip would you like to give? 10 12 15 12
How many people to split the bill? 7
44.35
