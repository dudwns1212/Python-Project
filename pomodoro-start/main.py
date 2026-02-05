from tkinter import *
import math
import time
from numpy.ma.core import size

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
resp = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global resp
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text ,text="00:00")
    check_label.config(text="")
    resp = 0
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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
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
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        if resp % 2 == 0:
            mark = ""
            for _ in range(math.floor(resp/2)):
                mark += "✓"
                check_label.config(text=mark)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# label
timer_label = Label(bg=YELLOW, fg=GREEN, text="Timer", font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)
check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=3)

# button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)









window.mainloop()