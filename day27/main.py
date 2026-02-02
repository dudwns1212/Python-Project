import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


def my_function(a=1, b=2, c=3):
    sum_param = a + b + c
    print(sum_param)

my_function()
my_function(b=5)

def add(n1, n2):
    return n1 + n2

add(1,5)

def add_arg(*args):
    sum_param = 0
    for n in args:
        sum_param += n
    print(sum_param)

add_arg(3,5,7,9)

def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)

    print(kwargs["add"])

calculate(add=3, multiply=5)

def cal(n, **kwargs):
    n += kwargs["add"]
    n -= kwargs["minus"]
    n *= kwargs["gop"]
    print(n)

cal(2,add=3, gop=3, minus=1)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.model)

def button_click():
    my_label["text"] = "Button Clicked"
    print(input.get())

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






window.mainloop()