USE_SQL_SERVER = False

"""Importing modules"""
from tkinter import *
import ctypes
from datetime import datetime
"""End of importing modules"""

"""Connecting to DB"""
if(USE_SQL_SERVER):
    import mysql.connector as db
    try:
        dbHandle = db.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database = ""
        )
    except db.Error as error:
        print(error, datetime.now())
else:
    import pyodbc
    dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                          r'DBQ=C:\Users\Xmart\Documents\Calculator.accdb;')

"""Getting screen size"""
screenSize = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]

"""master window #1"""
m1 = tk.Tk()

m1.geometry(f"{screenSize[0]}x{screenSize[1]}")
# cartscreen

   # labels
orange_frame = Frame(m1, bg="orange", width=1524, height=788)
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
logout_button = Button(orange_frame, text="Logout", bg="orange", fg="white", font=("aerial", 13, "italic"))
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

m1.tk.mainloop()