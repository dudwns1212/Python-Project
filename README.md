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

![image.png](attachment:dfe081b3-c28d-4b56-bf5c-7932f9e19a99:image.png)

move()를 호출하면 로봇의 방향으로 한칸 이동하는 것을 볼 수 있다

![image.png](attachment:b0be2473-3775-4787-a9c8-e1f24383234a:image.png)

리보그의 키보드 라는 버튼을 클릭하면 리보그가 움직일 수 있는 함수들을 알려준다

![image.png](attachment:d5f2098a-fa37-4dd8-94f1-1bfe9d02b218:image.png)

### 실습- turn around, turn right를 만들어보기

키보드를 보면 turn_left만 존재해서 다시 돌리려면 turn_left를 여러번 입력해야한다

이를 함수로 쉽게 만들어보자

 

![image.png](attachment:7c4a5e92-4d68-47de-b5cb-d2ca8422b09f:image.png)

위와 같이 turn_right, turn_around() 함수를 만들어서 동네를 한바퀴 돌아보는 프로그램을 실행

## 과제-여러 장애물을 넘어, 목적지에 도착하

![image.png](attachment:7ed03a17-6a51-4bfb-bf49-f8d52a871374:image.png)

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

![image.png](attachment:8a310432-c6f5-43c1-a2e1-9a7271880e8f:image.png)

추가로 반복문 안에 들어가는 저 구문도 함수로 만들어서 넣을 수 있다. (코드가 더 깔끔해보임)

** 코드 한번에 들여쓰기 하는법 Ctrl + ]

## 들여쓰기

![image.png](attachment:6bbb34c4-54ac-4f49-a55f-f1c9c7acb714:image.png)

항상 저 사각형의 구역을 생각하고, 함수 내에 코드가 존재하는지, 어디까지 이 함수의 코드인지 생각해야 함

### Tap VS Space ⇒ 탭이냐 공백이냐

파이썬 공식 문서에는 들여쓰기를 할 때, 공백을 4개 입력하라고 나와있음,

하지만 아래와 같이 한번만 공백을 해도, 코드는 실행됨

![image.png](attachment:bf71a8db-acd4-48ee-8a80-ef1db66525c7:image.png)

취향 차이, 뭘 선택하든 똑같긴함

### While(반복문)

![image.png](attachment:453dae42-d165-47f5-b100-4e3b656ecb7a:image.png)

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

![image.png](attachment:51aa85b2-e61f-415d-aa5b-c5b857ff3b73:image.png)

위의 코드를 작성 후 실행시킨 모습, 출력문을 보면 6번을 반복하고, 0이 되었을 때, 반복문이 종료된 것을 볼 수 있다.

### huddle2 → at_goal()이 참일 경우 while 실행

![image.png](attachment:32736ce1-f5bc-4d5f-a1bc-56f39de6ee6d:image.png)

허들의 구조는 huddle1과 동일하지만, 마지막이 골인 지점이 아니다. 

6개의 지점은 at_goal()이 참일수도 거짓일수도 있다.

![image.png](attachment:85ce40e9-9283-4b61-81ee-e9319fce76f5:image.png)

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

![image.png](attachment:db3e3975-f948-4266-93aa-a576ef687765:image.png)

실행을 시키면 위와 같이 잘 작동하는 것을 볼 수 있다.

## huddle3-조건을 설정한 반복문

![image.png](attachment:7f75a7d0-2715-49d8-a1f1-cb991ccc3ccc:image.png)

허들3의 경우는 벽이 제 각각 존재한다, 즉 범위만 정해서 일정한 반복문을 실행하는건 맞지 않다.

![image.png](attachment:3bdb309e-118b-4919-8295-d26f67f61a85:image.png)

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

![image.png](attachment:f1840bd9-15d3-4bed-9471-e05583498d3e:image.png)

## huddle4-높이가 다른 장애물

![image.png](attachment:538e5128-9f25-4755-907c-3101bc7cf69a:image.png)

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

![image.png](attachment:a34d7530-3440-4840-a6c7-210dee71f807:image.png)

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

![image.png](attachment:c6973c72-519b-486c-b439-3a8723eb8a3b:image.png)

잘 동작하는 것을 볼 수 있다.

강의에서는 아래와 같은 코드로 작성하여 실행하였다.

![image.png](attachment:5bd8cc88-5eb4-40a1-bd21-5aa20656061c:image.png)

내가 작성한 코드와 다른 점은, 강사님은 하나의 함수로 안에 로직을 작성하였다, 나는 down이라는 함수를 만들고 walls라는 변수를 만들어 벽의 개수만큼 내려오는 반복문을 실행했다면 wall_on_right() 라는 함수를 활용, 나는 이걸 확인 못했는데 라이브러리에 함수가 있었다.

![image.png](attachment:98de8969-2e27-4614-9a58-49f86fa690d4:image.png)

조금 어렵게 푼 감이 없지 않아 있지만 잘 작동하니 해결!

## 6일차 프로젝트 - 미로탈출

[20251229-1152-43.5126257.mp4](attachment:95313d8b-62aa-4e3a-85ca-d5d011878303:20251229-1152-43.5126257.mp4)

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

![image.png](attachment:54304ccf-890a-4fb9-ad6a-ff9b52172407:image.png)

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

![image.png](attachment:55722339-6d31-463b-ae7b-00cfeb5621b5:image.png)

![image.png](attachment:27b92a49-10db-4692-a0eb-d48cb14a5db4:image.png)

강의에서는 위와 같은 코드를 작성함, right_is_clear() 라는 함수가 있었나봄;;

그건 둘째치고, 위의 코드에서도 내가 만났던 반복로직에서 계속 반복되는 문제가 발생함

강의에서는 변수를 만들어서 해결하는게 아니라

![image.png](attachment:bd5b8c0c-6e0e-4349-9381-f034bfdfea40:image.png)

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
