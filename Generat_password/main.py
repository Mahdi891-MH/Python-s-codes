import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    password_list += [choice(letters) for letter in range(randint(8, 10))]
    password_list += [choice(numbers) for number in range(randint(2, 4))]
    password_list += [choice(symbols) for symbol in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(END, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = entry_web.get()
    password = entry_password.get()
    email = entry_email.get()
    new_data = {web:{
                "email": email,
                "password": password
                }
                }
    if len(web)==0 or len(password)==0 or len(email)== 0:
        messagebox.showinfo("Oops", "Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            entry_web.delete(0,END)
            entry_password.delete(0, END)
            entry_web.focus()
# ---------------------------- Find PASSWORD ------------------------------- #
def find_password():
    website = entry_web.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(website, f"Email: {email}\n\nPassword: {password}")
        else:
            messagebox.showinfo("Not found",f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")
canvas = Canvas(height=200, width=200, highlightthickness=0)
lock_image= PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)
lbl_website = Label(text="Website:")
lbl_website.grid(row=1, column=0)
lbl_email = Label(text="Email/Username:")
lbl_email.grid(row=2, column=0)
lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0)
entry_web = Entry(width=21)
entry_web.focus()
entry_web.grid(row=1, column=1)
entry_email = Entry(width=35)
entry_email.insert(0, "aliahmadi89@gmail.com")
entry_email.grid(row=2, column=1, columnspan=2)
entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)
btn_generate = Button(text="Generate Password", command= generate)
btn_generate.grid(row=3, column=2)
btn_add = Button(text="Add", width=30, command= save)
btn_add.grid(row=4, column=1, columnspan=2)
btn_search = Button(text="Search", width=14, command=find_password)
btn_search.grid(row=1, column=2)
window.mainloop()


