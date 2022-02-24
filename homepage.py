from tkinter import  *
from PIL import Image , ImageTk
from tkinter import ttk
from ctypes import windll

screenSize = [windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1)]

def aboutusinit():
	homepagewindow.destroy()
	from aboutus import showAboutUsWindow
	showAboutUsWindow()

def contactusinit():
	homepagewindow.destroy()
	from contactus import showContactUsWindow
	showContactUsWindow()

def loginPageinit():
	homepagewindow.destroy()
	from loginpage import ShowLoginPage
	ShowLoginPage()

def ourshopsinit():
	homepagewindow.destroy()
	from ourshops import ShowOurShops
	ShowOurShops()

def Showhomepage():
	global homepagewindow
	homepagewindow = Tk()
	homepagewindow.title("Elegante Shopping Mall")
	homepagewindow.geometry(f"{screenSize[0]}x{screenSize[1]}")
	homepagewindow.resizable(0,0)
	homepagewindow.iconbitmap('.\images\icon_img.ico')
	image = Image.open(r"images\title (5).jpg")
	imagenew = ImageTk.PhotoImage(image)
	imagelabel = Label(homepagewindow, image=imagenew)
	imagelabel.place(x=0,y=0)
	#logo
	f1=Frame(homepagewindow)
	f1.place(x=10,y=10,width=250,height=250)
	logo = PhotoImage(file=r'images\my.png')
	label = Label(f1, image = logo, bd=0)
	PhotoImage(file=r'images\my.png')
	label.pack()
	#text
	l1= Label(homepagewindow,text="Elegante Shopping Mall" , bg="black", fg="white",padx=15, pady=15,font=("Segoe Script",25,"bold"))
	l1.place(x=580,y=3)
	#buttons
	login_img=PhotoImage(file=r'images\2.png')
	login=Button(homepagewindow,image=login_img,bg="DodgerBlue4",height=100,width=250, command=loginPageinit)
	login.place(x=320,y=110)

	ourshop_img=PhotoImage(file=r'images\tg1.png')
	ourshop=Button(homepagewindow,image=ourshop_img,bg="DarkGoldenrod2",height=100,width=250, command = ourshopsinit)
	ourshop.place(x=610,y=110)

	aboutus_img=PhotoImage(file=r'images\a1.png')
	aboutus=Button(homepagewindow,image=aboutus_img,bg="white",height=100,width=250,command = aboutusinit)
	aboutus.place(x=905,y=110)

	contact_us_img=PhotoImage(file=r'images\c1.png')
	contact=Button(homepagewindow,image=contact_us_img,bg="white",height=100,width=250,command=contactusinit)
	contact.place(x=1200,y=110)

	homepagewindow.mainloop()
