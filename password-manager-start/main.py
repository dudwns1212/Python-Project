from logging import raiseExceptions
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# 위에 *로 다 import했는데 왜 또 import해요?
# -> *은 실제로 모든 클래스와 상수만을 가져오지, 또 다른 코드 모듈인 messagebox는 가져오지 못함
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

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

    pyperclip.copy(encrypt_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_identity():
    is_full = True
    website = website_entry.get().strip()
    password = password_entry.get().strip()
    email = email_name_entry.get().strip()

    new_data = {
        website: {
            "email":email,
            "password": password,
        }
    }

    if len(website) < 1 or len(password) < 1 or len(email) < 1:
        messagebox.showerror(title="필드 에러" ,message="빈 필드가 존재합니다. 필드를 모두 채워주세요")
        is_full = False

    if is_full:
        user_select = messagebox.askokcancel(title="save", message="정보를 파일에 저장하시겠습니까?")
        print(user_select)
        if user_select:
            try:
                with open("data.json", mode="r") as data_file:
                    # 1. 데이터를 읽음
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    # 2. 파일이 없다면 데이터를 새로 씀
                    json.dump(new_data, data_file, indent=4)
            else:
                # 3. 오류가 나지 않는다면 데이터를 업데이트
                data.update(new_data)

                with open("data.json", mode="w") as data_file:
                    # 업데이트 된 데이터를 파일에 업데이트
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, last=END)
                password_entry.delete(0, last=END)

            messagebox.showinfo(title="save", message="저장되었습니다")

def search():
    website = website_entry.get().strip()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="User Info", message=f"email: {email}\npassword: {password}")
    except KeyError:
        messagebox.showerror(title="Key Error", message="해당 웹사이트가 없음")

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

website_entry = Entry(width=28)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_name_entry = Entry(width=37)
email_name_entry.grid(row=2, column=1,columnspan=2)
email_name_entry.insert(0, "email.com")

password_entry = Entry(width=28)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Password", command=encrypt)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add", width=37, command=save_identity)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search", width=7 , command=search)
search_button.grid(row=1, column=2)

window.mainloop()