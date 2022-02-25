from tkinter import *
from PIL import ImageTk, Image


def back(window):
	if(window == "aboutUsWindow"):
		aboutUsWindow.destroy()
		from homepage import Showhomepage
		Showhomepage()
	elif(window == "whatWeOffer"):
		whatWeOffer.destroy()
		showAboutUsWindow()
	elif(window == "ourClientsWindow"):
		ourClientsWindow.destroy()
		showAboutUsWindow()


def whatweoffer():
	aboutUsWindow.destroy()
	global whatWeOffer
	whatWeOffer = Tk()

	whatWeOffer.title("What we offer")
	whatWeOffer.state('zoomed')
	whatWeOffer.configure(background='grey21')
	hlabel = Label(whatWeOffer, text="What We Offer",font=("Segoe Script",25,"bold"),bg ='Red',fg='black')
	hlabel.grid(row=0,column=1,padx=530)

	#images
	image = Image.open(r"images\open shop.jpg")
	imagenew = ImageTk.PhotoImage(image)
	imagelabel = Label(whatWeOffer, image=imagenew)
	imagelabel.place(x=70, y=200)

	image2 = Image.open(r"images\cinema.jpg")
	imagenew2 = ImageTk.PhotoImage(image2)
	imagelabel2 = Label(whatWeOffer, image=imagenew2)
	imagelabel2.place(x=500, y=200)

	image3 = Image.open(r"images\nature.jpg")
	imagenew3 = ImageTk.PhotoImage(image3)
	imagelabel3 = Label(whatWeOffer, image=imagenew3)
	imagelabel3.place(x=900, y=200)

	image4 = Image.open(r"images\food.jpg")
	imagenew4 = ImageTk.PhotoImage(image4)
	imagelabel4 = Label(whatWeOffer, image=imagenew4)
	imagelabel4.place(x=70, y=550)

	image5 = Image.open(r"images\play.jpg")
	imagenew5 = ImageTk.PhotoImage(image5)
	imagelabel5 = Label(whatWeOffer, image=imagenew5)
	imagelabel5.place(x=500, y=550)

	image6 = Image.open(r"images\car parking.jpg")
	imagenew6 = ImageTk.PhotoImage(image6)
	imagelabel6 = Label(whatWeOffer, image=imagenew6)
	imagelabel6.place(x=900, y=550)

	back_button = Button(whatWeOffer, text="Back", bg="black", fg="#febe53", font=("aerial", 13, "italic"), command = lambda: back("whatWeOffer"))
	back_button.place(x=150, y=690)
	
	#labels
	label1 = Label(whatWeOffer, text="Shopping Line", font=("Segoe Script", 30, "bold"), bg='red', fg='black')
	label1.place(x=90,y=440)

	label2 = Label(whatWeOffer, text="Multiplex Cinema", font=("Segoe Script", 25, "bold"), bg='red', fg='black')
	label2.place(x=515, y=440)

	label3 = Label(whatWeOffer, text="Health and Beauty", font=("Segoe Script", 23, "bold"), bg='red', fg='black')
	label3.place(x=915, y=440)

	label4 = Label(whatWeOffer, text="Food Court", font=("Segoe Script", 35, "bold"), bg='red', fg='black')
	label4.place(x=100, y=785)

	label5 = Label(whatWeOffer, text="Play Area", font=("Segoe Script", 35, "bold"), bg='red', fg='black')
	label5.place(x=540, y=785)

	label6 = Label(whatWeOffer, text="Car Parking", font=("Segoe Script", 30, "bold"), bg='red', fg='black')
	label6.place(x=940, y=785)

	
	whatWeOffer.mainloop()


def ourclients():
	aboutUsWindow.destroy()

	global ourClientsWindow
	ourClientsWindow = Tk()

	ourClientsWindow.title("Our Clients")
	ourClientsWindow.state('zoomed')
	ourClientsWindow.configure(background='indian red')

	hlabel = Label(ourClientsWindow, text="Our Clients",font=("Segoe Script",60,"bold"),bg ='indian red',fg='black')
	hlabel.grid(row=0,column=1,padx=380,pady=50)

	#images
	image = Image.open(r"images\kfc.png")
	imagenew = ImageTk.PhotoImage(image)
	imagelabel = Label(ourClientsWindow, image=imagenew)
	imagelabel.place(x=50, y=230)

	image2 = Image.open(r"images\ecs.png")
	imagenew2 = ImageTk.PhotoImage(image2)
	imagelabel2 = Label(ourClientsWindow, image=imagenew2)
	imagelabel2.place(x=350, y=230)

	image3 = Image.open(r"images\bata.png")
	imagenew3 = ImageTk.PhotoImage(image3)
	imagelabel3 = Label(ourClientsWindow, image=imagenew3)
	imagelabel3.place(x=650, y=230)

	image4 = Image.open(r"images\warda.jpg")
	imagenew4 = ImageTk.PhotoImage(image4)
	imagelabel4 = Label(ourClientsWindow, image=imagenew4)
	imagelabel4.place(x=950, y=230)

	image5 = Image.open(r"images\pizza.png")
	imagenew5 = ImageTk.PhotoImage(image5)
	imagelabel5 = Label(ourClientsWindow, image=imagenew5)
	imagelabel5.place(x=50, y=550)

	image6 = Image.open(r"images\gulahmed.png")
	imagenew6 = ImageTk.PhotoImage(image6)
	imagelabel6 = Label(ourClientsWindow, image=imagenew6)
	imagelabel6.place(x=350, y=550)

	image7 = Image.open(r"images\hbl.png")
	imagenew7 = ImageTk.PhotoImage(image7)
	imagelabel7 = Label(ourClientsWindow, image=imagenew7)
	imagelabel7.place(x=650, y=550)

	image8 = Image.open(r"images\1step.png")
	imagenew8 = ImageTk.PhotoImage(image8)
	imagelabel8 = Label(ourClientsWindow, image=imagenew8)
	imagelabel8.place(x=950, y=550)

	back_button = Button(ourClientsWindow, text="Back", bg="black", fg="#febe53", font=("aerial", 13, "italic"), command =lambda:back("ourClientsWindow"))
	back_button.place(x=150, y=690) 

	ourClientsWindow.mainloop()


def showAboutUsWindow():
	global aboutUsWindow
	aboutUsWindow = Tk()
	aboutUsWindow.state("zoomed")
	aboutUsWindow.title("About us")
	aboutUsWindow.resizable(0,0)
	#background
	my_img = ImageTk.PhotoImage(Image.open(r"images\about bg9.png"))
	my_label = Label(aboutUsWindow, image=my_img)
	my_label.place(x=0,y=0)

	#btn for back
	btnback = Button(aboutUsWindow,text='Back',bg='black',fg='white' ,borderwidth=0,command=back)
	btnback.place(x=3,y=900,width=100,height=50)

	#label
	l = Label(aboutUsWindow,text="Elegante Mall and Cinemas is one of the biggest mixed-use development in Pakistan. The mall is centrally",font=("Segoe Script",16,"bold"),bg ='Indian red',fg='white')
	l.grid(row=2,column=1,padx=25,pady=27)
	
	l1 = Label(aboutUsWindow,text=("air-conditioned with valet parking services for customers.It is the first of its kind mall in Pakistan"),font=("Segoe Script",15,"bold"),bg ='Indian red',fg='white')
	l1.grid(row=3,column=1)

	#btn for what we offer
	btn1 = Button(aboutUsWindow, text='What we offer', bg='firebrick2', fg='white', borderwidth=9,relief=SUNKEN,font=('Segoe Script',20,"bold"),command = whatweoffer)
	btn1.place(x=900, y=350, width=300, height=100)
	
	btn2 = Button(aboutUsWindow, text='Our Clients', bg='firebrick2', fg='white', borderwidth=9, relief=SUNKEN,font=('Segoe Script', 20, "bold"),command=ourclients)
	btn2.place(x=900, y=500, width=300, height=100)


	back_button = Button(aboutUsWindow, text="Back", bg="black", fg="#febe53", font=("aerial", 13, "italic"), command = lambda: back("aboutUsWindow"))
	back_button.place(x=150, y=690) 
	aboutUsWindow.mainloop()

showAboutUsWindow()