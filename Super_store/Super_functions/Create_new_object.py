from Home_work_year_2.Super_store.Super_Classes.Product import Product
from Home_work_year_2.Super_store.Super_Classes import Client
from Home_work_year_2.Super_store.Super_functions import Check_Email
from Home_work_year_2.Super_store.Super_Classes.Smartphone import Smartphone
from Home_work_year_2.Super_store.Super_Classes.Laptop import Laptop


def create_new_product():
    """A function that gets inputs from the user and returns a Product"""
    product_id = input("Enter the product id:")
    while not product_id.isnumeric():
        product_id = input("Wrong input!\nenter the product type(numbers only):")
    product_type = input("Enter the product type:")
    while not product_type.isalpha():
        product_type = input("Wrong input!\nEnter the product type(letters only!):")
    product_brand = input("Enter the product brand:")
    product_model = input("Enter the product model:")
    product_year = input("Enter the product year:")
    while product_year.isnumeric() is False or len(product_year) != 4:
        product_year = input("Wrong input!\nEnter the product year(4 numbers only!):")
    product_price = input("Enter the product price(float):")
    while not product_price.isnumeric():
        product_price = input("Wrong input!\nEnter the product price(numbers only):")
    if product_type.upper() == "LAPTOP":
        cpu = input("Enter CPU name:")
        hard_disk = input("Enter the size of the hard disk(GB)")
        while not hard_disk.isnumeric():
            hard_disk = input("Wrong input!\nenter the size of the hard disk(numbers only):")
        screen = input("Enter the size of the screen(Inch)")
        while not hard_disk.isnumeric():
            hard_disk = input("Wrong input!\nenter the size of the screen(numbers only):")
        return Laptop(product_id, product_brand, product_model, product_year, product_price, cpu, hard_disk, screen)
    elif product_type.upper() == "SMARTPHONE":
        cell_net = input("Enter the cell_net:")
        num_cores = input("Enter the number of the cores:")
        while not num_cores.isnumeric():
            num_cores = input("Wrong input!\nEnter the number of the cores(numbers only):")
        cam_res = input("Enter the resolution of the camera:")
        while not cam_res.isnumeric():
            cam_res = input("Wrong input!\nEnter the resolution of the camera (numbers only):")
        return Smartphone(product_id, product_brand, product_model, product_year, product_price, cell_net,
                          num_cores, cam_res)
    else:
        return Product(product_id, product_brand, product_model, product_year, product_price)


def create_new_client():
    """A function that gets inputs from the user and returns a Client"""
    client_id = input("Enter the client id(numbers only):")
    while not client_id.isnumeric():
        client_id = input("Wrong input!\nenter the client id(numbers only):")

    client_name = input("Enter the client name:")
    while not client_name.isalpha():
        client_name = input("Wrong input!\nenter the client name(letters only):")
    client_mail = input("Enter the clients Email :")
    while Check_Email.check_email(client_mail) == "Invalid Email":
        client_mail = input("Wrong input!\nEnter the clients Email again(__@__.com):")

    client_address = input("Enter the clients address:")
    client_phone = input("Enter the clients phone number:")
    while client_phone.isnumeric() == False or len(client_phone) != 10:
        client_phone = input("Wrong input!\nenter the client phone(10 numbers only):")

    client_gender = input("Enter the clients gender(F or M):")
    while client_gender.upper() != "F" and client_gender.upper() != "M":
        client_gender = input("Wrong input!\nenter the client name(F or M):")
    return Client.Client(client_id, client_name, client_mail, client_address, client_phone, client_gender)


def create_new_order():
    """A function that gets inputs from the user and returns an Order"""
    client_id = input("Enter the clients id:")
    product_id = input("Enter the product id:")
    quantity = input("Enter the quantity:")

    return client_id,product_id,quantity
