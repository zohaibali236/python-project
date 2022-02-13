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


# cartscreen

   # labels
orange_frame = Frame(m1, bg="orange", width=1524, height=screenSize[1])
white_frame = Frame(m1, bg="white", width=1220, height=730)
seller_label = Label(orange_frame, text="SELLER", bg="orange", fg="white", font=("aerial", 30))
categories_label = Label(orange_frame, text="CATEGORIES", bg="orange", fg="white", font=("aerial", 30))
manage_products = Label(white_frame, text="MANAGE PRODUCTS", bg="white", fg="orange", font=("aerial", 25, "bold"))
id = Label(white_frame, text="ProductID", bg="white", fg="orange", font=("aerial", 15, "bold"))
name = Label(white_frame, text="NAME", bg="white", fg="orange", font=("aerial", 15, "bold"))
quantity = Label(white_frame, text="QUANTITY", bg="white", fg="orange", font=("aerial", 15, "bold"))
price = Label(white_frame, text="PRICE", bg="white", fg="orange", font=("aerial", 15, "bold"))
category = Label(white_frame, text="CATEGORY", bg="white", fg="orange", font=("aerial", 15, "bold"))
product_list = Label(white_frame, text="PRODUCTS LIST", bg="white", fg="orange", font=("aerial", 25, "bold"))


   # buttons
logout_button = Button(orange_frame, text="Logout", bg="orange", fg="white", font=("aerial", 13, "italic"), command = cmd)
add_button = Button(white_frame, text="ADD", bg="orange", fg="white", width=7, height=1,
                       font=("aerial", 15, "italic"))
edit_button = Button(white_frame, text="EDIT", bg="orange", fg="white", width=7, height=1,
                        font=("aerial", 15, "italic"))
delete_button = Button(white_frame, text="DELETE", bg="orange", fg="white", width=7, height=1,
                          font=("aerial", 15, "italic"))
clear_button = Button(white_frame, text="CLEAR", bg="orange", fg="white", width=7, height=1,
                         font=("aerial", 15, "italic"))

   # entry boxes
id_entry = Entry(white_frame, bg="white", bd=3, width=25)
name_entry = Entry(white_frame, bg="white", bd=3, width=25)
quantity_entry = Entry(white_frame, bg="white", bd=3, width=25)
price_entry = Entry(white_frame, bg="white", bd=3, width=25)

# putting on screen
orange_frame.place(x=3, y=1)
white_frame.place(x=300, y=50)
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
product_list.place(x=475, y=350)


m1.mainloop()