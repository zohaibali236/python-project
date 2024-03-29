from tkinter import *
from datetime import datetime
from tkinter import messagebox
from PIL import ImageTk
import pyodbc


def back():
	loginPage.destroy()
	from homepage import Showhomepage
	Showhomepage()

def cPanelinit():
	loginPage.destroy()
	from cpanel import showCpanel
	showCpanel()

def login(_):
	if(UserName.get() == "" or password.get() == ""): return messagebox.showerror("Error!", "User Name or Password cannot be empty!")
	try:
		dbHandle = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
						r"DBQ=.\shopping mall.accdb")
	except Exception as error: print(error, datetime.now())

	cur = dbHandle.cursor()

	cur.execute(f"SELECT * FROM `Users` WHERE `UserName` = '{UserName.get()}' AND `Password` = '{password.get()}'")

	if(len(cur.fetchall()) == 0): 
		messagebox.showerror("Error!", "Invalid Credentials\nPlease try again!")
		password.delete(0, END)
		UserName.delete(0, END)
		return dbHandle.close()

	dbHandle.close()
	cPanelinit()

def ShowLoginPage():

	global loginPage
	loginPage = Tk()
	loginPage.title("Login")
	bgimg = ImageTk.PhotoImage(file=r"images\loginPage.png", master = loginPage)
	
	Label(loginPage, image=bgimg).pack()

	loginPage.configure(bg = "white")
	loginPage.state('zoomed')
	loginPage.resizable(0,0)
	loginPage.iconbitmap('.\images\icon_img.ico')

	Button(loginPage, text="Back", bg="#febe53", fg="white", font=("aerial", 13, "italic"), command = back).place(x=150, y=690)

	global UserName
	UserName = Entry(loginPage, bd = 0, bg="white", font=("Open Sans Extra Bold", 12))
	UserName.place(x=369, y=383, height=19, width=167)

	global password
	password = Entry(loginPage, show="*", bg="white", bd=0, font=("Open Sans Extra Bold", 12))
	password.place(x=369, y=440, height=19, width=167)

	Button(loginPage, text="Login", command=lambda: login(0), bd=1, bg="white",font=("Open Sans Extra Bold", 12)).place(x=400, y=525, anchor="center")
	
	loginPage.bind("<Return>", login)

	loginPage.mainloop()