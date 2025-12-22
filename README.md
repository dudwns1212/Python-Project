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
