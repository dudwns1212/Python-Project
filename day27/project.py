from tkinter import *
from turtledemo.penrose import start

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=40, pady=40)

def calc():
    mile = float(input.get())
    ans_km = round(mile * 1.609)
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









window.mainloop()