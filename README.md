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

## 3일차
## 조건문(If Else)

### 조건 확인

Python에서 조건문을 사용하여 조건을 확인하고 각 경우에 컴퓨터가 무엇을 해야 할지 알려주는 방법을 배웁니다.

예:

if <이 조건이 참이라면>:

<이 코드를 실행하세요>

### 조건이 거짓이라면?

else 키워드는 if 문에서 확인한 조건이 거짓일 때 실행될 코드 블록을 정의하는 데 사용됩니다.

if pigs can fly:

<절대 실행되지 않을 코드>

else:

print("이것이 현실입니다")

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height <= 120:
   print("Can't ride")
else:
    print("Can ride")
```

### Python 들여쓰기

Python에서 들여쓰기의 중요성을 이해해야 한다. 들여쓰기를 통해 특정 코드 라인을 다른 코드 라인의 하위로 만든다는 것을 표시할 수 있다

예:

if 5 > 2: #이것은 부모 코드 라인입니다

print("yes") #이것은 자식 코드 라인입니다 → 들여쓰기를 해야 오류가 나지 않음, if문 안에 있음을 명시

### 비교 연산자

- > 크다 (greater than)
- < 작다 (less than)
- >= 크거나 같다 (greater than or equal to)
- <= 작거나 같다 (less than or equal to)
- == 같다 (equal to)
- != 같지 않다 (not equal to)

## 나머지(Modulo Operator) %

모듈로 연산자는 나누기의 나머지를 제공

ex) 10 % 5 = 0

10 % 3 = 1

### 홀수인지 짝수인지 확인하기

Python에서 모듈로 연산자와 조건 검사를 사용하여 입력된 숫자가 홀수인지 짝수인지 확인하는 코드를 작성하세요.

만약 숫자가 홀수라면 "Odd"를 출력하고, 짝수라면 "Even"을 출력하세요.

```python
num = int(input("What is thinking of number"))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## 중첩 및 Elif

if/else 문을 다른 if/else 문 안에 넣을 수 있습니다. 이를 중첩(nesting)이라고 합니다.

예시:

```python
if maths_score>=90:
    if english_score>=90:
        print("당신은 모든 과목을 잘합니다.")
    else:
        print("당신은 수학을 잘합니다.")
if english_score>=90:
    print("당신은 영어를 잘합니다.")

```

이 경우, 학생이 수학과 영어 모두 90점을 넘긴 경우에만 "당신은 모든 과목을 잘합니다."라는 메시지를 받을 수 있습니다.

참고: else 문과 짝이 없는 독립적인 if 문도 사용할 수 있습니다.

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("please pay  $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
```

## 다중 If

다음과 같이 서로 관련이 없는 조건들을 확인하기 위해 필요한 만큼의 if 문을 작성할 수 있습니다.

아래 코드 블록을 비교해 보세요:

```python
# If/elif/else
if<조건1이 참일 경우>
    <A 수행>
elif<조건2가 참일 경우>
    <B 수행>
else
    <C 수행>
## A, B, C 중 하나만 수행
```

```python
# 중첩된 if 문
if<조건1이 참일 경우>
    <A 수행>
    if<조건2가 참일 경우>
        <B 수행>
        if<조건3이 참일 경우>
            <C 수행>
            
## 모두 실행될 수 있지만, 위의 조건이 모두 참이어야 함, 즉, 조건 1이 참일 경우만 조건 2가 확인됨
```

```python
# 다수의 if 문
if<조건1이 참일 경우>
    <A 수행>
if<조건2가 참일 경우>
    <B 수행>
if<조건3이 참일 경우>
    <C 수행>
    
## A, B, C 모두 수행할 수도 있음, 모두 조건이 확인되면 실행가능, 위에 있는 조건이 참이 아니여도 가능
```

if/elif/else 블록에서는 A, B, 또는 C 중 하나만 실행될 수 있습니다. 이는 if/elif/else가 서로 배타적이기 때문입니다. 첫 번째 조건이 거짓이어야 elif로 넘어가고, elif(혹은 여러 개의 elif)도 거짓이어야 else로 갑니다. 조건 2는 조건 1이 거짓일 경우에만 확인됩니다.

중첩된 if 문에서는 A, B, C 모두 실행될 수 있지만, 조건 1, 2, 3이 모두 참이어야 합니다. 컴퓨터는 조건 1이 참일 경우에만 조건 2를 확인합니다.

다수의 if 문에서는 A, B, C 모두 실행될 수 있습니다. 하지만 각각은 서로 완전히 독립적입니다. A와 B가 실행되지 않아도 C는 실행될 수 있습니다. 모든 조건은 다른 조건의 결과와 상관없이 모두 확인됩니다

## 파이썬 피자

축하합니다! 당신은 Python 피자에서 일자리를 얻게 되었습니다! 첫 번째 업무는 자동 피자 주문 프로그램을 만드는 것입니다.

사용자의 주문을 기반으로 최종 요금을 계산하세요. input() 함수를 사용하여 사용자의 선호 사항을 입력받고, 주문 총액을 합산한 후 그들에게 지불해야 할 금액을 알려주세요.

작은 피자 (S): $15

중간 피자 (M): $20

큰 피자 (L): $25

작은 피자에 페퍼로니 추가 (Y 또는 N): +$2

중간 또는 큰 피자에 페퍼로니 추가 (Y 또는 N): +$3

어떤 사이즈의 피자든 치즈 추가 (Y 또는 N): +$1

```python
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    if pepperoni == "Y" and extra_cheese == "Y":
        print("최종 요금은 $18. 입니다.")
    elif pepperoni == "N" and extra_cheese == "N":
        print("최종 요금은 $15. 입니다.")
    elif pepperoni == "N":
        print("최종 요금은 $16. 입니다.")
    else:
        print("최종 요금은 $17. 입니다.")
elif size == "M":
    if pepperoni == "Y" and extra_cheese == "Y":
        print("최종 요금은 $24. 입니다.")
    elif pepperoni == "N" and extra_cheese == "N":
        print("최종 요금은 $20. 입니다.")
    elif pepperoni == "N":
        print("최종 요금은 $21. 입니다.")
    else:
        print("최종 요금은 $23. 입니다.")
elif size == "L":
    if pepperoni == "Y" and extra_cheese == "Y":
        print("최종 요금은 $29. 입니다.")
    elif pepperoni == "N" and extra_cheese == "N":
        print("최종 요금은 $25. 입니다.")
    elif pepperoni == "N":
        print("최종 요금은 $26. 입니다.")
    else:
        print("최종 요금은 $28. 입니다.")

```

## 논리연산자

다양한 조건들을 논리 연산자를 사용하여 결합할 수 있습니다.

```python
A and B #두 조건 모두 참이어야 합니다
C or D #한 개의 조건만 참이어도 됩니다
not E #조건이 거짓이어야 합니다

```

### PAUSE 1 - 나이 45에서 55 수정

코드를 업데이트하여 나이가 45에서 55 사이(45와 55를 포함)의 사람들이 무료로 탑승할 수 있도록 하십시오.

나이가 45보다 크고 55보다 작은지 확인하려면 논리 연산자를 사용하세요.

주의: 간소화를 위한 경고는 단순히 제안일 뿐입니다. 참고하여 선택할 수도 있고, 무시할 수도 있습니다.

이 강의에서는 and, or, not 논리 연산자를 보여주고 싶었습니다. 따라서 복습을 위해 이 강의로 돌아올 경우를 대비하여 원래 코드를 유지하는 것을 권장합니다.

```python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        if age >= 45 & age <= 55: ## 45 <= age <= 55
            bill = 0
        else:
            bill = 12
            print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
```

## 보물섬 프로젝트

오늘의 목표는 "나만의 모험을 선택하는 게임"을 만드는 것입니다.

오늘 배운 내용을 사용하여 이 텍스트 기반 게임의 매우 간단한 버전을 만들어볼 것입니다.

게임의 논리를 설계하려면 [여기 링크된](https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload) 구조도를 사용하세요.

프로젝트를 완료한 후에는 게임을 확장하고 더 흥미롭게 만들 수도 있습니다!

```python
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first = input('\tType "left" or "right\n').lower()
if first == "left":
    print("You've come to lake. There is an island in the middle of the lake.")
    second = input('\t"wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if second == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        last = input("\tOne red, one yellow and one blue. Which colour do you choose?\n").lower()
        if last == "red":
            print("It's a room full of fire. Game Over.")
        elif last == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
```

⇒

Welcome to Treasure Island.
Your mission is to find the treasure.
Type "left" or "right
left
You've come to lake. There is an island in the middle of the lake.
"wait" to wait for a boat. Type "swim" to swim across.
wait
You arrive at the island unharmed. There is a house with 3 doors.
One red, one yellow and one blue. Which colour do you choose?
YELLOW
You found the treasure! You Win!

추가 사항으로 아예 다른 값을 넣었을 때는 조건이 다시 진행되게 하던가, 아니면 다음으로 못넘어가게 만드는 로직을 추가하는 것도 가능함

## 4일차
## Random Module

강의는 좀 내용이 복잡한데, 간단하게 말해서 컴퓨터 과학자들이 발명한 의사난수 생성기 → 랜던 숫자 생성

import random 으로 모듈을 불러와서 사용

```python
import random # 모듈, .py파일을 생성하여 모듈을 생성, import 키 워드를 사용해 해당 파일의 변수나 함수를 가져올 수 있음
rand_num = random.randint(1, 10)
print(rand_num) # 랜덤한 숫자 1~10

rand_num_0_to_1 = random.random()
print(rand_num_0_to_1) # random() -> 0.0~<1.0

#만약 5.0 전 까지만 뽑고싶다?
rand_num_0_to_5 = random.random()*5
print(rand_num_0_to_5)

```

여기서 보면 random(), randint(a,b), choice(list) 등의 함수들이 존재한다

### PAUSE 1 - 앞면 또는 뒷면

Python의 랜덤화에 대해 배운 내용을 사용하여 동전 던지기 프로그램을 만들어 보세요. 이 프로그램은 실행될 때마다 "앞면" 또는 "뒷면"을 랜덤하게 출력해야 합니다.

```python
rand_num = random.randint(0,1)

if rand_num == 1:
    print("앞")
else:
    print("뒤")
```

## 리스트

fruits = ["Cherry", "Apple", "Pear"]

### 리스트의 항목 접근하기

리스트 이름을 적고 대괄호 안에 접근하려는 항목의 인덱스를 입력하여 항목에 접근할 수 있다

states_of_america = ["Delaware", …]

states_of_america[0] → "Delaware”

컴퓨터와 관련된 모든 것에서, 숫자를 셀 때 첫 번째 번호는 항상 0부터 시작

### 음수 인덱스

리스트의 끝에서부터 항목을 접근하려면 음수 정수를 사용할 수 있다

```python
fruits= ["Cherry","Apple","Pear"]
fruits[-1]# 이것은 "Pear"를 반환합니다

```

### 항목 수정하기

리스트의 항목을 가져오는 동일한 구문을 사용해 항목을 수정할 수 있다

```python
fruits= ["Cherry","Apple","Pear"]
fruits[0] ="Orange"
# fruits는 이제 ["Orange", "Apple", "Pear"]가 됩니다

```

### 항목 추가하기

리스트의 끝에 항목을 추가하려면 append() 함수를 사용할 수 있다

```python
fruits= ["Cherry","Apple","Pear"]
fruits.append("Orange")
# fruits는 이제 ["Cherry", "Apple", "Pear", "Orange"]가 됩니다
```

```python
phone = ["Samsung", "Apple", "Shalom", "LG"]
        #    0         1        2        3
        #   -4        -3       -2       -1
print(phone[0])
print(phone[1])
print(phone[2])
print(phone[3])
print("--------------------------------")
phone[0] = "ICON"  # 이렇게 다른 값을 넣어 항목을 수정할 수 있음
print(phone[0]) # ICON
print(phone[1]) # Apple
print("--------------------------------")
# 항목 추가 => append
phone.append("Samsung")
print(phone[4]) # 마지막 인덱스에 추가
```

## 뱅커 룰렛

목록 friends에서 무작위로 이름을 선택하는 방법을 알아보세요.
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

⇒위에서 말했던 choice 함수를 써도 되고, randint를 써도 무관

```python
# import random으로 0~4(index)를 랜덤으로 뽑는 변수를 생성
import random
rand_num_index = random.randint(0, len(friends)-1)

print(friends[rand_num_index])

#random.py 안에 choice 라는 함수도 존재함, 리스트 내에서 랜덤의 값을 뽑아주는 함수
print(random.choice(friends)) # 위의 함수와 동일하게 작동함
```

## IndexError

### 리스트의 길이

len() 함수를 사용하여 리스트의 길이(리스트에 있는 항목의 수)나 문자열의 길이(문자열의 문자 수)를 구할 수 있다.

```python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america) # 그냥 리스트를 모두 출력
print(len(states_of_america)) # 리스트의 길이(개수)
print(len(states_of_america[0])) # 0번째 index 원소의 길이
```

리스트 길이 = 50  ⇒ 즉, 0~49의 index를 가지는 리스트, 그러면 만약에 50번째를 부르면?

```python
# 그럼 index 범위를 벗어난 숫자를 입력하면?
print(states_of_america[50])  -> IndexError 발생
```

⇒ File "C:\Users\admin\PycharmProjects\100 Days of Code - The Complete Python Pro Bootcamp\Day 4\IndexError\[task.py](http://task.py/)", line 14
print(states_of_america[50])  -> IndexError 발생
^^
SyntaxError: invalid syntax

### 중첩 리스트

리스트 안에 다른 리스트를 넣을 수 있으며, 이를 "중첩 리스트" 또는 "2차원 리스트"라고 한다.

```python
fruits= ["Cherry","Apple","Pear"]
veg= ["Cucumber","Kale","Spinnach"]
fruits_and_veg= [fruits,veg]
#리스트는 다음과 같은 모양이 됩니다: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
```

```python
# 중첩리스트, 2차원 리스트
mount_food = ['beef', 'namul']
sea_food = ['fish', 'solt']
food = [mount_food, sea_food]
print(food)
```

## 가위 바위 보 프로젝트

당신은 가위, 바위, 보 게임을 만들 것입니다. 랜덤화와 리스트에 대해 배운 내용을 사용해야 합니다.

```python
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
```

⇒ 실제 콘솔 화면

<p align="center">
  <img src="https://github.com/user-attachments/assets/49c907e8-4eb7-4991-94cc-b758b56ece7f" width="45%" />
  <img src="https://github.com/user-attachments/assets/d576cdbd-f44c-4908-80d9-bcb3225a9bb2" width="45%" />
</p>

## 5일차
## For Loops(반복문)

파이썬에서의 반복문 구조는 다음과 같다

for 변수명 int 리스트:

(들여쓰기필수)할일 1

(들여쓰기필수)할일 2

```python
fruits = ["Apple", "Peach", "Pear"]

i = 0
for fruit in fruits:
    i += 1
    print(f"{i}. {fruit}")
```

출력 ⇒

1. Apple
2. Peach
3. Pear

### PAUSE 1 - 컴퓨터처럼 생각하기

아래 코드가 출력할 내용을 예측해 보세요: Apple pie → Peach pie → Pear pie

```python
fruits= ["Apple","Peach","Pear"]
forfruitinfruits:
    print(fruit)
    print(fruit+" pie")
 
```

### 들여쓰기

들여쓰기는 Python 프로그래밍에서 매우 중요합니다. 매번 : 기호가 사용될 때, 그 뒤에 오는 들여쓰기에 주의해야 합니다.

예: 이 코드는 매우 다르게 동작합니다.

```python
fruits= ["Apple","Peach","Pear"]
forfruitinfruits:
    print(fruit)
    print("Hello")
```

이 코드와 비교하면:

```python
fruits= ["Apple","Peach","Pear"]
forfruitinfruits:
    print(fruit)
print("Hello")
```

첫 번째 반복문의 경우는 print(”Hello”)가 반복문 안에 포함되어 있다

하지만 두 번째 반복문은 print(”Hello”)가 반복문에 포함되어 있지 않아,  전혀 다른 코드라고 볼 수 있다.

## 최고 점수

### 합계

파이썬에는 통계를 위한 다양한 함수가 존재한다

합계의 경우는 sum()

```python
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
student_scores_sum = sum(student_scores)
print(student_scores_sum)
```

⇒ 2068

sum 함수는 어떻게 작성되었을까? → 반복문을 활용

```python
score_sum = 0
for students_score in student_scores:
    score_sum += students_score
print(score_sum)
```

### PAUSE 1 - 최대값

파이썬에는 max()와 min()이라는 내장 메서드도 있으며, 이를 사용하면 숫자 리스트를 전달하여 가장 큰 숫자나 가장 작은 숫자를 얻을 수 있습니다.

당신의 과제는 Python 프로그래머들이 이 기능을 루프와 조건문을 사용해서 어떻게 구축했을지 알아내는 것입니다.

⇒ 반복문을 활용해, 과거의 수와 현재의 수를 비교해서 더 크거나 작은 값들만 선별하는 방법

```python
max_score = 0
for student_score in student_scores:
    if student_score > max_score:
        max_score = student_score
    print(f"현재 가장 큰 점수 : ${max_score}")

min_score = 99999
for student_score in student_scores:
    if student_score < min_score:
        min_score = student_score
    print(f"현재 가장 작은 점수 : ${min_score}")
```

## Range와 함께 사용되는 For 루프

range() 함수와 Python For Loop의 조합은 우리가 원하는 횟수만큼 반복문을 실행할 수 있게 해줍니다. 리스트의 각 항목을 순회하는 대신, 숫자 범위를 순회할 수 있습니다.

### range 함수

range(1, 10)

이 코드는 자체적으로 아무 작업도 하지 않습니다. 예를 들어, 이를 출력하려고 하면 개별 숫자를 제공하지 않습니다.

그러나 이는 For Loop와 함께 사용할 수 있습니다. 예:

```python
fornumberinrange(1,10):
		print(number)

```

위 코드는 1부터 9까지의 숫자를 하나씩 출력합니다. 따라서 range는 다음과 같이 표현될 수도 있습니다:

a <= range(a, b) < b

여기서 숫자의 범위는 하한값(포함)과 상한값(미포함)에 의해 정의됩니다.

즉 자바의 반복문에서 for(i=1; i < 10; i ++;) { } 라고 생각하면 되는 것 같다.

→반복의 범위는 지정

### 정지 1 - 가우스 도전 과제

1부터 100까지의 숫자의 합을 구하세요. 여기서 1과 100 모두 포함됩니다.

```python
gaus = 0
for i in range(1,101):
		gaus += i
print(gaus)
```

## 비밀번호 생성기 프로젝트

프로그램은 다음과 같이 묻습니다:

```
비밀번호에 몇 글자를 원하시나요?
몇 개의 기호를 원하시나요?
몇 개의 숫자를 원하시나요?

```

사용자가 위 질문들에 응답하여 입력한 값을 기반으로 랜덤 비밀번호를 생성하는 것이 목표입니다. Python의 리스트와 반복문에 대한 지식을 활용하여 이 과제를 완성하세요.

### 쉬운 버전

비밀번호를 순차적으로 생성하세요. 먼저 글자, 그다음 기호, 마지막으로 숫자를 추가하십시오. 예를 들어, 사용자가

4개의 글자,

2개의 기호, 그리고

3개의 숫자를 원한다고 하면,

비밀번호는 다음과 같이 보일 수 있습니다:

fgdx$*924

모든 글자가 함께 있고, 모든 기호가 함께 있으며, 모든 숫자가 연달아 나타나는 것을 볼 수 있습니다. 먼저 이 문제를 해결해 보세요.

```python
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#랜덤의 글, 숫자, 기호를 활용해야 하므로 random을 불러온다
import random

#반복문과 range 함수를 활용해서 사용자가 고른 수만큼 반복하여 랜덤의 문자를 출력
password = []
for user_letter in range(nr_letters):
    rand_letter = random.randint(0, len(letters) - 1)
    password.append(letters[rand_letter])
for user_number in range(nr_numbers):
    rand_number = random.randint(0, len(numbers) - 1)
    password.append(numbers[rand_number])
for user_symbol in range(nr_symbols):
    rand_symbol = random.randint(0, len(symbols) - 1)
    password.append(symbols[rand_symbol])
for pw in password:
    print(pw, end="")
```

자동으로 줄바꿈이 되는 print에서 줄바꿈을 없애주는게 , end=”” 이다.

여기서는 randint를 활용했지만 choice를 사용하는게 더 깔끔해 보인다.

### 어려운 버전

쉬운 버전을 완성했다면, 이제 어려운 버전에 도전할 준비가 되었습니다. 이 프로젝트의 고급 버전에서는 최종 비밀번호가 특정 패턴을 따르지 않습니다. 그래서 위 예시는 다음과 같이 보일 수도 있습니다:

x$d24g*f9

그리고 비밀번호를 생성할 때마다 기호, 숫자, 글자의 위치가 다르게 나타납니다. 이것은 해커가 비밀번호를 깨기 더 어렵게 만듭니다.

⇒ 위의 리스트를 만들었고 이제 리스트를 복불복으로 출력해주는 함수를 찾으면 된다.

위에서와 같이 직접 함수를 만들어서 적용할 수도 있지만, **random.shuffle() 함수를 활용**

```python
random.shuffle(password)
for pw in password:
    print(pw, end="")
```

한 줄만 추가한다면 결과는 → $MH04HddD*1Z1l!n!W&6  이렇게 랜덤으로 섞여서 나오는 것을 확인할 수 있다.

## 6일차
# 6일차 프로젝트는 모두 아래의 링크에서 실행됨

https://reeborg.ca/reeborg.html

## 함수

파이썬에서는 함수를 다음과 같이 만들 수 있다.

```python
def <함수 이름>():
    print("Hello")
    # 다른 작업 수행
    # 다른 작업 계속 ...
```

함수이름() 을 호출하면 함수 내부의 들여쓰기 한 부분이 실행된다.

```python
def hello():
    print("Hello")

hello()
```

⇒ Hello

파이썬 함수 실습을 위해 Reeborg’s World 라는 웹페이지로 이동

<img width="1948" height="1121" alt="스크린샷 2025-12-29 175346" src="https://github.com/user-attachments/assets/459099fe-082b-42c5-b641-cf2961bdff95" />

move()를 호출하면 로봇의 방향으로 한칸 이동하는 것을 볼 수 있다

<img width="1879" height="909" alt="스크린샷 2025-12-29 175443" src="https://github.com/user-attachments/assets/f2b8a5f3-f3fa-4fa3-a729-6a43c952f0df" />

리보그의 키보드 라는 버튼을 클릭하면 리보그가 움직일 수 있는 함수들을 알려준다

<img width="1148" height="637" alt="스크린샷 2025-12-29 175652" src="https://github.com/user-attachments/assets/3541fc7c-2bd4-452b-9b01-1ac2a32ca7f8" />


### 실습- turn around, turn right를 만들어보기

키보드를 보면 turn_left만 존재해서 다시 돌리려면 turn_left를 여러번 입력해야한다

이를 함수로 쉽게 만들어보자


<img width="1497" height="880" alt="스크린샷 2025-12-29 180237" src="https://github.com/user-attachments/assets/ae6bbbcc-1f98-4cca-8256-cbbb1b937fad" />

위와 같이 turn_right, turn_around() 함수를 만들어서 동네를 한바퀴 돌아보는 프로그램을 실행

## 과제-여러 장애물을 넘어, 목적지에 도착하

<img width="1900" height="1011" alt="스크린샷 2025-12-29 180356" src="https://github.com/user-attachments/assets/f7a45156-2814-4791-8b1b-8a74b6c97e47" />

→ move() → turn_left() → move() → turn_right → move() → turn_right() → move()→ turn_left() 

→ move() …

이 반복문을 활용해서 코드를 작성해보자

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

for huddle in range(0,6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
```

<img width="1913" height="1017" alt="스크린샷 2025-12-29 181208" src="https://github.com/user-attachments/assets/9a5941a9-247b-4f21-ae07-a0e00672c434" />

추가로 반복문 안에 들어가는 저 구문도 함수로 만들어서 넣을 수 있다. (코드가 더 깔끔해보임)

** 코드 한번에 들여쓰기 하는법 Ctrl + ]

## 들여쓰기

<img width="655" height="335" alt="스크린샷 2025-12-29 181623" src="https://github.com/user-attachments/assets/ca0e2f3d-11c9-4ab0-9a6c-da6bfdf33a8d" />

항상 저 사각형의 구역을 생각하고, 함수 내에 코드가 존재하는지, 어디까지 이 함수의 코드인지 생각해야 함

### Tap VS Space ⇒ 탭이냐 공백이냐

파이썬 공식 문서에는 들여쓰기를 할 때, 공백을 4개 입력하라고 나와있음,

하지만 아래와 같이 한번만 공백을 해도, 코드는 실행됨

<img width="622" height="250" alt="스크린샷 2025-12-29 182138" src="https://github.com/user-attachments/assets/6c75f85b-c008-459f-86d5-a43c1a2e6f4b" />

취향 차이, 뭘 선택하든 똑같긴함

### While(반복문)

<img width="1627" height="843" alt="스크린샷 2025-12-29 182528" src="https://github.com/user-attachments/assets/d64380cf-5378-49d2-b972-010912536cc5" />

간단하게 For의 경우는 범위를 정해놓고 시작함, 해당 범위동안 사이클을 돌며 함수를 반복 실행

하지만 While의 경우는 조건이 참일 경우에 반복문이 실행, 조건이 False가 되기 전까지 무한으로 반복함

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_huddle = 6
while number_of_huddle > 0:
    jump()
    number_of_huddle -= 1
    print(number_of_huddle)
```

<img width="1866" height="1008" alt="스크린샷 2025-12-29 200622" src="https://github.com/user-attachments/assets/49701838-8516-4018-8e51-8064a80c8e60" />

위의 코드를 작성 후 실행시킨 모습, 출력문을 보면 6번을 반복하고, 0이 되었을 때, 반복문이 종료된 것을 볼 수 있다.

### huddle2 → at_goal()이 참일 경우 while 실행

<img width="1255" height="945" alt="스크린샷 2025-12-29 200921" src="https://github.com/user-attachments/assets/8a7516ed-4b7a-49d9-8c56-e56d35e405d9" />

허들의 구조는 huddle1과 동일하지만, 마지막이 골인 지점이 아니다. 

6개의 지점은 at_goal()이 참일수도 거짓일수도 있다.

<img width="901" height="175" alt="스크린샷 2025-12-29 201007" src="https://github.com/user-attachments/assets/cd2b0763-a4f3-4895-91eb-206e5aa2331b" />

while의 조건에 not at_goal()을 넣으면 될 것 같다

함수는 아래와 같이 작성했다.

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()
```

<img width="1888" height="874" alt="스크린샷 2025-12-29 201335" src="https://github.com/user-attachments/assets/16041a21-1d0b-4619-a382-807c55820ee1" />

실행을 시키면 위와 같이 잘 작동하는 것을 볼 수 있다.

## huddle3-조건을 설정한 반복문

<img width="976" height="545" alt="스크린샷 2025-12-29 201609" src="https://github.com/user-attachments/assets/9ba3e515-29e1-4da8-ad58-98a092ebcaca" />

허들3의 경우는 벽이 제 각각 존재한다, 즉 범위만 정해서 일정한 반복문을 실행하는건 맞지 않다.

<img width="1106" height="277" alt="스크린샷 2025-12-29 201701" src="https://github.com/user-attachments/assets/4423955d-8934-42ec-8b71-20871d6b1cf4" />

front_is_clear() : 앞이 비어있는가, wall_in_front() : 앞에 벽이 있는가, at_goal() : 목표 지점인가 를 활용하여 문제를 해결해야 한다.

다음과 같이 생각했다, 반복문은 동일하게 while문을 활용해 not at_goal(),

while문 안에서 조건문을 나눠 front_is_clear() → move() / wall_in_front() → is_wall()

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def is_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        is_wall()
    
```

위와 같이 코드를 작성했고, 실행하니 잘 되는 것을 확인했다, 다른 모양의 허들에서도 동일하게 잘 작동된다.

<img width="1875" height="896" alt="스크린샷 2025-12-29 202503" src="https://github.com/user-attachments/assets/ef241a2f-3ac2-4dbb-bb0d-2caf4bc9bcbb" />

## huddle4-높이가 다른 장애물

<img width="966" height="551" alt="스크린샷 2025-12-29 202804" src="https://github.com/user-attachments/assets/2bc8e74b-4825-49ce-bdcb-210ae82d8249" />

마지막 허들이다. 사진과 같이 높이가 다른 장애물을 고려해 로직을 작성해야 한다.

1. while not at_goal():
2. front_is_clear() → move()
3. wall_in_front() → [ turn_left() → move() → turn_right() ]
4. 다시 체크 front_is_clear()

이런 식으로 벽을 한칸 넘고 체크하는 로직을 추가해보자

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def is_wall():
    turn_left()
    move()
    turn_right()

walls = 0

def is_clear():
    move()
    turn_right()
    for down in range(walls):
        move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        is_wall()
        walls += 1
        if front_is_clear():
            is_clear()
    
```

처음에는 위와 같이 로직을 작성 후 실행 

<img width="965" height="483" alt="스크린샷 2025-12-29 203910" src="https://github.com/user-attachments/assets/370f0134-78b4-48f4-8061-7833a48bfa05" />

→ 잘 되는가 싶었는데 실패했다, 다시 로직을 살펴보니 walls를 초기화해주는 로직이 없었다.

따라서 조건문 함수 제일 마지막에 walls = 0을  추가 후 재실행했다.

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def is_wall():
    turn_left()
    move()
    turn_right()

walls = 0

def is_clear():
    move()
    turn_right()
    for down in range(walls):
        move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        is_wall()
        walls += 1
        if front_is_clear():
            is_clear()
				    walls = 0
```

<img width="1885" height="907" alt="스크린샷 2025-12-29 204402" src="https://github.com/user-attachments/assets/c2a660f7-6e11-4677-bc80-8ab1b39f5197" />

잘 동작하는 것을 볼 수 있다.

강의에서는 아래와 같은 코드로 작성하여 실행하였다.

<img width="735" height="677" alt="스크린샷 2025-12-29 204602" src="https://github.com/user-attachments/assets/c5889acf-5f2f-45eb-afb6-58e4f2958f16" />

내가 작성한 코드와 다른 점은, 강사님은 하나의 함수로 안에 로직을 작성하였다, 나는 down이라는 함수를 만들고 walls라는 변수를 만들어 벽의 개수만큼 내려오는 반복문을 실행했다면 wall_on_right() 라는 함수를 활용, 나는 이걸 확인 못했는데 라이브러리에 함수가 있었다.

<img width="1133" height="608" alt="스크린샷 2025-12-29 204929" src="https://github.com/user-attachments/assets/5bfe50e7-d33a-4b32-b5eb-dad819d0f021" />

조금 어렵게 푼 감이 없지 않아 있지만 잘 작동하니 해결!

## 6일차 프로젝트 - 미로탈출



위의 동영상과 같이 로봇은 계속 움직인다.

미로는 오른쪽 벽을 따라가게 되면 목적지에 도착한다.

1. 앞에 벽이 있는지, 오른쪽에 벽이 있는지 체킹
2. 오른쪽에 벽이 있으며, 앞이 비어있다면 move()
3. 오른쪽에 벽이 있으며, 앞에도 벽이 있다면 turn_right()
4. 앞에 벽이 있는지 체크 → 있다면 turn_right, 없다면 move()

위의 생각을 정리하고 코드를 작성, 작성하면서 생각이 바뀌어서 위의 생각과 달라진 코드도 있음

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        move()
```

1차로 코드를 작성 후 테스트

<img width="478" height="466" alt="스크린샷 2025-12-29 213446" src="https://github.com/user-attachments/assets/683f56ec-25c7-4f7d-9822-918ded30c0cb" />

대부분의 상황에서는 잘 작동하는데, 어떤 상황에서는 이렇게 루프를 돌면서 코드가 반복됨

4번 돌면서 오른쪽 벽을 찾지 못하면 미아가 되는 경우가 발생함

go 라는 변수를 추가해서 go가 4를 넘어가면 강제로 move 실행

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
go = 0
while not at_goal():
    if go < 4:
        if wall_on_right():
            if front_is_clear():
                move()
                go = 0
            else:
                turn_left()
        else:
            turn_right()
            move()
            go += 1
    else:
        turn_left()
        go = 0
```

이렇게 코드를 작성하고 실행하니 아주 잘됨

<img width="1878" height="916" alt="스크린샷 2025-12-29 215001" src="https://github.com/user-attachments/assets/e25160fc-f688-48aa-8a59-73ece38cf48b" />

<img width="650" height="574" alt="스크린샷 2025-12-29 214911" src="https://github.com/user-attachments/assets/e91a4ccd-4a58-49d2-b47c-a570e432f51f" />

강의에서는 위와 같은 코드를 작성함, right_is_clear() 라는 함수가 있었나봄;;

그건 둘째치고, 위의 코드에서도 내가 만났던 반복로직에서 계속 반복되는 문제가 발생함

강의에서는 변수를 만들어서 해결하는게 아니라

<img width="450" height="419" alt="스크린샷 2025-12-29 215627" src="https://github.com/user-attachments/assets/a5bee2c5-0e7e-431f-84dc-1e01e0abbb48" />

이렇게 사진과 같이 처음부터 오른쪽 벽을 만들어 준 후에 본 while 로직을 실행함

사진이 안나오는 관계로 아래에 설명

```python
while is_front_clear():
	move()
turn_left()

while .. 실행
```

위 처럼 처음에 while문을 실행하면 앞에 벽이 있는 상태에서 왼쪽으로 돌면 

다음 while문을 실행 시, 오른쪽에 벽이 위치하게

## 7일차
## Hangman 프로젝트

단계별로 나눠서 총 5단계로 행맨 프로젝트를 진행,

완성 사진은 아래와 같다.

![image.png](attachment:fb0df7c3-fe79-497e-8844-4a5cee891c48:image.png)

### 1단계

### TODO-1

word_list에서 무작위로 단어를 선택하여 chosen_word라는 변수에 할당하십시오. 그런 다음 이를 출력하세요.

```jsx
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
import random
chosen_word = random.choice(word_list)
print(chosen_word)
```

### TODO-2

사용자에게 글자를 추측하게 한 뒤 답변을 guess라는 변수에 할당하세요. guess에 저장된 문자열을 소문자로 변환하세요.

```jsx
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("안에 들어갈 글자는 뭘까용?: ").lower()
```

### TODO-3

사용자가 추측한 글자 guess가 chosen_word의 글자 중 하나인지 확인하세요. chosen_word의 각 글자를 반복하여 검사하고, 글자가 일치하면 "Right"를, 그렇지 않으면 "Wrong"을 출력하세요.

```jsx
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
index = 0
for check_word in range(len(chosen_word)):
    if guess == chosen_word[index]:
        print("Right")
    else:
        print("Wrong")
```

이 방법도 가능하지만 파이썬 공식문서에서 알아보니 아래의 코드만 작성해도 알아서 문자열을 index순으로 차례차례 넘겨준다. 따라서 index는 필요가 없었던 것.

```jsx
for char in chosen_word:
    print(char)
```

⇒

```jsx
for char in chosen_word:
    if guess == char:
        print("Right")
    else:
        print("Wrong")
```

### 검사

```jsx
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

```

다음 스텝으로 넘어가면 맞았는지 확인이 가능한데, 변수명을 제외하면 동일하다.

### 2단계

### TODO-1

- 비어 있는 문자열 placeholder를 만드세요.
- chosen_word의 각 글자에 대해 placeholder에 _를 추가하세요.
- 예를 들어 chosen_word가 "apple"이라면, placeholder는 _ _ _ _ _이 되어야 하며, 이는 추측해야 할 각 글자를 *"_”*로 나타냅니다.
- hint를 출력하세요.

```jsx
# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

guess = input("Guess a letter: ").lower()
length = len(chosen_word)
placeholder = ""
for under_cover in range(length):
    placeholder += "_"
print(placeholder)
```

### TODO-2

- 비어 있는 문자열 display를 만드세요.
- chosen_word의 각 글자를 반복문으로 순회하세요.
- 해당 위치의 글자가 guess와 일치하면, 그 글자를 display에서 해당 위치에 표시하세요.
- 예: 사용자가 "p"를 추측했고 선택된 단어가 "apple"이라면, display는 _ p p _ _가 되어야 합니다.
- display를 출력하면, 맞춘 글자가 올바른 위치에 보이는 것을 확인할 수 있습니다.
- 그러나 일치하지 않는 모든 글자는 "_"로 표시됩니다.

```jsx
# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

display = ""

for letter in chosen_word:
    if letter == guess:
        print("Right")
        display += guess
    else:
        print("Wrong")
        display += "_"

print(display)
```

### 3단계

### TODO-1

- while 루프를 사용하여 사용자가 다시 추측할 수 있도록 하세요.
- 루프는 사용자가 chosen_word의 모든 글자를 맞힐 때까지 멈추지 않아야 합니다.
- 그 시점에서 display에는 더 이상 빈칸("_")이 없습니다. 그런 다음 사용자가 이겼음을 알릴 수 있습니다.

### TODO-2

- for 루프를 업데이트하여 이전 추측들이 display 문자열에 추가되도록 하세요.
- 현재는 사용자가 새로 추측할 때 이전 추측이 "_"로 대체되고 있습니다. 이를 for 루프를 업데이트하여 수정해야 합니다.

→ 둘을 동시에 진행할 것이다. 

→ numerate를 사용할거다, for문에서 사용하는 함수로 index와 값을 둘다 사용할 수 있다.

→ 새로운 값을 적용해야 해서 new_display를 while문 안에 지역변수로 생성한다.

```jsx
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.

guess = input("Guess a letter: ").lower()

display = ""

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)

is_win = False
while not is_win:
    guess = input("Guess a letter: ").lower()
    new_display = ""
    for index,letter in enumerate(chosen_word):
        if letter == guess:
            new_display += letter
        else:
            new_display += display[index]
    display = new_display

    if "_" not in display:
        is_win = True
    print(display)

print("축하합니다 이겼어요!")
```

1. 처음 for문으로 display 문자열을 정의 및 is_win을 False로 설정
2. while 반복문을 설정해 성공해야 종료
3. guess를 다시 물어보고, new_display라는 전역변수 생성
4. for문을 enumerate함수를 활용해서 만듦
5. 추측한게 값에 들어왔다면 new_display에 letter 값을 추가하고 아니라면 “_” 추가
6. display에 new_display 대입 → 지역변수는 밖에서 사용할 수 없기 때문에
7. 마지막 if를 통해 not in display → display에 “_” 가 없다면 → is_win을 True로 설정하며 while문 빠져나오기

enumerate가 필요한 이유 → 없으면 반복문이 실행되면서 계속 이전에 맞췄던 글이 사라지게 됨, 

즉, 처음에는 a_ _ _ _ 였고 다음 반복문에서 _b _ _ _ 가 다시 대입되니까 이전의 a가 사라짐,

따라서 enumerate로 index를 추가해줘야됨,

당연히 enumerate를 안써도 그냥 index를 전역변수로 선언해서 추가해줘도 됨

강의에서는 correct_letters = [] 로 리스트를 생성 후, append로 추가해줌

```python
for letter in chosen_word:
    if letter == guess:
        display += letter
        correct_letters.append(guess)
    elif letter in correct_letters:
        display += letter
    else:
        display += "_"
```

이렇게 되면 추측이 맞을 시, display에 letter을 추가 + 리스트에 guess를 추가

다음 조건으로 letter가 correct_letters에 존재할 때(기억), display에 다시 letter을 추가 → 즉, 이전의 정답이 사라지지 않기 위한 기억장치라고 생각하면 된다.

### 4단계

### TODO-1:

- lives라는 변수를 만들어 남은 목숨 수를 추적하세요.
- lives를 6으로 설정하세요.

```python
# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
```

### TODO-2:

- guess가 chosen_word에 포함되지 않은 문자라면, lives를 1 줄이세요.
- lives가 0으로 내려가면 게임이 끝나야 하며, "You lose."라는 메시지를 출력해야 합니다.

### TODO-3:

- 사용자가 현재 남은 lives 수에 해당하는 stages 리스트의 ASCII 아트를 출력하세요.

```python
# TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives+1])
        print(f"***************{lives}/6 LIVES LEFT*****************")
        if lives == 0:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.
```

![image.png](attachment:3369c6c7-59b4-4a75-bc3f-c5282d17ddcc:image.png)

demo 버전과 동일하게 만들어 놓음

### 5단계

### TODO-1:

- hangman_words.py에서 word_list를 사용하도록 단어 목록을 업데이트하세요.

```python
import hangman_words
```

### TODO-2:

- hangman_art.py 파일에서 stages를 사용하도록 코드를 업데이트하세요.

```python
import hangman_art

# TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])
```

### TODO-3:

- hangman_art.py에서 logo를 가져와 게임 시작 시 출력하세요.

```python
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art
print(hangman_art.logo)
```

### TODO-4:

- 사용자가 이미 추측한 문자를 입력한 경우, 해당 문자를 출력하고 이미 추측했음을 알리세요.
- 이 상황에서는 목숨을 차감하지 않아야 합니다.
- 예: 이미 a를 추측하셨습니다.

```python
for letter in chosen_word:
    if letter == guess:
        display += letter
        correct_letters.append(guess)
    elif letter in correct_letters:
        display += letter
        print(f"Already guessed : {letter}")
    else:
        display += "_"
```

### TODO-5:

- 만약 그 문자가 chosen_word에 포함되지 않은 경우, 해당 문자를 출력하고 단어에 없음을 알리세요.
- 예: d를 추측했지만, 단어에 없습니다. 목숨을 잃습니다.

```python
    if guess not in chosen_word:
        print(f"{guess} : not in the word, lost life")
        lives -= 1
```

### TODO-6:

- 아래 코드를 업데이트하여 사용자에게 남은 목숨 수를 알려주세요. print("****************************<???>/6 LIVES LEFT****************************")

```python
# TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
```

### TODO-7:

- 출력 문장을 업데이트하여 사용자가 맞추려던 정답 단어를 알려주세요.
- 예: 정답은 <Correct Word>였습니다! 패배하셨습니다.

```python
# TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"GAME OVER : 정답은 {chosen_word}였습니다")
```

⇒ 

```python
import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
import hangman_words
import hangman_art

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
            print(f"Already guessed : {letter}")
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        print(f"{guess} : not in the word, lost life")
        lives -= 1

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"GAME OVER : 정답은 {chosen_word}였습니다")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])

```

## 8일차
## 입력이 있는 함수

이전에 우리는 함수가 코드를 이름이 지정된 블록으로 묶어 나중에 반복적으로 사용할 수 있도록 해준다는 것을 보았습니다.

### PAUSE 1 - 검토

- greet()라는 이름의 함수를 생성하세요.
- 함수 내부에 3개의 print 문을 작성하세요.
- greet() 함수를 호출하고 코드를 실행하세요.

### 입력

새로운 함수를 만들 때 (정의할 때) 괄호 안에 변수 이름을 추가하면, 함수를 호출할 때 해당 입력값을 받을 수 있습니다.

즉, 다른 입력값을 전달함으로써 함수의 동작을 호출할 때마다 다르게 변경할 수 있다는 뜻입니다.

```python
def myfunction(parameter):
    print(f"안녕! {parameter}")

myfunction("영준")
```

### 입력은 변수

입력을 받는 함수를 생성할 때는 전달된 데이터를 받을 변수 이름을 정의합니다.

입력 변수 이름, 예를 들어 이 코드에서 def greet(name):의 name은 매개변수(parameter)라고 부릅니다.

입력 변수의 값, 예를 들어 이전 greet 함수를 호출할 때의 greet("Angela")에서의 값 Angela는 인자(argument)라고 부릅니다.

## 위치 인자 VS 키워드 인자

### 여러 개의 입력값

함수에 여러 개의 입력값을 사용할 수 있습니다. 필요한 것은 각 입력값을 쉼표 ,로 구분하는 것뿐입니다.

함수를 수정하여 예상 값을 출력하도록 만드세요.

```python
defgreet_with(name,location)
    Hello name
    Whatisit likeinlocation
```

⇒

```python
# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"Hello {name}\nWhat is it like in {location}")

greet_with("영준", "광주")
```

### 위치 기반 인수

기본적으로 Python에서 함수를 생성하면 함수 정의에서 인수들의 순서를 유지합니다.

예: 아래의 함수에서 첫 번째로 전달받은 인수는 항상 두 번째 인수보다 먼저 출력됩니다. a = 2, b = 1

```python
defmy_function(a,b)
  print(a)
  print(b)

my_function(2,1)
#출력 결과는:
# 2
# 1

```

### 키워드 인수

함수를 호출할 때 인수를 제공할 때 키워드를 사용할 수 있으며, 이를 통해 어떤 값이 어떤 입력 매개변수에 할당되는지에 대한 혼동을 줄일 수 있습니다.

greet_with() 함수를 키워드 인수를 사용하여 호출하세요.

```python
def greet_with(name, location):
    print(f"Hello {name}\nWhat is it like in {location}")

greet_with(location="광주", name="영준")
```

→ 

Hello 영준
What is it like in 광주

## Caesar Cipher 1

### TODO-1:

encrypt()라는 이름의 함수를 생성하세요. 이 함수는 original_text와 shift_amount라는 2개의 입력값을 받습니다.

### TODO-2:

encrypt 함수 내부에서, original_text의 각 문자를 shift_amount만큼 알파벳에서 앞으로 이동시키고, 암호화된 텍스트를 출력하세요.

Python의 내장 함수 index()를 사용하여 리스트에서 항목의 위치를 찾을 수 있습니다. 예:

```
fruits= ["Apple","Pear","Orange"]
fruits.index("Pear")#1

```

예를 들어 다음과 같은 값이 주어졌다면:

```
plain_text="hello"
shift_amount=1

```

최종 암호화된 출력값은 아래와 같이 나와야 합니다:

여기 암호화된 결과가 있습니다: ifmmp

'hello'의 각 문자가 1만큼 위로 이동했습니다.

```python
# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
display = ""
def encrypt(original_text, shift_amount):
    global display
    for char in original_text:
            index = alphabet.index(char) + shift_amount
            display = display + alphabet[index]
    print(display)
```

### TODO-3:

문자 'z'를 9만큼 앞으로 이동시키려고 하면 어떻게 될까요? 코드를 수정할 수 있나요?

```python
display = ""
list_length = len(alphabet)
def encrypt(original_text, shift_amount):
    global display
    for char in original_text:
        index = alphabet.index(char) + shift_amount
        if list_length - 1 < index:
            extends = index - list_length
            display = display + alphabet[extends]
        else:
            display = display + alphabet[index]
    print(display)
```

### TODO-4:

encrypt() 함수를 호출하고 사용자 입력값을 전달하세요. 코드를 테스트하고 메시지를 암호화할 수 있어야 합니다.

```python
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift)
```

⇒

Type your message:
abcdefgzzz
Type the shift number:
3
defghijccc

```python
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")
```

강의에서는 위의 코드를 활용했다. %= 을 활용해서 나누고 남은 수, 즉 리스트 길이가 7, 암호화된 index 값이 9라고 하면 %=을 통해 shifted_position=2가 된다.

따라서 결국 내가 복잡하게 짠 코드를 한줄로 간단하게 활용이 가능하다.

또한 전역으로 변수를 정의하지 않아도 함수 내에서 만들면 되는 것을 알았다, 어차피 밖에서 안쓰니까

## Caesar Cipher 2

### TODO-1:

decrypt()라는 이름의 함수를 생성하고, 이 함수는 original_text와 shift_amount를 두 가지 입력으로 받습니다.

### TODO-2:

decrypt() 함수 내에서 original_text의 각 문자를 알파벳에서 *뒤로* shift_amount만큼 이동시키고, 복호화된 텍스트를 출력하세요.

```python
def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        cipher_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {cipher_text}")

decrypt(original_text=text, shift_amount=shift)
```

여기서는 어차피 a = 0이고 뒤로가도 -1이므로 z가 나옴, 따라서 코드 수정은 필요 없다 

### TODO-3:

- encrypt()와 decrypt() 함수를 결합하여 caesar()라는 단일 함수로 만드세요.
- 사용자가 선택한 direction 변수 값을 사용해 어떤 기능을 실행할지 결정하세요.
- encrypt/decrypt 대신 caesar 함수를 호출하고 세 가지 변수인 direction/text/shift를 전달하세요.

```python
def caesar(direct, original_text, shift_amount):
    if direct == "encode":
        encrypt(original_text=original_text, shift_amount=shift)
    elif direct == "decode":
        decrypt(original_text=original_text, shift_amount=shift)
    else:
        print("Wrong Type, Restart Please")

caesar(direct=direction, original_text=text, shift_amount=shift)
```

⇒

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
aaa
Type the shift number:
1

Here is the encoded result: bbb

⇒

Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
aaaa
Type the shift number:
1
Here is the decoded result: zzzz

⇒ 

Type 'encode' to encrypt, type 'decode' to decrypt:
dddd
Type your message:
1
Type the shift number:
1
Wrong Type, Restart Please

합치라는게 저게 아니였음, 

```python
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")
```

하나의 함수로 그냥 만들라는거였음, encode일 때는 그대로, decode일 땐 -1을 곱해줌

그래야 빼지니까, 어차피 %=을 해도 decode는 -를 더하므로 그냥 shifted_position에는 영향이 없음

## Caesar Cipher 3

### TODO-1:

프로그램이 실행될 때, art.py에서 로고를 가져와 출력하세요.

```python
# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)
```

### TODO-2:

사용자가 List alphabet에 없는 숫자/기호/공백을 입력하면 어떻게 될까요?

코드를 수정하여 텍스트가 인코딩/디코딩될 때 숫자/기호/공백을 유지할 수 있도록 만들어보세요.

예:

```python
original_text="meet me at 3!"
cipher_text="XXXX XX XX 3!"

```

```python
# TODO-2: What happens if the user enters a number/symbol/space?

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")
```

### TODO-3:

암호 프로그램을 다시 시작할 방법을 생각해볼 수 있나요?

예:

다시 실행하려면 'yes'를 입력하세요. 그렇지 않으면 'no'를 입력하세요.

사용자가 'yes'를 입력하면 방향/텍스트/시프트를 다시 묻고 caesar() 함수를 다시 호출하세요.

```python
# TODO-3: Can you figure out a way to restart the cipher program?
game_loop = True
while game_loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    is_loop = input("restart? yes :\n")
    if is_loop != "yes":
        game_loop = False
        print("종료합니다.")
```

⇒

,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,

a8"     "" ""     `Y8 a8P_____88 I8[    "" ""`     Y8 88P'   "Y8

8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88           "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88`            "Ybbd8"' `"8bbdP"Y8`  "Ybbd8"' `"YbbdP"'` "8bbdP"Y8 88

88             88

""             88

88

,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,

a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8

8b         88 88       d8 88       88 8PP" 88

"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88

`"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88

88

88

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
aaaa
Type the shift number:
1
Here is the encoded result: bbbb
restart? : yesyes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
aaaa
Type the shift number:
1
Here is the decoded result: zzzz
restart? : yesno

완성본 ⇒

```python
# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        if encode_or_decode == "decode":
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# TODO-3: Can you figure out a way to restart the cipher program?
game_loop = True
while game_loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    is_loop = input("restart? yes :\n")
    if is_loop != "yes":
        game_loop = False
        print("종료합니다.")
```

## 9일차
## 딕셔너리

파이썬에서 딕셔너리는 실제 상황의 사전과 유사하게 작동한다.

이름 : 정의… 이런식으로 키와 값을 연결하여 두 데이터를 연결

```python
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
```

다음은 딕셔너리를 생성하고, 값을 집어넣고 수정하는 코드이다.

{}를 활용해서 빈 딕셔너리를 생성

minsu : friends 라는 값을 집어 넣는다

minsu : not friends 라는 값으로 재할당

```python
my_empty_dictionary = {}

my_empty_dictionary["minsu"] = "friends"
print(my_empty_dictionary["minsu"])

my_empty_dictionary["minsu"] = "not friends"
print(my_empty_dictionary["minsu"])
```

다음은 반복문을 활용해 사전에 있는 키와 값을 출력하는 방법이다

```python
fruit = {"apple": "red", "banana": "yello", "oi": "green"}

for key in fruit:
    print(f"{key} : {fruit[key]}") 
```

반복문에 key값으로 들어가는건 키(사과, 바나나 등) 이고 값을 꺼내기 위해서는 코드처럼 fruit[”apple”]를 활용해아 한다.

## 중첩 리스트와 딕셔너리

딕셔너리는 키 → 값 의 형태로 키에 할당된 값을 가지는 구조인데, 여기서 값에 리스트가 들어갈 수 있다.

```python
list1 = [1, 2, 3, 4]
my_dictionary = {
    "key" : list1,
    "key2" : 5
}
print(my_dictionary)
```

⇒ {'key': [1, 2, 3, 4], 'key2': 5}

### 중간문제

중첩된 리스트 travel_log에서 "Lille"을 출력하는 방법을 찾아보세요.

```python
travel_log= {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Stuttgart","Berlin"],
}
```

⇒ `print(travel_log["France"][1])`

앞의 딕셔너리에서 도출된 값이 list이므로 [index로 값을 꺼내줄 수 있다]

```python
nested_list= ["A","B", ["C","D"]]
```

### 중간문제 2

깊이 중첩된 리스트 항목을 얻는 방법을 기억하시나요? 리스트 nested_list에서 "D"를 출력해보세요.
`print(nested_list[2][1])`

### 딕셔너리 안에 딕셔너리 중첩하기

딕셔너리 안에 딕셔너리를 중첩할 수도 있습니다:

```python
my_dictionary= {
    key1:Value,
    key2: {Key:Value,Key:Value},
}
```

### 중간문제 3

다음 리스트에서 "Stuttgart"를 출력하는 방법을 찾아보세요:

```python
travel_log= {
  "France": {
    "cities_visited": ["Paris","Lille","Dijon"],
    "total_visits":12
   },
  "Germany": {
    "cities_visited": ["Berlin","Hamburg","Stuttgart"],
    "total_visits":5
   },
}
```

⇒ `print(travel_log["Germany"]["cities_visited"][2])`

딕셔너리 ⇒ 딕셔너리 ⇒ 리스트

## 블라인드 경매 프로젝트

![image.png](attachment:fa704f8a-17a8-4859-95b7-0ff84246b983:image.png)

블라인드 경매 프로그램으로 player1이 입력하면 콘솔에 전에 입력된 내용이 사라지고 다음 player2의 입력 창이 나옴, 마지막으로 player중에서 가장 높은 금액을 선정한 사람이 경매에 당첨됨

### 기능

- 각 사람은 자신의 이름과 경매 금액을 입력합니다.
- 프로그램은 다른 사람이 경매에 참여할 필요가 있는지 묻습니다. 만약 그렇다면, 컴퓨터는 출력을 지우고(여러 개의 빈 줄을 출력) 다시 이름과 경매 금액을 묻는 루프로 돌아갑니다.
- 각 사람의 이름과 경매 금액은 딕셔너리에 저장됩니다.
- 모든 참가자가 경매를 완료하면, 프로그램은 최고 입찰자를 찾아서 출력합니다.

```python
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)

bgp = {}
type_no = True

name_list = []
bid_list = []

while type_no:
    name = input("What is your name?:\t")
    bid = int(input("What is your bid?:\t$"))
    types = input("Are there any other bidders? Type 'yes' or 'no'.")

    name_list.append(name)
    bid_list.append(bid)

    if types != 'yes':
        type_no = False
    else:
        print("\n" * 20)

bgp = {
    "name" : name_list,
    "bid" : bid_list
}

print(bgp) ## name과 bid를 가지는 리스트 형태의 dictionary 생성
maxi = 0
name = ''

for index,big in enumerate(bgp["bid"]):
    if big > maxi:
        maxi = big
        name = bgp["name"][index]
    bgp["winner"] = [name, maxi]

print(f"The winner is {bgp["winner"][0]} with a bid of ${bgp['winner'][1]}")
```

기능은 위의 코드로 구현했다, 딕셔너리 구조에 플레이어를 리스트 형태로 이름과 가격을 넣었다, 

반복문이 끝나면 가장 큰 수와 이름을 빈 변수로 생성 후 for문을 통해 maxi와 name에 값을 집어넣고 bgp에 넣은 후 print해주었다.

강의에서는 어떻게 했는지 살펴보자

```python
 bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
```

우선 while구문이다.

나와 같이 dictionary, True값을 지정해주었고 반복문을 실행했다. 

dictionary 자체를 name : price로 만들었고, no를 입력하면 dictionary를 argument로 전송하며 find_highest_bidder 함수를 실행하였다.

ex) jun : 12, go : 15, min : 20, ho : 8 이런식으로 dictionary에 저장됨

```python
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
```

이 함수는 가장 큰 수를 낸 winner를 찾 함수이다.

→ highest_bid = 0, winner = “” 으로 결과값들을 변수로 선언

→ for문을 통해 bids를 하나씩 꺼냄(1. jun, 2. min)

→ bid_amount에 bidding_record[bidder] → bids[key] → bid 대입

→ big_amount가 highest_bid보다 크다면 highest_bid를 계속 큰 값으로 갱신, winner값도 그에 맞게 갱신

나랑 구조가 같음, 다만 나는 name = list, bid = list 형태로 진행했고, 강사님은 key : value로 진행함,

key에 이름, value에 가격을 넣어서 해결


## 10일차
## 출력이 있는 함수

지금까지는 실행 본문만 있는 함수, 함수 본문의 실행에 변화를 줄 수 있는 입력을 가진 함수를 공부하였다.

오늘은 함수의 마지막 형태로 출력을 가질 수 있는 함수를 살펴본다.

### 중간문제1

format_name() 이라는 함수를 생성하세요. 이 함수는 두 개의 입력값인 f_name과 l_name을 받습니다.

```python
def format_name(f_name, l_name):
    print("중간1")
```

### 중간문제2

title() 함수를 사용하여 f_name과 l_name 매개변수를 Title Case로 수정하세요.

```python
def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())

format_name("GoYOUng", "JuN")
```

### 문법

다음과 같은 방식으로 실행 본문, 입력, 출력을 가진 함수를 생성할 수 있습니다:

```python
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("GOyOUng", "JuN"))
```

### Print와 Output

Return vs. 출력: return 문은 함수로부터 값을 반환하여 나중에 사용할 수 있게 해주는 반면, print는 프로그래머가 확인할 수 있도록 값만 콘솔에 출력합니다.

## 다중 반환 값

함수는 return 키워드에서 종료됩니다. return 문 아래에 코드를 작성하면 해당 코드는 실행되지 않습니다.

하지만, 하나의 함수에 여러 개의 return 문을 가질 수 있습니다. 그렇다면 이것이 어떻게 작동할까요?

### 조건부 반환

조건부 흐름 제어(코드가 특정 조건 검사에 따라 다르게 동작하여 다른 실행 경로를 따르는 경우)가 있을 때, 여러 가지 종료점(return)이 생길 수 있습니다.

예:

```python
defcanBuyAlcohol(age):
    ifage>=18:
        return True
    else:
        return False

```

### 빈 반환

return 뒤에 아무 것도 작성하지 않고 반환할 수도 있습니다. 이것은 단순히 함수에게 종료하라고 지시합니다.

예:

```python
defcanBuyAlcohol(age):
    # age 입력의 데이터 타입이 int가 아니면 종료합니다.
    iftype(age) !=int:
        return

    ifage>=18:
        return True
    else:
        return False
```

## Dcostrings

“””…”””

코드의 문서를 작성하기 위해 여러 줄 주석을 작성할 때 docstring을 사용할 수 있습니다.

### 문법

텍스트를 세 개의 큰따옴표로 감싸서 작성하면 됩니다.

예:

```python
"""
나의
여러 줄
주석
"""
```

### 함수 문서화하기

docstring의 유용한 기능 중 하나는 함수 정의 바로 아래에 작성할 수 있으며, 그렇게 작성된 텍스트는 함수 호출 위에 마우스를 올릴 때 표시됩니다. 이는 자신이 만든 함수가 무엇을 하는지 기억하기에 좋은 방법입니다.

예:

```python
defmy_function(num):
    """숫자를 제곱합니다."""
    return num*num
```

## 계산기 프로젝트

![image.png](attachment:a2accf66-cf38-46ec-a75d-74b9d2d0f5e9:image.png)

### 함수를 변수 값으로 저장하기

함수를 참조하여 변수 값으로 저장할 수 있습니다.

예:

```python
def add(n1,n2):
    returnn1+n2

my_favourite_calculation=add
my_favourite_calculation(3,5)# 8을 반환합니다

```

시작 파일에서, 계산기가 수행할 수 있는 각 수학 계산을 참조하는 사전을 확인할 수 있습니다. 이를 시도해보고 덧셈, 뺄셈, 곱셈, 나눗셈을 수행할 수 있는지 확인하세요.

### PAUSE 1

TODO: 나머지 3개의 함수 작성하기 - subtract(뺄셈), multiply(곱셈), divide(나눗셈).

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
```

### PAUSE 2

TODO: 이 4개의 함수를 사전에 값으로 추가하세요. 키 = "+", "-", "*", "/"

```python
calculate = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

```

### PAUSE 3

TODO: 사전의 연산을 사용하여 계산을 수행하세요. 사전을 사용하여 4 * 8을 곱하세요.

```python
calculate = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

result = calculate["*"](4,2)
print(result)
```

### 기능

- 프로그램이 사용자가 첫 번째 숫자를 입력하도록 요청합니다.
- 프로그램이 사용자가 수학 연산자를 입력하도록 요청합니다 ("+", "-", "*", "/" 중 선택).
- 프로그램이 사용자가 두 번째 숫자를 입력하도록 요청합니다.
- 프로그램이 선택된 수학 연산자를 기준으로 결과를 계산합니다.
- 프로그램이 사용자가 이전 결과로 계속 작업할지 여부를 묻습니다.
- 사용자가 "예"를 선택하면, 프로그램은 이전 결과를 첫 번째 숫자로 사용하여 계산 과정을 반복합니다.
- 사용자가 "아니오"를 선택하면, 프로그램이 사용자에게 첫 번째 숫자를 다시 입력하도록 요청하고 이전 계산의 모든 메모리를 초기화합니다.
- art.py에서 로고를 추가하세요.

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculate = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

import art
print(art.logo)

is_continue = "Continue"
while True:
    if is_continue == "Continue":
        num1 = int(input("Enter first number: "))

    operation = input("Enter operation\n+\n-\n*\n/: ")
    num2 = int(input("Enter second number: "))

    result = calculate[operation](num1, num2)
    print(result)

    continue_key = input("Press any key to continue...y/n : ")
    if continue_key == "y":
        num1 = result
        is_continue = "Pass"
    else:
        is_continue = "Continue"
```

오늘은 출력(return)이 있는 함수를 만들고, 그걸 활용해서 계산기를 만들어보는 시간을 가졌다.

또한 Dcostrings를 활용해 다른 개발자가 내 코드를 볼 때, 조금 더 손쉽게 내 코드를 살펴볼 수 있게 가독성 있는 코드를 짤 수 있다는 것도 알았다.

## 11일차
## 블랙잭 프로젝트

### 난이도를 선택하세요

- **보통** 😎: 아래의 모든 힌트를 사용하여 프로젝트를 완성하세요.
- **어려움** 🤔: 힌트 1, 2, 3만 사용하여 프로젝트를 완성하세요.
- **매우 어려움** 😭: 힌트 1, 2만 사용하여 프로젝트를 완성하세요.
- **전문가** 🤯: 힌트 1만 사용하여 프로젝트를 완성하세요.

### 블랙잭 게임 하우스 규칙

- 카드 덱의 크기는 무제한입니다.
- 조커 카드는 사용하지 않습니다.
- Jack/Queen/King은 모두 10으로 계산됩니다.
- Ace는 11 또는 1로 계산될 수 있습니다.
- 다음 리스트를 카드 덱으로 사용하세요:

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

- 리스트의 카드들은 동일한 확률로 선택됩니다.
- 뽑힌 카드는 덱에서 제거되지 않습니다.
- 컴퓨터가 딜러 역할을 합니다.

1. 딜러(컴퓨터)는 번갈아가며 플레이어와 자신에게 카드를 나눠준다.
2. 플레이어는 받은 카드를 확인하고 카드를 더 받던지 멈출 수 있다.
3. 21이 넘어가면 자동으로 패배이며, 딜러의 카드 합 보다, 플레이어의 카드 합이 더 커야 이기는 게임이다.

힌트는 안봄, 첫번째 코드 풀이로 아래와 같이 풀었음

```python
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

first_second = input("먼저 받으시겠습니까?(y/n) : ")
for card in range(2):
    if first_second == "y":
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    else:
        computer_cards.append(random.choice(cards))
        player_cards.append(random.choice(cards))

is_continue = True
sum_card_computer = 0
for c_card in computer_cards:
    sum_card_computer += c_card
    if 11 in computer_cards and sum_card_computer > 21:
        sum_card_computer -= 10

while is_continue:
    sum_card_player = 0
    now_status = ""
    for p_card in player_cards:
        sum_card_player += p_card
        if sum_card_player > 21:
            if 11 in player_cards:
                sum_card_player -= 10
            else:
                print(f"BOOM!! {sum_card_player}, 21이 넘었어요, 패배!")
                now_status = 'boom'
    if now_status == 'boom':
        break

    print(f"당신의 카드 합은 {sum_card_player} 입니다!")
    more = input("카드를 더 받으시겠습니까?(y/n) : ")
    if more != "y":
        is_continue = False
        if sum_card_player > sum_card_computer:
            print(f"딜러 카드 합->{sum_card_computer}, 승리!")
        elif sum_card_player < sum_card_computer:
            print(f"딜러 카드 합->{sum_card_computer}, 패배..")
        else:
            print("같은 합 입니다. 비겼습니다")
    else:
        player_cards.append(random.choice(cards))
```

![image.png](attachment:959e8386-a38d-4696-845c-4f281fb6a534:image.png)

위의 결과 외에도, 승리, 무승부, 패배 등의 경우도 모두 검증함

여기서 추가하고 싶은 사항은 원래 딜러의 패가 17 미만이면 딜러도 카드를 더 받아야됨

그 로직을 추가

1. 딜러도 초반에 카드를 2장 받음, 합이 21이 넘는데 11이 안에 있다면 -10
2. 근데 이게 아니다.. 11은 1 또는 11

```python
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
```

이렇게 복잡한 코드가 완성됐다.

코드 설명

1. import문을 선언 후 처음 로고를 print
2. 프로젝트에 사용될 변수를 선언
    1. player_cards = [] ⇒ 플레이어가 뽑은 카드를 모아둔 리스트
    2. computer_cards = [] ⇒ 컴퓨터가 뽑은 카드를 모아둔 리스트
    3. is_continue_player = True ⇒ 플레이어가 카드를 더 뽑을지 while문의 조건
    4. is_continue_computer = True ⇒ 플레이어가 카드를 다 뽑고 이제 딜러가 카드를 뽑는 while문의 조건
    5. sum_card_computer = 0 ⇒ 컴퓨터가 뽑은 카드의 합

1. 코드 1
    
    ```python
    first_second = input("먼저 받으시겠습니까?(y/n) : ")
    for card in range(2):
        if first_second == "y":
            player_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
        else:
            computer_cards.append(random.choice(cards))
            player_cards.append(random.choice(cards))
    ```
    
    처음 카드를 2장씩 나눠가지는 코드, first_second로 먼저 받을지 나중에 받을지 선택 후 2장을 받음
    
2. 코드 2
    
    ```python
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
    ```
    
    플레이어가 카드를 더이상 받지 않음을 선택했을 때, 이제 딜러가 카드를 뽑아야 되므로 실행 될 반복문을 함수 형태로 만들어서, 코드를 간결화하고자 함
    
    안에서의 로직은 컴퓨터 카드 리스트 안에 11이 있고, 합이 21이 넘는다면? (11 또는 1) → 1로 변경 후 
    
    sums에 더해줌
    
    만약 합이 17보다 작다면 카드를 계속 뽑고, 아니라면 sums를 리턴
    
3. 코드 3
    
    ```python
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
    ```
    
    코드 2와 매우 동일한 형태로 위는 작성되었고, 위의 코드가 플레이어가 카드를 받을지 말지 선택하는 로직, 플레이어가 카드를 다 뽑았다면 위에서 말한대로 computer_last()를 실행하며, sum_card_computer를 추출하였다면 player의 sum과 비교해 print

	## 클린코드 적용

	1. 카드를 뽑는 함수를 deal_card()
	2. 카드의 합을 계산하는데, 21인지, 11과 1을 비교해서 넣는 로직을 담는 함수를 calculate_cards()
	3. 카드의 합에 따라 결과를 리턴해주는 함수를 compared()
	4. 실제 로직을 함수로 만들어 play_game()
	
	이렇게 4개의 함수를 만들고, 함수만 실행하여 게임을 돌아가게 만들어보았다.
	
	```python
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
	
	```
	
	확실히 함수로 나눠놓으니까, 이게 어떤 함수인지 파악이 쉽고, 코드가 훨씬 간결해졌다.
   
## 12 일차
## 네임스페이스와 범위

이건 변수를 선언한 위치와 그에 따른 범위를 알려주는 내용

### 지역 범위

함수 안에서 선언된 변수(또는 함수)는 지역 범위(함수 범위라고도 함)를 가집니다. 이러한 변수는 동일한 코드 블록 내의 다른 코드에서만 볼 수 있습니다.

예:

```python
def my_function():
    my_local_var=2

# 이것은 NameError를 발생시킵니다.
print(my_local_var)
```

### 전역 범위

코드 파일의 최상위 수준(들여쓰기 없음)에 선언된 변수 또는 함수는 전역 범위를 가집니다. 이는 코드 파일 어디에서나 접근할 수 있습니다.

예:

```python
my_global_var=3

def my_function():
    # 이는 아무 문제 없이 작동합니다.
    print(my_global_var)
```

아래의 코드를 작성하여 설명

```python
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
```

본래 변수는 마지막에 선언된 값이 출력되기 마련인데, 위의 코드에서는 전역 , 지역 범위가 나눠져서 선언됨

첫 번째 enemies=1 → 전역 범위

두 번째 enemies=2 → 지역 범위

따라서 함수 내에서 사용된 enemies는 2가 출력이 되며

밖에서 출력 된 enemies는 함수 내의 enemies를 사용할 수 없으므로 1이 출력됨

⇒ 결과 출력

enemies inside function: 2
enemies outside function: 1

## 블록 범위

파이썬은 블록 범위를 가지지 않는다는 점에서 다른 프로그래밍 언어와 조금 다르다.

이 말은 for 루프, if 문, while 루프 등과 같은 다른 코드 블록 내부에서 생성된 변수는 로컬 범위를 갖지 않는다는 말이다.

```python
my_global_var = 1

def my_function():
    my_local_var = 2
    
for _ in range(1):
    my_block_var = 3
    
print("전역 변수를 출력 : ", my_global_var)
print("지역 변수는 출력이 안돼요")
print("블록 범위 안의 변수는? : ", my_block_var)
```

1 → 전역 / 2 → 지역(함수) / 3 → 블록(for문)

3가지의 각각 다른 위치의 변수를 선언 후 print문을 출력(지역변수는 오류가 발생하므로 뺌)

⇒ 결과

전역 변수를 출력 :  1
지역 변수는 출력이 안돼요
블록 범위 안의 변수는? :  3

결과와 같이 블록 범위(for, if, while) 안에 있는 my_block_var이 출력되는 것을 볼 수 있다.

## 글로벌 변수

```python
a=1
def my_function():
    a+=1
    print(a)
```

위의 함수는 오류가 발생한다, 왜일까?

언뜻보면 문제없는 코드 같지만 a += 1 → a = a+1, 즉 a를 지역변수로 새로 만들어버리는거, 

위의 a =1인 전역 변수는 참조하지 않고 새로 지역변수를 만들어 a = a+1을 실행하는데 a를 함수 내부에서   선언한 적이 없음

즉, 함수 안에서 한번이라도 대입을 하면 지역변수로 간주됨

```python
a = 1
def my_function():
    global a
    a += 1
    print(a)
```

위의 코드로 해결 할 수 있다. 

global a 의 뜻은 전역변수 a를 사용/수정하겠다 라는 의미

## 글로벌 상수

코드 파일에 전역 상수를 정의하여 쉽게 접근할 수 있다. 전역 상수는 값을 한 번 설정하면 수정할 필요 없이 사용할 수 있도록 설계되었다.

### 명명 규칙

전역 상수는 일반적으로 모든 문자를 대문자로 선언하며, 단어 사이에는 언더스코어 사용

예시:

```python
PI=3.14159
GOOGLE_URL="https://www.google.com"
```

글로벌 변수나 상수나 똑같은거 아닌가?

→ 문법적으로 동일함, 다만 사용용도와 개념이 다름

→ 파이썬에서는 const, final 같은 상수의 개념이 없음, 따라서 PI같은 값도 수정이 됨

→ 그럼 왜 글로벌 상수가 존재하는가, 그냥 저런 변수명이 나오면 수정하지 않고 상수처럼 사용할거야

| **구분** | **전역 변수** | **전역 상수(관례)** |
| --- | --- | --- |
| 문법적 차이 | 없음 (둘 다 그냥 변수)  | 없음 (동일)  |
| 이름 규칙 | 소문자 또는 카멜/스네이크  | 대문자 + 언더스코어(ALL_CAPS)  |
| 값 변경 | 자유롭게 변경해도 됨  | “변경하지 말자”는 약속일 뿐, 변경 가능 |

## 숫자 맞추기 프로젝트

숫자 맞추기 게임을 만들어 보자

![image.png](attachment:896f9ec9-2462-479d-abe8-0ec6627fa5b7:image.png)

1. print(logo)
2. input(”~~~”) → game start, easy는 life가 10, hard는 life가 5
3. 목숨이 남아있다면 user가 숫자를 입력하고 Too low, Too high를 출력

이 간단한 프로젝트를 오늘 배운 변수의 범위, 글로벌 상수, 변수 등을 활용해서 코드를 작성해보자

우선 게임이 시작되면 1~100 사이의 숫자를 글로벌 상수로 설정

User가 뽑는 수는 global 변수로 설정해 값이 바뀌게끔 설정함

```python
import art
import random

# 정답을 전역 상수로 설정
ANSWER = random.randint(0,100)
life = 0

def guess():
    global life
    game_over = False
    if input("choose a difficulty. Type 'easy' or 'hard' : ") == 'easy':
        life = 10
    else:
        life = 5

    while not game_over:
        if life < 1:
            game_over = True
            print("You've run out of guess. Refresh the page to run again")
        else:
            print(f"You have {life} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess :"))
            if guess_number < ANSWER:
                life -= 1
                if life > 0:
                    print("Too low\nGuess again")

            elif guess_number > ANSWER:
                life -= 1
                if life > 0:
                    print("Too high\nGuess again")

            else:
                game_over = True
                print(f"You got it! The answer was {ANSWER}")

print(art.logo)
guess()
```

굳이 User가 뽑은 수를 글로벌 변수로 설정하지 않아도 될 것 같아서 안했고,

간단하게 해결 가능한 프로젝트였음	

## 13일차
## 문제를 설명하세요

문제를 해결하는 첫 번째 단계는 문제를 설명할 수 있는 능력입니다.

### PAUSE 1

task.py에 있는 코드를 보고 다음 질문에 답하세요:

```java
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")

my_function()
```

1. for 루프는 무엇을 하고 있나요?
    
    → i를 1부터 19까지 반복하며, if문에서 i가 20일 때, print문을 통해 출력
    
2. 함수가 "You got it"을 출력하는 시점은 언제인가요?
    
    → 없어요
    
3. i 값에 대한 당신의 가정은 무엇인가요?
    
    → 안나와여
    

### PAUSE 2

코드가 print 문을 실행하도록 수정하세요.

```java
def my_function():
    for i in range(1, 20):
        if i == 19:
            print("You got it")

my_function()
```

## 버그 재현 하기

어떤 버그는 특정 조건에서만 발생하기 때문에 찾기 어렵습니다. 이러한 버그를 디버깅하려면, 버그를 신뢰할 수 있게 재현하고 문제를 진단하여 어떤 조건이 버그를 유발하는지 파악해야 합니다.

```java
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

```

### PAUSE 1

코드를 변경하여 간헐적으로 발생하는 오류가 항상 발생하도록 만드세요.

→ index가 5까지인데 1~6을 출력함

```java
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[6])

```

### PAUSE 2

코드를 수정하여 버그를 제거하세요.

```java
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0,5)
print(dice_images[dice_num])
```

## 컴퓨터를 실행해보기

컴퓨터처럼 코드 실행하기는 디버깅에 중요한 기술입니다. 컴퓨터처럼 코드 한 줄 한 줄을 따라가면서 무엇이 잘못되었는지 파악하는 데 도움을 줄 수 있어야 합니다.

### PAUSE 1

컴퓨터처럼 코드 한 줄 한 줄을 따라가서 1994가 예상대로 작동하지 않는 이유를 찾아보세요. 그런 다음 코드를 수정하세요.

```java
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

```

→ 1994년도는 어디에도 해당되지 않음, 오류는 아니지만 원하는 출력이 나오지 않음

```java
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")

```

## 오류 수정하기

편집기에서 코드를 실행하기 전에 표시되는 오류(빨간색 밑줄)를 수정하십시오. 경고(노란색)는 선택적으로 수정할 수 있으며, 때로는 문제를 일으킬 수도 있지만, 다른 경우에는 괜찮고 편집기가 여러분의 의도를 이해하지 못하는 경우도 있습니다.

### 예외 처리하기

Python에서는 try/except 블록을 사용하여 발생할 수 있는 예외를 처리할 수 있습니다. 예를 들어 사용자의 실수가 있을 가능성이 있다고 상상해 보십시오. 이를 예측함으로써 코드가 충돌하지 않도록 방지할 수 있습니다. 위험한 코드를 try 블록 안에 넣고 except 블록을 사용하여 잠재적인 오류를 잡습니다. 그런 다음 오류가 발생했을 때 실행되어야 할 동작을 정의함으로써 단순히 충돌하거나 코드 실행이 멈추는 것을 방지할 수 있습니다.

예:

```python
try:
    print(6>"five")
exceptTypeError:
    print("정수와 문자열을 비교할 수 없습니다")

```

### 일시 정지 1

버그를 수정하여 출력 영역에 나이의 올바른 값이 표시되도록 하십시오.

```python
age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")
```

→ 들여쓰기가 안되어있음. 

```python
age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.")
```

## Print() 사용하기

print()은 여러분의 친구입니다. 이는 코드 실행 중 숨겨진 값을 드러내는 데 도움을 줄 수 있습니다. for 루프에서는 일정한 규칙을 따라 반복 블록 코드를 수행합니다. 하지만 루프 도중, 중간 값을 확인하기는 어렵습니다. 이런 경우가 바로 중간 값을 드러내고 디버깅에 도움을 줄 수 있는 print를 사용할 완벽한 예시입니다.

### PAUSE 1

코드는 페이지 수와 페이지당 단어 수를 기준으로 총 단어 수를 계산해야 합니다. 하지만 현재는 아무 출력도 하지 않습니다.

print() 문을 사용하여 문제를 진단하세요.

```python
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
```

→word_per_page를 출력해보면 숫자를 입력해도 0으로 뜨는것을 확인, 따라서 0에 뭘 곱하든 0임 

```python
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words)
```

### PAUSE 2

코드를 수정하세요.

→ word_per_page == 이거는 boolean 타입으로 맞냐 아니냐를 물어보는 것, 따라서 = 으로 수정

```python
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
```

## 디버거 사용하기

대부분의 IDE(통합 개발 환경)인 PyCharm과 같은 도구에는 디버깅을 위한 내장 도구가 포함되어 있습니다. 일반적으로 디버거라고 알려져 있습니다. 여러 면에서, 이것들은 일종의 강화된 print 문이라고 할 수 있습니다.

디버거는 코드 실행 중 내부 메커니즘을 살펴보고, 선택한 지점에서 프로그램을 일시 정지하여 어떤 문제점이 있는지 파악할 수 있도록 도와줍니다.

대부분의 IDE에서 공통적으로 사용되는 몇 가지 기능이 있으니 이에 익숙해져야 합니다:

1. **중단점(Breakpoint)** - 코드의 행 번호가 있는 왼쪽 여백을 클릭하여 중단점을 설정할 수 있습니다. 이 부분은 디버그 실행 중 프로그램이 멈추는 위치를 나타냅니다.
2. **단계 건너뛰기(Step Over)** - 이 버튼을 사용하여 코드를 한 줄씩 실행하며 변수의 중간 값을 확인할 수 있습니다.
3. **단계 들어가기(Step Into)** - 코드에서 참조된 다른 모듈 내부로 들어갑니다. 예를 들어, random 모듈의 함수를 사용하는 경우 해당 함수의 원래 코드로 이동하여 기능을 더 잘 이해하고 문제와 어떻게 관련이 있는지 파악할 수 있습니다.
4. **내 코드로 들어가기(Step Into My Code)** - Step Into와 동일한 작업을 수행하지만 범위를 자신의 프로젝트 코드로만 제한하여 random과 같은 라이브러리 코드는 무시합니다.

### PAUSE 1

PyCharm 디버거를 사용하여 시작 코드에서 문제가 무엇인지 파악하고 이를 수정하세요.

```python
import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
```

![image.png](attachment:16e88273-10d3-40e0-8e6a-3a983e35058e:image.png)

→ b_list의 값이 빈 값으로 계속 진행되는 문제를 확인 후 오류 수정하고 다시 디버그

![image.png](attachment:e0acbe70-7258-40bd-b8c4-893e6073416a:image.png)

```python
import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
```

간단하게 오류 해결!

## 14 일차
## Higher or lower

사용자가 Instagram에서 누가 더 많은 팔로워를 가지고 있는지 추측하도록 하는 게임을 만드는 것이 목표입니다.

1. 초기 화면
    
    ![image.png](attachment:5b20c6b7-743a-40b0-b1ae-1b6f89f0c758:image.png)
    
2. 실패
    
    ![image.png](attachment:f64e3f57-7c6a-4d85-bc3f-b4432fcf25f6:image.png)
    
3. 성공
    
    ![image.png](attachment:a7e813b4-e61e-40e6-a055-5c31220311af:image.png)
    

성공하면 점수가 계속 올라감(누적)

실패하면 해당 점수를 반환하며 종료

성공하면 다음 단계에서 Against B가 Compare A가 됨 

random.randint(len(game_data.data)) → 0~data의 길이 전까지의 랜덤 값을 뽑아줌

1. A,B의 랜덤 숫자가 겹치면 안됨
    
    ```python
    data_len = len(game_data.data)
    a = random.randint(0, data_len-1)
    def choice_b(choice_a):
        bb = random.randint(0, data_len-1)
        while bb == choice_a:
            bb = random.randint(0, data_len-1)
        return bb
    b = choice_b(a)
    ```
    
2.  각 팔로워 수를 비교하며 조건문에 따라 나눠야됨
    
    ```python
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
    
    ```
    
3. while문을 통해 성공 시 계속 진행하며 실패하면 break를 통해 중지
    
    ```python
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
    
    ```
    

### 초기 화면

![image.png](attachment:f9497370-11b4-40a2-9a8f-52139d47328b:image.png)

### 실패 화면

![image.png](attachment:98e3a09a-361f-4bdb-9ec2-60608fc93228:image.png)

### 성공 화면

![image.png](attachment:077012cd-27f3-4226-9196-7c633d8d70ad:image.png)

이상 14일차 프로젝트 완료!

아래는 강의에서 제공된 솔루션, 내 풀이와 어떤 차이가 있는지 분석

```python
# Display art
from art import logo, vs
from game_data import data
import random

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
# Generate a random account from the game data
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:

    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
```

1. from ~ import를 활용해서 불필요한 코드를 줄임
2. format_data라는 함수를 생성해 각 딕셔너리의 값들을 함수에서 출력하여 불필요한 코드를 줄임
3. 솔루션에서도 a와 b의 값이 같을 때를 조건문을 통해서 방지하는 코드가 있음
    
    ```python
    account_a = account_b
        account_b = random.choice(data)
    
        if account_a == account_b:
            account_b = random.choice(data)
    ```
    
    다만 랜덤한 값이기 때문에 2번 연속 같은 숫자가 안 나온다는 보장이 없음, 따라서 내 코드가 더 안전
    

비슷비슷한 풀이지만 디테일적인 부분에서 보완할 부분이 있다고 느꼈음, 너무 길어지는 코드는 가독성을 해치므로, 강의 솔루션 처럼 함수로 빼거나 다른 방법을 생각해봐야 할듯.

## 15일차
## 커피머신 프로젝트

### 커피 머신 프로그램 요구사항

### 1. 사용자 프롬프트

"무엇을 드시겠습니까? (espresso/latte/cappuccino):" 메시지로 사용자에게 묻습니다.

- 사용자의 입력을 확인하여 다음 작업을 결정합니다
- 음료가 제공된 후 등 작업이 완료될 때마다 프롬프트가 다시 표시되어 다음 고객을 응대합니다

### 2. 커피 머신 끄기

프롬프트에 "off"를 입력하면 머신이 꺼집니다.

- 커피 머신 관리자는 "off"를 비밀 단어로 사용하여 머신을 끌 수 있으며, 이때 코드 실행이 종료됩니다

### 3. 리포트 출력

프롬프트에 "report"를 입력하면 현재 자원 상태를 보여주는 리포트가 생성됩니다.

- 예시: Water: 100ml, Milk: 50ml, Coffee: 76g, Money: $2.5

### 4. 자원 충분 여부 확인

사용자가 음료를 선택하면 프로그램은 해당 음료를 만들기에 충분한 자원이 있는지 확인합니다.

- 예를 들어 라떼에 200ml의 물이 필요한데 머신에 100ml만 남아있다면, 음료 제조를 계속하지 않고 "Sorry there is not enough water."를 출력합니다
- 우유나 커피 등 다른 자원이 부족할 때도 동일하게 처리됩니다

### 5. 동전 처리

선택한 음료를 만들 충분한 자원이 있으면 프로그램은 사용자에게 동전 투입을 요청합니다.

- 동전 가치: quarters(쿼터) = $0.25, dimes(다임) = $0.10, nickles(니켈) = $0.05, pennies(페니) = $0.01
- 투입된 동전의 금액을 계산합니다. 예: 쿼터 1개, 다임 2개, 니켈 1개, 페니 2개 = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

### 6. 거래 성공 여부 확인

사용자가 선택한 음료를 구매하기에 충분한 금액을 투입했는지 확인합니다.

- 라떼 가격이 $2.50인데 $0.52만 투입했다면 동전을 계산한 후 "Sorry that's not enough money. Money refunded."를 출력합니다
- 충분한 금액을 투입했다면 음료 가격이 머신의 수익으로 추가되며, 다음번 "report" 실행 시 반영됩니다
- 너무 많은 금액을 투입했다면 거스름돈을 제공합니다. 예: "Here is $2.45 dollars in change." (거스름돈은 소수점 둘째 자리로 반올림)

### 7. 커피 제조

거래가 성공하고 사용자가 선택한 음료를 만들 충분한 자원이 있으면, 음료를 만드는 데 필요한 재료가 커피 머신 자원에서 차감됩니다.

- 라떼 구매 전 리포트 예시: Water: 300ml, Milk: 200ml, Coffee: 100g, Money: $0
- 라떼 구매 후 리포트 예시: Water: 100ml, Milk: 50ml, Coffee: 76g, Money: $2.5
- 모든 자원이 차감되면 사용자에게 "Here is your latte. Enjoy!"를 출력합니다 (라떼를 선택한 경우)

### 풀이

```python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
## 현재 자원을 output 해주는 함수
def resource_report():
    return print(f"Water: {resources["water"]}, Milk: {resources["milk"]}, "
            f"Coffee: {resources["coffee"]}, Money:{resources["money"]}")
## 고른 음료에 대해서 현재 남은 자원이 충분한지 판단해주는 함수
def resource_enough(drink):
    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    if drink != 'espresso':
        milk = MENU[drink]["ingredients"]["milk"]

    if resources['water'] < water:
        return f"Sorry there is not enough water"
    elif coffee > resources['coffee']:
        return f"Sorry there is not enough coffee"
    elif drink != 'espresso':
        if milk > resources['milk']:
            return f"Sorry there is not enough milk"

    return 'enough'

def cost_enough(q, d, n, p, drink):
    global cost
    global customer_money
    customer_money = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    cost = MENU[drink]['cost']
    if cost > customer_money:
        return False
    else:
        return True

def add_resource(income, drink):
    resources["money"] += income
    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    if drink != 'espresso':
        milk = MENU[drink]["ingredients"]["milk"]

    resources["water"] -= water
    resources["coffee"] -= coffee
    if drink != "espresso":
        resources["milk"] -= milk

customer_money = 0
cost = 0
while True:
    if "money" not in resources:
        resources["money"] = 0

    selected_drink = input("무엇을 드시겠습니까? (espresso/latte/cappuccino): ")
    if selected_drink == 'off':
        break
    elif selected_drink == 'report':
        resource_report()
        continue

    enough = resource_enough(selected_drink)
    if enough != 'enough':
        print(enough)
        break

    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))

    enough_cost = cost_enough(quarters, dimes, nickles, pennies, selected_drink)
    if enough_cost:
        print(f"Here is ${customer_money - cost} in change.\n"
              f"Here is your {selected_drink} ☕️. Enjoy!")
        add_resource(cost, selected_drink)
    else:
        print("Sorry that's not enough money. Money refunded.")

```

우선 함수들 먼저 보면

def resource_report() → 프롬프트에서 report를 입력할 때, 남은 자원 및 금액을 출력해주는 함수

def resource_enough(drink) → 고른 음료에 대해서 현재 남은 자원이 충분한지 알려주는 함수, 여기서 중요한 점은 espresso는 milk가 없기 때문에 걸러주지 않는다면 오류가 발생함

def cost_enough(q, d, n, p, drink) → 고객이 건네준 돈이 충분한지 알려주는 함수로, 각 q/d/n/p는 동전을 의미하며 각각 다른 값어치를 가짐, drink는 고른 음료임, 이 함수에서 True/False를 반환해주고, 실제 메인 실행에서 조건문을 통해 실행을 달리함.

def add_resource(income, drink) → 위의 함수에서 True를 반환할 때, 실행됨. 쓴 자원과 벌어들인 돈을 dictionary에 추가 및 빼주는 함수

- 보기 싫은 부분은 아래의 코드임, 이 코드는 2 함수에 중복으로 들어가 있음
    
    ```python
    water = MENU[drink]["ingredients"]["water"]
        coffee = MENU[drink]["ingredients"]["coffee"]
        if drink != 'espresso':
            milk = MENU[drink]["ingredients"]["milk"]
    ```
    
    그래서 별로 효율적이지 않아보여서, 차라리 while 구문 안에 저 변수들을 미리 선언하고 함수를 부를 때, 넣어주는게 더 효율적이지 않을까 생각함.
    

### 강의 솔루션

```python
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
```

나중에 분석해봄

## 16일차
## 객체지향 프로그래밍

```python
from turtle import Turtle, Screen
# 다른 파일의 클래스를 import하여 내 클래스에서 객체를 생성할 수 있음
timy = Turtle()
print(timy)
timy.shape("turtle")
timy.color("red")
timy.forward(100)

my_screen = Screen()
print(my_screen.canvwidth)

# 생성한 객체를 활용해 메소드를 실행할 수 있음
my_screen.exitonclick()

# 라이브러리에 있는 다양한 메서드를 활용할 수 있음
```

클래스를 생성하고, 그 클래스를 활용해, 다른 파일에서 객체를 만들면, 위의 코드와 같이 해당 클래스 안에 있는 변수, 메서드, 객체, 클래스 등을 활용할 수 있음

## 객체지향 프로그래밍으로 커피머신 프로젝트 진행

파일이 하나 주어짐

![image.png](attachment:e4cbc19d-5f72-4302-96f2-ee68f87622ee:image.png)

```python
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

```

클래스 coffeeMaker - 커피를 만들어주는 클래스스

```python
class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

```

class MenuItem - 카페의 메뉴를 알려주는 클래스

```python
class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False

```

클래스 MoneyMachine - 돈 계산을 해주는 역할을 맡음

이 파일의 클래스를 활용해서(해당 파일들은 수정 불가) 프로젝트를 완수해야함

### 분석 및 풀이

MenuItem - 음료의 이름(name), 가격(cost), 소모되는 자원(ingredients)을 알려줌

Menu - get_items() 모든 메뉴를 알려줌, find_drink(name) 메뉴가 있는지 없는지

CoffeeMaker - report() 현재 자원의 상태, is_resource_sufficient(drink) 만들 수 있는지 없는지

make_coffee(order) 만들어주고 자원에서 깜

MoneyMachine - report() 현재 돈 얼마 번지, make_payment(cost) 소수타입, True면 적립, Fasle면 돈이 부족하니까 적립 안됨    

1. Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.

해석하면 input값을 통해 user가 정해야된다. 

한 손님의 주문이 끝나면 다음 주문이 반복되어야 한다.

```python
while True:     
    coffee = input("What would you like? (espresso/latte/cappuccino/): ")

```

1. Turn off the Coffee Machine by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the
machine. Your code should end execution when this happens

off를 입력하면 종료한데요.

```python
while True:
    coffee = input("What would you like? (espresso/latte/cappuccino/): ")
    if coffee == 'off':
        break
```

1. Print report()
    
    a. When the user enters “report” to the prompt, a report should be generated that shows the
    current resource values. e.g.
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
    
    ```python
    while True:
        coffee = input("What would you like? (espresso/latte/cappuccino/): ")
        if coffee == 'off':
            break
        elif coffee == 'report':
            CoffeeMaker.report(CoffeeMaker())
            MoneyMachine.report(MoneyMachine())
    ```
    
    ![image.png](attachment:4f41427c-4870-4570-b9f6-27c94179ed72:image.png)
    
2. Check resources sufficient?
    
    a. When the user chooses a drink, the program should check if there are enough resources
    to make that drink.
    b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not
    continue to make the drink but print: “Sorry there is not enough water.”
    c. The same should happen if another resource is depleted, e.g. milk or coffee.
    

사용자가 음료를 골랐어요, 그럼 프로그램은 **자원이 충분한지 채킹**, 만약에 부족하면, 어떤 자원이 부족한지 알려줘야됨(“Sorry there is not enough water.”)

```python
money_machine = MoneyMachine()
menu = Menu()
coffe_maker = CoffeeMaker()

while True:
    options = menu.get_items()
    coffee = input(f"What would you like? {options}: ")
    if coffee == 'off':
        break
    elif coffee == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee)
        coffe_maker.is_resource_sufficient(drink)
```

![image.png](attachment:4ba68f3a-7d69-4554-8da4-4a1387620480:image.png)

1. Process coins.
    
    a. If there are sufficient resources to make the drink selected, then the program should
    prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
    

음료를 만들기 충분하다면, 코드을 넣어야돼, 

```python
money_machine = MoneyMachine()
menu = Menu()
coffe_maker = CoffeeMaker()

while True:
    options = menu.get_items()
    coffee = input(f"What would you like? {options}: ")
    if coffee == 'off':
        break
    elif coffee == 'report':
        coffe_maker.report()
        money_machine.report()
        continue
    else:
        drink = menu.find_drink(coffee)
        print(drink.cost)
        is_sufficient = coffe_maker.is_resource_sufficient(drink)

        if is_sufficient:
            money_machine.make_payment(drink.cost)
        else:
            continue
```

1. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected. E.g
Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program
should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places
2. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the user
selected, then the ingredients to make the drink should be deducted from the coffee
machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte
was their choice of drink.

```python
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffe_maker = CoffeeMaker()

while True:
    options = menu.get_items()
    coffee = input(f"What would you like? {options}: ")
    if coffee == 'off':
        break
    elif coffee == 'report':
        coffe_maker.report()
        money_machine.report()
        continue
    else:
        drink = menu.find_drink(coffee)
        print(drink.cost)
        is_sufficient = coffe_maker.is_resource_sufficient(drink)

        if is_sufficient:
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
            else:
                continue
        else:
            continue
```

![image.png](attachment:df434017-8ca5-4177-bdbb-32d99136ef9c:image.png)

### 중요한점

클래스-객체, 메서드를 활용해서 drink = menu.find_drink(coffee)로 drink라는 객체를 생성하고,

객체를 생성하면 그 객체 안에 있는 name, cost, ingredients를 활용할 수 있다.

해당 패키지를 꼼꼼하게 체크해서 어떤 메서드가 들었는지, 해당 메서드는 어떤 값을 리턴하고 어떤 역할을 수행하는지 알아보는게 중요한 것 같다.

## 17일차
## 클래스를 만들어보기

```python
class User:
	pass

user_1 = User()
```

function과 마찬가지로 :(콜론)을 이용해서 클래스를 만들 수 있다.

원래 파이썬은 클래스나, 함수를 만들고 안에 아무것도 없으면 오류가 발생함(pass로 해결됨)

클래스를 만들고 그 클래스를 활용해서 객체를 생성(어제 배웠던 내용)

### 파이썬 표기법

PascalCase - 첫 단어의 앞글자가 대문자고 다음에 나오는 단어의 앞글자도 모두 대문자

camelCase - 첫 단어는 소문자이고 다음 단어의 앞글자들은 모두 대문자

snake_case - 모두 소문자이며 단어 사이사이에 _ 가 표기됨

파이썬은 클래스의 경우는 PascalCase를 활용하며, 다른 대부분의 속성이나 함수명은 snake_case가 활용됨

** 자바에서는 camelCase를 자주 활용했는데 이런 표기법에서의 차이가 있음

## 클래스에서 속성 만들어보기

```python
class User:
    # 파이썬은 클래스나 function을 생성 후 안에 아무것도 없으면 오류를 발생시킴, pass를 활용하면 아무것도 없는 껍데기 클래스를 만들 수 있음
    pass

# 클래스를 활용해 객체를 만듦
user_1 = User()

#PascalCase / camelCase / snake_case
# 클래스 이름에는 파스칼, 다른 모든 변수들은 대부분 스네이크 케이스

user_1.id = "001"
user_1.username = "angela"

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "jack"

print(user_2.username)
```

이렇게 클래스로 객체를 만들고 객체를 활용해 속성을 부여할 수 있다.

하지만 사용자가 100명 1000명이라면? 하나하나 코드를 쳐서 속성을 부여할건가?

### 생성자

객체가 생성될 때, 무슨 일이 일어나는지 명시해 놓은 함수

파이썬에서 생성자를 만들려면 init이라는 특별한 함수를 활용

```python
class User:
    def __init__(self):
        print("new user being created")

# 클래스를 활용해 객체를 만듦
user_1 = User()

user_2 = User()
```

![image.png](attachment:546eb4f4-91da-4b04-8589-31c898ab8e5a:image.png)

user_1과 user_2라는 객체가 생성되며 생성될 때, print문이 작동하는 것을 볼 수 있음

### 속성 부여

객체를 생성할 때, 괄호 안에 속성 값을 부여하면 객체가 생성됨과 동시에 속성 값을 정할 수 있음

ex) my_car = Car(5)

→ def —init—(self, seat):

self.seats = seats

⇒ my_car.seats = 5

```python
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        print(f"user_id : {id}, user_name : {name}")

# 클래스를 활용해 객체를 만듦
user_1 = User("001", "angela" )

user_2 = User("002", "jack")
```

![image.png](attachment:ec5c4e8e-e33a-49a5-95f4-9e365a133d6e:image.png)

이제 User라는 클래스에서 객체를 생성하려면 id와 name값을 넣어서 만들어야됨,

만약에 그냥 만들려고 한다면 오류가 발생함.

반대로 생성자에서 기본값을 설정할수도 있음

```python
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        print(f"user_id : {id}, user_name : {name}, user_followers : {self.followers}")
```

이렇게 되면 객체가 생성될 때, 자동으로 팔로워가 0으로 값이 설정돼서 들어감

![image.png](attachment:725db6b3-6c64-4093-9be7-7bc01a502b31:image.png)

## 클래스에 메소드 추가하기

속성 - 객체가 가지는 것 ex) Car - seats

메소드 - 객체가 하는 것 ex) Car - drive()

코드에서는 객체.메소드() 이렇게 사용할 수 있음

그냥 기존의 def함수들과는 다르게 Class안의 메소드(def)는 항상 (self)를 가지고 시작함.

그래야 어떤 객체가 나를 불렀는지 컴퓨터가 확인할 수 있음

```python
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0
        print(f"user_id : {id}, user_name : {name}, user_followers : {self.followers}, user_following : {self.following}")

    def follow(self, user):
        user.followers += 1
        self.following += 1
```

방금 계정을 생성한 user_1과 user_2가 있음,

user_1이 user_2를 팔로우 하기 위해 함수를 실행

user_1.follow(user_2) → user_2의 팔로워가 +1, user_1의 팔로윙도 + 1

```python
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0
        print(f"user_id : {id}, user_name : {name}, user_followers : {self.followers}, user_following : {self.following}")

    def follow(self, user):
        user.followers += 1
        self.following += 1

# 클래스를 활용해 객체를 만듦
user_1 = User("001", "angela" )

user_2 = User("002", "jack")

user_1.follow(user_2)
print(f"user_1의 followers : {user_1.followers}, user_2의 followers : {user_2.followers}\n"
      f"user_1의 following : {user_1.following}, user_2의 following : {user_2.following}")
```

![image.png](attachment:aadc0436-9f45-4bf0-9d19-052f518b81d8:image.png)

## 퀴즈 프로젝트

### 1부 : 질문 클래스 만들기

퀴즈 질문에 대한 모델을 만들어야됨.

속성 - text, answer ⇒ 새로운 질문 객체가 생성될 때, 생성자로 값이 항상 생겨야함

Question class 생성

```python
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        print(f"text: {self.text}, answer: {self.answer}")
```

### 2부 : 데이터로부터 질문 객체 리스트 만들기

우리는 1부에서 question_model.py에서 클래스를 생성했고, data.py에는 미리 만들어둔 questiondata가 dictionary 형태로 존재한다.

![image.png](attachment:a311b10d-09af-4972-bc80-5908406fc5f5:image.png)

이 2 파일을 활용해서 main.py에 question_bank = [ Question(q1, a1), Question …. ] 형태의 리스트를 생성해야 한다.

하나하나 객체를 생성해서 만들면? 시간이 오래걸림, question = Question(question_data[0][”text], question_data[0][”answer”]) → 이렇게하면 객체가 하나 생성됨.

이거를 어떻게 효과적으로 줄일 수 있을까 → 반복문

사전에는 0~11 총 12번 반복을 하면 됨(모른다면 len(question_data))

```python
from data import question_data
from question_model import Question

for question in question_data:
    question_bank = [
        Question(question["text"], question["answer"])
    ]

for question in question_bank:
    print(question_bank[2].text)
```

![image.png](attachment:3c6b98b7-40c9-4c81-b05b-5edcd66e0a3c:image.png)

생성자가 잘 작동해서 된 줄 알았는데 결국 리스트에는 하나의 값만 들어있음, 생성자마다 이름을 붙여서 다른 객체라는 것을 인지시켜야 될듯

```python
from data import question_data
from question_model import Question

question_bank = []

for question in question_data:
    qt = Question(question["text"], question["answer"])
    question_bank.append(qt)

print(question_bank[0].text)
print(question_bank[1].text)
print(question_bank[2].text)
```

![image.png](attachment:4b7da0ce-e563-4cc3-99cc-682bc81a3b6a:image.png)

반복문은 생성자만 만들고 미리 만들어둔 빈 리스트에 append하여 다른 index로 추가함.

### 3부 : 퀴즈브레인과 next_question() 메소드

위에 2부에서 question_bank를 만들었다, 이제 질문 중 하나를 제시하고, 사용자에게 그 질문에 대답하도록 요구하는 기능을 만들어야 한다.

quiz_brain.py 파일에서, 우리는 질문, 확인, 응답을 해줘야한다.

attributes - question_number = 0, question_list

methods - next_question()

Q.1: A sulg’s bllood is green. (True/False)?: 

```python
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
```

QuizBrain 생성자 - 게임 스타트와 같음, question_list를 넣고(question_bank),

시작값을 0으로 생성

다음으로 next_question() 생성 → question_list의 text를 가져오고 사용자에게 답을 요구

```python
    def next_question(self):
        question_list = self.question_list
        question_number = self.question_number
        question = self.question_list[question_number]
        answer = input(f"Q.{question_number+1}: {question_list["text"]} (True/False)?: ")
```

이렇게 만들어서 main.py에서 import 후 실행

```python
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    qt = Question(question["text"], question["answer"])
    question_bank.append(qt)

quiz_brain = QuizBrain(question_bank)

quiz_brain.next_question()
```

![image.png](attachment:14fb05f6-9421-4e24-a5ad-ea85f065cc49:image.png)

### 4부 : 질문을 계속 보여주기

그냥 while문 추가하면 되는거 아닌가?

```python
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        while True:
            question = self.question_list[self.question_number]
            answer = input(f"Q.{self.question_number+1}: {question.text} (True/False/Off)?: ")
            if answer == question.answer:
                self.question_number += 1
            elif answer == "Off":
                break
            else:
                print(f"Wrong answer. Try again.")
                break
```

이렇게 만들고 main에서는 그대로 실행하면 

![image.png](attachment:41b967c7-c70a-4d32-9b11-fd29e91d1b73:image.png)

출력값을 보면 틀리거나 Off를 입력하면 멈추지만, 맞추면 계속 진행됨

근데 강의에서는 다른 방법을 씀 - 우선 quiz_brain 파일에서 still_has_questions 메소드를 만들어서 남은 퀴즈가 있는지 없는지 확인

```python
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            # 0~11 까지만
            return True
        else:
            return False
```

⇒ 이거를 간단하게 입력할 수있음

```python
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
```

어차피 ture false기 때문에 그냥 return 해주면 됨.

### 5부 : 답변을 확인하고 점수 유지하기

```python
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number+1}: {question.text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(answer, question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")

        print(f"The answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
```

quiz_brain 객체에 score라는 속성을 추가하고 check_answer라는 정답 확인을 해주는 메소드를 추가함

next_question에서는 question_number를 추가하고 check_answer메소드를 실행시키며 사용자의 답과 실제 사전에 있는 정답을 파라미터로 보내줌

check_answer에서는 answer와 correct_answer를 비교하고 정답일 때는 score를 1 증가 및 다른 구문을 print함, 마지막으로 현재 진행도와 맞춘 개수를 확인

```python
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    qt = Question(question["text"], question["answer"])
    question_bank.append(qt)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
```

메인의 while 구문은 한줄로 끝남

![image.png](attachment:64d6be85-ebd8-465f-a795-e389887842f6:image.png)

### Open Trivia DB 활용

https://opentdb.com/api_config.php

해당 url로 이동 (회원가입 해야됨) → API 클릭

![image.png](attachment:18c4a4b3-a283-4c18-8a9e-f4d0722e02ac:image.png)

작성 후 URL 얻기 버튼을 누르면 상단에 URL 링크가 뜨고 해당 주소로 들어가면

```
{"response_code":0,"results":[{"type":"boolean","difficulty":"easy","category":"Science
: Computers","question":"&quot;HTML&quot; stands for Hypertext Markup Language.","correct
_answer":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"easy","cat
egory":"Science: Computers","question":"The programming language &quot;Python&quot; is ba
sed off a modified version of &quot;JavaScript&quot;.","correct_answer":"False","incorre
ct_answers":["True"]},{"type":"boolean","difficulty":"easy","category":"Science: Compute
rs","question":"Linux was first created as an alternative to Windows XP.","correct_answ
er":"False","incorrect_answers":["True"]},{"type":"boolean","difficulty":"easy","categor
y":"Science: Computers","question":"RAM stands for Random Access Memory.","correct_answe
r":"True","incorrect_answers":["False"]},{"type":"boolean","difficulty":"easy","category":"
Science: Computers","question":"The Python programming language gets its name from the Bri
tish comedy group &quot;Monty Python.&quot;","correct_answer":"True","incorrect_answers":["F
alse"]},{"type":"boolean","difficulty":"easy","category":"Science: Computers","question":"A Ma
c is not a PC","correct_answer":"False","incorrect_answers":["True"]},{"type":"boolean","dif
ficulty":"easy","category":"Science: Computers","question":"In most programming languages, t
he operator ++ is equivalent to the statement &quot;+= 1&quot;.","correct_answer":"True","in
correct_answers":["False"]},{"type":"boolean","difficulty":"easy","category":"Science: Computers"
,"question":"Time on Computers is measured via the EPOX System.","correct_answer":"False",
"incorrect_answers":["True"]},{"type":"boolean","difficulty":"easy","category":"Science: Computers"
,"question":"Ada Lovelace is often considered the first computer programmer.","correct_answer":"True",
"incorrect_answers":["False"]},{"type":"boolean","difficulty":"easy","category":"Science: Computers","
question":"Linus Torvalds created Linux and Git.","correct_answer":"True","incorrect_answers":["False"]}]}
```

이런 JSON 형태의 코드를 받을 수 있음

![image.png](attachment:5235b979-ae58-494c-ba16-e260f6e7b6ea:image.png)

data.py에 복사해서 형태를 보면, question과 correct_answer 로 이루어진 것을 볼 수 있음,

다른 Key값들도 있지만 우리는 필요없음

```python
for question in question_data:
    qt = Question(question["question"], question["correct_answer"])
    question_bank.append(qt)
```

메인으로 돌아와서 for문에서 아까는 text와 answer였으므로 수정

![image.png](attachment:02517555-7462-4316-837f-7b9ba998623e:image.png)

실행하면 정상적으로 코드가 돌아가는걸 확인할 수 있음

객체지향으로 프로그래밍을 작성했기 때문에 이렇게 data.py의 값만 바꾸고도 다른 퀴즈 풀이를 진행할 수 있음.

끝!

## 18일차
## 파이썬 Turtle 라이브러리를 활용하여 과제

### 정사각형 그리기

```python
from turtle import Turtle, Screen

turtle_study = Turtle()
screen_study = Screen()
# 1. 정사각형 만들기
turtle_study.forward(100)
turtle_study.right(90)
turtle_study.forward(100)
turtle_study.right(90)
turtle_study.forward(100)
turtle_study.right(90)
turtle_study.forward(100)

screen_study.exitonclick()
```

![image.png](attachment:c9662828-3c50-4705-bdd2-4c59ef778280:image.png)

### 모듈 임포트

```python
# 모듈 임포트
from turtle import *
```

turtle 패키지에 있는 모든 모듈을 임포트 → *

하지만 이렇게 되면 내가 사용한 메서드가 어디서 온건지 확인이 잘 안됨, 따라서 가독성이 떨어지기 때문에 좋은 방법이 아니다

### 알리아싱 모듈

```python
# 모듈 임포트
import turtle as t
tim = t.Turtle()
```

임포트한 패키지에 이름을 붙여서 활용할 수 있음

### 설치 모듈

![image.png](attachment:caf9ed76-d36e-4c85-9b6a-7476011c051c:image.png)

heros 모듈을 import하려고 했지만 파이썬 라이브러리에 없어서 import가 안됨

그때 저 패키지 설치를 눌러서 파이썬 라이브러리에 heros 모듈을 설치할 수 있음

![image.png](attachment:d0d6cace-d8fa-41c0-8fba-9605c1df8a14:image.png)

![image.png](attachment:8f463279-20f1-4215-b45f-d2e940fcdab1:image.png)

설치가 완료되면 사진처럼 heroes 패키지를 사용할 수 있음

### 점선 그리기

turtle패키지를 활용해 점선 사각형을 그리기

![image.png](attachment:4a13db89-4926-41c1-a193-63d86076d858:image.png)

pendown, penup 메소드를 활용할 수 있음

```python
# 2. 점선 그리기
def draw():
    turtle_study.forward(10)
    turtle_study.pendown()
    turtle_study.forward(10)
    turtle_study.penup()
    turtle_study.forward(10)
    turtle_study.pendown()
    turtle_study.forward(10)
    turtle_study.penup()
    turtle_study.forward(10)
    turtle_study.right(90)
for _ in range(4):
    draw()

screen_study.exitonclick()
```

![image.png](attachment:4955f16e-8019-437b-877d-e0d938370bc0:image.png)

### 다양한 도형 그리기

```python
# 다양한 도형 그리기
import random as rd
count = 3
color_list = ["red", "yellow", "blue"
              ]
for i in range(3):
    count += 1
    for j in range(count):
        turtle_study.forward(100)
        turtle_study.right(360/count)
    turtle_study.color(rd.choice(color_list))
```

사각형 = 4, 오각형 = 5를 이용해 360/count로 도형을 구현

### 무작위 행보 구현하기

```python
# 무작위 행보 구현하기
direction = [0, 90, 180, 270]
turtle_study.pensize(15)
turtle_study.speed("fastest")

for _ in range(200):
    turtle_study.forward(100)
    turtle_study.setheading(rd.choice(direction))
    turtle_study.color(rd.choice(color_list))
```

## 파이썬 튜플

![image.png](attachment:aea29379-97ce-49de-8be5-abc61cd470b7:image.png)

파이썬 튜플은 () → 소괄호로 이루어진 리스트이며

위에 사진과 같이 값을 바꿀 수 없음(재할당 x)

### 터틀에 임의의 RGB 색상 생성하기

```python
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0,90,180,270]
tim.pensize(10)
tim.speed("fastest")

for _ in range(100):
    tim.color(random_color())
    tim.forward(10)
    tim.right(random.choice(directions))
```

![image.png](attachment:0ac875ca-4477-46e6-ae46-dd76e654aa33:image.png)

### 스피로 그래프 그리기

1. 원 생성

```python
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")
tim.color(random_color())
tim.circle(100)

screen = t.Screen()
screen.exitonclick()
```

![image.png](attachment:8bd11788-5a7b-44b4-907d-d344100b4ed5:image.png)

1. 방향 바꾸기

```python
current_heading = tim.heading()
tim.setheading(current_heading + 10)
tim.color(random_color())
tim.circle(100)
```

![image.png](attachment:70dacff1-e25c-4097-9fae-cd9d09e86d77:image.png)

1. 반복문 생성

```python
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")

for _ in range(100):
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)

screen = t.Screen()
screen.exitonclick()
```

![image.png](attachment:854dc665-c74a-44f8-a987-c60724503429:image.png)

## 프로젝트 1. 이미지에서 rgb값 추출

이미지에서 rgb값 추출하기

img.jpg는 구글에 있는 paiting 사진을 하나 다운

colorgram이라는 패키지를 활용해서 extract 메소드를 활용

→ 

![image.png](attachment:1d24231a-9c3e-4125-a379-ebacd7bc08c0:image.png)

처음에는 이러한 값들을 얻게 됨

여기서 우리는 Rgb값을 사용하므로 반복문을 통해 

colors.rgb를 활용

```python
import colorgram
colors = colorgram.extract('img.jpg', 25)

rgb_colors = []

for c in colors:
    rgb_colors.append(c.rgb)

print(rgb_colors)
```

→ 

![image.png](attachment:ee2a1064-e80b-4ba3-a9e4-ff3d44976993:image.png)

이제 마지막으로 튜플 형태의 rgb 값들을 가져와야 하기 때문에 아래의 코드를 적용해 값을 얻음

```python
import colorgram
colors = colorgram.extract('img.jpg', 25)
rgb_colors = []

for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    col = (r, g, b)
    rgb_colors.append(col)

print(rgb_colors)
```

→ 

![image.png](attachment:203bb319-200e-44e6-aa7d-46135ecae7eb:image.png)

마지막으로 main.py에 해당 리스트를 등록

```python
colors = [(229, 228, 226), (225, 223, 224), (199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), (222, 223, 226), (200, 216, 205), (108, 67, 85), (39, 36, 35), (86, 142, 58), (20, 123, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (210, 200, 113), (179, 175, 177), (151, 176, 164), (93, 142, 156), (28, 80, 59)]

```

## 프로젝트2 점 그리기

10x10 크기의 점이 있는 그림을 그려야 함

1. 준비 

```python
# 점 그리기
from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()
tim.speed("fastest")
screen.colormode(255)
```

1. 점 그리기 함수 

```python
def draw_dot():
    for _ in range(10):
        choice_color = random.choice(colors)
        tim.dot(10, choice_color)
        tim.penup()
        tim.fd(25)
```

랜덤 컬러 생성 후 dot 메소드로 점 생성 및 앞으로 이동하는데 penup 메소드로 선이 안보이게 설정

1. 방향 바꾸기

```python
def draw_dot():
    for _ in range(10):
        choice_color = random.choice(colors)
        tim.dot(10, choice_color)
        tim.penup()
        tim.fd(25)
    tim.left(90)
    tim.fd(25)
    tim.right(90)
    tim.setx(0)
```

추가로 반복문이 끝나고 방향을 바꾼 후 위로는 25만큼 이동 후 x좌표는 0으로 설정

1. 위로 10개 추가 반복문

```python
for _ in range(10):
    draw_dot()

tim.home()
screen.exitonclick()
```

함수를 10번 실행해 10x10 형태로 만들어줌

![image.png](attachment:fc4b0017-0282-438d-a625-af06ea458d81:image.png)

## 19일차
## 파이썬 고차함수 및 이벤트리스너

### 터틀 이벤트리스너

![image.png](attachment:82cf090c-4abc-463c-8e6a-e65634ab41de:image.png)

```python
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()
```

listen() 함수로 screen에 대한 이벤트를 들을 준비

onkey()를 활용 → key와 fun을 인자로 받음

key → 값을 누르면 → fun → 함수를 실행, 즉 이벤트(스페이스바를 누름)가 발생하면 함수를 실행

현재 함수는 앞으로 10 이동

![image.png](attachment:d79d181d-6885-4db2-aa9d-dbd1a1f175e6:image.png)

누를 때마다 10 이동하는 것을 볼 수 있음

### 함수를 다른 함수에 전달하는 형태(고차함수)

```python
def add(n1, n2):
    return n1+n2

def calculator(n1,n2,func):
    return func(n1,n2)

result = calculator(1, 2, add)
print(result)
```

→ 3이 출력되는 것을 알 수 있음

이러한 형태의 calculator함수들을 고차함수라고 부르며 이벤트 함수들 또한 고차함수임

## 에치어스케치 앱 만들기

터틀 스크린에서 다음의 기능을 만들어야 함

w - forwards

s - backwards

a - counter-clockwise(반시계 방향 회전)

d - clockwise

c - clear-drawing

![image.png](attachment:1f19e3fb-60f6-43fe-b34b-4dee235a0c4d:image.png)

![image.png](attachment:a337bce5-1f41-4f56-b6fc-f05b05f52e62:image.png)

다음의 함수들을 활용해서 과제를 진행

```python
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# 에치어스케치 앱 만들기
def w_forwards():
    tim.forward(1)

def s_forwards():
    tim.backward(1)

def a_counter_clockwise():
    tim.left(1)

def d_clockwise():
    tim.right(1)

def c_clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeyrelease(w_forwards, "w")
screen.onkeypress(s_forwards, "s")
screen.onkeyrelease(a_counter_clockwise, "a")
screen.onkeypress(d_clockwise, "d")
screen.onkey(c_clear_drawing, "c")

screen.exitonclick()
```

![image.png](attachment:51e064b9-1301-46cb-9761-aa5945a86242:image.png)

## 객체의 상태 및 인스턴스

우리는 여러 turtle 객체를 생성할 수 있다.

tim = Turtle()

tom = Turtle()

tim.color(”blue”)

tom.color(”red”) 

이런식으로 turtle 객체를 여러 개 만들고 다른 동작을 수행하게 할 수 있다.

## 터틀 좌표계 이해하기

```python
# 터틀 레이싱 게임 프로젝트
screen.setup(width=500, height=400) # screen의 크기를 지정
user_bet = screen.textinput(title="Make you bet", prompt="Witch turtle will win the race? Enter a color: ")
print(user_bet)

screen.exitonclick()
```

먼저 스크린의 크기를 지정해주며, textinput 함수를 사용해 팝업창을 띄워서 사용자에게 배팅을 고를 수 있게 해준다.

![image.png](attachment:8bbcaa8d-764d-47d8-a1d2-c9aa70d27504:image.png)

![image.png](attachment:76f1b20a-cda1-4ca0-b559-699043f3346e:image.png)

이렇게 팝업 텍스트 창이 뜨면서 red를 입력하면 user_bet에 red가 저장되는 것을 볼 수 있다

이제 turtle의 좌표를 지정해야 한다.

turtle 패키지에서는 화면의 정 가운데가 0,0의 좌표이므로 x축의 첫 출발선을 지정하기 위해

우리가 screen의 크기를 지정했던 500에서 절반, 즉 x좌표는 -250이 된다

```python
 # 터틀 레이싱 게임 프로젝트
screen.setup(width=500, height=400) # screen의 크기를 지정
user_bet = screen.textinput(title="Make you bet", prompt="Witch turtle will win the race? Enter a color: ")
print(user_bet)

tim.setx(-240)

screen.exitonclick()
```

250을 지정했는데 화면에 객체가 안보여서 240으로 조정했다.

![image.png](attachment:71da0219-d63d-48a0-8703-f5f116991945:image.png)

이렇게 penup과 goto 함수를 활용하면 선을 그리지 않고 x와 y좌표를 선택하여 이동할 수 있다

```python
# 터틀 레이싱 게임 프로젝트
screen.setup(width=500, height=400) # screen의 크기를 지정
user_bet = screen.textinput(title="Make you bet", prompt="Witch turtle will win the race? Enter a color: ")
print(user_bet)
tim.penup()
tim.goto(x=-240,y=-100)

screen.exitonclick()
```

![image.png](attachment:d52134be-89ea-4b84-9f0c-35a6694d933c:image.png)

이제 여러 개의 turtle 객체를 생성해주며 색상 리스트도 만들어준다

```python
red = Turtle(shape="turtle")
blue = Turtle(shape="turtle")
orange = Turtle(shape="turtle")
yellow = Turtle(shape="turtle")
green = Turtle(shape="turtle")
purple = Turtle(shape="turtle")

colors = ["red","orange","yellow","green","blue","purple"]
```

각각 다른 좌표를 지정하며 다른 색상으로 시작점으로 보낸다

```python
# 터틀 레이싱 게임 프로젝트
screen.setup(width=500, height=400) # screen의 크기를 지정
user_bet = screen.textinput(title="Make you bet", prompt="Witch turtle will win the race? Enter a color: ")
print(user_bet)
red.penup()
red.color("red")
red.goto(x=-240,y=-100)
blue.penup()
blue.color("blue")
blue.goto(x=-240,y=-60)
orange.penup()
orange.color("orange")
orange.goto(x=-240,y=-20)
yellow.penup()
yellow.color("yellow")
yellow.goto(x=-240,y=20)
green.penup()
green.color("green")
green.goto(x=-240,y=60)
purple.penup()
purple.color("purple")
purple.goto(x=-240,y=100)
```

![image.png](attachment:105d23f5-2e61-4dd6-baee-1f43f81bd3e7:image.png)

반복문을 활용하면 코드를 하나하나 작성하지 않아도 여러 개의 객체를 생성할 수 있다.

```python
# 터틀 레이싱 게임 프로젝트
colors = ["red","orange","yellow","green","blue","purple"]

screen = Screen()
screen.setup(width=500, height=400) # screen의 크기를 지정
user_bet = screen.textinput(title="Make you bet", prompt="Witch turtle will win the race? Enter a color: ")
y_positions = [-100, -60, -20, 20, 60, 100]

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-240, y=y_positions[turtle_index])

screen.exitonclick()
```

![image.png](attachment:71c91b05-ee75-42a3-b972-74b10ef241de:image.png)

## 레이싱 프로젝트

이제 출발선 까지 준비했으므로 무작위로 거북이가 움직여야 함

임의의 숫자를 생성하고 반복문을 통해서 각 숫자만큼 객체들이 움직이게 해야 함

여기서 생성된 객체를 따로따로 다른 값들을 줘야 하므로 빈 리스트에 객체를 담아서 반복문 실행

```python
from turtle import Turtle, Screen

# 터틀 레이싱 게임 프로젝트
is_race_on = False
import random
all_turtles = []

colors = ["red","orange","yellow","green","blue","purple"]

screen = Screen()
screen.setup(width=500, height=400) # screen의 크기를 지정
user_bet = screen.textinput(title="Make you bet", prompt="Witch turtle will win the race? Enter a color: ")
y_positions = [-100, -60, -20, 20, 60, 100]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    # 임의의 숫자 가져오기
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
    
    
screen.exitonclick()
```

all_turtles라는 빈 리스트를 만들고, 전에 만들었던 반복문 코드 마지막에 append를 통해 객체들을 리스트에 넣어줌

user_bet이 선택되면 반복문이 실행되며 리스트에 들어있는 각 객체들은 각각의 거리값을 가지며 앞으로 이동함

이제 마지막으로 x축이 250에 도착한다면 반복문을 종료해야 함.

여기서 터틀 객체의 크기는 20x20이므로 거북이가 실제로 도착해야 하는 좌표는 230이 됨

```python
from turtle import Turtle, Screen

# 터틀 레이싱 게임 프로젝트
is_race_on = False
import random
all_turtles = []

colors = ["red","orange","yellow","green","blue","purple"]

screen = Screen()
screen.setup(width=500, height=400) # screen의 크기를 지정
user_bet = screen.textinput(title="Make you bet", prompt="Witch turtle will win the race? Enter a color: ")
y_positions = [-100, -60, -20, 20, 60, 100]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    # 임의의 숫자 가져오기
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
            if user_bet == winner:
                print(f"You correct! winner is {winner}")
            else:
                print(f"You lose! winner is {winner}")
            break
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
```

![image.png](attachment:df340f38-d9ec-4309-94b8-e77c17eebfac:image.png)

이렇게 레이스가 종료되면 콘솔창에 결과를 말해주고 while문이 종료됨

19일차 강의에서는 여러 객체를 만들고, 각 객체에 다른 메소드를 부여하여 각각의 행동을 지정할 수 있는 것을 배웠음

## 20 일차
20일차와 21일차, 2일에 거쳐서 snake 게임 만들기 프로젝트를 진행

## 뱀 몸체 만들기

### 터틀 객체의 좌표 설정

사각형 3개가 나란히 있는 상태의 객체를 만들어야 함

객체 하나의 픽셀은 20x20

따라서 (0,0), (0,-20), (0,-40)

```python
# 초기 설정(스크린 크기, 배경, 타이틀)
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

# 초기 터틀 객체
segment_1 = Turtle(shape="square")
segment_1.color("white")
segment_2 = Turtle(shape="square")
segment_2.color("white")
segment_2.goto(-20,0)
segment_3 = Turtle(shape="square")
segment_3.color("white")
segment_3.goto(-40,0) 
```

즉, 코드를 작성하면 goto함수를 활용해서 위의 코드를 작성할 수 있음

![image.png](attachment:d4084836-71bf-440b-bbec-f8cc04163c82:image.png)

이 객체를 일일이 만드는 것이 아니라 반복문을 활용해서 만들면

```python
# 초기 설정(스크린 크기, 배경, 타이틀)
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_position = [(0,0), (-20,0), (-40,0)]
# 초기 터틀 객체
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
```

이렇게 위치좌표를 배열 안의 튜플로 만들어서 반복문을 실행할 수 있음

## 뱀 움직이기

```python
# 뱀 움직이기
game_is_on = True
while game_is_on:
    for segment in segments:
        segment.forward(10)
```

이런식으로 뱀을 움직이게 할 수 있지만, 반복문 하나하나 객체들이 움직이기 때문에 자연스러운 움직임이 보이지 않음

### tracer, update

tracer 함수를 활용해서 객체가 움직이는 애니메이션을 끌 수 있음 → 객체는 이동했지만 화면에 안보임

update 함수를 활용해 tracer 함수로 움직이지 않던 객체를 애니메이션 없이 한번에 움직이게 할 수 있음

초기설정에서 screen.tracer(0) 으로 애니메이션을 끔

![image.png](attachment:1f45b46c-6a21-476c-9bec-77619005e147:image.png)

객체 생성 또한 애니메이션이라서 생성되지 않음

여기서 while문의 첫 부분에 screen.update()를 해주게 된다면 객체가 한꺼번에 움직이는 것을 볼 수 있음

[20260120-1130-07.3489934.mp4](attachment:127ee33f-c17d-4ad3-9fa3-3762f5aa3970:20260120-1130-07.3489934.mp4)

```python
from turtle import Screen, Turtle
import time

# 초기 설정(스크린 크기, 배경, 타이틀)
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(0,0), (-20,0), (-40,0)]

segments = []

# 초기 터틀 객체
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# 뱀 움직이기
game_is_on = True
while game_is_on:
    screen.update()
    for segment in segments:
        segment.forward(20)
        time.sleep(1)
```

여기서 time은 느린 속도로 객체의 이동을 확인하기 위해 import하여 사용함

## 뱀 방향 바꾸기

뱀의 방향을 바꾸기 위해서 첫 번째 객체의 방향을 바꾸면, 첫 번째 객체의 방향만 바뀌고 나머지 객체의 방향은 바뀌지 않음.

즉, 머리와 몸통이 따로 노는 뱀이 탄생하게 됨

→ 전부 다 앞으로 가는게 아니라, segment3를 segment2자리로, segment2를 segment1자리로, segment1은 방향을 바꿔서 앞으로 이동

```python
# 뱀 움직이기
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # 뱀 방향 바꾸기
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)
```

반복문을 만듦, 총 뱀의 길이에서 0까지

new_x → 해당 뱀 객체의 전 객체의 x좌표

new_y → 해당 뱀 객체의 전 객체의 y좌표

마지막으로 반복문이 끝나면 가장 첫 번째 객체(머리)를 이동시킴

그러면 위에서 말한 것처럼 각 객체의 위치를 내 앞 객체의 위치로 이동시킬 수 있음

즉 가장 중요한 포인트는 반복문에서 선택된 seg_num의 위치를 내 앞 객체의 위치로 이동시키는 것.

→ 의문이 생길 수 있음, seg_num -1의 x와 y좌표를 추출해서 seg_num 객체의 좌표로 옮겼는데 그러면 내 앞 객체가 아니라 전 객체의 위치로 옮긴거 아니에요?

→ 아님, 왜냐면 반복문을 가장 마지막 인덱스부터 시작했기 때문에 거꾸로 가는 반복문임

[20260120-1203-54.4700602.mp4](attachment:bcf9899d-74fc-42d4-93e1-f2e935948e43:20260120-1203-54.4700602.mp4)

## 뱀 클래스를 만들고, 객체지향 프로그래밍 하기

snake.py에서 뱀 객체를 생성하고, 움직이는 메서드를 넣음

```python
from turtle import Turtle

starting_position = [(0,0), (-20,0), (-40,0)]
segments = []

class Snake:
    def __init__(self):
        for position in starting_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            segments.append(new_segment)

    def move(self):
        # 뱀 방향 바꾸기
        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)
        segments[0].left(90)
```

main.py에서는 Screen 객체를 만들어 설정하고 while문을 통해 move 메서드를 실행

```python
from turtle import Screen, Turtle
from snake import Snake
import time

from snake import Snake

# 초기 설정(스크린 크기, 배경, 타이틀)
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

# 뱀 움직이기
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
```

이렇게 객체지향 프로그래밍을 만들 수 있음

앞으로의 방향→  현재 snake.py를 만들어 뱀에 관한 객체 생성 및 움직이는 메소드를 넣음

→ 먹이클래스를 만들어, Screen에 먹이를 생성하는 파일을 만듦

→ 점수클래스를 만들어, 먹이를 먹을 때마다 점수가 올라가는 파일을 만들거임

```python
from turtle import Turtle

starting_position = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        for position in starting_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # 뱀 방향 바꾸기
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
        self.segments[0].left(90)
```

강사님은 생성자를 실행하면서 create_snake() 메소드를 실행시킴, 해당 메소드의 self → 생성하는 객체가 되며 해당 객체의 segments 임을 명시해줄 수 있음

move()메소드도 마찬가지로 이렇게 해주면 self.segments라고 자신의 객체임을 명시할 수 있음

## 키 입력으로 뱀의 방향 바꾸기

어제 배웠던 키 바인딩을 통해 뱀의 방향을 바꿀 수 있음

먼저 이벤트를 듣기 위해 main.py에 해당 코드 입력

```python
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
```

이제 해당 키를 누를 때마다 방향을 바꾸는 메소드를 snake.py에 만들기만 하면 됨

→ setheading(0) / ← setheading(180) 이런식으로

```python
    def up(self):
            self.segments[0].setheading(90)

    def down(self):
            self.segments[0].setheading(270)

    def left(self):
            self.segments[0].setheading(180)

    def right(self):
            self.segments[0].setheading(0)
```

여기서 뱀의 머리는 몸통을 만나면 게임오버인데 위를 향할 때, 아래키를 누른다면 만나게 되어있음

이 문제를 해결하기 위해 조건문을 통해 각 메소드에 반대 방향인 경우에는 해당 키를 누를 수 없게 설정

```python
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)  
```

각 방향은 최상단에 상수로 만들어놓음

```python
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
```

이렇게 하면 오류를 해결할 수 있다.

## 21 일차
20일차의  snakegame 프로젝트를 이어서 마무리하는 시간을 가져보겠습니다 ㅎ

## 클래스 상속

클래스1, 클래스2가 있을 때, 클래스1에 어떤 메소드, 객체를 만들었다.

클래스2에서도 그 객체와 메소드를 사용하면서 추가로 어떤 메소드를 만들어야 할 때,

우리는 처음부터 시작하는게 아니라, 클래스2에서 클래스1을 상속하여 클래스1의 메소드를 활용할 수 있다.

활용법은 class Fish(Animal): 이런식으로 소괄호 안에 상속받고 싶은 클래스를 입력하면 된다.

```python
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
```

⇒

![image.png](attachment:7c572691-1d95-4dc3-996c-27161ce13243:image.png)

이런식으로 Fish 클래스에서 Animal클래스의 메소드를 사용하며

__init__()을 통해 Fish 객체를 생성하면 Animal클래스의 생성자 또한 실행된다.

```python
class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("Moving in water")
```

추가로 Fish 클래스에 같은 이름의 메소드인 breathe를 만들었다.

그리고 super()를 통해 상속하는 Animal클래스의 breathe를 실행하며, 자신만의 doing this underwater를 출력할수도 있다.

## 뱀이 먹이를 먹었는지 알아내기

### Food 클래스를 만들고 Turtle 클래스를 상속받게 하기

```python
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
```

이렇게 해주면 Food 객체가 생성되면 → Food 객체 = Turtle 객체

이제 self.으로 Turtle 클래스의 메소드를 활용할 수 있음

```python
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
```

생성되면 0.5x0.5크기의 작은 파란색 먹이가 랜덤한 좌표값에 생성됨

이제 food객체를 main.py에서 만들어주면

![image.png](attachment:d59ef1b8-bb88-4083-b194-f9047a188fce:image.png)

이렇게 screen에 먹이가 뿅하고 나타남

### 먹이와의 충돌을 감지

distance라는 Turtle 클래스의 메소드를 활용, 

distance(x, y) → 괄호안의 좌표와 비교함, 여기서 x값만 넣을 수 있는데 그 x값은 turtle 객체를 넣을 수 있음

즉, 객체끼리 비교할 수 있음 → 우리는 뱀의 머리 객체와 먹이 객체를 비교하여 만나있으면 새롭게 먹이를 다시 생성하는 로직을 구상할 수 있음

```python
# 먹이와의 충돌을 감지
    if snake.head.distance(food) < 15:
        print("냠냠냠")
```

![image.png](attachment:e9ca0902-8e50-4474-9a86-2d9766098234:image.png)

이렇게 먹이가 가까우면 냠냠냠을 출력함

먹이 크기가 현재 10픽셀 10픽셀로 이루어져서 10보다는 좀 크게 설정해야 자연스러움

여기에 더해서

```python
# 먹이와의 충돌을 감지
    if snake.head.distance(food) < 15:
        print("냠냠냠")
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
```

아래 먹이를 먹을 때, 다시 위치를 조정해주는 함수를 추가하면 먹은 먹이는 사라지고 새로운 먹이가 생김

이 함수를 Food클래스에 만들어줄거임

```python
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
```

```python
# 먹이와의 충돌을 감지
    if snake.head.distance(food) < 15:
        print("냠냠냠")
        food.refresh()
```

이렇게 하면 간결하게 main.py에서는 실행만 시키면서 Food 클래스에 만들어줄 수 있음

## 점수판을 만들어 점수 기록하기

Turtle 객체를 활용해서 write함수를 사용

```python
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.color("white")
        self.write(f"Score: {self.score}", True, align="center", font=("Arial", 24, "normal"))
```

스코어보드 클래스를 하나 만들어주고 똑같이 main.py에 import해서 객체를 만들어줌

![image.png](attachment:88131435-0294-48aa-97e3-a3dd732bc8ad:image.png)

write함수를 써도 turtle객체의 초반 모양인 화살표는 그대로 남아있게 되는데,

ht()함수를 활용해 모습을 감출 수 있음

이제 이 스코어보드를 맨 상단으로 옮겨야됨

```python
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score: {self.score}", True, align="center", font=("Arial", 24, "normal")
```

write를 하기전에 goto메소드로 객체의 위치를 옮기고 write를 하게되면 해당 위치에 글자를 쓰게됨

![image.png](attachment:b6a51912-78cd-4307-80c7-88c7021118fb:image.png)

### 점수 기록하기

이제 점수를 기록하면 됨

이건 매우 쉽겠죠?

```python
    def increase_score(self):
        self.score += 1
        self.write(self.score, True, align="center", font=("Arial", 24, "normal"))
```

scoreboard 클래스에 해당 메소드를 만들어줌, score를 1올리고 다시 write

```python
# 먹이와의 충돌을 감지
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
```

![image.png](attachment:d7eac61d-3872-46f4-b773-04a69c0f420b:image.png)

이렇게 하면 전에 쓴 write가 안지워지고 겹쳐버림

clear() 함수를 활용해 객체를 초기화할 수 있음,(위치는 안변함)

```python
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
```

이렇게 update_score메소드를 하나 생성하고, 생성자와 increase_score에서는 해당 업데이트 메소드를 활용함, 또한 increase에서는 self.clear()를 통해 이전 wirte를 지움

![image.png](attachment:ca9a1e6f-7669-451b-96aa-682276cd36b0:image.png)

## Game Over

뱀이 벽과 만날 때

뱀의 머리가 몸통과 만날 때

1. 벽에 부딫힐 때

```python
# game over
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
```

![image.png](attachment:52a4821e-c020-4d62-b81b-2d9229d1ce24:image.png)

이렇게 벽에 부딫히면 멈춤

→ 이거에 더해서 벽과 부딫히면 게임오버가 화면에 떠야함

```python
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
```

![image.png](attachment:ecbcde14-f4a5-4f4f-b5ee-c1be16745398:image.png)

점수와 게임오버가 같이 보이게 화면 정 중앙에 옮김

1. 뱀이 자기 몸통과 부딫힐 때

우선 뱀의 길이가 늘어나야 함, 

snake 클래스에서 add_segment, extend 함수를 만들어보자

```python
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position) 
               
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
```

기존의 create_snake 메소드에 있던 함수들을 그대로 사용해 add_segment로 옮겨주고 create_snake는 add_segment를 호출하는 형식을 만들어준다.

이제 extend 메소드는 add_segment를 불러주는데 position을 뱀의 가장 마지막 부분, 즉 -1인덱스의 position을 부르면 됨

```python
    def extend(self):
        self.add_segment(self.segments[-1].position())
```

이렇게 하면 먹이를 먹을 때, extend()를 호출하고 그러면 뱀의 가장 꼬리에서 새로운 객체가 탄생함

```python
# 먹이와의 충돌을 감지
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
```

![image.png](attachment:43ee3053-1697-47b4-a300-9ae73fe8a3fe:image.png)

길이가 늘어난 것을 확인할 수 있음

이제 뱀의 몸통과의 충돌을 어떻게 확인할 것인가

```python
    for segment in snake.segments:
        if (snake.head.distance(segment) != 0) and (snake.head.distance(segment) < 200):
            game_is_on = False
            scoreboard.game_over()
```

이렇게 하면 손쉽게 끝일 줄 알았는데 segments 배열에는 머리도 포함이라 시작하자마자 gameover가 뜸

그래서 0이 아닐 때도 같이 넣어서 조건문을 작성했지만 그래도 똑같이 시작하자마자 gameover

따라서 확실하게 만약에 객체가 같다면 pass하고 나머지들을 비교

```python
# game over
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
```

![image.png](attachment:85665968-c007-4c1d-a4bc-f65ea119914a:image.png)

## 파이썬에서 리스트와 튜플 슬라이싱하기

```python
# game over
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
```

이 부분이 쓸데없이 길다

결국 거리를 알아내고, 그 거리를 비교하는 로직

우리는 segments 배열에서 슬라이싱을 통해 머리를 제외한 나머지 리스트만 가져오고

그 리스트를 비교하면 굳이 2중 조건문을 쓰지 않아도 된다.

key[0:5] → 0부터 5까지의 값을 덩어리로 가져온다, 여기서 중요한건 5는 포함되지 않음

따라서 0,1,2,3,4를 가져오게 되는것

```python
# game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
```

결국 우리는 반복문에서 segmets배열에서 머리를 제외하고 가져온 뒤

한번의 조건문을 통해 바로 game_over 함수를 활용할 수 있음

![image.png](attachment:b27b5058-8f8d-4e76-81bd-65217e11ca5f:image.png)

지금 너무 빨리눌러서 안보이는 것 같은데 머리와 몸통이 겹쳤음

슬라이싱은 다양한 방법으로 활용이 가능함

key[0:5:2]  → 0 뛰고 2 뛰고 4 ⇒ [0, 2, 4]를 가져옴, 이렇게 건너뛰게 할 수도 있음

key[::] → 모두 가져오기

key[1:] → 1부터 모두 가져오기

key[:5] → 처음부터 5(4) 까지 모두 가져오기

key[::2] → 모두 가져오는데 한칸씩 띄워서 가져오기

```python
key = [1,2,3,4,5,6,7,8,9]
print(key[::2])
```

![image.png](attachment:2bf093ba-a0b4-4899-be52-d2e336b7db17:image.png)

튜플 또한 마찬가지로 슬라이싱을 활용 가능함

## 22 일차
## pingpong 게임 프로젝트

2명의 플레이어가 각각의 바를 가지고 있고 가운데에서부터 움직이는 공이 있음

플레이어의 바에 맞으면 반대편으로 공이 이동하며, 바를 넘어서 상대의 벽에 부딫히면 점수를 획득하는 게임

필요 클래스 : player_bar, ball, scoreboard

### 1. main 세팅하기

Screen 객체 생성 및 배경, 크기 등을 지정

```python
from turtle import Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pingpong-game")

screen.exitonclick()
```

### 2. bar 클래스 생성

각 플레이어의 바를 2개 생성

바의 크기는 100 x 20으로 할 예정

바는 위 아래로 움직여야됨, bar1 - (w,s) / bar2 - ( up, down)

```python
from turtle import Turtle

class Bar(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.resizemode("user")
        self.turtlesize(5,1,1)
        self.penup()

    def create_bar1(self):
        self.goto(-380,0)

    def create_bar2(self):
        self.goto(375,0)

    def up_bar(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down_bar(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
```

위의 코드를 player_bar라는 파일에 만들어줌

```python
from turtle import Screen
from player_bar import Bar

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pingpong-game")
screen.tracer(0)

bar1 = Bar()
bar1.create_bar1()

bar2 = Bar()
bar2.create_bar2()

screen.listen()
screen.onkeypress(bar1.up_bar, "w")
screen.onkeypress(bar1.down_bar, "s")
screen.onkeypress(bar2.up_bar, "Up")
screen.onkeypress(bar2.down_bar, "Down")

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
```

main.py에서 위에서 만든 파일을 활용

![image.png](attachment:d91d63f2-b212-47b4-a83b-f712dde8e0a6:image.png)

키 입력에 따라 각각의 바들이 움직이는 것을 확인

### 3. 공 클래스

공 또한 터틀 객체를 원형으로 생성

move라는 메소드를 만들어서 화면에 들어가면 공이 자동으로 오른쪽 상단으로 이동하게 설정

```python
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        new_x = self.xcor() + 20
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

```

![image.png](attachment:33c52b77-df03-4cb2-afde-61078a8fabd1:image.png)

이제 이 공이 바에 부딪치거나, 왼쪽이나 오른쪽 벽에 움직였을 때, 로직을 추가해야 함

```python
# 벽에 부딫혔을 때
    if ball.xcor() > 390 or ball.xcor() < -398:
        ball.reset()
```

```python
    def reset(self):
        self.goto(0,0)
```

이렇게 하면 벽에 부딪칠 때 다시 중앙으로 돌아감

이제 bar에 부딪칠 때를 생각해야 함, 저 터틀 객체에 닿아야 하는데.. 

```python
# 바에 부딫혔을 때
    if bar1.distance(ball) < 20 or bar2.distance(ball) < 20:
        print("바에 닿았음")
```

이렇게 하니까 정 가운데만 인식이 됨, 옆 부분에 닿으면 인식 못하고 벽에 부딪쳐버림

distance를 50으로 완화하고, x축의 거리가 일정 이상일 때 바에 부딪친걸로 봐야할듯

```python
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.position_x = 20
        self.position_y = 10
        self.penup()

    def move(self):
        new_x = self.xcor() + self.position_x
        new_y = self.ycor() + self.position_y
        self.goto(new_x, new_y)

    def reset(self):
        self.goto(0,0)
        self.position_x *= -1
        self.position_y *= -1

    def touch_bar(self):
        self.position_x *= -1

    def touch_wall(self):
        self.position_y *= -1
```

reset으로 game_over가 되면 0,0으로 이동

touch_bar를 하면 x축을 기준으로 반대로 이동

touch_wall를 하면 y축을 기준으로 반대로 이동

```python
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # 벽에 부딫혔을 때
    if ball.xcor() > 390 or ball.xcor() < -400:
        ball.reset()

    # 바에 부딫혔을 때
    if (ball.distance(bar1) < 55 and ball.xcor() < -360)  or (ball.distance(bar2) < 50 and ball.xcor() > 350) :
        ball.touch_bar()

    # 위 또는 아래 벽에 부딪쳤을 때
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.touch_wall()
```

메인의 while로직, 벽에 부딪쳤을 때(game_over) → reset 호출

바에 부딪쳤을 때 → 볼과 바의 거리가 55이하 및 볼의 x좌표가 game_over 이상인 경우

위 또는 아래 벽에 부딪쳤을 때 → 위 아래만 해당하니 ycor을 비교

### 4. 좌표 계산 디테일

![image.png](attachment:33aa28fd-9b05-4b85-a9bc-a6feef313033:image.png)

```python
from turtle import Screen
from player_bar import Bar
from ball import Ball
import time
from sideline import Sideline

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pingpong-game")
screen.tracer(0)

sideline = Sideline()

bar1 = Bar()
bar1.create_bar1()

bar2 = Bar()
bar2.create_bar2()

screen.listen()
screen.onkeypress(bar1.up_bar, "w")
screen.onkeypress(bar1.down_bar, "s")
screen.onkeypress(bar2.up_bar, "Up")
screen.onkeypress(bar2.down_bar, "Down")

ball = Ball()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # 벽에 부딫혔을 때
    if ball.xcor() > 385 or ball.xcor() < -385:
        ball.reset()

    # 바에 부딫혔을 때
    if (ball.distance(bar1) < 54 and ball.xcor() < -360)  or (ball.distance(bar2) < 54 and ball.xcor() > 360) :
        ball.touch_bar()

    # 위 또는 아래 벽에 부딪쳤을 때
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.touch_wall()

screen.exitonclick()
```

```python
from turtle import Turtle

class Sideline(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color('white')
        self.penup()
        self.goto(400,300)
        self.pendown()
        self.goto(-400, 300)
        self.goto(-400, -300)
        self.goto(400, -300)
        self.goto(400,300)
```

위의 sideline은 정확하게 좌표를 지정하기 위해서 Screen 영역에 선을 그림

![image.png](attachment:95cb3ced-4d67-45ea-9909-2b489d627494:image.png)

### 5. 점수 계산

마지막으로 점수를 계산하는 scoreboard 파일을 만들고, 점수가 나면 해당 점수를 올려야됨, 이건 전 프로젝트에서도 했으니 쉽게 할 수 있음

```python
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.goto(position, 200)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial", 24, "normal"))

    def get_score(self):
        self.score += 1
        self.update_score()
```

이렇게 점수판을 만들어주고

```python
left_scoreboard = Scoreboard(-100)
right_scoreboard = Scoreboard(100)
```

main.py에서 위의 scoreboard 객체를 2개 만들어줌, 생성자에서 position으로 위치값을 받으니 파라미터로 x좌표값을 넘겨줌

![image.png](attachment:fe58339b-9b0b-4fdf-8a65-00307fc5cfae:image.png)

그러면 이렇게 각 위치에 점수판이 생김

```python
# 벽에 부딫혔을 때
    if ball.xcor() > 385:
        left_scoreboard.get_score()
        ball.reset()
    elif ball.xcor() < -385:
        right_scoreboard.get_score()
        ball.reset()
```

이제 벽을 부딪치는 로직을 나눠서 각각의 점수를 올려주면

![image.png](attachment:aeb3c20b-8a7a-4ada-a3d5-5dfccbc48f6e:image.png)

이렇게 각각의 점수가 올라가는 것을 볼 수 있음

끝!

## 23 일차
터틀 크로스 프로젝트

다양한 색깔의 차들이 도로를 달리며, 내 turtle객체는 up키 또는 좌우 키를 활용해서 도로를 건너야함

도로를 모두 건너면 다음 단계로 이동하며, 이때 차의 속도가 빨라짐

차와 turtle객체가 부딪치면 game_over가 되며 다시 level1 부터 시작함

해설을 보지 않고 일단 만들어보려고 함

### 1. 설계를 하고 클래스를 생성

![image.png](attachment:3d3bd12a-ca27-447f-a536-fdf0c30e309c:image.png)

회사 짜투리 시간에 진행하고 있어서 폴더 이름이 다를 수 있음

우선 움직이는 차 객체를 만들 car

성공하면 올라가는 단계를 체크하는 level

내가 직접 움직이는 my_turtle

점수를 표시하는 score

screen의 범위를 눈으로 파악하기 위해 만든 sideline

### 2. screen 구성 및 myturtle 객체 생성

스크린은 x,y ⇒ 600,400으로 설계함(너무 크면 안좋을 것 같아서)

![image.png](attachment:f1adbe18-aa5a-4260-9c36-795949b1db86:image.png)

기본 객체 크기는 20x20이므로 객체의 좌표는 0, 190이 되어야함(아래에 붙어있다는 기준으로)

```java
# 길건너기 게임 프로젝트
from turtle import Screen
from my_turtle import MyTurtle
from sideline import Sideline
from road import Road

screen = Screen()
screen.setup(width=600, height=420)
screen.title("turtle cross game")
screen.tracer(0)

# 내 본체
myCharacter = MyTurtle()

# 스크린 범위 확인
sideline = Sideline()

# 도로 선 그리기
position_y = -180
for _ in range(13):
    road = Road(position_y)
    position_y += 30

is_game_on = True

while is_game_on:
    screen.update()

screen.exitonclick()
```

main은 위의 코드로 구성함

```java
from turtle import Turtle

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(0,-200)
```

my_turtle은 위의 코드로 구성했으며 진행하면서 더 추가할 예정임

```java
from turtle import Turtle

class Sideline(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color('black')
        self.penup()
        self.goto(300,210)
        self.pendown()
        self.goto(-300, 210)
        self.goto(-300, -210)
        self.goto(300, -210)
        self.goto(300,210)
```

sideline은 위의 코드로 구성했으며 22일차에 이미 구성했었던 코드를 그대로 reusing함

### 3. 차 객체 만들기

y폭은 400이다, 객체의 크기는 20이다, 

도로의 크기를 30으로 잡고 차의 크기도 20으로 잡는다.

```java
from turtle import Turtle

class Road(Turtle):
    def __init__(self, position):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(300, position)
        self.setheading(180)
        for _ in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(10)
```

도로 선을 그리는 객체를 만들었다.

```java
# 도로 선 그리기
position_y = -180
for _ in range(13):
    road = Road(position_y)
    position_y += 30
```

main에 해당 코드를 추가하여 screen에 표시했는데 

![image.png](attachment:8286cf79-f966-48cf-b9a0-1e011a946115:image.png)

왜그런지는 모르겠지만 위 아래에 10정도가 부족해진다.

아마 선의 폭이나 그런게 작용해서 20정도가 차지하는 것 같다. 따라서 크기를 420으로 늘린 후 좌표를 다시 설정(위의 코드들도 수정함)

![image.png](attachment:2fb29e84-f590-44d9-b0ba-091e059f02bb:image.png)

딱 맞는 모습을 볼 수 있다

이제 차량이 생성되는 곳을 좌표로 지정해야 한다. 

y값은 도로의 정 중앙 ex) -180~-150의 중간 → -165가 y좌표

차는 총 12구간에 나타나므로 -165 += 30을 해주면서 차의 좌표를 만들어줄 수 있다.

라고 했는데 시작파일을 줬었네, 다시 처음부터 시작

![image.png](attachment:02fb2670-0569-49ca-9526-673103955a21:image.png)

이렇게 4가지 파일이 주어졌고 안에 들어있는 코드는 뭐 없었음, 간단한 클래스 이름과, 상수들이 적혀있음

### 1. player.py

```python
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

```

먼저 내가 움직이는 player 객체에서 생성자로 내 거북이를 만들어주고, 스타트 위치로 옮겨줌

up 키를 누르면 실행되는 move 함수를 만들어주고, finish 라인에 도착하면 시작 라인으로 돌아가게 설정

### 2. main.py

```python
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

```

메인에서는 실행에서 필요한 screen을 정의해주고 up키를 누르면 앞으로 가게 리스너이벤트를 등록해줌

1번에서 만든 player 객체를 만들어서 움직이는지 확인 완료

![image.png](attachment:83302fe5-63ed-4ff1-bbc4-31f607ed65fd:image.png)

### 3. car_manager.py

차량은 시작라인을 제외하고 무작위 y축에 생성되며 색깔은 주어졌음

```python
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.resizemode("user")
        new_car.shapesize(1, 2, 1)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(320, random.randint(-260, 260))
        self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
```

우선 클래스 생성자에 배열을 하나 만들어줌, 생성된 car 객체들은 모두 저 배열에 들어감

car 객체를 생성하는 메소드를 만든 후 마지막에 append로 리스트에 객체를 넣어줌

drive메소드에서 반복문을 통해서 배열에 있는 모든 차들을 앞으로 이동시킴

![image.png](attachment:dcdbbb17-89bc-4757-90fc-de0ae1ffb110:image.png)

이건 깰 수가 없음, 차량의 속도를 줄일수도 있지만 확률을 통해 차량의 생성을 억제할 수 있음

```python
    def create_car(self):
        dice = random.randint(1,6)
        if dice == 1:
            new_car = Turtle("square")
            new_car.resizemode("user")
            new_car.shapesize(1, 2, 1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(320, random.randint(-260, 260))
            self.all_cars.append(new_car)
```

1~6 사이의 숫자를 랜덤으로 뽑고, 1일 때만 객체를 생성함(1/6 확률)

![image.png](attachment:a6fae847-f570-4888-a3ea-f8cb5e5c7fdc:image.png)

나이스함

### 4. 충돌했을 때

만약 거북이와 차의 거리가 20보다 가까우면 반복문을 종료함

```python
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.drive()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
```

main의 반복문에 맨 마지막의 for문을 추가함

### 5. 결승점 도달 시 속도 up, level up

```python
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
```

player.py에 해당 메소드 생성

go_to_start는 따로 빼줌, 레벨이 올라가면 결승점에 도달해도 다시 안돌아가는 버그가 있길래 따로 빼준거

y좌표가 결승점보다 크면 True를 반환함

```python
    def __init__(self):
		    self.all_cars = []
		    self.car_speed = STARTING_MOVE_DISTANCE
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
```

car_manager.py 파일에 생성자에 차의 속도를 나타내는 변수를 추가하고, level_up이라는 메소드를 추가해, 차의 스피드를 더해줌

```python
    if player.finish():
        player.go_to_start()
        car_manager.level_up()
```

이제 마지막으로 main의 반복문 안에 해당 구문을 추가하면 차의 속도가 level이 올라갈수록 빨라짐

### 6. level과 game over 표시하기

이건 쉽죠

```python
from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.ht()
        self.penup()
        self.goto(-200,250)
        self.color('black')
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level : {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
```

스코어보드 파일에 생성자, Level을 갱신 해주는 update_score, 게임이 종료됐을 때, 알려주는 game_over 메소드를 생성함

```python
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.score += 1
        scoreboard.update_score()
```

기존의 main에 있던 로직에서 scoreboard 메소드들을 추가하면 끝

![image.png](attachment:767b90df-ff41-41d6-ba50-a469185a9373:image.png)

## 23일차 추가
길 건너기 게임에서 다음의 사항을 포함 시킴

### 1. 왼쪽, 오른쪽, 뒤로가기 추가

```python
# 이벤트 리스너 등록
screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkeypress(player.left_move, "Left")
screen.onkeypress(player.right_move, "Right")
screen.onkeypress(player.back_move, "Down")
```

```python
class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.player_speed = 12
        self.FINISH_LINE = 280
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(START_POSITION)

    def move(self):
        self.setheading(90)
        self.forward(self.player_speed)

    def finish(self):
        self.goto(START_POSITION)

    def left_move(self):
        self.setheading(180)
        self.forward(self.player_speed)
    def right_move(self):
        self.setheading(0)
        self.forward(self.player_speed)
    def back_move(self):
        self.setheading(270)
        self.forward(self.player_speed)
```

이건 뭐 그냥 추가만 하면 되는거라 바로 진행했다.

### 2. Item 기능 추가

1. 화면에 랜덤한 위치에 확률(1/500)에 따라 아이템이 생성됨
2. 아이템은 산호색 원형으로 지정했고, distance가 15미만이면 먹어진 것으로 정함
3. 아이템의 종류는 3가지, 내 속도 up, 차 속도 down, 화면의 모든 차 clear

```python
from turtle import Turtle
import random as rd

ITEM = ["speed_low", "clear", "speed_up"]

class EventItem:
    def __init__(self):
        self.all_item = []

    def create_item(self):
        dice = rd.randint(1,6)
        if dice == 1:
            new_item = Turtle("circle")
            new_item.color("cyan")
            new_x = rd.randint(-280,280)
            new_y = rd.randint(-250,250)
            new_item.penup()
            new_item.goto(new_x,new_y)

            new_item.event_type = rd.choice(ITEM)
            self.all_item.append(new_item)

```

이벤트 클래스를 만듦, 

지금 dice가 1/6으로 되어있는데 검증 때문에 저렇고 6을 500으로 바꿔주면 됨

아이템은 랜덤한 x좌표 280~280, y좌표는 차의 좌표에 맞게 250~250사이에 생성됨

마지막으로 append하기 전에, event_type이라는 속성을 만들고 거기에 item 3개중에 하나를 랜덤으로 넣음

다음으로 main에 아이템과 닿았을 때 상황을 코드로 생성

```python
    for it in item.all_item:
        if it.distance(player) < 15:
            if it.event_type == "speed_up":
                player.speed_up_item()
            elif it.event_type == "speed_low":
                car.speed_low_item()
            else:
                car.clear_item()
            it.ht()
            item.all_item.remove(it)
```

아이템의 위치와 내 객체의 위치가 15미만인 경우에서 조건문을 나눠 아이템의 종류가 무엇인지 판별

각각의 아이템에 따라서 함수들이 실행됨

함수를 실행했다면 아이템의 모습을 숨기고, 아이템 리스트에서 해당 아이템을 삭제하여 먹은 것 처럼 UI를 설정함

SpeedUp

```python
from turtle import Turtle

START_POSITION = (0, -280)

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.player_speed = 12
        self.FINISH_LINE = 280
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(START_POSITION)

    def move(self):
        self.setheading(90)
        self.forward(self.player_speed)

    def finish(self):
        self.goto(START_POSITION)

    def left_move(self):
        self.setheading(180)
        self.forward(self.player_speed)
    def right_move(self):
        self.setheading(0)
        self.forward(self.player_speed)
    def back_move(self):
        self.setheading(270)
        self.forward(self.player_speed)

    def speed_up_item(self):
        self.player_speed += 1
```

맨 아래 함수이며, 이걸 적용하기 위해 self.player_speed 속성을 생성하고, 아이템을 먹을 경우 +1

거리가 +1 늘어나는 것 이지만, 실제 게임 체감으로는 속도가 올라간 느낌

SpeedDown/Clear

```python
from turtle import Turtle
import random

COLORS = ["red","orange","yellow","green","blue","indigo","purple"]
INCREASE_SPEED = 5

class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_car(self):
        dice = random.randint(1,6)
        if dice == 1:
            new_car = Turtle("square")
            new_car.resizemode("user")
            new_car.shapesize(1,2,1)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.penup()
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += INCREASE_SPEED

    def speed_low_item(self):
        self.car_speed /= 2

    def clear_item(self):
        for car in self.all_cars:
            car.ht()
        self.all_cars.clear()
```

두 함수는 모두 Car 클래스에 있음, 우선 클리어부터 설명하자면

clear_item은 반복문을 통해서 아이템을 먹은 당시에 리스트에 있는 모든 car 객체들의 모습을 숨기고

당시의 리스트를 빈 리스트로 만듦, 이후에 생기는 객체는 적용 안됨

speed_low_item의 경우는 위에서 했던 speed_up_item과 동일함, 다만 car 객체의 경우 level이 올라가면 속도가 +5씩 빨라지기에 + 또는 -로 설정해버리면 초반에는 효율이 너무 좋고, 뒤에서는 너무 미비함

따라서 현재 속도의 절반으로 설정

이렇게 추가 개발을 하고 게임을 해봤는데 재밌음 ㅋㅋ

## 24 일차
# 뱀 게임 수정하기

### 뱀 게임에 최고 점수 추가하기

```python
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()
```

해당 클래스에 highscore라는 속성을 추가함

원래는 gameover였지만 이제는 게임이 끝나면 바로 새 게임이 시작되므로 reset으로 바꿈

reset에는 본래 지금의 점수가 최고점수라면 highscore에 score를 넣어줌

reset이므로 현재의 score는 0으로 넣어줌

마지막으로 update를 실행하며, update에는 기존의 score와 highscore를 보여주도록 함

![image.png](attachment:8a9072ba-a913-4fe9-a99c-2c04c2b29ba8:image.png)

현재는 죽어도 다시 시작되는 로직은 안만들었기에 저렇게 부딪치면 멈추고 HighScore에 현재 점수가 반영되는 것을 볼 수 있음

### 게임 지속하기

```python
from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.go_home()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        # 뱀 방향 바꾸기
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_home(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

```

go_home이라는 메소드를 만들어서, 객체를 새로 생성하는(생성자가 아닌) 메소드를 만들어줬음

코드가 겹치니까 생성자에 있던 코드는 해당 함수로 교체함 그리고 실행하면

![image.png](attachment:96d997ec-b582-4ca3-883d-d0c8f6d79a03:image.png)

이렇게 기존의 거북이가 사라지지 않음, 

```python
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]   
   
    def go_home(self):
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
```

따라서 segments.clear()를 통해 해결하였고, 게임을 플레이하는데 잔 오류가 생겨서 생성자도 그냥 입력해놈

![image.png](attachment:5398f3ff-e33a-4e71-8738-d706bbd2d22c:image.png)

게임은 잘 작동하는데 여전히 안사라짐, 배열에서 없애는것 만으로는 안되나봄

ht()활용해서 모습을 숨겨야겠음

```python
    def go_home(self):
        for segment in self.segments:
            segment.ht()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
```

지금은 게임을 종료하면 다시 highscore가 0으로 돌아간다.

어떻게하면 다시 게임을해도 최고점수가 기억되게 할 수 있을까

### With 키워드 사용 방법

![image.png](attachment:4a7c9af9-d91a-4ef7-8484-847c9398e43e:image.png)

my_file에는 Hello my name is gyj를 적어둠

```python
file = open("my_file.txt")
contents = file.read()
print(contents)
```

main.py에 위의 코드를 적고 실행해주면 해당 파일을 읽어서 contents에 내가 적은 값을 넣어줌

![image.png](attachment:2c10f0fe-c904-45e4-8a7f-93318173087d:image.png)

파일을 열고 하고싶은 코드를 작성한 후 마지막에는 항상 file.close()로 닫아줘야함

이유는 리소스를 낭비하지 않기 위해서임

```python
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
```

with 키워드를 이용하면 file이름을 붙여서 불러줄 수 있음

전의 코드와 같아 보이지만 다른점은 with키워드를 사용하면 마지막에 닫아줄 필요가 없다는거임

with는 들여쓰기의 구문이 끝나면 자동으로 file을 닫아줌

```python
with open("my_file.txt", mode="w") as file:
    file.write("New text")
```

파일에 새로운 text를 쓰기 위해서는 mode를 w로 변경해줘야 함

다만, w로 변경하면 읽는게 안됨(기본은 r모드)

![image.png](attachment:fa4c9846-5f7d-4b36-afb0-358bfac236d3:image.png)

코드를 실행해주면 파일에 새로운 text가 입력된 것을 볼 수 있음

만약에 기존에 있던 글에서 더해서 쓰고싶다면

```python
with open("my_file.txt", mode="a") as file:
    file.write("New text2")
```

모드를 a로 변경해주면 됨

![image.png](attachment:850d5a73-231f-446f-821c-a7fd12bed00f:image.png)

실행 후 확인하면 새로운 글이 써진 것을 볼 수 있고, 줄바꿈 \n도 가능함

```python
with open("new_file.txt", mode="w") as file:
    file.write("HI My new File")
```

새롭게 파일을 만들고 싶다면 새롭게 만들고싶은 파일 이름을 적고, mode를 w로 해주면 됨

![image.png](attachment:9e61f375-dd0f-4ee0-8299-bef8fb59cc99:image.png)

새로운 파일이 생성됐으며 내가 쓴 글이 적용된 것을 볼 수 있음

이제 뱀 프로젝트로 돌아가서 파일에 최고 점수를 기록하고 파일에 있는 최고 점수를 읽어서 값을 넣어줄 수 있음, scoreboard를 생성할 때, 파일에서 최고점수를 읽고 값을 대입하는거임

### 뱀 게임에서 파일에 최고 점수 읽고 쓰기

![image.png](attachment:06972dd5-5e0d-4820-a6f2-45394ec213b2:image.png)

우선 highscore_text라는 파일을 만들어줌

```python
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore_text.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 260)
        self.update_score()
```

기존에 highscore를 0으로 정의했던 코드를 파일에서 점수를 읽어오는 코드로 변환함

```python
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore_text.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score()
```

reset에서 최고점수를 바꿔주고 해당 점수를 파일에 기록함

![image.png](attachment:30e826ec-9a51-4cb3-aac2-6768d9c3fb36:image.png)

우선 highscore를 3으로 바꿔준 후, 종료하고 다시 실행해보면

![image.png](attachment:3a370057-a981-4286-8426-7951e7fd1378:image.png)

여전히 최고점수가 3으로 남아있는 것을 확인할 수 있음

### 상대 및 절대 파일 경로에 대한 이해

C:\Users\ernmq\PycharmProjects

Root 폴더 → C: (c드라이브)

내가 위에서 만든 highscore.txt의 경로는 

C:\Users\ernmq\PycharmProjects\day20\highscore_text.txt 

이 경로가 해당 파일의 절대 경로이다. 즉 내 파일의 근원부터 현재 어디 폴더에 위치하는지 나타내는 경로

그럼 만약에 내가 day20 안의 example이라는 폴더에 위치해 있다고 가정해보자

그러면 내가 highscore_text.txt에 어떻게 접근할 수 있을까? → ../highscore_text.txt 이렇게 접근이 가능함

../ → 내 상위 경로를 가리킴(day20), 그 안에 있는 해당 파일에 접근하겠다는 의미임

그렇다면 프로젝트에서 처럼, 내가 같은 폴더 안의 파일을 읽고 싶은데 절대 경로로 파일을 읽고 싶다면

main.py에서 file.txt를 읽는다 → ./file.txt 로 작성할 수 있다. 하지만 같은 디렉토리에 있으므로 생략이 가능하다. 따라서 그냥 file.txt로 읽는다

![image.png](attachment:bc3d3646-3a41-44ed-aeac-8d91a9190c77:image.png)

기존에 파이썬에 있던 txt 파일들을 바탕화면으로 옮겨줬다

![image.png](attachment:75727abf-da16-45c3-a195-49d14c28d74c:image.png)

해당 파일의 속성을 들어가보면 파일의 절대경로를 알 수 있다.

![image.png](attachment:f03e1973-31ed-4da7-ad89-789ceb260845:image.png)

파이참으로 돌아가서 해당 main을 실행하면 오류가 발생하는것을 볼 수 있다.

왜냐면 해당 디렉토리에 파일이 없어서 읽을 수 없다.

![image.png](attachment:f6de3d2c-252f-48e0-bea8-6a17479f9059:image.png)

이렇게 절대 경로를 통해서 파일을 읽을 수 있다.

```python
with open(r"../../OneDrive\바탕 화면\new_file.txt") as file:
    #C:\Users\ernmq\PycharmProjects\day24\main.py
    contents = file.read()
    print(contents)
```

또한 이렇게, 현재 아래 main.py의 경로를 보고 ../../을 통해 ernmq 폴더로 이동 후 바탕 화면 위치를 찾아서 해당 파일을 읽을 수도 있다.

### 메일 머지 프로젝트

![image.png](attachment:401aec77-0f3f-4819-a227-00b082d91024:image.png)

```python
Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Angela

```

편지 예시

```python
Aang
Zuko
Appa
Katara
Sokka
Momo
Uncle Iroh
Toph
```

편지 쓸 친구들, 편지가 저장될 경로는 Output/ReadyToSend 안에 넣어야됨

우선 해당 이름들을 배열로 생성해야됨

![image.png](attachment:fd33a9b9-5084-4eed-894d-fc071faf2f01:image.png)

파일 경로를 읽어서 해당 file안에 있는 이름들을 \n을 기준으로 spilt하여 배열로 만듦

```python
with open("Input/Letters/starting_letter.txt") as letter_default:
    letters = letter_default.read()
```

미리 만들어진 편지 틀을 파일에서 읽어서 letters에 담음

```python
for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}", mode='w') as letter:
        letter.write(letters.replace('[name]', f"{name}"))
```

마지막으로 write를 하는데, 해당 기본 편지 틀에 있는 [name]을 현재 반복문의 name으로 바꿔 편지를 작성함

![image.png](attachment:216631a9-ac46-496f-b655-8fe54d76d817:image.png)

![image.png](attachment:e9b3b5de-5e68-4a74-bda8-dfc99baac96c:image.png)

이렇게 편지에 각각의 이름이 들어갈 수 있음

### 강의 해설

```python
with open("Input/Names/invited_names.txt") as name:
    names = name.readlines()
    print(names)
```

![image.png](attachment:fe4919ce-867f-44a7-a694-ed0dddfeb49a:image.png)

```python
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        print(new_letter)
```

![image.png](attachment:b2b81881-d572-4763-ab40-69b38cc1a011:image.png)

\n이 들어가 있어서 줄이 띄어진 것이 보임

```python
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        print(stripped_name)
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
```

![image.png](attachment:c20079bd-9f53-4a52-904d-611ee35690c6:image.png)

strip()을 활용하면 앞 뒤의 공백을 모두 없애줌(\n까지 없애주나봄)

![image.png](attachment:b930378a-b62f-4c32-ba76-e5a2fab7d5fc:image.png)

후에 new_letter를 확인해보면 정상적인 편지를 확인할 수 있음

```python
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}", mode="w") as completed_letter:
            completed_letter.write(new_letter)
```

후에 write는 로직은 동일한데 같은 반복문 안에서 처리하는게 달랐음

![image.png](attachment:cf08f6e1-3a98-4626-884f-b9a59df28773:image.png)

```python
Dear Momo,

You are invited to my birthday this Saturday.

Hope you can make it!

Angela

```

실행해주면 편지들이 생성되며, 내용도 잘 나온것을 확인할 수 있음

내 방식대로 해결해본 후에 해설을 보면, 새로운 함수들을 배우면서 깨닫게 더 큼

새로운 함수를 활용해서 코드를 다시 짜보면 확실히 내 코드보다 깔끔하며 가독성도 더 좋아보임

## 25일차
## CSV 파일을 읽어서 데이터화

```python
# with open("weather_data.csv", mode='r') as weather:
#     data.append(weather.readlines())
#     print(data)

import csv

with open("weather_data.csv", mode='r') as weather:
    data=(csv.reader(weather))
    for _ in data:
        print(_)
```

24일차에 배웠던 파일을 읽는 with open을 이용해 csv파일을 읽고

파이썬에 기본적으로 있는 csv 라이브러리를 활용해서 간편하게 리스트로 만들 수 있다

![image.png](attachment:8d567dc9-6f16-4aac-8b11-6e0a4a0332fc:image.png)

### temperatures 리스트 만들기

현재 만든 리스트를 활용해서 온도만 따로 뺀 정수형 리스트를 만들어야 함

```python
import csv

with open("weather_data.csv", mode='r') as weather:
    data=(csv.reader(weather))
    temperatures = []
    for temperature in data:
        if temperature[1] == 'temp':
            continue
        temperatures.append(int(temperature[1]))
    print(temperatures)
```

이렇게 만들어볼 수 있다.

만약에 데이터가 간단하지 않고 매우 복잡하다면, 코드가 훨씬 더 어려워지는데

이러한 데이터를 간단하게 읽고 데이터로 변환하려면 Pandas를 활용해야 한다.

## Pandas

```python
import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
```

![image.png](attachment:ee43e44b-84f7-4889-96ce-fd70e5e43fa6:image.png)

ㅋㅋ지린다, 이래서 판다스판다스 하는구나 3줄로 끝나버리네

![image.png](attachment:0ed802bc-3712-47ec-ade4-79e8598d6153:image.png)

위 사진처럼 특정 컬럼만 보고싶다면 `print(data["temp"])` 이렇게 대괄호 안에 컬럼을 입력하면 됨

판다스는 첫 번째 줄을 각 열의 제목으로 사용하기 때문에 손쉽게 사용할 수 있음

## 행과 열

```python
print(type(data))
print(type(data["temp"]))
```

![image.png](attachment:551454ea-6f50-4de9-83af-042ccc429c1f:image.png)

행과 열을 가지는 표 형식의 데이터는 판다스에서 DataFrame이라는 클래스이며

해당 컬럼에 대한 각 데이터들을 Series 클래스임

즉, 전체 표는 데이터프레임, 각 열(날씨, 상태, 요일)은 시리즈임

### 판다스의 여러 API 활용

```python
data_dict = data.to_dict()
print(data_dict)
print(data_dict["day"])
print(data_dict["temp"])
```

![image.png](attachment:5663d7e9-73a8-4e83-907b-fd897c5abc91:image.png)

리스트 형태를 Dictionary형태로 바꿀 수 있음

```python
temp_list = data["temp"].to_list()
print(temp_list)
print(type(temp_list))
```

data[”temp”] → 시리즈 타입

이 시리즈 타입을 list 타입으로 바꿔줄 수 있음

![image.png](attachment:07c7ebca-5a4e-487a-a624-7fc220fff3c0:image.png)

값은 동일함

### 온도 열에서 평균 온도 구하기

python에서는 수학적인 값들을 계산할 때, numpy라는 라이브러리를 활용함

```python
import numpy

avg = numpy.average(temp_list)
print(avg)
```

![image.png](attachment:642c6960-8236-4b09-a36c-5741fa357715:image.png)

평균값 이외에도 최소, 최대 등등 다양한 함수들이 있음

numpy를 사용하지 않아도 판다스 내부 함수에 평균값을 계산하는 메소드가 있음

```python
avg = data["temp"].mean()
print(avg)
avg2 = temp_list.mean()
print(avg2)
```

avg는 series 타입이며 avg2는 list타입임

![image.png](attachment:c90897b7-19e7-4065-87b4-859f208d69f1:image.png)

당연하지만 list에는 평균값을 구하는 메소드가 없어서 오류가 발생하며, series 타입은 잘 작동함

### 최댓값 최솟값

```python
data_temp = data["temp"]
print(data_temp.max())
print(data_temp.min())
```

![image.png](attachment:e953a9c3-2fd2-490a-9865-df46d6e42e72:image.png)

### 행 데이터 출력

```python
# 행 데이터 구하기, 월요일
data_monday = data[data.day == "Monday"]
print(data_monday)
```

![image.png](attachment:241917d9-f5e1-469d-8459-ef5e9d935204:image.png)

데이터프레임(data)에서 data.day(day컬럼) 이 월요일인 값을 꺼냄

### 온도가 가장 높은 데이터가 있는 행을 구하기

```python
# 온도가 가장 높은 데어티가 있는 행을 구하기
data_temp_max = data[data.temp == data.temp.max()]
print(data_temp_max)
```

![image.png](attachment:d88796d2-c4ad-4014-9434-262d7ff3fe36:image.png)

### dict to dataframe

```python
data_dict = {
    "students": ["Amy", "Jack", "Mike"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
```

![image.png](attachment:690dabc9-2b8c-48f6-8660-88d365257502:image.png)

이렇게 딕셔너리 형태의 값을 DataFrame으로 바꿔줄 수 있음

### 새로운 csv 파일 만들기

```python
data_dict = {
    "students": ["Amy", "Jack", "Mike"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
```

![image.png](attachment:4759039b-30c8-42bc-812c-4aaac37a7431:image.png)

이렇게 to_csv를 활용해서 새롭게 파일로 추가할 수 있음

## 판다스로 하는 데이터 분석

![image.png](attachment:19598a91-8c23-443f-a881-182cc4f8b823:image.png)

미국에 있는 다람쥐의 생태분석 자료임

이 자료를 활용해서 회색 다람쥐는 얼마나 있는지 확인

```python
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color = len(data[data["Primary Fur Color"] == "Black"])

dict_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color, cinnamon_color, black_color]
}

data_color = pandas.DataFrame(dict_data)
data_color.to_csv("color_data.csv")
```

1. csv 파일 읽어서 확인
2. data[data[”primary Fur Color”] == Gray] → 마지막에 data[] 해주는거 주의!!
3. 각 색깔별로 DataFrame을 확인 후 len을 활용해 총 컬럼의 길이(개수) 추출
4. dict 형태 만들기, 열 → 색, 개수 + [행 값들]
5. dict 형태를 DataFrame 형태로 만들고 Csv 파일로 만들기

## 미국 주 이름 맞추기 게임 프로젝트

```python
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

screen.exitonclick()
```

![image.png](attachment:d43f8f47-16e1-4a18-91ea-8ebd3c18ffea:image.png)

이렇게 addshape 함수를 통해서 gif파일로 배경에 그림을 넣을 수 있다

```python
import turtle

screen = turtle.Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
```

get_mouse_click_coor 함수는 클릭한 위치의 x와 y좌표를 출력해주는 함수이며

onscreenclick는 클릭할 때 실행되는 이벤트 리스너 함수이다. 

이벤트 리스너로 클릭 시에 get_mouse_click_coor가 실행되며 해당 좌표가 출력됨

mainloop는 screen화면이 클릭해도 사라지지 않게 하기 위한 메서드이다

![image.png](attachment:2f7c18df-d177-4a4c-a160-84bf60ae275c:image.png)

이제 주들의 중심 좌표를 알았다면 csv파일에 정리할 수 있다(사실 파일로 이미 받았음)

![image.png](attachment:4f022c68-c08c-49f9-8670-29e8a42d4aa2:image.png)

```python
import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct",
                                    prompt="What's another state's name?").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.ht()
        t.penup()
        t.color("black")
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)

screen.exitonclick()
```

answer를 통해 input값으로 사용자에게 미국 주를 맞추라고 던져주고, 값을 받음(tilte로 앞글자만 대문자)

while문은 50개 주를 모두 맞출 때 까지 반복됨

그 다음 if문을 통해서 사용자가 입력한 값이 csv파일에 있는 주 이름의 값과 같은지 확인하고 있다면

turtle.write 메서드를 통해서 해당 위치에 주 이름을 입력함

여기서 x와 y좌표가 필요하므로, 해당 주 이름의 열 데이터를 뽑아서 x와 y값을 뽑음

```python
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_file")
        break

    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.ht()
        t.penup()
        t.color("black")
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)
```

마지막으로 같은 값을 입력했을 때는 score가 안올라가게 설정했으며

Exit를 입력 시 while문을 빠져나오면서 못맞춘 값들을 새 파일에 저장함

## 26 일차
목록과 디렉토리에 관한 이해

## 리스트 컴프리헨션을 통해 리스트 생성하기

```python
# 기존의 코드
numbers = [1,2,3]
new_list = []

for n in numbers:
    add_1 = n+1
    new_list.append(add_1)

print(new_list) # [2,3,4]

# 리스트 컴프리헨션을 사용하는 방법
new_numbers = [item+1 for item in numbers]
print(new_numbers) # [2,3,4]
```

기존에 여러 줄로 복잡하게 구성한 코드를 리스트 컴프리헨션을 활용해 1줄로 생성함

기본구조는 [new_item for n in list] 

list : 기존의 리스트

n : 기존의 리스트 안의 원소값

new_item : 새로운 리스트의 원소값(보통 n을 활용하여 다른 값으로 변환함)

리스트 컴프리헨션이라고 해서 무조건 리스트만 되는 것은 아님, 문자열 또한 가능함

```python
name = "Angela"
new_name = [letter for letter in name]
print(new_name) # ['A', 'n', 'g', 'e', 'l', 'a']
```

이렇게 문자열의 각 자리를 리스트에 담을 수 있으며, upper()를 활용해 모두 대문자로 바꿔 리스트에 넣는 등 활용이 가능함

이렇게 리스트 컴프리헨션에서 활용이 가능한 나열된 형태를 Sequences라고 함

시퀸스에는 list, range, string, tuple 등이 있음

### range(1~4)를 활용하여 2배의 범위를 가진 리스트를 생성하기

```python
ex_1 = [n*2 for n in range(1,5)]
print(ex_1) # [2,4,6,8]
```

매우 쉽군

### 조건부 리스트 컴프리헨션

new_list = [new_item for item in list if test]

if조건을 활용할 수 있다.

```python
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie" ]
# 4글자 이하로 구성
new_names = [new_name for new_name in names if len(new_name) < 5]
print(new_names) # ["Alex", "Beth", "Dave"]
```

![image.png](attachment:fc47e39f-dbf0-4319-8c24-08076180e5e5:image.png)

### 5글자 이상의 이름만 가져오며, 모두 대문자로 변환

```python
# 5글자 이상, 모두 대문자
ex_2 = [new_name.upper() for new_name in names if len(new_name) >= 5]
print(ex_2) # ['CAROLINE', 'ELANOR', 'FREDDIE']
```

## 제곱수 실습

**제곱수 실습**

리스트 컴프리헨션을 사용하여 `squared_numbers`라는 새 리스트를 만들 것입니다. 이 새 리스트에는 `numbers` 리스트의 각 숫자가 제곱된 숫자가 포함되어야 합니다.

예를 들어,

`4 * 4 = 16`

4의 제곱은 16입니다.

- *절대** `numbers`리스트를 직접 수정하지 마세요. 루프 대신 **List Comprehension**을 사용해보세요.

목표 출력:

`[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]`

```python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num*num for num in numbers]
print(squared_numbers)
```

![image.png](attachment:f183780e-5bad-4cf8-ad3d-bf56ee8718b7:image.png)

## 짝수 필터링 실습

**짝수 필터링 실습**

이 list comprehension 연습에서 여러 숫자 중에서 짝수를 걸러내기 위해 list comprehension을 사용하는 연습을 할 것입니다.

먼저 list_of_strings를 `numbers`라는 정수 리스트로 변환하기 위해 list comprehension을 사용하세요.

그런 다음 다시 리스트 컴프리헨션을 사용하여 `result`라는 새 리스트를 만드세요.

이 새 리스트는 `numbers`리스트에서 짝수만 포함해야 합니다.

다시 한 번 루프 대신 Python의 **List Comprehension**을 사용해보세요.

```python
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num%2 == 0]
print(result)
```

![image.png](attachment:6725d79d-efb3-4faf-aa14-451a0272426f:image.png)

## 데이터 중첩

**데이터 중첩**

💪 이번 실습은 어렵습니다. 💪

file1.txt와 file2.txt 안을 살펴보세요. 각 파일에는 각각 새 줄에 하나의 숫자가 포함되어 있습니다.

file1과 file2에 공통으로 있는 숫자를 포함하는 `result`라는 리스트를 만들 것입니다.

예를 들어, file1.txt에 다음이 포함되어 있다면:

1

2

3

그리고 file2.txt에 다음이 포함되어 있다면:

2

3

4

result = [2, 3]

중요: 출력은 문자열이 아닌 정수의 리스트여야 합니다!

반복문 대신 **리스트 컴프리헨션**을 사용해보세요.

```python
with open("file1.txt") as file1:
    list_1 = [string.strip() for string in file1.readlines()]

with open("file2.txt") as file2:
    list_2 = [string.strip() for string in file2.readlines()]
    
# 정수형 리스트화
new_list_1 = [int(num) for num in list_1]
new_list_2 = [int(num) for num in list_2]

# 중복값만 리스트에 넣기
result = [num for num in new_list_1 if num in new_list_2]

print(result)
```

![image.png](attachment:7631d7a6-7d89-4a36-8066-ee715515231c:image.png)

## 미국 주 게임에 List 컴프리헨션 적용시키기

```python
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_file")
        break
```

사용자가 Exit를 입력하면 반복문을 통해 맞추지 못한 주의 이름이 새로운 파일에 써지며 생성되는 코드인데 이 코드를 리스트 컴프리헨션을 통해 짧게 수정할 수 있다

```python
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_file")
        break
```

## 딕셔너리 컴프리헨션

new_dict = {**new_key**:**new_value** for **item** in **list**}

→ new_dict = {**new_key**:**new_value** for (**key**, **value**) ****in **dict.itmes()**}

→ new_dict = {**new_key**:**new_value** for (**key**, **value**) ****in **dict.itmes()** if **test**}

```python
# 딕셔너리 컴프리헨션
import random
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)
```

![image.png](attachment:fd3b6680-6e75-4bea-be8e-933106227227:image.png)

```python
# 딕셔너리를 활용한 컴프리헨션
passed_students = {key:value for(key, value) in dict.items(students_scores) if value > 60}
print(passed_students)
```

![image.png](attachment:ad8e25cd-b5f0-43cf-9d9d-eb52b08e2452:image.png)

딕셔너리를 활용할 때는 dict.items(dictionary) 를 써야 오류가 발생하지 않음, 그냥 딕셔너리만 넣는다면 오류가 발생함, 또는 아래와 같은 코드로 작성할수도 있음

```python
passed_students = {student:score for(student, score) in students_scores.items() if score > 60}
```

key와 value에 이름을 붙일 수 있으며, 딕셔너리.items() 로 딕셔너리를 사용할 수 있다.

## 딕셔너리 컴프리헨션1

주어진 문장의 각 단어를 취하여 각 단어의 글자 수를 계산하는 `result`라는 딕셔너리를 만들기 위해 딕셔너리 컴프리헨션을 사용할 것입니다.

문장을 단어의 리스트로 변환하는 방법을 알아보기 위해 구글링해보세요. *

- 절대** 직접 딕셔너리를 생성하지 마세요. 루프 대신 **딕셔너리 컴프리헨션**을 사용해보세요.

이 연습을 간단하게 유지하기 위해 공백이 없는 단어 뒤에 오는 모든 구두점을 단어의 일부로 계산하세요. 따라서 "Swallow?"의 길이는 8입니다.

```python
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split(" ")}
```

![image.png](attachment:8f1fa0f2-346c-4272-8c78-866cccb7564a:image.png)

## 딕셔너리 컴프리헨션2

섭씨 온도를 화씨 온도로 변환하는 `weather_f`라는 딕셔너리를 만들기 위해 딕셔너리 컴프리헨션을 사용할 것입니다.

`temp_c`를 `temp_f`로 변환하려면 이 공식을 사용하세요:

`(temp_c * 9/5) + 32 = temp_f`

섭씨에서 화씨로 변환하는 차트

![](https://img-c.udemycdn.com/redactor/raw/coding_exercise_instructions/2024-08-02_15-08-18-b00faeae64310d6fb7272605cd37a8da.png)

- 절대** 직접 딕셔너리를 생성하지 마세요. 루프 대신 **딕셔너리 컴프리헨션**을 사용해보세요.

```python
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temp * 9/5) + 32 for (day,temp) in weather_c.items()}

print(weather_f)
```

![image.png](attachment:4f9a1107-bf15-4043-8a76-8e85f605f655:image.png)

## 판다스 데이터 프레임에서 반복하는 방법

```python
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for(key, value) in student_data_frame.items():
    print(key)
    print(value)
```

![image.png](attachment:5a227e56-dba7-4e5b-8a36-778734662b83:image.png)

위의 코드는 컬럼을 기준으로 해당 데이터들을 뽑은 것

```python
for(index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
```

![image.png](attachment:492c00e8-7635-4b8c-adf2-251ae1bddcc2:image.png)

index와 iterrows() 메서드를 통해서 해당 index의 행을 뽑을 수 있음(유의미한 데이터값)

그럼 1번째 행의 score를 뽑기 위해서는?

```python
for(index, row) in student_data_frame.iterrows():
    if index == 1:
        print(row.score)
```

![image.png](attachment:0801c125-48a2-433b-b288-1721a3af6302:image.png)

## NATO 알파벳 음성기호 프로젝트

![image.png](attachment:695bbbee-588a-4420-a2d5-b4023832e85c:image.png)

```python
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
```

위의 메인파일과 알파벳 코드가 적힌 csv파일을 받음

프로젝트 수행 사항은 다음과 같음

1. 다음과 같은 형식으로 dictionary를 생성 {”A” : “Alfa”, …}
2. 사용자가 입력하는 단어로부터 음성 규약 단어 리스트를 생성
    
    Thomas → [”Tango”, “Hotel” …]
    

### 1. dictionary 생성하기

```python
#TODO 1. Create a dictionary in this format:
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_key = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_key)
```

![image.png](attachment:303bdbee-d253-4caf-8173-86c15ae053a1:image.png)

강의에서 배운 내용으로, data_frame을 생성하고, 딕셔너리 컴프리헨션 및 iterrows() 메서드를 활용하여 새로운 nato_key라는 딕셔너리를 생성함

### 2. 사용자 입력으로 부터 Nato 리스트 생성

```python
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("단어를 입력하세요 : ").upper()
user_input_list = [word.upper() for word in user_input]
nato_list = [nato_key[key] for key in user_input_list]
print(nato_list)
```

1. input 값 받기
2. input 값으로부터 key를 뽑기위해 리스트 생성
3. key값에 따른 nato 단어 리스트 생성

![image.png](attachment:1c3b192a-46f4-4b32-9fd1-b6319a17382d:image.png)

### 해설

```python
# 해설
output_list = [nato_key[key] for key in user_input]
print(output_list)
```

그냥 user_input_list를 만들 필요가 없는데 굳이 만들었음,,,

끝!

## 27일차
## Tkinter로 Window와 Label 만들기

![image.png](attachment:e80a279f-bec2-4adc-834b-1891ad1bdea4:image.png)

tutle 패키지 처럼, 파이썬에서 GUI를 표현해주는 라이브러리로 tkinter 패키지 안에 Tk 클래스를 활용해서 화면을 만들고 사이즈를 정할 수 있다.

또한 화면에 라벨링을 해줄 수 있는데 tkinter.Label() 을 통해 만들 수 있으며 소괄호 안에 내가 원하는 문자열과 폰트 등을 지정할 수 있다.

pack 메서드는 라벨의 위치, 크기 등을 변환할 수 있는 메서드이다.

![image.png](attachment:859434c6-ea92-4297-887a-6f6278fa4fcf:image.png)

## 선택적 인수에 기본값 설정하기

### Advanced Python Arguments

기본값을 받는 함수 

```python
def my_function(a=1, b=2, c=3):
    sum_param = a + b + c
    print(sum_param)
    
my_function()
my_function(b=5)
```

![image.png](attachment:a1a1b4cf-e442-4ae2-b39b-3673de546bd3:image.png)

이렇게 기본값을 가지면 그냥 함수를 불러도, 만약 값을 바꾸고 싶다면 b만 바꿔도 나머지 인자들은 default 값을 가지기 때문에 함수가 잘 작동한다.

## args : 여러 인수를 갖는 함수 만들기

```python
def add_arg(*args):
    for n in args:
        print(n)

add_arg(3,5,7,9)
```

인자로 *args 를 사용하면 여러 값을 받는 파라미터가 된다.

![image.png](attachment:6acf82ce-4a91-49d9-b103-de0ed11001f0:image.png)

기본적으로 print(args)를 하게 된다면 tuple 형태가 나옴

ex) : (3,5,7,9)

## **kwargs: 임의의 숫자 키워드 인수 다루기

```python
def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))

calculate(add=3, multiply=5)
```

![image.png](attachment:84b0e3ee-eec9-446f-b77e-aaddf51d6368:image.png)

**kwargs는 딕셔너리 형태로 인자를 받으며 무슨 이름을 붙이든 상관없다

```python
def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)

    print(kwargs["add"])

calculate(add=3, multiply=5)
```

![image.png](attachment:b3628ee7-646f-458f-9440-3026c804dd22:image.png)

이렇게 다양한 형태로 변형하여 사용할 수 있음

모든 입력을 검색해서 우리가 원하는 값을 찾을 수 있도록 해줌

```python
def cal(n, **kwargs):
    n += kwargs["add"]
    n -= kwargs["minus"]
    n *= kwargs["gop"]
    print(n)

cal(2,add=3, gop=3, minus=1)
```

클래스에서도 활용이 가능하다

```python
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
```

![image.png](attachment:83cd869a-5d1f-4843-89f2-8b931b8fdfa8:image.png)

만약에 생성할 때, model의 값을 주지 않는다면 아래 사진처럼 model의 값을 주지 않아서 오류가 발생함

![image.png](attachment:c6592897-190a-4808-830f-bd9a33a3e555:image.png)

```python
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)
```

딕셔너리는 [] 말고도 .get으로도 value를 불러올 수 있으며 이렇게 get으로 불러오면 없는 값이 있어도 오류가 뜨지 않는다

![image.png](attachment:7d9f5144-9636-4b72-8c2a-899879108848:image.png)

## Tkinter 위젯 설정 바꾸기

![image.png](attachment:fd7ca95e-bb94-40f8-b67c-aee1a206d310:image.png)

```python
my_label["text"] = "new Text"
my_label.config(text="New Text")

button = tkinter.Button(text="Click Me")
button.pack()
```

딕셔너리 형태임을 알고 있으므로 첫 번째 줄 처럼 [”key”] = “key” 로 변환할 수도 있고

config를 활용해 바꿔줄 수도 있다.

또한 button을 통해서 화면에 버튼을 넣어 줄 수도 있다

```python
def button_click():
    print("I got clicked")

button = tkinter.Button(text="Click Me", command=button_click)
button.pack()
```

버튼에 이벤트 리스너를 command 키워드를 통해 달아줄 수 있다.

![image.png](attachment:859ae37c-bb16-4114-a6b2-5bbc10023025:image.png)

### 버튼 클릭 시 라벨 변환

```python
def button_click():
    my_label["text"] = "Button Clicked"

button = tkinter.Button(text="Click Me", command=button_click)
button.pack()
```

![image.png](attachment:2d0a71d9-d9b5-4590-8223-066b74b039b4:image.png)

위에서도 말했지만 config로도 변환이 가능하다

### Entry

```python
# Entry
input = tkinter.Entry()
input.pack()
```

![image.png](attachment:beace731-5c49-4a71-bee3-41da5086f5ec:image.png)

Entry 클래스를 활용하면 위의 사진처럼 텍스트를 입력할 수 있는 상자를 만들 수 있다.

화면에 생성되는건 pack메서드임

입력된 값을 받고싶다면 get 메서드를 활용한다.

```python
def button_click():
    my_label["text"] = "Button Clicked"
    print(input.get())

button = tkinter.Button(text="Click Me", command=button_click)
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()
```

![image.png](attachment:78469c0b-472c-4d8a-bb3f-b244930168d5:image.png)

![image.png](attachment:aee6aa38-c8a5-439a-a077-47cae3f18b0f:image.png)

이렇게 텍스트를 입력하고 버튼을 누르면 값이 출력된다

### 다양한 위젯

Label, Button, Entry 이외에도

Text : 여러 줄을 입력할 수 있는 Entry

Spinbox : 상하로 이동할 수 있는 박스

Scale : 축을 따라 이동하는 박스

Checkbutton : 체크를 할 수 있는 버튼

Radiobutton : 체크는 동일, 원형

Listbox : 리스트 형태의 박스

```python
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

```

![image.png](attachment:d4d93b44-baf9-49f2-bbe3-739e22862f70:image.png)

## Tkinter 레이아웃 메니저

Pack , Place, Grid

pack : 각각의 위젯을 논리적 형태로 다음 위젯 옆에 배치하는 역할, 디폴트값으로 center와 최상단에 위치하며 다음 pack은 그 아래 위치하게 됨

place : 정확한 위치에 위젯을 배치, x와 y값을 주어서 위치값을 정해줌

grid : column, row를 지정하여 위치를 나눔 (표 형태)

### 그리드를 활용하여 배치

```python
# 라벨
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label["text"] = "new Text"
my_label.config(text="New Text")

# button
button = tkinter.Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

# new button
new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)
```

![image.png](attachment:4902101c-f804-4bee-ba4e-64cc69f5824b:image.png)

 

### Padding

```python
window.config(padx=20, pady=20)

# 라벨
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label["text"] = "new Text"
my_label.config(text="New Text")

# button
button = tkinter.Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

# new button
new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)
```

윈도우에 있는 모든 위젯의 x와 y에 20씩 여유를 두게 됨

![image.png](attachment:c917ff87-5f5f-4b5c-8a36-b254efd6036b:image.png)

위의 사진과 비교하면 윈도우 화면의 x와 y에 붙어있던 위젯들이 좀 띄어진 것을 볼 수 있음

## 마일을 킬로미터로 바꾸는 프로젝트

우선 먼저 해보기

```python
from tkinter import *
from turtledemo.penrose import start

window = Tk()
window.minsize(width=400, height=200)
window.config(padx=40, pady=40)

def calc():
    mile = input.get()
    ans_km = int(float(mile) * 1.609)
    answer.config(text=ans_km)

# label
is_equal_to = Label(text="is_equal_to", font=("Arial", 10, "bold"), padx=10, pady=5)
is_equal_to.grid(column=0, row=1)

miles = Label(text="Miles", font=("Arial", 10, "bold"), padx=10, pady=5)
miles.grid(column=2, row=0)

answer = Label(text="0", font=("Arial", 10, "bold"), padx=10, pady=5)
answer.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 10, "bold"), padx=10, pady=5)
km.grid(column=2, row=1)

# entry
input = Entry(width=10)
input.grid(column=1, row=0)

calculate_button = Button(text="Calculate", command=calc)
calculate_button.grid(column=1, row=3)

indow.mainloop()
```

![image.png](attachment:df4cb9ba-80f9-42d0-b4d4-e7775df963a6:image.png)

거의 똑같은데 하나 추가하자면 

```python
def calc():
    mile = float(input.get())
    ans_km = round(mile * 1.609)
    answer.config(text=ans_km)
```

이렇게 해주는게 더 깔끔해보임

끝!

## 28 일차
## Pomodoro 프로젝트

![image.png](attachment:a0fe2d6f-0441-4a48-8302-299333b5b6a4:image.png)

25분 → 5분 휴식 → 25분 → 5분 휴식 … 4번 반복하면 20분 휴식을 하는 타이머이며

작업을 하다가 쉬는시간이 되면 가장 첫 창에 Pomodoro가 떠야함

### UI 세팅

```python
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

window.mainloop()
```

기본적인 세팅이므로 설명은 생략

### Tkinter에 이미지를 배경으로 넣고 타이머를 추가

```python
canvas = Canvas(width=200, height=224)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.pack()
```

canvas는 Tkinter 안에 있는 클래스로, 화면에 이미지를 넣을 수 있다.

create_image로 canvas안에 이미지를 넣을 수 있으며, 여기서 image를 넣어줄 때 PhotoImage로 넣어줘야 한다.(그렇게 파라미터가 설정 되어있음)

![image.png](attachment:9be64ec0-58df-4b81-ac6e-806c17021778:image.png)

이렇게 작업하면 귀여운 토마토가 배경에 나오게 된다

```python
canvas.create_text(103,112, text="00:00")
```

canvas에는 text도 넣을 수 있는데 위의 코드를 작성 후 실행해주면

![image.png](attachment:8cfd27e3-6fcb-4c15-82d9-8689f8cef12b:image.png)

이렇게 지정해준 위치에 텍스트가 표시된다.

(화면에 공백은 window.config(padx, pady)를 넣어줬다.)

이제 canvas text에 추가적으로 값을 더 넣어서 텍스트를 꾸며본다.

색상을 정해주는 fill과 폰트를 정해주는 font를 설정

```python
canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) 
```

![image.png](attachment:8b18b36e-412a-41c2-8b94-7b73ccaa9d4e:image.png)

배경이 밋밋하니 배경 색을 추가해보자

```python
window.config(padx=100, pady=50, bg=YELLOW)
```

여기서 YELLOW는 상수로 위에 정의해둔 색상 코드이다. bg에는 원래 `"#f7f5dd"` 이렇게 색상 코드가 들어가야 한다.

![image.png](attachment:d4b95346-f2fd-4f1a-86c7-45abfb6b129b:image.png)

실행을 해보니, canvas영역인 부분은 배경색이 여전히 흰색이다.

canvas에도 배경색을 추가해보자

```python
canvas = Canvas(width=200, height=224, bg=YELLOW)
```

![image.png](attachment:3ec3139d-4d9d-41cc-859a-2234c28fbd33:image.png)

잘 안보이는데 canvas영역에 약간의 경계선으로 하얀색이 보인다.

이를 제거하려면 canvas에 `highlightthickness=0` 을 설정해줘야 한다.

![image.png](attachment:391e0264-3e08-4668-9226-0b4f50de8d71:image.png)

오른쪽에 벌레가 먹은듯한 부분은 canvas 이미지를 약간 조정해주면 된다.

```python
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()
```

### 도전과제

![image.png](attachment:15a620c3-3fb8-4f94-a3c0-2c44bf2829aa:image.png)

Text의 색상을 바꾸는 방법은 fg=”#~~”

```python
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# label
timer_label = Label(bg=YELLOW, fg=GREEN, text="Timer", font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)
check_label = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=3)

# button
start_button = Button(text="Start")
start_button.grid(column=0, row=2)
restart_button = Button(text="Restart")
restart_button.grid(column=2, row=2)

window.mainloop()
```

![image.png](attachment:e95821da-baa1-4cfe-b0c8-cbfe4a4560d4:image.png)

쨘 최대한 동일하게 따라해봤다

### 카운트다운 메커니즘 구현하기

이벤트 구동형 - Event Driven

```python
def say_something(thing):
    print(thing)

window.after(1000, say_something, "Hello")
```

Tk클래스의 메서드로 after라는 함수는 내가 지정한 ms초 뒤에 지정된 함수가 실행됨

위의 코드를 보면 1000ms → 1초 , say_something  → 함수, “Hello” → thing(parameter)

```python
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count-1)

timer_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

count_down(5)
```

이전에 만들었던 canvas를 변수로 정의하고, count_down함수 안에서 canvas의 설정을 변경한다.

캔바스의 경우에는 itemconfig로 변경할 수 있으며 text를 count로 변경하면 아래의 사진과 같이 카운트 다운이 시작된다.

중요한점은 count_down(5)가 canvas를 만든 후에 정의되어야 오류가 나지 않는다.

![image.png](attachment:2a5f2a0b-c4cd-40db-a245-10f525f885a6:image.png)

### 버튼과 연계

위에서 count_down(5)를 따로 아래 실행해줬는데 버튼을 누르면 시작되는 함수로 만들어준다.

```python
def start_timer():
    count_down(5)
    
start_button = Button(text="Start", command=start_timer)
```

![image.png](attachment:56f1a243-593c-4a5b-9c66-190a976d21d6:image.png)

![image.png](attachment:5350f339-715a-4c71-a615-b3d74cd6ccb2:image.png)

코드를 작성 후 클릭하면 시작 화면은 우리가 처음에 설정한 Text가 나오고, Start버튼을 누르게 된다면 타이머가 시작된다.

### 초 → 분

우리는 5초가 아닌 25분, 5분 등 분 단위로 시간 타이머를 설정해야 한다.

```python
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mm = math.floor(count / 60)
    ss = count % 60
    
    canvas.itemconfig(timer_text, text=f"{mm}:{ss}")
    if count > 0:
        window.after(1000, count_down, count-1)
```

math 라이브러리는 import math로 파이썬에 임포트 해주고 사용

floor메서드는 나누고 나서 남은 소수점을 반올림하지 않고 그냥 없애줌

mm ⇒ 60으로 나눈 정수, ss ⇒ 60으로 나눈 나머지가 된다.

![image.png](attachment:522eb8e3-c943-498d-ab06-7c679e23f0ff:image.png)

하지만 문제가 처음 시작할 때 5:0 → 이렇게 표시가 된다

이거를 5:00로 변경해야 한다.

### 파이썬 동적 타이핑

![image.png](attachment:03a1f1dc-9e7d-4c09-89dd-194c4fb48d6e:image.png)

이 문제를 해결하기 위해서는 동적 타이핑이 필요하다

![image.png](attachment:d74a5fe2-4df5-44bc-9dc8-8170a28a133b:image.png)

처음 3 + “4”를 그냥 콘솔에 입력하면, int와 str은 더할 수 없다고 나온다.

그렇다면 파이쏜 콘솔에 a라는 변수에 3을 넣으면 → int

그 다음 a에 Hello라는 문자열을 넣으면 → str로 타입이 변경되는데 이를 동적 타이핑이라고 한다.

```python
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mm = math.floor(count / 60)
    ss = count % 60

    if ss == 0:
        ss = '00'
    canvas.itemconfig(timer_text, text=f"{mm}:{ss}")
    if count > 0:
        window.after(1000, count_down, count-1)
```

즉 우리는 동적 타이핑을 이용해 이렇게 표시할 수 있으며, 이제 초가 0이면 00으로 표시가 된다

하지만 9, 8, 7.. 이렇게 1자리의 초나 분의 경우에도 09 이런식으로 00:00으로 표시가 되어야 한다.

```python
    if mm < 10:
        mm = f"0{mm}"
    if ss < 10:
        ss = f"0{ss}"
```

![image.png](attachment:b8ebd385-ffa6-4628-bd78-df8efe904961:image.png)

![image.png](attachment:bc35fc80-7e87-4d0d-8a00-f8071ff3f1bc:image.png)

이런식으로 조건문을 짜주게 된다면 초나 분이 이제 00의 형식으로 맞춰지게 된다.

### 타이머 세션 및 값 설정하기

25분 → 5분휴식 → 25분 → 5분휴식 → 25분 → 5분 휴식 → 25분 → 20분 휴식

4번째 휴식에는 20분의 휴식시간이 주어짐

```python
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global resp
    if count == 0:
        resp += 1
        print(resp)
        if resp == 4:
            count = 20 * 60
            resp = 0
        else:
            count = 5 * 60

    mm = math.floor(count / 60)
    ss = count % 60

    if mm < 10:
        mm = f"0{mm}"
    if ss < 10:
        ss = f"0{ss}"
    canvas.itemconfig(timer_text, text=f"{mm}:{ss}")
    if count > 0:
        window.after(1000, count_down, count-1)
```

resp는 전역변수로 상단에 0을 초기값으로 넣어줌

![image.png](attachment:ec344e17-b77e-48dd-983b-2b52b311d050:image.png)

검증을 위해서 우선 1분을 기본으로 설정 

![image.png](attachment:22ea2494-a301-4046-a735-e1557a6b4982:image.png)

시간이 다 지나면 1번째 휴식시간 5분이 주어짐

이제 다시 25분 일하는 타이머가 작동되며 4번째 휴식에서 20분이 주어짐

이러면 resp는 항상 +1을 해주며 홀수 = 일, 짝수 = 쉬는시간

```python
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global resp
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    resp += 1
    if resp % 2 == 0:
        if resp == 2:
            count_down(long_break_sec)
            resp = 0
        else:
            count_down(short_break_sec)
    else:
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mm = math.floor(count / 60)
    ss = count % 60

    if mm < 10:
        mm = f"0{mm}"
    if ss < 10:
        ss = f"0{ss}"
    canvas.itemconfig(timer_text, text=f"{mm}:{ss}")
    if count > 0:
        window.after(1000, count_down, count-1)
    elif count == 0:
        start_timer()
```

시간을 설정하여 start_timer에서 count변수를 넘겨주는 방식으로 변경하였고, 상수를 설정하여 이용함

시간이 0이 된다면 다시 start_timer가 실행되며 다른 시간 값을 넘겨주게 됨

검증을 위해서 long_break_sec를 첫 휴식 때 설정, 이렇게 되면 1분의 타이머가 지난 뒤 20분의 휴식시간이 나와야됨

![image.png](attachment:7712c032-e400-4841-a4bf-fd03550c6817:image.png)

![image.png](attachment:8cf6eed3-5caa-4bbb-b183-9215c17c289d:image.png)

![image.png](attachment:8c4229ad-5235-42c6-ba86-706ad0d0d38c:image.png)

![image.png](attachment:258ccc44-bf7c-4a62-b38a-6cfa235fbdad:image.png)

resp1 : 1분 확인O

resp2 : 2분 확인O

resp3 : 1분 확인O

이렇게 검증을 통해 로직이 잘 돌아간다는 것을 확인했음

강의에서는 해답으로 이런 방식을 활용함

```python
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global resp
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    resp += 1
    if resp % 8 == 0:
        count_down(long_break_sec)
    elif resp % 2 == 0:
        count_down(short_break_sec)
    else:
        count_down(work_sec)
```

이렇게 해주면 resp를 다시 0으로 안돌려도 되고, 코드의 가독성도 더 높아보임(조건문이 하나니까)

```python
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global resp
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    resp += 1
    if resp % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break Time", fg=RED)
    elif resp % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break Time", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time", fg=GREEN)
```

각각의 타이머별로 Text와 색상을 변경함

### 체크 표시 추가하고 애플리케이션 리셋하기

```python
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mm = math.floor(count / 60)
    ss = count % 60

    # 검증을 위해서, 나중에 주석
    if ss == 55:
        count = 1

    if mm < 10:
        mm = f"0{mm}"
    if ss < 10:
        ss = f"0{ss}"
    canvas.itemconfig(timer_text, text=f"{mm}:{ss}")
    if count > 0:
        window.after(1000, count_down, count-1)
    elif count == 0:
        if resp % 2 == 0:
            mark = ""
            for _ in range(math.floor(resp/2)):
                mark += "✓"
                check_label.config(text=mark)
        start_timer()
```

처음에 check_label의 text를 없애주고, resp가 짝수인 경우에만 mark에 체크표시를 늘려가면서 check_label에 표시해준다.

이렇게 되면 한번의 반복(일, 휴식)이 종료되면 체크표시가 한개씩 증가하게 된다.

<img src = "attachment:357600a8-af24-4157-b000-eef8519b2f6a:image.png"

<img src = "attachment:e16699bd-2e21-4857-9e09-f7f94c98b44e:image.png"

### 타이머 리셋

1. timer 멈추기
    
    `window.after(1000, count_down, count-1)` 타이머 기능인 옆의 함수를 멈춰야한다.
    
    멈추기 위해서는 window.after_cancel 메서드를 활용할 수 있으며 after_cancel을 사용하기 위해 window.after를 변수로 만들어야 함
    
    따라서 timer = None라는 전역변수를 하나 만든 후, 
    
    ```python
    # 당연히 함수 내부 이므로 함수 상단에 global timer 설정
     
    canvas.itemconfig(timer_text, text=f"{mm}:{ss}")
        if count > 0:
            timer = window.after(1000, count_down, count-1)
    ```
    
    본래 있던 코드에서 그냥 변수로 설정만 추가
    
    이제 새로운 함수인 reset_timer에서 after_cancel을 활용하여 타이머를 멈추면 된다.
    
    ```python
    def reset_timer():
        window.after_cancel(timer)
    ```
    
    [20260205-0207-47.2794555.mp4](attachment:c82129da-588d-46a0-a94f-e274921c0e1d:20260205-0207-47.2794555.mp4)
    
    동영상을 확인하면 타이머가 정지하는 것을 볼 수 있다.
    
    이제 모든 것을 초기로 돌려보자
    
    ```python
    # ---------------------------- TIMER RESET ------------------------------- # 
    def reset_timer():
        global resp
        window.after_cancel(timer)
        timer_label.config(text="Timer")
        canvas.itemconfig(timer_text ,text="00:00")
        check_label.config(text="")
        resp = 0
    ```
    
    이렇게 reset을 누르면 00:00이 되면서 resp, mark 등 모든 값이 초기로 돌아가게 된다.
    
    [20260205-0216-52.0310634.mp4](attachment:deaccbeb-c3af-465d-8735-62ee59d77f0f:20260205-0216-52.0310634.mp4)
    

끝!
