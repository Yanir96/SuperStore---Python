from Home_work_year_2.Super_store.Super_Classes.Client import Client
from Home_work_year_2.Super_store.Super_Classes.Smartphone import Smartphone
from Home_work_year_2.Super_store.Super_Classes.Laptop import Laptop
from Home_work_year_2.Super_store.Super_Classes.Shirts import Shirts
from Home_work_year_2.Super_store.Super_Classes.Order import Order


def line_to_client(line: str):
    (client_id, name, email, address, number, gender) = line.split(',')
    return Client(client_id, name, email, address, number, gender)


def line_to_product(line: str):
    (product_id, product_type, brand, model, year, price, check1, check2, check3, check4, check5, check6)\
        = line.split(',')

    if product_type == "laptop":
        cpu = check1
        hard_disk = check2
        screen = check3
        return Laptop(product_id, brand, model, year, price, cpu, hard_disk, screen)
    else:
        cell_net = check4
        num_cores = check5
        cam_res = check6
        return Smartphone(product_id, brand, model, year, price, cell_net, num_cores, cam_res)


def line_to_shirt(line: str):
    try:
        (product_id, product_name, price, units_in_stock) = line.split(',')
        return Shirts(product_id, "SuperStore", "", 2023, price, product_name, units_in_stock)
    except ValueError:
        (product_id, product_name, product_name2, price, units_in_stock) = line.split(',')
        return Shirts(product_id, "SuperStore", "", 2023, price, product_name, units_in_stock)


def line_to_order(line: str):
    try:
        (order_id, client_id, product_id, quantity) = line.split(',')
        return Order(order_id, client_id, product_id, quantity)
    except ValueError:
        pass


def clear_str(file_list):
    for cell in file_list:
        if type(cell) == {None}:
            file_list.remove(cell)
    return file_list


def map_csv(list_of_files):
    for file in list_of_files:
        is_ok = False
        while not is_ok:
            try:
                with open(file) as csvfile:
                    lines = csvfile.readlines()
                    if file == "clients.csv":
                        clients_map = list(map(line_to_client, lines[1:]))
                        is_ok = True
                    elif file == "products_supply.csv":
                        products_map = list(map(line_to_product, lines[1:]))
                        is_ok = True
                    elif file == "shirts.csv":
                        shirts_map = list(map(line_to_shirt, lines[1:]))
                        is_ok = True
                    elif file == "orders.csv":
                        orders_map = list(map(line_to_order, lines[1:]))
                        is_ok = True
            except FileNotFoundError as e:
                print(e, "\n"f"Couldn't open the file: {file}")
                file = input("insert the file path: ")
    shirts_map = clear_str(shirts_map)
    return clients_map, products_map, shirts_map, orders_map
