from tkinter import*
from tkinter import ttk
from tkinter import messagebox

import helper
import tools

class Meter:
    def __init__(self):
        self.window  = Tk()
        self.window.state('zoomed')
        self.window.config(bg="#639ba9")
        self.window.title("Electricity Bill Payment System")
        self.lblTitle = Label(text="Meter Detail", font=("Engravers MT", 20, "bold"), bg="#639ba9")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=(20, 50), padx=(160,0))
        self.tree = ttk.Treeview(self.window, columns=("Meter ID", "Customer ID", "Meter Type", "Installation Date", "Status"),show="headings", height=15)

        style = ttk.Style()
        style.configure("Treeview.Heading", font= ("Segoe UI", 8, "bold"))

        f_style = ttk.Style()
        f_style.configure("Custom.TFrame", background="#639ba9")

        self.panel = ttk.Frame(style="Custom.TFrame")
        self.panel.grid(row=1, column=1, padx=(75, 0))
        self.lbl_meter_id = Label(self.panel, text="Meter ID: ", bg="#639ba9")
        self.lbl_meter_id.grid(row=0, column=0, pady=10)
        self.entry_meter_id = Entry(self.panel, width=30)
        self.entry_meter_id.grid(row=0, column=1, ipady=4, columnspan=2)
        self.lbl_cust_id = Label(self.panel, text="Customer ID: ", bg="#639ba9")
        self.lbl_cust_id.grid(row=1, column=0, pady=10)
        self.entry_cust_id = Entry(self.panel, width=30)
        self.entry_cust_id.grid(row=1, column=1, ipady=4, columnspan=2)
        self.lbl_type = Label(self.panel, text="Meter Type: ", bg="#639ba9")
        self.lbl_type.grid(row=2, column=0, pady=10)
        self.entry_type = Entry(self.panel, width=30)
        self.entry_type.grid(row=2, column=1, ipady=4, columnspan=2)
        self.lbl_date = Label(self.panel, text="Installation Date: ", bg="#639ba9")
        self.lbl_date.grid(row=3, column=0, pady=10)
        self.entry_date = Entry(self.panel, width=30)
        self.entry_date.grid(row=3, column=1, ipady=4, columnspan=2)
        self.lbl_status = Label(self.panel, text="Status: ", bg="#639ba9")
        self.lbl_status.grid(row=4, column=0, pady=10)
        self.entry_status = Entry(self.panel, width=30)
        self.entry_status.grid(row=4, column=1, ipady=4, columnspan=2)
        self.btn_delete = Button(self.panel,text="Delete", width=8, command=self.delete, bg="#990000", fg="white")
        self.btn_delete.grid(row=5, column=0, sticky="e")
        self.btn_add = Button(self.panel,text="Add", width=8, command=self.add, bg="green", fg="white")
        self.btn_add.grid(row=5, column=1, sticky="e")
        self.btn_update = Button(self.panel, text="Update", width=8, command=self.update, bg="green", fg="white")
        self.btn_update.grid(row=5, column=2, sticky="e", pady=20)

        self.table()
        self.insert()
        self.add_menu()
        self.window.mainloop()


    def table(self):
        self.tree.heading("Meter ID", text="Meter ID")
        self.tree.heading("Customer ID", text="Customer ID")
        self.tree.heading("Meter Type", text="Meter Type")
        self.tree.heading("Installation Date", text="Installation Date")
        self.tree.heading("Status", text="Status")
        self.tree.column("Meter ID", width=70, anchor="center")
        self.tree.column("Customer ID", width=90, anchor="center")
        self.tree.column("Meter Type", width=120, anchor="center")
        self.tree.column("Installation Date", width=160, anchor="center")
        self.tree.column("Status", width=150, anchor="center")
        self.tree.grid(row=1, column=0, padx=(165, 0))
        self.tree.bind("<<TreeviewSelect>>", self.get_selected_row)

    def insert(self):
        con = tools.connect()
        cursor = con.cursor()
        sql = "SELECT * from meter;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            self.tree.insert("", 0, values=row)

    def get_selected_row(self,event):
        selected_item = self.tree.focus()
        value = self.tree.item(selected_item, "values")
        if len(value) > 0:
            self.clear()
            self.entry_meter_id.insert(END, value[0])
            self.entry_cust_id.insert(END, value[1])
            self.entry_type.insert(END, value[2])
            self.entry_date.insert(END, value[3])
            self.entry_status.insert(END, value[4])

    def clear(self):
        self.entry_meter_id.delete(0, END)
        self.entry_cust_id.delete(0, END)
        self.entry_type.delete(0, END)
        self.entry_date.delete(0, END)
        self.entry_status.delete(0, END)

    def delete(self):
        meter_id = self.entry_meter_id.get()
        if len(meter_id) > 0:
            confirm = messagebox.askyesno("Confirmation", "Do you want to delete this record?")
            if confirm:
                try:
                   con = tools.connect()
                   sql = f"delete from meter where meter_ID = {int(meter_id)};"
                   cursor = con.cursor()
                   cursor.execute(sql)
                   con.commit()
                   self.clear()
                   for item in self.tree.get_children():
                       self.tree.delete(item)
                   self.insert()
                   self.lbl_cust_id.focus()
                except Exception as e:
                    messagebox.showerror("Error",f"Could not delete this record {str(e).split(":")[-1].strip()}")


    def update(self):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")
        table_m_id = int(values[0])
        m_id = int(self.entry_meter_id.get())
        c_id = int(self.entry_cust_id.get())
        m_type = self.entry_type.get()
        date = self.entry_date.get()
        status = self.entry_status.get()
        sql = f"update meter set meter_ID={m_id},cust_ID={c_id},meter_type='{m_type}' ,install_date='{date}',status='{status}' where meter_ID={table_m_id};"
        try:
            con = tools.connect()
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.insert()
            self.clear()
            self.lbl_cust_id.focus()
        except Exception as e:
            messagebox.showerror("Error", f"Could not update this record {str(e).split(":")[-1].strip()}")

    def add(self):
        m_id = int(self.entry_meter_id.get())
        c_id = int(self.entry_cust_id.get())
        m_type = self.entry_type.get()
        date = self.entry_date.get()
        status = self.entry_status.get()
        sql = f"insert into meter values ({m_id}, {c_id}, '{m_type}', '{date}', '{status}');"
        try:
            con = tools.connect()
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.insert()
            self.clear()
            self.lbl_cust_id.focus()
        except Exception as e:
            messagebox.showerror("Error", f"Could not add {str(e).split(":")[-1].strip()}")

    def add_menu(self):
        menu = Menu(self.window)
        menu.add_cascade(label="Customer", command=self.customer)
        menu.add_cascade(label="Meter")
        menu.add_cascade(label="Meter Usage", command=self.meter_usage)
        menu.add_cascade(label="Bill", command=self.bill)
        menu.add_cascade(label="Payment", command=self.payment)
        self.window.config(menu=menu)

    def customer(self):
        self.window.destroy()
        helper.customer()

    def meter_usage(self):
        self.window.destroy()
        helper.meter_usage()

    def bill(self):
        self.window.destroy()
        helper.bill()

    def payment(self):
        self.window.destroy()
        helper.payment()
