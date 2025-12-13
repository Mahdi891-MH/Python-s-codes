from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import tools
import helper

class Bill:
    def __init__(self):
        self.window  = Tk()
        self.window.state('zoomed')
        self.window.config(bg="#639ba9")
        self.window.title("Electricity Bill Payment System")
        self.lblTitle = Label(text="Bill Detail", font=("Engravers MT", 20, "bold"), bg="#639ba9")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=(20, 50), padx=(130,0))
        self.tree = ttk.Treeview(self.window, columns=("b_id", "c_id", "u_id", "date", "amount", "unpaid", "status"),show="headings", height=16)

        style = ttk.Style()
        style.configure("Treeview.Heading", font= ("Segoe UI", 8, "bold"))

        f_style = ttk.Style()
        f_style.configure("Custom.TFrame", background="#639ba9")

        self.panel = ttk.Frame(style="Custom.TFrame")
        self.panel.grid(row=1, column=1, padx=(50, 0))
        self.lbl_b_id = Label(self.panel, text="Bill ID: ", bg="#639ba9")
        self.lbl_b_id.grid(row=0, column=0, pady=10)
        self.entry_b_id = Entry(self.panel, width=30)
        self.entry_b_id.grid(row=0, column=1, ipady=4, columnspan=2)
        self.lbl_c_id = Label(self.panel, text="Customer ID: ", bg="#639ba9")
        self.lbl_c_id.grid(row=1, column=0, pady=10)
        self.entry_c_id = Entry(self.panel, width=30)
        self.entry_c_id.grid(row=1, column=1, ipady=4, columnspan=2)
        self.lbl_u_id = Label(self.panel, text="Usage ID: ", bg="#639ba9")
        self.lbl_u_id.grid(row=2, column=0, pady=10)
        self.entry_u_id = Entry(self.panel, width=30)
        self.entry_u_id.grid(row=2, column=1, ipady=4, columnspan=2)
        self.lbl_date = Label(self.panel,text="Bill Date: ", bg="#639ba9")
        self.lbl_date.grid(row=3, column=0, pady=10)
        self.entry_date = Entry(self.panel,width=30)
        self.entry_date.grid(row=3, column=1, ipady=4, columnspan=2)
        self.lbl_amount = Label(self.panel, text="Amount: ", bg="#639ba9")
        self.lbl_amount.grid(row=4, column=0, pady=10)
        self.entry_amount = Entry(self.panel, width=30)
        self.entry_amount.grid(row=4, column=1, ipady=4, columnspan=2)
        self.lbl_unpaid = Label(self.panel, text="Unpaid: ", bg="#639ba9")
        self.lbl_unpaid.grid(row=5, column=0, pady=10)
        self.entry_unpaid = Entry(self.panel, width=30)
        self.entry_unpaid.grid(row=5, column=1, ipady=4, columnspan=2)
        self.lbl_status = Label(self.panel, text="Status: ", bg="#639ba9")
        self.lbl_status.grid(row=6, column=0, pady=10)
        self.entry_status = Entry(self.panel, width=30)
        self.entry_status.grid(row=6, column=1, ipady=4, columnspan=2)
        self.read_only()
        self.btn_delete = Button(self.panel,text="Delete", command=self.delete, width=8, bg="#990000", fg="white")
        self.btn_delete.grid(row=7, column=0, sticky="e")
        self.btn_add = Button(self.panel,text="Add", width=8, command=self.add, bg="green", fg="white")
        self.btn_add.grid(row=7, column=1, sticky="e")
        self.btn_update = Button(self.panel, text="Update", width=8, command=self.update, bg="green", fg="white")
        self.btn_update.grid(row=7, column=2, sticky="e", pady=20)



        self.table()
        self.insert()
        self.add_menu()
        self.window.mainloop()

    def table(self):
        self.tree.heading("b_id", text="Bill ID")
        self.tree.heading("c_id", text="Customer ID")
        self.tree.heading("u_id", text="Usage ID")
        self.tree.heading("date", text="Bill Date")
        self.tree.heading("amount", text="amount")
        self.tree.heading("unpaid", text="Unpaid")
        self.tree.heading("status", text="Status")
        self.tree.column("b_id", width=70, anchor="center")
        self.tree.column("c_id", width=80, anchor="center")
        self.tree.column("u_id", width=80, anchor="center")
        self.tree.column("date", width=160, anchor="center")
        self.tree.column("amount", width=100, anchor="center")
        self.tree.column("unpaid", width=100, anchor="center")
        self.tree.column("status", width=100, anchor="center")
        self.tree.grid(row=1, column=0, padx=(130, 0))
        self.tree.bind("<<TreeviewSelect>>", self.get_selected_row)

    def insert(self):
        con = tools.connect()
        cursor = con.cursor()
        cursor.callproc("p_bill")
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                b_id, c_id, u_id, date, amount,unpaid, status= row
                formated_amount = f"{amount} AF"
                formated_unpaid = f"{unpaid} AF"
                self.tree.insert("", 0, values=(b_id, c_id, u_id, date, formated_amount, formated_unpaid, status))

    # get the values of selected row
    def get_selected_row(self,event):
        selected_item = self.tree.focus()
        value = self.tree.item(selected_item, "values")
        if len(value) > 0:
            self.entry_amount.config(state="normal")
            self.entry_unpaid.config(state="normal")
            self.entry_status.config(state="normal")
            self.clear()
            self.entry_b_id.insert(END, value[0])
            self.entry_c_id.insert(END, value[1])
            self.entry_u_id.insert(END, value[2])
            self.entry_date.insert(END, value[3])
            self.entry_amount.insert(END, (value[4]).replace(" AF",""))
            self.entry_amount.config(state="readonly")
            self.entry_unpaid.insert(END, value[5].replace(" AF",""))
            self.entry_unpaid.config(state="readonly")
            self.entry_status.insert(END, value[6])
            self.entry_status.config(state="readonly")


    def delete(self):
        b_id = self.entry_b_id.get()
        if len(b_id) > 0:
            confirm = messagebox.askyesno("Confirmation", "Do you want to delete this record?")
            if confirm:
                try:
                   con = tools.connect()
                   sql = f"delete from bill where bill_ID = {int(b_id)};"
                   cursor = con.cursor()
                   cursor.execute(sql)
                   con.commit()
                   self.normal()
                   self.clear()
                   for item in self.tree.get_children():
                       self.tree.delete(item)
                   self.insert()
                   self.read_only()
                   self.lbl_c_id.focus()
                except Exception as e:
                    messagebox.showerror("Error",f"Could not delete this record {str(e).split(":")[-1].strip()}")

    def add(self):
        self.normal()
        b_id = int(self.entry_b_id.get())
        c_id = int(self.entry_c_id.get())
        u_id = int(self.entry_u_id.get())
        date = self.entry_date.get()
        sql = f"insert into bill values ({b_id}, {c_id}, {u_id},'{date}');"
        try:
            con = tools.connect()
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.insert()
            self.clear()
            self.read_only()
            self.lbl_c_id.focus()
        except Exception as e:
            messagebox.showerror("Error", f"Could not add {str(e).split(":")[-1].strip()}")

    def update(self):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")
        table_id = int(values[0])
        b_id = int(self.entry_b_id.get())
        c_id = int(self.entry_c_id.get())
        u_id = int(self.entry_u_id.get())
        date = self.entry_date.get()
        self.normal()
        sql = f"update bill set bill_ID={b_id},cust_ID={c_id},usage_ID={u_id},bill_date='{date}' where bill_ID={table_id};"
        try:
            con = tools.connect()
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.insert()
            self.clear()
            self.read_only()
            self.lbl_c_id.focus()
        except Exception as e:
            messagebox.showerror("Error", f"Could not update this record {str(e).split(":")[-1].strip()}")

    def clear(self):
        self.entry_b_id.delete(0, END)
        self.entry_c_id.delete(0, END)
        self.entry_u_id.delete(0, END)
        self.entry_amount.delete(0, END)
        self.entry_date.delete(0, END)
        self.entry_unpaid.delete(0, END)
        self.entry_status.delete(0, END)

    def read_only(self):
        self.entry_amount.config(state="readonly")
        self.entry_unpaid.config(state="readonly")
        self.entry_status.config(state="readonly")

    def normal(self):
        self.entry_amount.config(state="normal")
        self.entry_unpaid.config(state="normal")
        self.entry_status.config(state="normal")

    def add_menu(self):
        menu = Menu(self.window)
        menu.add_cascade(label="Customer", command=self.customer)
        menu.add_cascade(label="Meter", command=self.meter)
        menu.add_cascade(label="Meter Usage", command=self.meter_usage)
        menu.add_cascade(label="Bill")
        menu.add_cascade(label="Payment", command= self.payment)
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

    def payment(self):
        self.window.destroy()
        helper.payment()




