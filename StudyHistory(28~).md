## 28 일차
## Pomodoro 프로젝트

<img width="621" height="519" alt="스크린샷 2026-02-04 201034" src="https://github.com/user-attachments/assets/839fa672-0cfa-4180-8459-2d28d9f3b85b" />

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

<img width="349" height="410" alt="스크린샷 2026-02-04 201831" src="https://github.com/user-attachments/assets/08ce63f3-9ce8-49eb-83c0-b0f03a83ab29" />

이렇게 작업하면 귀여운 토마토가 배경에 나오게 된다

```python
canvas.create_text(103,112, text="00:00")
```

canvas에는 text도 넣을 수 있는데 위의 코드를 작성 후 실행해주면

<img width="630" height="549" alt="스크린샷 2026-02-04 202232" src="https://github.com/user-attachments/assets/39b7fbf0-5ce6-4316-b4f0-63d66f8227bf" />

이렇게 지정해준 위치에 텍스트가 표시된다.

(화면에 공백은 window.config(padx, pady)를 넣어줬다.)

이제 canvas text에 추가적으로 값을 더 넣어서 텍스트를 꾸며본다.

색상을 정해주는 fill과 폰트를 정해주는 font를 설정

```python
canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) 
```

<img width="610" height="546" alt="스크린샷 2026-02-04 202528" src="https://github.com/user-attachments/assets/35474454-9a53-4497-ac7d-4fc27f10ecd5" />

배경이 밋밋하니 배경 색을 추가해보자

```python
window.config(padx=100, pady=50, bg=YELLOW)
```

여기서 YELLOW는 상수로 위에 정의해둔 색상 코드이다. bg에는 원래 `"#f7f5dd"` 이렇게 색상 코드가 들어가야 한다.

<img width="634" height="548" alt="스크린샷 2026-02-04 202855" src="https://github.com/user-attachments/assets/dd988006-74d3-4fb1-ac82-d173a8a5d2d6" />

실행을 해보니, canvas영역인 부분은 배경색이 여전히 흰색이다.

canvas에도 배경색을 추가해보자

```python
canvas = Canvas(width=200, height=224, bg=YELLOW)
```

<img width="615" height="553" alt="스크린샷 2026-02-04 203044" src="https://github.com/user-attachments/assets/a292b93d-d946-46b6-bcfb-c930843049cc" />

잘 안보이는데 canvas영역에 약간의 경계선으로 하얀색이 보인다.

이를 제거하려면 canvas에 `highlightthickness=0` 을 설정해줘야 한다.

<img width="618" height="544" alt="스크린샷 2026-02-04 203227" src="https://github.com/user-attachments/assets/b1182aeb-0380-4d86-a6e4-3a4f105476a9" />

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

<img width="536" height="459" alt="스크린샷 2026-02-04 203643" src="https://github.com/user-attachments/assets/db417347-a6a5-48c0-8b63-634d48234d20" />

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

<img width="739" height="728" alt="스크린샷 2026-02-04 204935" src="https://github.com/user-attachments/assets/1b4210c6-f6d8-4573-8a5f-08dc4a80d1bf" />

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

<img width="756" height="736" alt="스크린샷 2026-02-05 090807" src="https://github.com/user-attachments/assets/715624ba-6257-4cd2-9c5c-d27459d4c903" />

### 버튼과 연계

위에서 count_down(5)를 따로 아래 실행해줬는데 버튼을 누르면 시작되는 함수로 만들어준다.

```python
def start_timer():
    count_down(5)
    
start_button = Button(text="Start", command=start_timer)
```

<img width="747" height="730" alt="스크린샷 2026-02-05 091307" src="https://github.com/user-attachments/assets/5ad40183-0edc-4c07-9c49-f2f39936a631" />

<img width="741" height="723" alt="스크린샷 2026-02-05 091319" src="https://github.com/user-attachments/assets/c9ee942f-66e0-4911-8e6f-c4d397f91180" />

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

<img width="749" height="732" alt="스크린샷 2026-02-05 092845" src="https://github.com/user-attachments/assets/dd634718-5747-4d0f-b0cb-92d917a72199" />

하지만 문제가 처음 시작할 때 5:0 → 이렇게 표시가 된다

이거를 5:00로 변경해야 한다.

### 파이썬 동적 타이핑

<img width="747" height="729" alt="스크린샷 2026-02-05 094221" src="https://github.com/user-attachments/assets/14ee5fea-c6a1-42f9-a39b-2f8b2976771c" />

이 문제를 해결하기 위해서는 동적 타이핑이 필요하다

<img width="755" height="211" alt="스크린샷 2026-02-05 094450" src="https://github.com/user-attachments/assets/717d21f1-97d7-476c-9b8f-05f2a022195b" />

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

<img width="732" height="727" alt="스크린샷 2026-02-05 095112" src="https://github.com/user-attachments/assets/857d90db-a968-406b-97be-27808fb1e84d" />

<img width="744" height="727" alt="스크린샷 2026-02-05 095124" src="https://github.com/user-attachments/assets/1769a76b-adb8-4948-8538-987ad4d40510" />

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

<img width="738" height="739" alt="스크린샷 2026-02-05 101724" src="https://github.com/user-attachments/assets/f7a23b11-fa7e-4114-8076-ecce3c7d27d2" />

검증을 위해서 우선 1분을 기본으로 설정 

<img width="843" height="744" alt="스크린샷 2026-02-05 101827" src="https://github.com/user-attachments/assets/72b2293d-34c3-4594-91b7-c42590bf3b1f" />

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

<img width="257" height="136" alt="스크린샷 2026-02-05 103156" src="https://github.com/user-attachments/assets/be1fdea0-e697-4af1-ad70-fd91833e76b1" />

<img width="745" height="728" alt="스크린샷 2026-02-05 103213" src="https://github.com/user-attachments/assets/a8d7a98b-0935-45ab-89a2-1bb2d32f015d" />

<img width="738" height="726" alt="스크린샷 2026-02-05 103505" src="https://github.com/user-attachments/assets/92fbf257-8f13-4e75-985c-ed17cd81096c" />

<img width="746" height="723" alt="스크린샷 2026-02-05 103705" src="https://github.com/user-attachments/assets/896f76a5-46bb-4f99-bdbc-4e58f8df48a3" />

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

<img width="888" height="736" alt="스크린샷 2026-02-05 105842" src="https://github.com/user-attachments/assets/c5bceb9d-654b-48f3-a7e7-317881453bfe" />

<img width="889" height="735" alt="스크린샷 2026-02-05 105854" src="https://github.com/user-attachments/assets/bf6f00a4-c3d3-4b01-88ef-dfdd9ba39044" />

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

## 29일차
## 패스워드 저장 및 생성 프로그램(Tkinter로 GUI 구현)

### 캔바스를 활용해서 이미지 생성하기

```java
window = Tk()
window.title("password encoder")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image)
canvas.pack()
```

<img width="477" height="531" alt="image" src="https://github.com/user-attachments/assets/48c003ae-3d1c-4672-86b4-dd882a64de30" />

### grid()와 columnspan으로 사용자 인터페이스 완성하기

columnspan이란 열을 추가하지 않고도 이어서 추가함

grid(row=2, column=0, columnspan=2) → 컬럼이 0~1까지 2

```java
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image)
canvas.grid(row=0, column=1)

site_label = Label(text="Website:")
site_label.grid(row=1,column=0)

email_name_label = Label(text="Email/Username:")
email_name_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry = Entry(width=37)
website_entry.grid(row=1,column=1,columnspan=2)

email_name_entry = Entry(width=37)
email_name_entry.grid(row=2, column=1,columnspan=2)

password_entry = Entry(width=28)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Password")
generate_button.grid(row=3,column=2)

add_button = Button(text="Add", width=37)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
```

<img width="715" height="674" alt="image" src="https://github.com/user-attachments/assets/d30257e8-23e1-4038-a2b8-0a5fd0e926f8" />

위의 코드에서 지정한 width의 숫자는 컴퓨터마다 다를 수 있음.(나도 강의에서 했던 숫자로 하면 위젯의 배치가 이상해져서 내가 수정함)

### 데이터를 파일에 저장하기

<img width="486" height="444" alt="image (29)" src="https://github.com/user-attachments/assets/ff720186-a4d8-459f-998b-13bb22242d35" />

<img width="477" height="438" alt="image (30)" src="https://github.com/user-attachments/assets/8da364b8-a951-4345-9873-03007b7406f0" />

이 두 사진은 모두 처음 실행 했을 때 사진이다. 같아  보이지만 약간의 차이점이라면, 두번째 사진은 들어가자마자 Website에 focus가 되어있다. 

```java
website_entry.focus()
```

위의 코드를 써주면 되고 실행하면 사진처럼 포커스가 된다.

만약 값을 미리 입력해두고 싶다면 insert 메서드를 활용할 수 있다.

`email_name_entry.insert(0, "email.com")`

<img width="591" height="536" alt="image (31)" src="https://github.com/user-attachments/assets/abf985c5-395f-46ad-abf0-72bf6d2943e4" />

```java
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image)
canvas.grid(row=0, column=1)

site_label = Label(text="Website:")
site_label.grid(row=1,column=0)

email_name_label = Label(text="Email/Username:")
email_name_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry = Entry(width=37)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_name_entry = Entry(width=37)
email_name_entry.grid(row=2, column=1,columnspan=2)
email_name_entry.insert(0, "email.com")

password_entry = Entry(width=28)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Password")
generate_button.grid(row=3,column=2)

add_button = Button(text="Add", width=37)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
```

### 도전과제

website, email, password에 입력한 값을 data.txt라는 이름으로 저장하기

Add 버튼을 누르면 저장이 되어야 하므로 command 파라미터를 활용함

Add 버튼을 누르면 email을 제외한 나머지 값들은 모두 사라져야 함

1. `add_button = Button(text="Add", width=37, command=save_identity)` 
    
    command 함수 추가
    
2. 함수 생성
    
    ```java
    def save_identity():
        website = website_entry.get()
        password = password_entry.get()
        email = email_name_entry.get()
        with open("data.txt", mode="a") as data:
            data.write(f"{website} | {email} | {password}\n")
    
        website_entry.delete(0, last=END)
        password_entry.delete(0, last=END)
    ```
    

각 entry의 값을 변수로 할당 → get() 활용

open 메서드와 with as를 활용해 파일을 쓰고 누를 때 마다 추가 → mode - a

<img width="742" height="209" alt="스크린샷 2026-02-07 203804" src="https://github.com/user-attachments/assets/9ef8bd22-dfe8-4657-a0d8-2f515ddc0a68" />

마지막으로 delete 메서드를 활용  → 0 ~ END(last index) 

![화면 녹화 중 2026-02-07 213951](https://github.com/user-attachments/assets/27d77b9c-e9c4-46e4-9bfe-7dcb09c892ad)

### Tkinter의 대화박스와 팝업창

Add를 눌렀는데 갑자기 내가 입력한 website와 password가 사라진다면? 사용자 입장에서는 ux가 매우 좋지 않음, 따라서 add를 눌렀을 때, 잘 실행됐다는 표시를 대화박스와 팝업창을 통해서 알려줌

```java
def save_identity():
    website = website_entry.get()
    password = password_entry.get()
    email = email_name_entry.get()

    ***messagebox.showinfo(title="title", message="my first messagebox")***

    with open("data.txt", mode="a") as data:
        data.write(f"{website} | {email} | {password}\n")

    website_entry.delete(0, last=END)
    password_entry.delete(0, last=END)
```

<img width="775" height="673" alt="스크린샷 2026-02-07 204832" src="https://github.com/user-attachments/assets/64bce394-120b-45c7-93f9-cc7cd8251121" />

add버튼을 누르면 위 사진처럼 messagebox가 뜸

```java
def save_identity():
    website = website_entry.get()
    password = password_entry.get()
    email = email_name_entry.get()

    user_select = messagebox.askokcancel(title="save", message="정보를 파일에 저장하시겠습니까?")
    print(user_select)

    if user_select:
        with open("data.txt", mode="a") as data:
            data.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, last=END)
        password_entry.delete(0, last=END)
```

askokcancel은 확인과 취소로 창을 띄워주며, 해당 값은 True와 False를 가짐

따라서 확인을 누를 때만, 정보를 저장 후 화면에서 삭제시킴

<img width="796" height="813" alt="스크린샷 2026-02-07 205259" src="https://github.com/user-attachments/assets/8ef008b3-b2b4-4932-903b-72f7c7701751" />

정보를 입력, data 파일에는 아직 아무것도 없음

<img width="792" height="806" alt="스크린샷 2026-02-07 205337" src="https://github.com/user-attachments/assets/cc33f354-7cfe-4b6c-a23f-1829b525b3d1" />

Add  버튼을 누르면 팝업 창이 뜨게 되며 선택을 할 수 있음

<img width="828" height="810" alt="스크린샷 2026-02-07 205405" src="https://github.com/user-attachments/assets/ca02be51-de9c-4593-b53e-d749afefbcda" />

<img width="776" height="728" alt="스크린샷 2026-02-07 205451" src="https://github.com/user-attachments/assets/db3c586b-e88d-4032-9245-20fd41020ea7" />

취소를 선택하면 아무 일도 일어나지 않고, 확인을 선택하면 데이터가 저장되는 것을 볼 수 있음

### 입력 값 검증

만약에 website나 password 등 값이 존재하지 않으면 오류 messagebox를 띄우는 과제

```java
def save_identity():
    is_full = True
    website = website_entry.get().strip()
    password = password_entry.get().strip()
    email = email_name_entry.get().strip()
    print(len(password))
    if len(website) < 1 or len(password) < 1 or len(email) < 1:
        messagebox.showerror(title="필드 에러" ,message="빈 필드가 존재합니다. 필드를 모두 채워주세요")
        is_full = False

    if is_full:
        user_select = messagebox.askokcancel(title="save", message="정보를 파일에 저장하시겠습니까?")
        print(user_select)

        if user_select:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, last=END)
            password_entry.delete(0, last=END)

            messagebox.showinfo(title="save", message="저장되었습니다")
```

1. boolean 변수 생성
2. strip()을 사용해 공백 제거
3. 각 길이를 꺼내서 1보다 작은 값이 하나라도 존재하면 오류 메세지 박스 생성 후 is_full을 False로 설정
4. 그 다음 로직에 조건문으로 is_full을 설정

<img width="738" height="674" alt="스크린샷 2026-02-07 210657" src="https://github.com/user-attachments/assets/ee2210c8-c193-4a9f-a629-127f26c565d2" />

### 패스워드 생성하고 클립보드에 복사하기

```java
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
```

강의에서 주어진 암호화 코드로 8~9자리의 문자, 2~3자리의 숫자, 2~3자리의 기호를 활용해 비밀번호 생성

생성된 password_list값을 shuffle을 활용해서 섞어주면 비밀번호가 완성됨

우선 복잡한 반복문을 제거하고 list 컴프리헨션으로 변경

```java
password_letters = [random.choice(letters) for _ in range(nr_letters)]
password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

password_list = password_letters + password_symbols + password_numbers

print(password_list)
```

<img width="919" height="91" alt="스크린샷 2026-02-07 212955" src="https://github.com/user-attachments/assets/3916e315-4843-492b-8a7e-19f300227dc1" />

```java
encrypt_password = ""
    for char in password_list:
      encrypt_password += char
      
=>

encrypt_password = "".join(password_list)
    print(f"Your password is: {encrypt_password}")
```

복잡한 리스트를 string으로 변환해주는 작업을 join 메서드를 활용해서 한줄로 끝낼 수 있음

join은 앞의 기호를 기준으로 괄호 안에 있는 여러 값을 결합해줌

```java
def encrypt():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    print(password_list)
    shuffle(password_list)

    encrypt_password = "".join(password_list)
    print(f"Your password is: {encrypt_password}")

    password_entry.insert(0, encrypt_password)
```

이제 암호화 메서드를 완성했으니 암호화 버튼에 command 함수를 추가해주기만 하면 암호화 프로젝트 완성

![화면 녹화 중 2026-02-07 214049](https://github.com/user-attachments/assets/8961429a-8fb1-47bc-88a9-492afc1ca79f)

### 패스워드를 클립보드에 복사하기

비밀번호 생성 버튼을 클릭하면 복사되는 기능

두 문장이면 된다

```java
import pyperclip
```

일단 패키지를 가져오고 암호화 함수 가장 마지막에 copy 메서드를 사용

```java
pyperclip.copy(encrypt_password)
```

![화면 녹화 중 2026-02-07 214431](https://github.com/user-attachments/assets/9dcd3856-a233-431e-80c6-6b78ca97a72c)
