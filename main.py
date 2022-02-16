USE_SQL_SERVER = True

"""Importing modules"""
from tkinter import*
import ctypes
from datetime import datetime
from tkinter import messagebox
from PIL import ImageTk
"""End of importing modules"""


"""Connecting to DB"""
if(USE_SQL_SERVER):
    import mysql.connector as db
    try:
        dbHandle = db.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database = "mall"
        )
    except db.Error as error:
        print(error, datetime.now())

else:
    import pyodbc
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                          r'DBQ=C:\Users\Xmart\Documents\Calculator.accdb;')

"""Getting screen size"""
screenSize = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]

"""windows"""
m1 = Tk()


"""window sizes"""
m1.geometry(f"{screenSize[0]}x{screenSize[1]}")

"""window titles"""
m1.title("Shopping mall")

def cmd():

    m1.destroy()
    global loginPage
    loginPage = Tk()
    loginPage.title("Login")
    loginPage.configure(bg="white")
    loginPage.geometry(f"{screenSize[0]}x{screenSize[1]}")

    backgroundimage = ImageTk.PhotoImage(file=r"images\icon.jpg", master = loginPage)
    Label(loginPage, image=backgroundimage, bd=0).pack(side=TOP)

    Frame(loginPage, width = 340, height=338, bd=0, bg="pink").place(x = 550, y = 350)

    Label(loginPage, text="User Name", bd = 0, bg = "green", width=10).place(x=696, y=400, anchor="center")

    global e1
    e1 = Entry(loginPage)
    e1.place(x=722, y=420, anchor="center")

    Label(loginPage, text="Password", width=10, bg="green").place(x=698, y=450, anchor="center")

    global e2
    e2 = Entry(loginPage, show="*")
    e2.place(x=722, y=472, anchor="center")

    Button(loginPage, text="Login", command=login, bg="blue", width=10).place(x=712, y=510, anchor="center")
    loginPage.mainloop()


def login():
    print(e1.get())
    mysql_query = dbHandle.cursor(dictionary = True, buffered = True)

    mysql_query.execute(f"SELECT * FROM `USERS` WHERE `NAME` = '{e1.get()}' AND `PASSWORD` = '{e2.get()}'")

    if(not mysql_query.rowcount): return messagebox.showerror("Error!", "Invalid Credentials\nPlease try again!")

    print(mysql_query.fetchall())
    loginPage.destroy()


# shops items management screen
   # labels
orange_frame = Frame(m1, bg="orange", width=1524, height=788)
white_frame = Frame(m1, bg="white", width=1220, height=730)
black_frame = Frame(m1, bg="grey", width=1025, height=310 )
seller_label = Label(orange_frame, text="SELLER", bg="orange", fg="white", font=("aerial", 30))
categories_label = Label(orange_frame, text="CATEGORIES", bg="orange", fg="white", font=("aerial", 30))
manage_products = Label(white_frame, text="MANAGE PRODUCTS", bg="white", fg="orange", font=("aerial", 25, "bold"))
id = Label(white_frame, text="ProductID", bg="white", fg="orange", font=("aerial", 15, "bold"))
name = Label(white_frame, text="NAME", bg="white", fg="orange", font=("aerial", 15, "bold"))
quantity = Label(white_frame, text="QUANTITY", bg="white", fg="orange", font=("aerial", 15, "bold"))
price = Label(white_frame, text="PRICE", bg="white", fg="orange", font=("aerial", 15, "bold"))
category = Label(white_frame, text="CATEGORY", bg="white", fg="orange", font=("aerial", 15, "bold"))
product_lis = Label(white_frame, text="PRODUCTS LIST", bg="white", fg="orange", font=("aerial", 25, "bold"))


# creating combo box
cur.execute("select shopname from shops")
shops = cur.fetchall()
categories = []
for i in range(len(shops)):
    a = list(shops[i])
    categories.extend(a)
combo_box = ttk.Combobox(white_frame, value=categories, width=22)
combo_box.insert(0, "Type")



# creating and placing treeview
col = ("pid", "pname", "pquantity", "price")
product_list = ttk.Treeview(m1, height=13, columns=col)

product_list.column("#0", width=0, minwidth=0)
product_list.column("pid", width=200, minwidth=200, anchor=CENTER)
product_list.column("pname", width=300, minwidth=300, anchor=CENTER)
product_list.column("pquantity", width=300, minwidth=300, anchor=CENTER)
product_list.column("price", width=200, anchor=CENTER)

product_list.heading("pid", text="Product ID", anchor=CENTER)
product_list.heading("pname", text="Product NAME", anchor=CENTER)
product_list.heading("pquantity", text="Product QUANTITY", anchor=CENTER)
product_list.heading("price", text="PRICE", anchor=CENTER)

product_list.place(x=426, y=460)


def search(event):
    global val
    val = event.widget.get()
    if val == "":
        combo_box['value'] = categories
    else:
        data=[]
        for categ in categories:
            if val.lower() in categ.lower():
                data.append(categ)
        combo_box['value'] = data


var_id = StringVar()
var_name = StringVar()
var_quantity= IntVar()
var_price = IntVar()

    
def display():
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=C:\Users\Xmart\Documents\shopping mall.accdb;')
    cur4 = dbHandle.cursor()
    global val
    global all_data
    cur4.execute(f"select * from {val}")
    all_data = cur4.fetchall()
    for row in product_list.get_children():
        product_list.delete(row)
    j=0
    for i in all_data:
        id = i[0]
        name = i[1]
        qty = i[2]
        pr = i[3]
        product_list.insert(parent='', index='end', iid=j, values=(id, name, qty, pr))
        j += 1

    dbHandle.close()
    
    
def add():
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=C:\Users\Xmart\Documents\shopping mall.accdb;')
    cur1 = dbHandle.cursor()
    global val
    cur1.execute(f"insert into {val}(pid,pname,pquantity,price) "
                f"values('{var_id.get()}','{var_name.get()}','{var_quantity.get()}','{var_price.get()}')")

    dbHandle.commit()
    dbHandle.close()
    display()

def edit():
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=C:\Users\Xmart\Documents\shopping mall.accdb;')
    cur2 = dbHandle.cursor()
    global val
    cur2.execute(f"update {val} set pname='{var_name.get()}',"
                f" pquantity='{var_quantity.get()}', price='{var_price.get()}' where pid='{var_id.get()}'")

    dbHandle.commit()
    dbHandle.close()
    display()
    
    
def delete():
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=C:\Users\Xmart\Documents\shopping mall.accdb;')
    cur3 = dbHandle.cursor()
    cur3.execute(f"delete from {val} where pid='{var_id.get()}'")
    dbHandle.commit()
    dbHandle.close()
    display()
    


   # buttons
logout_button = Button(orange_frame, text="Logout", bg="orange", fg="white", font=("aerial", 13, "italic"))
add_button = Button(white_frame, text="ADD", bg="orange", fg="white", width=7, height=1,
                       font=("aerial", 15, "italic"), command=add)
edit_button = Button(white_frame, text="EDIT", bg="orange", fg="white", width=7, height=1,
                        font=("aerial", 15, "italic"), command=edit)
delete_button = Button(white_frame, text="DELETE", bg="orange", fg="white", width=7, height=1,
                          font=("aerial", 15, "italic"), command=delete)
clear_button = Button(white_frame, text="DISPLAY", bg="orange", fg="white", width=7, height=1,
                         font=("aerial", 15, "italic"), command=display)


   # entry boxes
id_entry = Entry(white_frame, bg="white", textvariable=var_id, bd=3, width=25)
name_entry = Entry(white_frame, bg="white", textvariable=var_name, bd=3, width=25)
quantity_entry = Entry(white_frame, bg="white", textvariable=var_quantity, bd=3, width=25)
price_entry = Entry(white_frame, bg="white", textvariable=var_price, bd=3, width=25)




# putting on screen

orange_frame.place(x=3, y=1)
white_frame.place(x=300, y=50)
black_frame.place(x=415, y=450)
seller_label.place(x=5, y=200)
categories_label.place(x=5, y=250)
logout_button.place(x=150, y=730)
manage_products.place(x=440, y=15)
id.place(x=100, y=110)
id_entry.place(x=235, y=113)
name.place(x=100, y=160)
name_entry.place(x=235, y=163)
quantity.place(x=700, y=110)
quantity_entry.place(x=850, y=110)
price.place(x=700, y=160)
price_entry.place(x=850, y=160)
category.place(x=100, y=210)
add_button.place(x=250, y=270)
edit_button.place(x=450, y=270)
delete_button.place(x=650, y=270)
clear_button.place(x=850, y=270)
product_lis.place(x=475, y=350)
combo_box.place(x=236, y=214)
combo_box.bind("<KeyRelease>", search)


m1.mainloop()
