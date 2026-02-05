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

<img width="1067" height="761" alt="image" src="https://github.com/user-attachments/assets/b0281b06-b2c5-41ea-b549-9d8b648c44ba" />

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

<img width="1457" height="551" alt="스크린샷 2025-12-31 191008" src="https://github.com/user-attachments/assets/6b151107-1c8f-4f58-a9a8-1edc72577aed" />

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

<img width="1096" height="529" alt="image" src="https://github.com/user-attachments/assets/e5691540-aa60-42bb-a72a-730b1efc4f17" />

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

<img width="1833" height="813" alt="스크린샷 2026-01-03 175720" src="https://github.com/user-attachments/assets/ce7e3cc6-b8a0-4d42-a348-d09fe27f2631" />

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

<img width="673" height="612" alt="image (1)" src="https://github.com/user-attachments/assets/dc7fb836-5889-4ee8-a418-d1836a6e1dfc" />

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

<img width="1203" height="846" alt="image (2)" src="https://github.com/user-attachments/assets/6160b583-73bf-42ed-a344-2c3f877f08a7" />

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

<img width="657" height="392" alt="image (3)" src="https://github.com/user-attachments/assets/ec93299f-625c-484d-895d-a40a8b121709" />

→ b_list의 값이 빈 값으로 계속 진행되는 문제를 확인 후 오류 수정하고 다시 디버그

<img width="692" height="277" alt="image (4)" src="https://github.com/user-attachments/assets/57f9357b-8522-428a-8e4f-5b0aa987b653" />

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
    
    <img width="1877" height="1032" alt="스크린샷 2026-01-11 152531" src="https://github.com/user-attachments/assets/a2863253-e461-4b44-8afe-c323bfa292fd" />

2. 실패
    
    <img width="1037" height="620" alt="스크린샷 2026-01-11 152603" src="https://github.com/user-attachments/assets/47ba5b7f-7c09-444b-891d-dd475cc8e25e" />

3. 성공
    
    <img width="1832" height="1097" alt="스크린샷 2026-01-11 152643" src="https://github.com/user-attachments/assets/f99f78ed-d230-4b8e-89e9-8eb1b3344d23" />


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

<img width="1832" height="1097" alt="스크린샷 2026-01-11 152643" src="https://github.com/user-attachments/assets/5c5f742c-9390-49a5-8f5f-14d259afb376" />

### 실패 화면

<img width="692" height="499" alt="스크린샷 2026-01-11 180942" src="https://github.com/user-attachments/assets/362503a2-2fd2-487f-9cc9-e1e7a7308cf8" />

### 성공 화면

<img width="885" height="713" alt="스크린샷 2026-01-11 181014" src="https://github.com/user-attachments/assets/3c1d85b1-326a-40c1-beee-46418a50e75a" />

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

<img width="694" height="365" alt="스크린샷 2026-01-14 190454" src="https://github.com/user-attachments/assets/7b878bc3-c6bf-4240-b676-bf54b0237aa8" />

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

2. Turn off the Coffee Machine by entering “off” to the prompt.
	a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the
	machine. Your code should end execution when this happens

off를 입력하면 종료한데요.

```python
while True:
    coffee = input("What would you like? (espresso/latte/cappuccino/): ")
    if coffee == 'off':
        break
```

3. Print report()
    
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
    
    <img width="757" height="269" alt="스크린샷 2026-01-14 192545" src="https://github.com/user-attachments/assets/a3aebe21-e9b2-4b8a-a98b-bb58fe02cd16" />

4. Check resources sufficient?
    
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

<img width="922" height="231" alt="스크린샷 2026-01-14 195046" src="https://github.com/user-attachments/assets/7f97294b-1a4d-4d67-badc-4fc6d37843f7" />

5. Process coins.
    
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

6. Check transaction successful?
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
7. Make Coffee.
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

<img width="1279" height="1051" alt="스크린샷 2026-01-14 200826" src="https://github.com/user-attachments/assets/cf9f1a1b-b937-4aea-8e83-4797efe64479" />

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

<img width="683" height="201" alt="스크린샷 2026-01-15 112017" src="https://github.com/user-attachments/assets/9db84390-7f59-4cb4-9662-79beb1ddad34" />

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

<img width="797" height="237" alt="스크린샷 2026-01-15 112452" src="https://github.com/user-attachments/assets/97710356-f47a-400e-af8e-664c29a23be0" />

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

<img width="709" height="246" alt="스크린샷 2026-01-15 112911" src="https://github.com/user-attachments/assets/adf2dffc-f5ba-48ba-b09e-d9cab4dff6a1" />

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

<img width="987" height="318" alt="스크린샷 2026-01-15 113647" src="https://github.com/user-attachments/assets/c87e38d9-c4fe-4de0-b93c-a6fc2576b56f" />

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

<img width="1046" height="493" alt="스크린샷 2026-01-15 115534" src="https://github.com/user-attachments/assets/e75ea20c-1a78-4320-8be7-80bd55fa3353" />

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

<img width="1145" height="656" alt="스크린샷 2026-01-15 120415" src="https://github.com/user-attachments/assets/a8c57ed8-c34b-4138-9969-9d938c775700" />

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

<img width="939" height="480" alt="스크린샷 2026-01-15 120702" src="https://github.com/user-attachments/assets/a68f1113-9bbb-41ff-946b-402cfe33e80b" />

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

<img width="638" height="162" alt="스크린샷 2026-01-15 122958" src="https://github.com/user-attachments/assets/98a01124-79a8-4982-8d73-89de3a41548b" />

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

<img width="638" height="162" alt="스크린샷 2026-01-15 122958" src="https://github.com/user-attachments/assets/5eda2dbc-6a64-47e7-9f5a-4b03298989c9" />

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

<img width="1348" height="602" alt="스크린샷 2026-01-15 130801" src="https://github.com/user-attachments/assets/4efd2b36-30a4-43a0-8528-2a169e0c1457" />

### Open Trivia DB 활용

https://opentdb.com/api_config.php

해당 url로 이동 (회원가입 해야됨) → API 클릭

<img width="1516" height="874" alt="스크린샷 2026-01-15 131646" src="https://github.com/user-attachments/assets/f10f25ed-9175-4c14-9055-ab23e1a30e88" />

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

<img width="972" height="269" alt="스크린샷 2026-01-15 132705" src="https://github.com/user-attachments/assets/38dd3368-f50a-43af-92dd-aa97c5afa831" />

data.py에 복사해서 형태를 보면, question과 correct_answer 로 이루어진 것을 볼 수 있음,

다른 Key값들도 있지만 우리는 필요없음

```python
for question in question_data:
    qt = Question(question["question"], question["correct_answer"])
    question_bank.append(qt)
```

메인으로 돌아와서 for문에서 아까는 text와 answer였으므로 수정

<img width="1125" height="691" alt="스크린샷 2026-01-15 132832" src="https://github.com/user-attachments/assets/a592e77e-0e7e-4e0b-adcd-bf82da4f2ad6" />

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

<img width="666" height="504" alt="스크린샷 2026-01-18 205254" src="https://github.com/user-attachments/assets/3725a312-984b-47fe-8e6c-37d2a3af37c5" />

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

<img width="671" height="161" alt="스크린샷 2026-01-18 205934" src="https://github.com/user-attachments/assets/96d3b1b3-32b8-4577-8593-71c92de33c09" />

heros 모듈을 import하려고 했지만 파이썬 라이브러리에 없어서 import가 안됨

그때 저 패키지 설치를 눌러서 파이썬 라이브러리에 heros 모듈을 설치할 수 있음

<img width="846" height="78" alt="스크린샷 2026-01-18 210040" src="https://github.com/user-attachments/assets/1a9b9478-c686-418f-a5fb-9013c92bed97" />

<img width="1308" height="308" alt="스크린샷 2026-01-18 210219" src="https://github.com/user-attachments/assets/25a4edc5-253b-4d68-b159-ad338e37ec8c" />

설치가 완료되면 사진처럼 heroes 패키지를 사용할 수 있음

### 점선 그리기

turtle패키지를 활용해 점선 사각형을 그리기

<img width="501" height="379" alt="스크린샷 2026-01-18 210544" src="https://github.com/user-attachments/assets/54fb34df-6eea-4e9c-a166-9c3e499257d8" />

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

<img width="308" height="239" alt="스크린샷 2026-01-18 210850" src="https://github.com/user-attachments/assets/eb2e807d-3fa6-4ed3-8eb4-2e3263a54e19" />

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

<img width="749" height="314" alt="스크린샷 2026-01-18 214241" src="https://github.com/user-attachments/assets/d6b81b18-c014-4be6-b6b7-3ad67af0f7ee" />

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

<img width="361" height="388" alt="스크린샷 2026-01-18 215220" src="https://github.com/user-attachments/assets/44282b67-f112-4b21-9c05-a9e1393a7dda" />

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

<img width="1146" height="747" alt="스크린샷 2026-01-18 215526" src="https://github.com/user-attachments/assets/7f86132f-3982-4832-8ffb-1e80322b6319" />

1. 방향 바꾸기

```python
current_heading = tim.heading()
tim.setheading(current_heading + 10)
tim.color(random_color())
tim.circle(100)
```

<img width="1192" height="715" alt="스크린샷 2026-01-18 215823" src="https://github.com/user-attachments/assets/8ed6f694-b3ea-4bb4-879b-52e1387c797a" />

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

<img width="1148" height="1118" alt="스크린샷 2026-01-18 215954" src="https://github.com/user-attachments/assets/902965dc-2bbb-4d3d-9699-9803491979b8" />

## 프로젝트 1. 이미지에서 rgb값 추출

이미지에서 rgb값 추출하기

img.jpg는 구글에 있는 paiting 사진을 하나 다운

colorgram이라는 패키지를 활용해서 extract 메소드를 활용

→ 

<img width="1148" height="1118" alt="스크린샷 2026-01-18 215954" src="https://github.com/user-attachments/assets/9335cba6-b6d5-4328-a09a-460b16ef882d" />

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

<img width="1561" height="92" alt="스크린샷 2026-01-18 225808" src="https://github.com/user-attachments/assets/1bb53f2a-fbfc-45bd-8863-92389f20a46b" />

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

<img width="1894" height="150" alt="스크린샷 2026-01-18 225907" src="https://github.com/user-attachments/assets/d845e6cb-08e9-45c7-8396-e96f42d45a2c" />

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

<img width="449" height="456" alt="스크린샷 2026-01-18 232922" src="https://github.com/user-attachments/assets/a30d4219-f4e7-4a3e-8228-dc0ca8ef05c3" />

## 19일차
## 파이썬 고차함수 및 이벤트리스너

### 터틀 이벤트리스너

<img width="478" height="313" alt="image (5)" src="https://github.com/user-attachments/assets/a3f89b09-116d-4fc9-9a09-055fa78ce92b" />

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

<img width="1175" height="1121" alt="image (6)" src="https://github.com/user-attachments/assets/5c1b1c45-2e8d-40b9-b99d-0b44a9820d0c" />

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

<img width="1272" height="896" alt="image (7)" src="https://github.com/user-attachments/assets/43d2fe2a-864b-4c62-a1a9-241a2338a813" />

<img width="1228" height="293" alt="image (8)" src="https://github.com/user-attachments/assets/45df6f33-3f04-4cf2-8f26-729b023a50e8" />

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

<img width="1195" height="1140" alt="image (9)" src="https://github.com/user-attachments/assets/01c85f8a-a4b4-4c69-a40c-fe4b1c39afcc" />

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

<img width="792" height="687" alt="image (10)" src="https://github.com/user-attachments/assets/986adda7-f1be-473b-acfb-282feda641d1" />

<img width="512" height="237" alt="image (11)" src="https://github.com/user-attachments/assets/3a7dd52a-1263-4643-a3dd-345277860924" />

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

<img width="835" height="693" alt="image (12)" src="https://github.com/user-attachments/assets/dd1a443b-572b-4234-91a2-ffbe56d2ca1f" />

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

<img width="826" height="705" alt="image (13)" src="https://github.com/user-attachments/assets/1c7da9d3-921d-41a0-acc5-33da985c97bc" />

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

<img width="807" height="680" alt="image (14)" src="https://github.com/user-attachments/assets/d4cedfd2-1aa9-4962-be15-d47a704bc2f7" />

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

<img width="786" height="671" alt="image (15)" src="https://github.com/user-attachments/assets/49989c94-c6f9-4c2a-9009-0f761b7a7d93" />

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

<img width="1411" height="721" alt="image (16)" src="https://github.com/user-attachments/assets/94713fa7-5cc6-431e-9db2-9450b71e1ee0" />

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

<img width="934" height="968" alt="image (17)" src="https://github.com/user-attachments/assets/fb19ef69-90ce-429a-816a-3de8dbbabf01" />

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

<img width="926" height="961" alt="image (18)" src="https://github.com/user-attachments/assets/67b73a28-1552-480f-9633-621dad0e8ad7" />

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
