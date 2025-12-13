from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import tools
import helper

class Payment:
    def __init__(self):
        self.window  = Tk()
        self.window.state('zoomed')
        self.window.config(bg="#639ba9")
        self.window.title("Electricity Bill Payment System")
        self.lblTitle = Label(text="Payment Detail", font=("Engravers MT", 20, "bold"), bg="#639ba9")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=(20, 50), padx=(220,0))
        self.tree = ttk.Treeview(self.window, columns=("p_id", "b_id", "date", "amound", "method"),show="headings", height=15)

        style = ttk.Style()
        style.configure("Treeview.Heading", font= ("Segoe UI", 8, "bold"))

        f_style = ttk.Style()
        f_style.configure("Custom.TFrame", background="#639ba9")

        self.panel = ttk.Frame(style="Custom.TFrame")
        self.panel.grid(row=1, column=1, padx=(50, 0))
        self.lbl_p_id = Label(self.panel, text="Payment ID: ", bg="#639ba9")
        self.lbl_p_id.grid(row=0, column=0, pady=10)
        self.entry_p_id = Entry(self.panel, width=30)
        self.entry_p_id.grid(row=0, column=1, ipady=4, columnspan=2)
        self.lbl_b_id = Label(self.panel, text="Bill ID: ", bg="#639ba9")
        self.lbl_b_id.grid(row=1, column=0, pady=10)
        self.entry_b_id = Entry(self.panel, width=30)
        self.entry_b_id.grid(row=1, column=1, ipady=4, columnspan=2)
        self.lbl_date = Label(self.panel,text="Payment Date: ", bg="#639ba9")
        self.lbl_date.grid(row=2, column=0, pady=10)
        self.entry_date = Entry(self.panel,width=30)
        self.entry_date.grid(row=2, column=1, ipady=4, columnspan=2)
        self.lbl_amound = Label(self.panel, text="Amound Paid: ", bg="#639ba9")
        self.lbl_amound.grid(row=3, column=0, pady=10)
        self.entry_amound = Entry(self.panel, width=30)
        self.entry_amound.grid(row=3, column=1, ipady=4, columnspan=2)
        self.lbl_method = Label(self.panel, text="Payment Method: ", bg="#639ba9")
        self.lbl_method.grid(row=4, column=0, pady=10)
        self.entry_method = Entry(self.panel, width=30)
        self.entry_method.grid(row=4, column=1, ipady=4, columnspan=2)

        self.btn_delete = Button(self.panel,text="Delete", command=self.delete, width=8, bg="#990000", fg="white")
        self.btn_delete.grid(row=5, column=0, sticky="e")
        self.btn_add = Button(self.panel,text="Add", width=8, command=self.add, bg="green", fg="white")
        self.btn_add.grid(row=5, column=1, sticky="e")
        self.btn_update = Button(self.panel, text="Update", width=8, command=self.update, bg="green", fg="white")
        self.btn_update.grid(row=5, column=2, sticky="e", pady=20)

        self.table()
        self.insert()
        self.add_menu()
        self.window.mainloop()

    #main table
    def table(self):
        self.tree.heading("p_id", text="Payment ID")
        self.tree.heading("b_id", text="Bill ID")
        self.tree.heading("date", text="Payment Date")
        self.tree.heading("amound", text="Amound Paid")
        self.tree.heading("method", text="Payment Method")
        self.tree.column("p_id", width=70, anchor="center")
        self.tree.column("b_id", width=70, anchor="center")
        self.tree.column("date", width=140, anchor="center")
        self.tree.column("amound", width=100, anchor="center")
        self.tree.column("method", width=120, anchor="center")
        self.tree.grid(row=1, column=0, padx=(220, 0))
        self.tree.bind("<<TreeviewSelect>>", self.get_selected_row)

    #insert data from database
    def insert(self):
        con = tools.connect()
        cursor = con.cursor()
        sql = "SELECT * from payment;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            p_id, b_id, date, amound, method = row
            formated_amound = f"{amound} AF"
            self.tree.insert("", 0, values=(p_id, b_id, date, formated_amound, method))

    # get the values of selected row
    def get_selected_row(self,event):
        selected_item = self.tree.focus()
        value = self.tree.item(selected_item, "values")
        if len(value) > 0:
            self.clear()
            self.entry_p_id.insert(END, value[0])
            self.entry_b_id.insert(END, value[1])
            self.entry_date.insert(END, value[2])
            self.entry_amound.insert(END, value[3].replace(" AF",""))
            self.entry_method.insert(END, value[4])


    def delete(self):
        p_id = self.entry_p_id.get()
        if len(p_id) > 0:
            confirm = messagebox.askyesno("Confirmation", "Do you want to delete this record?")
            if confirm:
                try:
                   con = tools.connect()
                   sql = f"delete from payment where payment_ID = {int(p_id)};"
                   cursor = con.cursor()
                   cursor.execute(sql)
                   con.commit()
                   self.clear()
                   for item in self.tree.get_children():
                       self.tree.delete(item)
                   self.insert()
                   self.lbl_b_id.focus()
                except Exception as e:
                    messagebox.showerror("Error",f"Could not delete this record {str(e).split(":")[-1].strip()}")

    def add(self):
        p_id = int(self.entry_p_id.get())
        b_id = int(self.entry_b_id.get())
        date = self.entry_date.get()
        amound = int(self.entry_amound.get())
        method = self.entry_method.get()

        sql = f"insert into payment values ({p_id}, {b_id}, '{date}',{amound}, '{method}');"
        try:
            con = tools.connect()
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.insert()
            self.clear()
            self.lbl_b_id.focus()
        except Exception as e:
            messagebox.showerror("Error", f"Could not add {str(e).split(":")[-1].strip()}")

    def update(self):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")
        table_id = int(values[0])
        p_id = int(self.entry_p_id.get())
        b_id = int(self.entry_b_id.get())
        date = self.entry_date.get()
        amound = int(self.entry_amound.get())
        method = self.entry_method.get()

        sql = f"update payment set payment_ID={p_id},bill_ID={b_id},payment_date='{date}',amount_paid={amound} ,payment_method='{method}' where payment_ID={table_id};"
        try:
            con = tools.connect()
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.insert()
            self.clear()
            self.lbl_b_id.focus()
        except Exception as e:
            messagebox.showerror("Error", f"Could not update this record {str(e).split(":")[-1].strip()}")
    def clear(self):
        self.entry_p_id.delete(0, END)
        self.entry_b_id.delete(0, END)
        self.entry_amound.delete(0, END)
        self.entry_method.delete(0, END)
        self.entry_date.delete(0, END)

    def add_menu(self):
        menu = Menu(self.window)
        menu.add_cascade(label="Customer", command=self.customer)
        menu.add_cascade(label="Meter", command=self.meter)
        menu.add_cascade(label="Meter Usage", command=self.meter_usage)
        menu.add_cascade(label="Bill", command=self.bill)
        menu.add_cascade(label="Payment")
        self.window.config(menu=menu)

    def customer(self):
        self.window.destroy()
        helper.customer()

    def meter(self):
        self.window.destroy()
        helper.meter()

    def meter_usage(self):
        self.window.destroy()
        helper.meter_usage()

    def bill(self):
        self.window.destroy()
        helper.bill()
