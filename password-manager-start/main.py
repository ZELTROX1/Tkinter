from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_genrator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

    password1: str = ""
    for char in password_list:
        password1 += char
    text_password.delete(0, END)
    text_password.insert(0, password1)
    pyperclip.copy(password1)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    email = text_username.get()
    web = text_website.get()
    usr_pass = text_password.get()
    if len(web)==0 or len(usr_pass)==0:
        messagebox.showinfo(title="ERROR", message="You can not add a empty Credentials")
    elif messagebox.askyesno(title=web, message=f"The details entered are:\nEmail:{email}\nPassword:{usr_pass}\nWebsite:{web}\nCan we conform"):
        with open("user_text","a") as f:
            f.write(f"Email:{email} | website:{web} | password:{usr_pass}\n")
            text_website.delete(0,END)
            text_password.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password-manger-start")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=1, row=0)

website = Label(text="Website:",font=("Times New Roman",8))
website.grid(column=0,row=1)

text_website = Entry(width=35)
text_website.focus()
text_website.grid(column=1,row=1,columnspan=2)

username = Label(text="Email/Username:",font=("Times New Roman",8))
username.grid(column=0, row=2)

text_username = Entry(width=35)
text_username.insert(0,"praneet0210@gmail.com")
text_username.grid(column=1, row=2,columnspan=2)

password = Label(text="Password:",font=("Times New Roman",8))
password.grid(column=0,row=3)

text_password = Entry(width=21)
text_password.grid(column=1,row=3)

generate_password = Button(text="Generate Password",width=12,font=("Airal",6),command=password_genrator)
generate_password.grid(column=2,row=3)

add = Button(text="Add",width=36,command=add_password)
add.grid(column=1,row=4,columnspan=2)




window.mainloop()