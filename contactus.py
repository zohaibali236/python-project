from tkinter import *
from PIL import Image , ImageTk
import webbrowser


def openUrl(url):
	webbrowser.open_new_tab(url)

def back():
	contactUsWindow.destroy()
	from homepage import Showhomepage
	Showhomepage()

def showContactUsWindow():
	global contactUsWindow
	contactUsWindow = Tk()

	contactUsWindow.state('zoomed')
	contactUsWindow.title("Contact us")
	contactUsWindow.resizable(0,0)
	my_img = ImageTk.PhotoImage(Image.open(r"images\contact (1).jpg"))
	my_label = Label(contactUsWindow, image=my_img)
	my_label.place(x=0, y=0)

	hlabel = Label(contactUsWindow, text="Contact Info", font=("Helvetica", 60, "bold"), bg='grey90', fg='black')
	hlabel.place(x=470,y=150)
	
	link = Label(contactUsWindow, text="www.eleganteshoppingmall.com", font=('Helveticabold', 15), fg="blue", cursor="hand2")
	link.place(x=520,y=410)
	link.bind("<Button-1>", lambda _: openUrl("http://www.eleganteshoppingmall.com"))

	link = Label(contactUsWindow, text="mahnoorwaseem@gmail.com", font=('Helveticabold', 15), fg="blue", cursor="hand2")
	link.place(x=520,y=600)
	link.bind("<Button-1>", lambda _: openUrl("openUrl:mahnoorwaseem@gmail.com"))

	link = Label(contactUsWindow, text="zohaib.ali236@gmail.com", font=('Helveticabold', 17), fg="blue", cursor="hand2")
	link.place(x=520,y=645)
	link.bind("<Button-1>", lambda _: openUrl("openUrl:zohaib.ali236@gmail.com"))

	link = Label(contactUsWindow, text="jazebjaved52@gmail.com", font=('Helveticabold', 17), fg="blue", cursor="hand2")
	link.place(x=520,y=693)
	link.bind("<Button-1>", lambda _: openUrl("openUrl:jazebjaved52@gmail.com"))

	l1 = Label(contactUsWindow,text='Zaibun Nissa Street, Saddar, Karachi, Pakistan',font=('calibri',15,"bold"),fg='black')
	l1.place(x=520,y=325)

	l1 = Label(contactUsWindow,text='Monday To Saturday: 11:00am till 10:00pm | Food Court: 11:00am till 11:59pm',font=('calibri',15,"bold"),fg='black')
	l1.place(x=520,y=510)

	image = Image.open(r"images\loc icon.png")
	imagenew = ImageTk.PhotoImage(image)
	imagelabel = Label(contactUsWindow, image=imagenew)
	imagelabel.place(x=400, y=320)


	image2 = Image.open(r"images\web.png")
	imagenew2 = ImageTk.PhotoImage(image2)
	imagelabel2 = Label(contactUsWindow, image=imagenew2)
	imagelabel2.place(x=400, y=410)

	image3 = Image.open(r"images\clock.jpg")
	imagenew3 = ImageTk.PhotoImage(image3)
	imagelabel3 = Label(contactUsWindow, image=imagenew3)
	imagelabel3.place(x=400, y=505)

	image4 = Image.open(r"images\msg.png")
	imagenew4 = ImageTk.PhotoImage(image4)
	imagelabel4 = Label(contactUsWindow, image=imagenew4)
	imagelabel4.place(x=400, y=597)

	back_button = Button(contactUsWindow, text="Back", bg="black", fg="#febe53", font=("aerial", 13, "italic"), command = back)
	back_button.place(x=120, y=730) 

	contactUsWindow.mainloop()

