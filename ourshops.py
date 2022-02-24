from tkinter import*
from tkinter import ttk
import pyodbc
from ctypes import windll

screenSize = [windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1)]

def back():
	ourShops.destroy()
	from homepage import Showhomepage
	Showhomepage()

def ShowOurShops():
	
	global ourShops
	ourShops=Tk()

	ourShops.geometry(f"{screenSize[0]}x{screenSize[1]}")
	ourShops.resizable(0,0)
	ourShops.title("Our Shops")
	ourShops.iconbitmap('.\images\icon_img.ico')

	orange_frame=Frame(ourShops,bg="#febe53",width=1524,height=900)
	white_frame=Frame(ourShops,bg="white",width=950,height=730)
	black_frame=Frame(ourShops,bg="grey",width=725,height=690)
	manage_shops=Label(white_frame,text="OURSHOPS",bg="white",fg="#febe53",font=("aerial",25,"bold"))

	back_button = Button(orange_frame, text="Back", bg="#febe53", fg="white", font=("aerial", 13, "italic"), command = back)


	col=("sID","sName","sLoc")

	shops=ttk.Treeview(ourShops,height=32,columns=col)

	shops.column("#0",width=0,minwidth=0)
	shops.column("sID",width=200,minwidth=200,anchor=CENTER)
	shops.column("sName",width=300,minwidth=300,anchor=CENTER)

	shops.column("sLoc",width=200,anchor=CENTER)
	shops.heading("sID",text="ID",anchor=CENTER)
	shops.heading("sName",text="Name",anchor=CENTER)
	shops.heading("sLoc",text="Location",anchor=CENTER)

	dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
							  r'DBQ=.\shopping mall.accdb;')

	cur=dbHandle.cursor()
	cur.execute("SELECT sID,sName,sLoc FROM `shops`")
	
	cache_rows=cur.fetchall()

	j=0
	for i in cache_rows:
		id = i[0]
		name = i[1]
		loc = i[2]
		if j % 2 == 0:
			shops.insert('', END, iid = j, values=(id, name, loc),tags=("even",))
		else:
			shops.insert('', END, iid = j, values=(id, name, loc), tags=("odd",))
		j += 1
	shops.tag_configure("even", foreground="black", background="gray82")
	shops.tag_configure("odd", foreground="black", background="white")

	orange_frame.place(x=0,y=0)
	white_frame.place(x=300,y=50)
	black_frame.place(x=415,y=75)
	manage_shops.place(x=440,y=15)
	shops.place(x=426,y=85)
	back_button.place(x=150,y=730)

	ourShops.mainloop()
