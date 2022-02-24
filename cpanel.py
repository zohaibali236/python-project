from tkinter import *




def manageShopInit():
	Cpanel.destroy()
	from manageshop import showManageShop
	showManageShop()

def manageItemInit():
	Cpanel.destroy()
	from manageitem import showItemManage
	showItemManage()

def logout():
	Cpanel.destroy()
	from loginpage import ShowLoginPage
	ShowLoginPage()


def showCpanel():
	global Cpanel
	Cpanel = Tk()
	Cpanel.state('zoomed')
	Cpanel.title("Management")
	Cpanel.state('zoomed')
	Cpanel.resizable(0,0)
	Cpanel.iconbitmap('.\images\icon_img.ico')
	frame = Frame(Cpanel, bg="#febe53", width=1536, height=864)

	shopIcon = PhotoImage(file=r"images\shopicon.png")
	itemsIcon = PhotoImage(file=r"images\itemsicon.png")

	shops_button = Button(frame, image=shopIcon, bg="#febe53", fg="white", activebackground="#febe53", command = manageShopInit)
	items_button = Button(frame, image=itemsIcon, bg="#febe53", fg="white", activebackground="#febe53", command = manageItemInit)
	logout_button = Button(frame, text="Logout", bg="#febe53", fg="white", font=("aerial", 13, "italic"), command = logout)


	frame.place(x = 0, y = 0)
	shops_button.place(x = 550, y = 350)
	items_button.place(x = 760, y = 350)
	logout_button.place(x=150, y=730)

	Cpanel.mainloop()