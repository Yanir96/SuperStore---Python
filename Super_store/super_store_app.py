from Home_work_year_2.Super_store.Exceptions_Classes.Errors import IdError, PriceError, ThirdEntryError, \
    SecondEntryError, YearError
from Home_work_year_2.Super_store.Super_Classes.SuperStore import SuperStore
from Home_work_year_2.Super_store.Super_functions.Csv_To_List import map_csv
from Home_work_year_2.Super_store.Super_Classes.Laptop import Laptop
from Home_work_year_2.Super_store.Super_Classes.Shirts import Shirts
from Home_work_year_2.Super_store.Super_Classes.Smartphone import Smartphone
from Home_work_year_2.Super_store.Exceptions_Classes.validators import VALID_YEARS, validate_year, validate_price, \
    validate_second_entry, validate_third_entry
from Home_work_year_2.Super_store.Exceptions_Classes.validators import validate_id
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *


clients, products, shirts, orders = map_csv(["clients.csv", "products_supply.csv", "shirts.csv", "orders.csv"])
list_of_products = products + shirts
list_of_clients = clients
list_of_orders = orders
super_store = SuperStore(list_of_products, list_of_clients, list_of_orders)

# Creating tkinter window
window = tk.Tk()
window.title('Super Store')
window.geometry('1250x500')


# Image label
img = PhotoImage(file="super_store_image.png")
label_photo = tk.Label(window, image=img, height=150, width=360, bg="#3d84bf")
label_photo.place(x=60, y=10)

# Label product type selection
select_product_lbl = Label(window, text="Select product type :", font=("Tomaha", 15), fg="#3d84bf")
select_product_lbl.place(x=60, y=180)

# Status label
status_text = ""
status_lbl = Label(window, text=status_text, font=("Tomaha", 10), fg="#990F02")

# Combobox creation
n = tk.StringVar()
product_choosen = ttk.Combobox(window, width=27, textvariable=n)

# Adding combobox drop down list
product_choosen['values'] = (' All products',
                             ' Laptops',
                             ' Smartphone',
                             ' Shirts')


def display_product_click():
    """A function that activates the display product button"""
    this_product = product_choosen.get()
    listbox.delete(0, END)
    if this_product == ' All products':
        this_row = 0
        for product in super_store.products:
            listbox.insert(this_row, product)
            listbox.insert(this_row + 1, "")
            this_row += 2

    elif this_product == ' Laptops':
        this_row = 0
        for product in super_store.products:
            if type(product) == Laptop:
                listbox.insert(this_row, product)
                listbox.insert(this_row + 1, "")
                this_row += 2

    elif this_product == ' Smartphone':
        this_row = 0
        for product in super_store.products:
            if type(product) == Smartphone:
                listbox.insert(this_row, product)
                listbox.insert(this_row + 1, "")
                this_row += 2

    elif this_product == ' Shirts':
        this_row = 0
        for product in super_store.products:
            if type(product) == Shirts:
                listbox.insert(this_row, product)
                listbox.insert(this_row + 1, "")
                this_row += 2


# Creates button and use it
product_choosen.place(x=335, y=195)
product_choosen.current()
btn = Button(window, text="Display products", width=15, height=2, command=display_product_click)
btn.place(x=525, y=185)

# Creates listbox object
listbox = Listbox(window, height=12, width=70, bg="#3d84bf", activestyle='dotbox',
                  font=("Tahoma", 10),
                  fg="white")

# Prints the listbox
listbox.place(x=700, y=20)

# Adding scrollbar
scrollbar = Scrollbar(window,width= 25)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Prints label of "create new product"
create_product_lbl = Label(window, text="Create new product:", fg="#3d84bf", font=("Tahoma", 15))
create_product_lbl.place(x=60, y=270)

# Defines the heights of the rows for the entries and their labels
first_row_height = 260
second_row_height = 280

# Prints the entries and their labels
title_lbl_id = Label(window, text="ID")
title_lbl_id.place(x=360, y=first_row_height)
id_entry = Entry(window, width=20)
id_entry.place(x=350, y=second_row_height)
id_entry.focus()

title_lbl_price = Label(window, text="Price")
title_lbl_price.place(x=510, y=first_row_height)
price_entry = Entry(window, width=20)
price_entry.place(x=500, y=second_row_height)
price_entry.focus()

title_lbl_brand = Label(window, text="Brand")
title_lbl_brand.place(x=660, y=first_row_height)
brand_entry = Entry(window, width=20)
brand_entry.place(x=650, y=second_row_height)
brand_entry.focus()

title_lbl_model = Label(window, text="Model")
title_lbl_model.place(x=810, y=first_row_height)
model_entry = Entry(window, width=20)
model_entry.place(x=800, y=second_row_height)
model_entry.focus()

year_lbl = Label(window, text="Year")
year_lbl.place(x=960, y=first_row_height)
year_combo = ttk.Combobox(window, values=VALID_YEARS)
year_combo.place(x=950, y=second_row_height)

# Defines the heights of the rows for the entries and their labels
first_row_height = 380
second_row_height = 400

# Prints the entries and their labels
title_lbl_first = Label(window, text="")
title_lbl_first.place(x=360, y=first_row_height)
first_entry = Entry(window, width=20)
first_entry.place(x=350, y=second_row_height)
first_entry.focus()

title_lbl_second = Label(window, text="")
title_lbl_second.place(x=510, y=first_row_height)
second_entry = Entry(window, width=20)
second_entry.place(x=500, y=second_row_height)
second_entry.focus()

title_lbl_third = Label(window, text="")
title_lbl_third.place(x=660, y=first_row_height)
third_entry = Entry(window, width=20)
third_entry.place(x=650, y=second_row_height)
third_entry.focus()


def radio_laptop_button():
    """A function that activates the laptop radio button"""
    global status_text
    status_text = ""
    status_lbl.configure(text=str(status_text))
    first_entry.delete(0, END)
    second_entry.delete(0, END)
    third_entry.delete(0, END)
    title_lbl_first["text"] = "CPU"
    title_lbl_second["text"] = "Hard disk"
    title_lbl_third["text"] = "Screen"


def radio_phone_button():
    """A function that activates the smartphone radio button"""
    global status_text
    status_text = ""
    status_lbl.configure(text=str(status_text))
    first_entry.delete(0, END)
    second_entry.delete(0, END)
    third_entry.delete(0, END)
    title_lbl_first["text"] = "Cellular network"
    title_lbl_second["text"] = "Number of cores"
    title_lbl_third["text"] = "Camera resolution"


# Set Radio buttons
mood_lbl = Label(window, text="What kind of product to create?", font=("Tahoma", 12)
                 , fg="#3d84bf")
mood_lbl.place(x=60, y=340)

product_var = StringVar()
r_laptop = Radiobutton(window, text="laptop", font=("Tahoma", 10), value="laptop",
                       command=radio_laptop_button)
r_laptop.place(x=100, y=380)

r_phone = Radiobutton(window, text="smartphone", font=("Tahoma", 10), value="smartphone",
                      command=radio_phone_button)
r_phone.place(x=100, y=400)

radio_phone_button()


def create_new_product():
    """A function that checks the data that was inputted from the user, and raises exceptions if needed"""
    global status_text

    # to restart the label
    status_text = ""
    status_lbl.configure(text=str(status_text))

    product_id = id_entry.get()
    price = price_entry.get()
    brand = brand_entry.get()
    model = model_entry.get()
    year = year_combo.get()
    try:
        if str(title_lbl_first["text"]) == "CPU":
            entry2 = "Disk size"
            entry3 = "Screen size"
            cpu = first_entry.get()
            disk = second_entry.get()
            screen = third_entry.get()
            new_product = Laptop(validate_id(product_id), brand, model, validate_year(year), validate_price(price)
                                 , cpu, validate_second_entry(disk), validate_third_entry(screen))
        else:
            entry2 = "Number of cores"
            entry3 = "Resolution"
            cell_net = first_entry.get()
            num_cores = second_entry.get()
            cam_res = third_entry.get()
            new_product = Smartphone(validate_id(product_id), brand, model, validate_year(year), validate_price(price)
                                     , cell_net, validate_second_entry(num_cores), validate_third_entry(cam_res))

        if super_store.add_product(new_product):
            first_entry.delete(0, END)
            second_entry.delete(0, END)
            third_entry.delete(0, END)
            id_entry.delete(0, END)
            brand_entry.delete(0, END)
            year_combo.delete(0, END)
            model_entry.delete(0, END)
            price_entry.delete(0, END)

            messagebox.showinfo(title="Product added!", message=new_product)
        else:
            id_entry.configure()

            messagebox.showerror(title="This ID is already exists!")
    except IdError as e:
        status_text = e
        status_x = 340
        status_y = 300
        status_lbl.place(x=status_x, y=status_y)
        status_lbl.configure(text=str(status_text))

    except PriceError as e:
        status_text = e
        status_x = 480
        status_y = 300
        status_lbl.place(x=status_x, y=status_y)
        status_lbl.configure(text=str(status_text))

    except YearError as e:
        status_text = e
        status_x = 910
        status_y = 300
        status_lbl.place(x=status_x, y=status_y)
        status_lbl.configure(text=str(status_text))

    except SecondEntryError as e:
        status_text = e
        status_x = 480
        status_y = 420
        status_lbl.place(x=status_x, y=status_y)
        status_lbl.configure(text=f"{entry2} {status_text}")

    except ThirdEntryError as e:
        status_text = e
        status_x = 620
        status_y = 420
        status_lbl.place(x=status_x, y=status_y)
        status_lbl.configure(text=f"{entry3} {status_text}")


# create button and use it
btn2 = Button(window, text="Create", width=15, height=2, command=create_new_product)
btn2.place(x=850, y=390)

# pack the widgets
window.mainloop()
