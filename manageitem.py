from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyodbc


def back():
	m1.destroy()
	from cpanel import showCpanel
	showCpanel()

def logout():
	m1.destroy()
	from loginpage import ShowLoginPage
	ShowLoginPage()

def search(event):
	global val
	val = event.widget.get()
	if val == "":
		combo_box['value'] = categories
	else:
		data=[]
		for categ in categories:
			if val.lower() in categ.lower():
				data.append(categ)
			combo_box['value'] = data


def display():
	try:
		dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
								r'DBQ=.\shopping mall.accdb;')
		cur4 = dbHandle.cursor()
		cur4.execute(f"SELECT * FROM `{val}`")
	except NameError:
		return messagebox.showerror("Error!", "Please select a shop")
		
	for row in product_list.get_children():
		product_list.delete(row)
	
	all_data = cur4.fetchall()
	if(len(all_data) == 0): return messagebox.showerror("Error!", "No data found to be displayed")

	j=0
	for i in all_data:
		id = i[0]
		name = i[1]
		qty = i[2]
		pr = i[3]
		if j % 2 == 0:
			product_list.insert(parent='', index='end', iid=j, values=(id, name, qty, pr),tags=("even",))
		else:
			product_list.insert(parent='', index='end', iid=j, values=(id, name, qty, pr), tags=("odd",))
		j += 1
	product_list.tag_configure("even", foreground="black", background="gray82")
	product_list.tag_configure("odd", foreground="black", background="white")
	dbHandle.close()

	var_id.set(0)
	var_name.set("")
	var_quantity.set(0)
	var_price.set(0)

def add():
	if(var_id.get() == 0 or var_name.get() == "" or var_price.get() == 0 or var_quantity.get() == 0): return messagebox.showerror("Error!", "fields cannot be empty")

	dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
							  r'DBQ=.\shopping mall.accdb;')
	cur1 = dbHandle.cursor()
	cur1.execute(f"insert into {val}(id,name,quantity,price) "
				f"values({var_id.get()},'{var_name.get()}',{var_quantity.get()},{var_price.get()})")

	dbHandle.commit()
	dbHandle.close()
	display()
	messagebox.showinfo("Information", f"{cur1.rowcount} item added")


def edit():
	if(var_id.get() == 0 or var_name.get() == "" or var_price.get() == 0 or var_quantity.get() == 0): return messagebox.showerror("Error!", "fields cannot be empty")
	dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
							  r'DBQ=.\shopping mall.accdb;')
	cur2 = dbHandle.cursor()
	cur2.execute(f"update `{val}` set name='{var_name.get()}',"
				f" quantity={var_quantity.get()}, price={var_price.get()} where id={var_id.get()}")
	dbHandle.commit()
	dbHandle.close()
	display()
	messagebox.showinfo("Information", f"{cur2.rowcount} Row updated")


def delete():
	if(var_id.get() == 0): return messagebox.showerror("Error!", "ID cannot be empty")
	dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
							  r'DBQ=.\shopping mall.accdb;')
	cur3 = dbHandle.cursor()
	cur3.execute(f"delete from `{val}` where id={var_id.get()}")
	dbHandle.commit()
	dbHandle.close()
	display()
	messagebox.showinfo("Information", f"{cur3.rowcount} Row deleted")

def updateForEdit(_):
	current = product_list.focus()
	currentItem = product_list.item(current)
	currentItem = currentItem["values"]

	if(current != ""):
		var_id.set(currentItem[0])
		var_name.set(currentItem[1])
		var_quantity.set(currentItem[2])
		var_price.set(currentItem[3])

def showItemManage():
	global m1
	m1 = Tk()

	m1.state('zoomed')
	m1.title("Items Management")
	m1.iconbitmap('.\images\icon_img.ico')
	m1.resizable(0,0)

	global var_id, var_name, var_price, var_quantity
	var_id = IntVar()
	var_name = StringVar()
	var_quantity= IntVar()
	var_price = IntVar()


	# shops items management screen
	# labels
	orange_frame = Frame(m1, bg="#febe53", width=1536, height=864)
	white_frame = Frame(m1, bg="white", width=1220, height=730)
	black_frame = Frame(m1, bg="grey", width=1025, height=310 )
	seller_label = Label(orange_frame, text="SELLER", bg="#febe53", fg="white", font=("aerial", 30))
	categories_label = Label(orange_frame, text="CATEGORIES", bg="#febe53", fg="white", font=("aerial", 30))
	manage_products = Label(white_frame, text="MANAGE PRODUCTS", bg="white", fg="#febe53", font=("aerial", 25, "bold"))
	id = Label(white_frame, text="ProductID", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
	name = Label(white_frame, text="NAME", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
	quantity = Label(white_frame, text="QUANTITY", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
	price = Label(white_frame, text="PRICE", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
	category = Label(white_frame, text="SHOP", bg="white", fg="#febe53", font=("aerial", 15, "bold"))
	product_lis = Label(white_frame, text="PRODUCTS LIST", bg="white", fg="#febe53", font=("aerial", 25, "bold"))


	dbHandle = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
								  r'DBQ=.\shopping mall.accdb;')
	# creating combo box
	cur = dbHandle.cursor()
	cur.execute("select sName from shops")
	shops = cur.fetchall()
	global categories
	categories = []
	for i in range(len(shops)):
		a = list(shops[i])
		categories.extend(a)
	global combo_box
	combo_box = ttk.Combobox(white_frame, value=categories, width=22)
	combo_box.insert(0, "Select")



	# creating and placing treeview
	col = ("pid", "pname", "pquantity", "price")
	global product_list
	product_list = ttk.Treeview(m1, height=13, columns=col)

	product_list.column("#0", width=0, minwidth=0)
	product_list.column("pid", width=200, minwidth=200, anchor=CENTER)
	product_list.column("pname", width=300, minwidth=300, anchor=CENTER)
	product_list.column("pquantity", width=300, minwidth=300, anchor=CENTER)
	product_list.column("price", width=200, anchor=CENTER)

	product_list.heading("pid", text="Product ID", anchor=CENTER)
	product_list.heading("pname", text="Product NAME", anchor=CENTER)
	product_list.heading("pquantity", text="Product QUANTITY", anchor=CENTER)
	product_list.heading("price", text="PRICE", anchor=CENTER)

	product_list.place(x=426, y=460)

	# buttons
	back_button = Button(orange_frame, text="Back", bg="#febe53", fg="white", font=("aerial", 13, "italic"), command = back)

	logout_button = Button(orange_frame, text="Logout", bg="#febe53", fg="white", font=("aerial", 13, "italic"), command = logout)
	add_button = Button(white_frame, text="ADD", bg="#febe53", fg="white", width=7, height=1,
						font=("aerial", 15, "italic"), command=add)
	edit_button = Button(white_frame, text="EDIT", bg="#febe53", fg="white", width=7, height=1,
							font=("aerial", 15, "italic"), command=edit)
	delete_button = Button(white_frame, text="DELETE", bg="#febe53", fg="white", width=7, height=1,
							font=("aerial", 15, "italic"), command=delete)
	clear_button = Button(white_frame, text="DISPLAY", bg="#febe53", fg="white", width=7, height=1,
							font=("aerial", 15, "italic"), command=display)


	# entry boxes
	id_entry = Entry(white_frame, bg="white", textvariable=var_id, bd=3, width=25)
	name_entry = Entry(white_frame, bg="white", textvariable=var_name, bd=3, width=25)
	quantity_entry = Entry(white_frame, bg="white", textvariable=var_quantity, bd=3, width=25)
	price_entry = Entry(white_frame, bg="white", textvariable=var_price, bd=3, width=25)




	# putting on screen

	orange_frame.place(x=0, y=0)
	white_frame.place(x=300, y=50)
	black_frame.place(x=415, y=450)
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
	product_lis.place(x=475, y=350)
	back_button.place(x=150, y=690)
	combo_box.place(x=236, y=214)
	combo_box.bind("<<ComboboxSelected>>", search)
	combo_box.bind("<KeyRelease>", search)
	product_list.bind("<Double-Button-1>", updateForEdit)
	
	m1.mainloop()