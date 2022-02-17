from tkinter import *
from datetime import datetime
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector as db
import ctypes

from cpanel import showCpanel


screenSize = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]

    
def cPanelinit():
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
    loginPage.configure(bg="white")
    loginPage.geometry(f"{screenSize[0]}x{screenSize[1]}")

    backgroundimage = ImageTk.PhotoImage(file=r"images\icon.jpg", master = loginPage)
    Label(loginPage, image=backgroundimage, bd=0).pack(side=TOP)

    Frame(loginPage, width = 340, height=338, bd=0, bg="pink").place(x = 550, y = 350)

    Label(loginPage, text="User Name", bd = 0, bg = "green", width=10).place(x=696, y=400, anchor="center")

    global UserName
    UserName = Entry(loginPage)
    UserName.place(x=722, y=420, anchor="center")

    Label(loginPage, text="Password", width=10, bg="green").place(x=698, y=450, anchor="center")

    global password
    password = Entry(loginPage, show="*")
    password.place(x=722, y=472, anchor="center")

    Button(loginPage, text="Login", command=login, bg="blue", width=10).place(x=712, y=510, anchor="center")
    loginPage.mainloop()

