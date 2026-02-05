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

<img width="283" height="171" alt="스크린샷 2026-01-21 185645" src="https://github.com/user-attachments/assets/46ed4d47-44f6-4713-a386-e2194535d0a4" />

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

<img width="613" height="872" alt="스크린샷 2026-01-21 191243" src="https://github.com/user-attachments/assets/20fad9a2-df55-4a59-8a4e-e8780dbc6f6a" />

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

<img width="1220" height="554" alt="스크린샷 2026-01-21 192812" src="https://github.com/user-attachments/assets/4fa6e3b4-4bd4-4ebc-b7cf-f0ed871da1ef" />

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

<img width="979" height="1032" alt="스크린샷 2026-01-21 194828" src="https://github.com/user-attachments/assets/1ab20145-0ab5-4e8d-b4ce-2fb1c3d3b5dd" />

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

<img width="946" height="985" alt="스크린샷 2026-01-21 195138" src="https://github.com/user-attachments/assets/8d923a90-2d92-432e-9beb-d12815faf91a" />

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

<img width="946" height="993" alt="스크린샷 2026-01-21 195406" src="https://github.com/user-attachments/assets/f402d098-ee53-41ed-ba76-2d7efc8a806d" />

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

<img width="961" height="999" alt="스크린샷 2026-01-21 195659" src="https://github.com/user-attachments/assets/03c58779-f249-47e5-b1c2-654273173d03" />

## Game Over

뱀이 벽과 만날 때

뱀의 머리가 몸통과 만날 때

1. 벽에 부딫힐 때

```python
# game over
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
```

<img width="934" height="998" alt="스크린샷 2026-01-21 200244" src="https://github.com/user-attachments/assets/fbc318e7-cbcf-449e-84dd-8bdd7241fb58" />

이렇게 벽에 부딫히면 멈춤

→ 이거에 더해서 벽과 부딫히면 게임오버가 화면에 떠야함

```python
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
```

<img width="934" height="987" alt="스크린샷 2026-01-21 200628" src="https://github.com/user-attachments/assets/d5f3eb82-2ded-4099-9e9e-7b083bc08c6b" />

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

<img width="948" height="994" alt="스크린샷 2026-01-21 201552" src="https://github.com/user-attachments/assets/5a5125a9-625d-4013-a4d4-3675c99e7be8" />

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

<img width="961" height="1003" alt="스크린샷 2026-01-21 202953" src="https://github.com/user-attachments/assets/2850012f-374e-4cb1-ad6a-4eb262089dc9" />

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

<img width="939" height="984" alt="스크린샷 2026-01-21 203342" src="https://github.com/user-attachments/assets/224a6943-febb-47cd-b0c2-3d66035e864d" />

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

<img width="212" height="63" alt="스크린샷 2026-01-21 203801" src="https://github.com/user-attachments/assets/31273c84-dea6-4e4e-a46a-c44649f10b7a" />

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

<img width="1236" height="974" alt="스크린샷 2026-01-24 104300" src="https://github.com/user-attachments/assets/577f7c0b-4820-48b0-a463-27c32dbb13c3" />

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

<img width="1228" height="977" alt="스크린샷 2026-01-24 105124" src="https://github.com/user-attachments/assets/a1c533d4-30e1-4356-af14-02f5dbd77490" />

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

<img width="1027" height="797" alt="스크린샷 2026-01-24 120026" src="https://github.com/user-attachments/assets/37d8c3dc-ab7a-44fa-997a-e115d4a29016" />

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

<img width="1264" height="949" alt="스크린샷 2026-01-24 120123" src="https://github.com/user-attachments/assets/a68b6a48-22a8-4d04-89d7-00e228c4647a" />

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

<img width="1228" height="975" alt="스크린샷 2026-01-24 123057" src="https://github.com/user-attachments/assets/a8e07060-474e-4161-9631-4ec20864268b" />

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

<img width="1236" height="985" alt="스크린샷 2026-01-24 123143" src="https://github.com/user-attachments/assets/2aff0987-6477-4414-9ce7-610a4202fd5b" />

이렇게 각각의 점수가 올라가는 것을 볼 수 있음

끝!

## 23 일차
터틀 크로스 프로젝트

다양한 색깔의 차들이 도로를 달리며, 내 turtle객체는 up키 또는 좌우 키를 활용해서 도로를 건너야함

도로를 모두 건너면 다음 단계로 이동하며, 이때 차의 속도가 빨라짐

차와 turtle객체가 부딪치면 game_over가 되며 다시 level1 부터 시작함

해설을 보지 않고 일단 만들어보려고 함

### 1. 설계를 하고 클래스를 생성

<img width="349" height="247" alt="image (19)" src="https://github.com/user-attachments/assets/cde29ca4-a9d7-40e4-af09-6605685f9c77" />

회사 짜투리 시간에 진행하고 있어서 폴더 이름이 다를 수 있음

우선 움직이는 차 객체를 만들 car

성공하면 올라가는 단계를 체크하는 level

내가 직접 움직이는 my_turtle

점수를 표시하는 score

screen의 범위를 눈으로 파악하기 위해 만든 sideline

### 2. screen 구성 및 myturtle 객체 생성

스크린은 x,y ⇒ 600,400으로 설계함(너무 크면 안좋을 것 같아서)

<img width="815" height="594" alt="image (20)" src="https://github.com/user-attachments/assets/bc4da232-8978-47c6-af15-56104cfd66c4" />

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

<img width="788" height="570" alt="image (21)" src="https://github.com/user-attachments/assets/89d2ff15-f9c2-4e9d-8562-f931e0e75f5b" />

왜그런지는 모르겠지만 위 아래에 10정도가 부족해진다.

아마 선의 폭이나 그런게 작용해서 20정도가 차지하는 것 같다. 따라서 크기를 420으로 늘린 후 좌표를 다시 설정(위의 코드들도 수정함)

<img width="868" height="757" alt="image (22)" src="https://github.com/user-attachments/assets/4c055206-8fd5-4672-a7e3-1f4624a15579" />

딱 맞는 모습을 볼 수 있다

이제 차량이 생성되는 곳을 좌표로 지정해야 한다. 

y값은 도로의 정 중앙 ex) -180~-150의 중간 → -165가 y좌표

차는 총 12구간에 나타나므로 -165 += 30을 해주면서 차의 좌표를 만들어줄 수 있다.

라고 했는데 시작파일을 줬었네, 다시 처음부터 시작

<img width="370" height="199" alt="image (23)" src="https://github.com/user-attachments/assets/22b5ba13-5274-4b5b-8a0b-db2688cf1f32" />

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

<img width="930" height="964" alt="image (24)" src="https://github.com/user-attachments/assets/a8ac15f4-bad2-4435-a19e-6c404ddafc5e" />

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

<img width="924" height="970" alt="스크린샷 2026-01-26 203640" src="https://github.com/user-attachments/assets/77f9a06e-d157-4053-b277-c1abc2146913" />

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

<img width="933" height="979" alt="스크린샷 2026-01-26 204030" src="https://github.com/user-attachments/assets/c8ad95ff-6bb8-4d9e-9de7-08b0bd8f1f1e" />

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

<img width="939" height="971" alt="스크린샷 2026-01-26 213106" src="https://github.com/user-attachments/assets/286f5398-7b6a-4cba-aa54-1305bc01d755" />

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

<img width="944" height="996" alt="스크린샷 2026-01-28 192544" src="https://github.com/user-attachments/assets/6db9cde8-f51a-4db1-9885-034dc2c6f874" />

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

<img width="933" height="972" alt="스크린샷 2026-01-28 193209" src="https://github.com/user-attachments/assets/ef2f2698-d9c7-49c5-8a99-a1475db9500e" />

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

<img width="931" height="971" alt="스크린샷 2026-01-28 194344" src="https://github.com/user-attachments/assets/4c99a688-67da-4663-b68f-2eb16ad79fa3" />

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

<img width="226" height="154" alt="스크린샷 2026-01-28 195225" src="https://github.com/user-attachments/assets/c9d92636-602b-4032-9cc9-8465d078018d" />

my_file에는 Hello my name is gyj를 적어둠

```python
file = open("my_file.txt")
contents = file.read()
print(contents)
```

main.py에 위의 코드를 적고 실행해주면 해당 파일을 읽어서 contents에 내가 적은 값을 넣어줌

<img width="443" height="233" alt="스크린샷 2026-01-28 195322" src="https://github.com/user-attachments/assets/16bd95ac-127b-4ec6-9248-ebfcae4ddf8c" />

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

<img width="406" height="222" alt="스크린샷 2026-01-28 200722" src="https://github.com/user-attachments/assets/1d737e92-3ff2-4565-ab8b-119870868278" />

코드를 실행해주면 파일에 새로운 text가 입력된 것을 볼 수 있음

만약에 기존에 있던 글에서 더해서 쓰고싶다면

```python
with open("my_file.txt", mode="a") as file:
    file.write("New text2")
```

모드를 a로 변경해주면 됨

<img width="815" height="233" alt="스크린샷 2026-01-28 200826" src="https://github.com/user-attachments/assets/0673441f-fdca-489c-b21f-b0482fd18f23" />

실행 후 확인하면 새로운 글이 써진 것을 볼 수 있고, 줄바꿈 \n도 가능함

```python
with open("new_file.txt", mode="w") as file:
    file.write("HI My new File")
```

새롭게 파일을 만들고 싶다면 새롭게 만들고싶은 파일 이름을 적고, mode를 w로 해주면 됨

<img width="1046" height="259" alt="스크린샷 2026-01-28 201001" src="https://github.com/user-attachments/assets/f9466861-1f90-4216-8c6f-86914ce6a825" />

새로운 파일이 생성됐으며 내가 쓴 글이 적용된 것을 볼 수 있음

이제 뱀 프로젝트로 돌아가서 파일에 최고 점수를 기록하고 파일에 있는 최고 점수를 읽어서 값을 넣어줄 수 있음, scoreboard를 생성할 때, 파일에서 최고점수를 읽고 값을 대입하는거임

### 뱀 게임에서 파일에 최고 점수 읽고 쓰기

<img width="734" height="276" alt="스크린샷 2026-01-28 201337" src="https://github.com/user-attachments/assets/d01686dc-ba95-4561-886c-0218c54f99a4" />

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

<img width="950" height="991" alt="스크린샷 2026-01-28 201606" src="https://github.com/user-attachments/assets/b3822f8c-d9e3-481b-baa9-472a8fccbde4" />

우선 highscore를 3으로 바꿔준 후, 종료하고 다시 실행해보면

<img width="971" height="1015" alt="스크린샷 2026-01-28 201634" src="https://github.com/user-attachments/assets/280a1b9c-b9b0-45f9-acca-700ad5d26890" />

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

<img width="1014" height="508" alt="스크린샷 2026-01-28 202941" src="https://github.com/user-attachments/assets/f98d153f-b741-4e63-8345-25d2d1298b1e" />

기존에 파이썬에 있던 txt 파일들을 바탕화면으로 옮겨줬다

<img width="499" height="251" alt="image (25)" src="https://github.com/user-attachments/assets/e660c785-a4b2-4bac-a4c7-bdf201499739" />

해당 파일의 속성을 들어가보면 파일의 절대경로를 알 수 있다.

<img width="1361" height="700" alt="스크린샷 2026-01-28 203244" src="https://github.com/user-attachments/assets/f4fb2fd0-5fe9-4672-8243-14222854afbf" />

파이참으로 돌아가서 해당 main을 실행하면 오류가 발생하는것을 볼 수 있다.

왜냐면 해당 디렉토리에 파일이 없어서 읽을 수 없다.

<img width="1494" height="467" alt="스크린샷 2026-01-28 204307" src="https://github.com/user-attachments/assets/48bd7ad1-33a7-4d9c-8179-f65f95b06a40" />

이렇게 절대 경로를 통해서 파일을 읽을 수 있다.

```python
with open(r"../../OneDrive\바탕 화면\new_file.txt") as file:
    #C:\Users\ernmq\PycharmProjects\day24\main.py
    contents = file.read()
    print(contents)
```

또한 이렇게, 현재 아래 main.py의 경로를 보고 ../../을 통해 ernmq 폴더로 이동 후 바탕 화면 위치를 찾아서 해당 파일을 읽을 수도 있다.

### 메일 머지 프로젝트

<img width="736" height="393" alt="스크린샷 2026-01-28 205348" src="https://github.com/user-attachments/assets/df2e1f45-a127-4bef-b867-dc24d24643af" />

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

<img width="1651" height="397" alt="스크린샷 2026-01-28 205734" src="https://github.com/user-attachments/assets/86d8d290-b7d8-4b1f-b18d-7e0359cbd579" />

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

<img width="1079" height="417" alt="스크린샷 2026-01-28 210550" src="https://github.com/user-attachments/assets/e236babf-7fe3-4a96-bc13-65b709875594" />

<img width="1125" height="480" alt="스크린샷 2026-01-28 210559" src="https://github.com/user-attachments/assets/5c327a06-f3c7-4a18-b765-be947a4b8fc8" />

이렇게 편지에 각각의 이름이 들어갈 수 있음

### 강의 해설

```python
with open("Input/Names/invited_names.txt") as name:
    names = name.readlines()
    print(names)
```

<img width="1076" height="69" alt="스크린샷 2026-01-28 210834" src="https://github.com/user-attachments/assets/285126f4-2260-4005-ad1c-7d99b0a6881a" />

```python
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        print(new_letter)
```

<img width="732" height="670" alt="image (26)" src="https://github.com/user-attachments/assets/a712f921-9d7f-41cf-a76f-a3c5e27f97f6" />

\n이 들어가 있어서 줄이 띄어진 것이 보임

```python
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        print(stripped_name)
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
```

<img width="393" height="294" alt="image (27)" src="https://github.com/user-attachments/assets/508560c5-b8dd-4632-b6a4-0b34b0d8be60" />

strip()을 활용하면 앞 뒤의 공백을 모두 없애줌(\n까지 없애주나봄)

<img width="624" height="824" alt="스크린샷 2026-01-28 211625" src="https://github.com/user-attachments/assets/546f6016-3d18-47e3-b269-1a3e058abc23" />

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

<img width="443" height="412" alt="스크린샷 2026-01-28 211843" src="https://github.com/user-attachments/assets/1f20c04d-8072-4661-9d2d-2cec049ef0bb" />

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

<img width="480" height="297" alt="스크린샷 2026-01-31 202831" src="https://github.com/user-attachments/assets/7c4080c7-0906-4ac3-81ae-060c7262b41f" />

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

<img width="382" height="288" alt="스크린샷 2026-01-31 204900" src="https://github.com/user-attachments/assets/92ff823c-155a-47dc-bf8a-0d6b65cc3360" />

ㅋㅋ지린다, 이래서 판다스판다스 하는구나 3줄로 끝나버리네

<img width="253" height="237" alt="스크린샷 2026-01-31 205018" src="https://github.com/user-attachments/assets/5747e830-bdea-4ea4-8130-b1c2076c2570" />

위 사진처럼 특정 컬럼만 보고싶다면 `print(data["temp"])` 이렇게 대괄호 안에 컬럼을 입력하면 됨

판다스는 첫 번째 줄을 각 열의 제목으로 사용하기 때문에 손쉽게 사용할 수 있음

## 행과 열

```python
print(type(data))
print(type(data["temp"]))
```

<img width="409" height="76" alt="스크린샷 2026-01-31 205352" src="https://github.com/user-attachments/assets/9983dd06-97d5-486a-a683-2d629940839e" />

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

<img width="1389" height="282" alt="스크린샷 2026-01-31 205854" src="https://github.com/user-attachments/assets/c7aee1d7-27ec-4fac-8564-bbbd3cba7ed7" />

리스트 형태를 Dictionary형태로 바꿀 수 있음

```python
temp_list = data["temp"].to_list()
print(temp_list)
print(type(temp_list))
```

data[”temp”] → 시리즈 타입

이 시리즈 타입을 list 타입으로 바꿔줄 수 있음

<img width="595" height="201" alt="스크린샷 2026-01-31 210205" src="https://github.com/user-attachments/assets/eb3856e9-0b02-49a0-aa6a-17eca012889a" />

값은 동일함

### 온도 열에서 평균 온도 구하기

python에서는 수학적인 값들을 계산할 때, numpy라는 라이브러리를 활용함

```python
import numpy

avg = numpy.average(temp_list)
print(avg)
```

<img width="412" height="185" alt="스크린샷 2026-01-31 210604" src="https://github.com/user-attachments/assets/fd60bc33-70bc-4499-b552-74696f88ec28" />

평균값 이외에도 최소, 최대 등등 다양한 함수들이 있음

numpy를 사용하지 않아도 판다스 내부 함수에 평균값을 계산하는 메소드가 있음

```python
avg = data["temp"].mean()
print(avg)
avg2 = temp_list.mean()
print(avg2)
```

avg는 series 타입이며 avg2는 list타입임

<img width="791" height="341" alt="스크린샷 2026-01-31 210926" src="https://github.com/user-attachments/assets/c5911486-0bcd-43f2-a954-c75c27d2f08e" />

당연하지만 list에는 평균값을 구하는 메소드가 없어서 오류가 발생하며, series 타입은 잘 작동함

### 최댓값 최솟값

```python
data_temp = data["temp"]
print(data_temp.max())
print(data_temp.min())
```

<img width="126" height="121" alt="스크린샷 2026-01-31 211122" src="https://github.com/user-attachments/assets/4da3c5c8-318c-4059-b97d-fc7f0cc67eeb" />

### 행 데이터 출력

```python
# 행 데이터 구하기, 월요일
data_monday = data[data.day == "Monday"]
print(data_monday)
```

<img width="400" height="162" alt="스크린샷 2026-01-31 211718" src="https://github.com/user-attachments/assets/372ad688-6bc4-4c60-b770-505b4e59bb7c" />

데이터프레임(data)에서 data.day(day컬럼) 이 월요일인 값을 꺼냄

### 온도가 가장 높은 데이터가 있는 행을 구하기

```python
# 온도가 가장 높은 데어티가 있는 행을 구하기
data_temp_max = data[data.temp == data.temp.max()]
print(data_temp_max)
```

<img width="467" height="213" alt="스크린샷 2026-01-31 213203" src="https://github.com/user-attachments/assets/74cda4e4-a7ea-415b-9cf0-d9a87f93ac3c" />

### dict to dataframe

```python
data_dict = {
    "students": ["Amy", "Jack", "Mike"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
```

<img width="566" height="259" alt="스크린샷 2026-01-31 215024" src="https://github.com/user-attachments/assets/629e6783-7015-4346-9f92-aa29d82da05a" />

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

<img width="424" height="204" alt="스크린샷 2026-01-31 215146" src="https://github.com/user-attachments/assets/90ee26b4-1b56-4008-a408-7e2b77fb0c60" />

이렇게 to_csv를 활용해서 새롭게 파일로 추가할 수 있음

## 판다스로 하는 데이터 분석

<img width="1535" height="565" alt="스크린샷 2026-01-31 215822" src="https://github.com/user-attachments/assets/4013002c-6776-46ef-8d4b-adad2f96a0c0" />

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

<img width="1164" height="1119" alt="스크린샷 2026-02-01 014223" src="https://github.com/user-attachments/assets/955a1fe9-1a7a-4480-bd12-3e7fe284cf7d" />

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

<img width="1517" height="858" alt="스크린샷 2026-02-01 015054" src="https://github.com/user-attachments/assets/247f3eaf-7dbd-415b-9fd4-84d76d7617d1" />

이제 주들의 중심 좌표를 알았다면 csv파일에 정리할 수 있다(사실 파일로 이미 받았음)

<img width="685" height="592" alt="스크린샷 2026-02-01 015207" src="https://github.com/user-attachments/assets/85b62b22-8265-4868-9173-9257ed8793fa" />

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

<img width="590" height="289" alt="스크린샷 2026-02-01 165624" src="https://github.com/user-attachments/assets/4a1e2be5-ccd5-4859-a04c-540ca3de8e1f" />

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

<img width="791" height="325" alt="스크린샷 2026-02-01 170315" src="https://github.com/user-attachments/assets/c6db8ee3-5cc6-4bc6-8736-bcd07bf32dce" />

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

<img width="829" height="331" alt="스크린샷 2026-02-01 170745" src="https://github.com/user-attachments/assets/8d0dcb29-5b79-46c2-8539-7152b16990de" />

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

<img width="805" height="307" alt="스크린샷 2026-02-01 171730" src="https://github.com/user-attachments/assets/ab8ad9d4-c426-4e25-b387-1fcd5f429edb" />

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

<img width="1675" height="115" alt="스크린샷 2026-02-01 173157" src="https://github.com/user-attachments/assets/150def59-bd51-4c1c-bf5c-e74fd3f8b540" />

```python
# 딕셔너리를 활용한 컴프리헨션
passed_students = {key:value for(key, value) in dict.items(students_scores) if value > 60}
print(passed_students)
```

<img width="978" height="73" alt="스크린샷 2026-02-01 173950" src="https://github.com/user-attachments/assets/e4e622d1-fffe-43b8-9622-57b222cd49d0" />

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

<img width="785" height="294" alt="스크린샷 2026-02-01 174610" src="https://github.com/user-attachments/assets/5d230aba-aaa7-485f-9ca9-d84ec5e18906" />

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

<img width="833" height="298" alt="스크린샷 2026-02-01 174911" src="https://github.com/user-attachments/assets/45dc066b-4ae3-459c-80f0-26d07f8de639" />

## 판다스 데이터 프레임에서 반복하는 방법

```python
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for(key, value) in student_data_frame.items():
    print(key)
    print(value)
```

<img width="408" height="471" alt="스크린샷 2026-02-01 175441" src="https://github.com/user-attachments/assets/bc44470c-b0c8-4903-ab07-e27906187ac9" />

위의 코드는 컬럼을 기준으로 해당 데이터들을 뽑은 것

```python
for(index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
```

<img width="446" height="417" alt="스크린샷 2026-02-01 175746" src="https://github.com/user-attachments/assets/af3622b9-0206-401c-8a57-87bbb19cb186" />

index와 iterrows() 메서드를 통해서 해당 index의 행을 뽑을 수 있음(유의미한 데이터값)

그럼 1번째 행의 score를 뽑기 위해서는?

```python
for(index, row) in student_data_frame.iterrows():
    if index == 1:
        print(row.score)
```

<img width="362" height="110" alt="스크린샷 2026-02-01 180020" src="https://github.com/user-attachments/assets/1bf90e48-4ad7-4077-b041-89101eb2d4b3" />

## NATO 알파벳 음성기호 프로젝트

<img width="357" height="180" alt="스크린샷 2026-02-01 180230" src="https://github.com/user-attachments/assets/48392657-433f-41d0-9cdd-a23c4de1adc6" />

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

<img width="1876" height="200" alt="스크린샷 2026-02-01 181512" src="https://github.com/user-attachments/assets/59022579-8ceb-497a-9b2d-019f7addf5da" />

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

<img width="509" height="158" alt="스크린샷 2026-02-01 182524" src="https://github.com/user-attachments/assets/789bf3fd-5903-4e2e-b2b1-419b1f17cfa1" />

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

<img width="1221" height="874" alt="스크린샷 2026-02-02 192828" src="https://github.com/user-attachments/assets/5a35be65-8e1e-4739-9e14-d9aa8a51f0a5" />

tutle 패키지 처럼, 파이썬에서 GUI를 표현해주는 라이브러리로 tkinter 패키지 안에 Tk 클래스를 활용해서 화면을 만들고 사이즈를 정할 수 있다.

또한 화면에 라벨링을 해줄 수 있는데 tkinter.Label() 을 통해 만들 수 있으며 소괄호 안에 내가 원하는 문자열과 폰트 등을 지정할 수 있다.

pack 메서드는 라벨의 위치, 크기 등을 변환할 수 있는 메서드이다.

<img width="1455" height="815" alt="스크린샷 2026-02-02 193216" src="https://github.com/user-attachments/assets/4bdc8dd6-f4cd-4a0f-b3e4-426465a17800" />

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

<img width="253" height="207" alt="스크린샷 2026-02-02 193701" src="https://github.com/user-attachments/assets/7fcbc882-8c91-4fac-a91f-8930ca7d8a36" />

이렇게 기본값을 가지면 그냥 함수를 불러도, 만약 값을 바꾸고 싶다면 b만 바꿔도 나머지 인자들은 default 값을 가지기 때문에 함수가 잘 작동한다.

## args : 여러 인수를 갖는 함수 만들기

```python
def add_arg(*args):
    for n in args:
        print(n)

add_arg(3,5,7,9)
```

인자로 *args 를 사용하면 여러 값을 받는 파라미터가 된다.

<img width="279" height="163" alt="스크린샷 2026-02-02 194656" src="https://github.com/user-attachments/assets/47720488-9f3b-4348-93fd-4fb37b7b8587" />

기본적으로 print(args)를 하게 된다면 tuple 형태가 나옴

ex) : (3,5,7,9)

## **kwargs: 임의의 숫자 키워드 인수 다루기

```python
def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))

calculate(add=3, multiply=5)
```

<img width="383" height="165" alt="스크린샷 2026-02-02 195349" src="https://github.com/user-attachments/assets/8ab3cc18-c84c-4e86-b172-d78162d4e954" />

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

<img width="402" height="315" alt="스크린샷 2026-02-02 195554" src="https://github.com/user-attachments/assets/109d9e54-05b4-4ba5-a8fb-67b5726e5b6e" />

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

<img width="126" height="63" alt="스크린샷 2026-02-02 200454" src="https://github.com/user-attachments/assets/2602cf2f-1ae0-4b57-a770-acff4ffbbecc" />

만약에 생성할 때, model의 값을 주지 않는다면 아래 사진처럼 model의 값을 주지 않아서 오류가 발생함

<img width="897" height="262" alt="스크린샷 2026-02-02 200918" src="https://github.com/user-attachments/assets/a9ca6ce5-f319-4185-acc5-08317c70df6e" />

```python
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)
```

딕셔너리는 [] 말고도 .get으로도 value를 불러올 수 있으며 이렇게 get으로 불러오면 없는 값이 있어도 오류가 뜨지 않는다

<img width="395" height="109" alt="스크린샷 2026-02-02 201052" src="https://github.com/user-attachments/assets/b2cf7fce-6299-4ffd-9e36-ab189af1c4e1" />

## Tkinter 위젯 설정 바꾸기

<img width="779" height="508" alt="스크린샷 2026-02-02 201826" src="https://github.com/user-attachments/assets/c7d92369-e9c4-4dd9-b148-910698819718" />

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

<img width="280" height="293" alt="스크린샷 2026-02-02 202214" src="https://github.com/user-attachments/assets/40528559-c807-4564-9c38-16f54a954b6e" />

### 버튼 클릭 시 라벨 변환

```python
def button_click():
    my_label["text"] = "Button Clicked"

button = tkinter.Button(text="Click Me", command=button_click)
button.pack()
```

<img width="804" height="543" alt="스크린샷 2026-02-02 202346" src="https://github.com/user-attachments/assets/b35a5473-9274-4828-ae23-5a128a2dc5ac" />

위에서도 말했지만 config로도 변환이 가능하다

### Entry

```python
# Entry
input = tkinter.Entry()
input.pack()
```

<img width="777" height="541" alt="스크린샷 2026-02-02 202553" src="https://github.com/user-attachments/assets/b11b802e-26b3-4654-8c0e-7d72d79062ee" />

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

<img width="772" height="515" alt="스크린샷 2026-02-02 202858" src="https://github.com/user-attachments/assets/3a49950b-fa65-4bdb-94e6-53ea9704de70" />

<img width="249" height="234" alt="스크린샷 2026-02-02 202906" src="https://github.com/user-attachments/assets/1e9f37f7-1e63-4f0f-8ffb-68ef674e854f" />

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

<img width="771" height="825" alt="스크린샷 2026-02-02 203914" src="https://github.com/user-attachments/assets/b82053ec-081a-4b43-8a4f-25a2eba57fbf" />

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

<img width="775" height="505" alt="스크린샷 2026-02-02 205104" src="https://github.com/user-attachments/assets/35dd425b-a10a-4b8e-ade0-5c976e16b63c" />

 

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

<img width="769" height="532" alt="스크린샷 2026-02-02 205326" src="https://github.com/user-attachments/assets/93b64c3f-16bc-469e-a280-0ca8177bb259" />

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

<img width="607" height="351" alt="스크린샷 2026-02-02 211012" src="https://github.com/user-attachments/assets/657c4179-3c3c-48c2-8b14-c478352b90e8" />

거의 똑같은데 하나 추가하자면 

```python
def calc():
    mile = float(input.get())
    ans_km = round(mile * 1.609)
    answer.config(text=ans_km)
```

이렇게 해주는게 더 깔끔해보임

끝!
