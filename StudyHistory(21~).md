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
