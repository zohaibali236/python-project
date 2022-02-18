from tkinter import *
from datetime import datetime
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector as db
import ctypes



screenSize = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]

def back():
    loginPage.destroy()
    from homepage import Showhomepage
    Showhomepage()

def cPanelinit():
    from cpanel import showCpanel
    loginPage.destroy()
    dbHandle.close()
    showCpanel()

def login():
    mysql_query = dbHandle.cursor(dictionary = True, buffered = True)

    mysql_query.execute(f"SELECT * FROM `USERS` WHERE `NAME` = '{UserName.get()}' AND `PASSWORD` = '{password.get()}'")
    mysql_query.close()

    if(not mysql_query.rowcount): return messagebox.showerror("Error!", "Invalid Credentials\nPlease try again!")

    cPanelinit()

def ShowLoginPage():
    global dbHandle
    try:
        dbHandle = db.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "mall"
            )
    except db.Error as error: print(error, datetime.now())


    global loginPage
    loginPage = Tk()
    loginPage.title("Login")
    bgimg = ImageTk.PhotoImage(file=r"images\loginPage.png", master = loginPage)
    
    Label(loginPage, image=bgimg).pack()

    loginPage.configure(bg = "white")
    loginPage.geometry(f"{screenSize[0]}x{screenSize[1]}")
    loginPage.resizable(0,0)

    Button(loginPage, text="Back", bg="#febe53", fg="white", font=("aerial", 13, "italic"), command = back).place(x=150, y=690)

    global UserName
    UserName = Entry(loginPage, bd = 0, bg="white", font=("Open Sans Extra Bold", 12))
    UserName.place(x=321, y=411, height=20, width=167)

    global password
    password = Entry(loginPage, show="*", bg="white", bd=0, font=("Open Sans Extra Bold", 12))
    password.place(x=321, y=468, height=20, width=167)

    Button(loginPage, text="Login", command=login, bd=1, bg="white",font=("Open Sans Extra Bold", 12)).place(x=400, y=525, anchor="center")
    loginPage.mainloop()