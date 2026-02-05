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

![image.png](attachment:357600a8-af24-4157-b000-eef8519b2f6a:image.png)

![image.png](attachment:e16699bd-2e21-4857-9e09-f7f94c98b44e:image.png)

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
