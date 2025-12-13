from tkinter import *
import tools
from customer import Customer
class Login:
    def __init__(self):
        self.window = Tk()
        self.window.overrideredirect(True)
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window.config(bg="#639ba9")
        self.window.update_idletasks()
        self.window_width = self.window.winfo_width()
        self.window_height = self.window.winfo_height()
        x = ((self.screen_width-self.window_width)//2)-70
        y = (self.screen_height-self.window_height)//2
        self.window.geometry(f"+{x}+{y}")
        self.border_width = self.window.winfo_rootx()-self.window.winfo_x()
        self.titlebar_height = self.window.winfo_rooty()-self.window.winfo_y()
        self.window.title("Electricity Bill Payment System")
        self.lbl_title = Label(text="Login to System", font=("arial", 20, 'normal'), bg="#639ba9")
        self.lbl_title.grid(row=0, column=0, columnspan=2, pady= 20)
        self.lbl_username = Label(text="Username:", bg="#639ba9")
        self.lbl_username.grid(row=1, column= 0, pady=10, padx=(50, 0))
        self.entry_username = Entry(width=35)
        self.entry_username.grid(row=1, column=1, ipady=4, padx=(0, 50))
        self.lbl_password = Label(text="Password:", bg="#639ba9")
        self.lbl_password.grid(row=2, column=0, pady=10, padx=(50, 0))
        self.entry_password = Entry(width=35, show="*")
        self.entry_password.grid(row=2, column=1, ipady=4, padx=(0, 50))
        self.btn_login = Button(self.window,text="Login", width=10,bg="green",fg="white", command=self.login)
        self.btn_login.grid(row=3, column=1, pady=10, sticky="w")
        self.btn_exit = Button(self.window,text="Exit",bg="#b30000", fg="white", command=self.window.destroy, width=10)
        self.btn_exit.grid(row=3, column=1, pady=10, sticky="e", padx=(0, 50))
        self.message = Label(text="", fg="#af0000", bg="#639ba9", font=('arial', 10, 'bold'))
        self.message.grid(row=4, column=1, padx=(0, 50), pady=(0, 15))

        self.window.mainloop()

    def login(self):
        user = self.entry_username.get()
        password = self.entry_password.get()
        con = tools.connect()
        cursor = con.cursor()
        cursor.execute(f"select * from user where user_name = '{user}' and password = '{password}';")
        result = cursor.fetchall()
        if len(result) == 0:
            self.message.config(text="incorrect username or password!")
        else:
            self.window.destroy()
            Customer()

