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

![image.png](attachment:d99d16f0-d91f-4b5c-aaf4-f72bbd989d43:image.png)

![image.png](attachment:40b7e722-6d97-4e09-a205-02d2c3b52b7d:image.png)

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
