from Home_work_year_2.Super_store.Super_functions import Create_new_object
from Home_work_year_2.Super_store.Super_Classes.Shirts import Shirts
from Home_work_year_2.Super_store.Exceptions_Classes.ClientNotFoundError import ClientNotFoundError
from Home_work_year_2.Super_store.Exceptions_Classes.ProductNotFoundError import ProductNotFoundError
from Home_work_year_2.Super_store.shirt_orders_analysis import most_expensive_shirt, shirt_orders_analysis, \
    client_orders_details, orders_clients_dict


def print_menu():
    """A function that prints the main menu"""
    print("\n1.", " Show the products of the store",
          "\t\t\t\t\t2.", " Show the clients of the store", "\n3.", " Add a new product to the store",
          "\t\t\t\t\t4.  Add a new client to the store",
          "\n5.", " Delete a product from the store", "\t\t\t\t6.", " Delete a client from the store",
          "\n7.", " Show products by price filter", "\t\t\t\t\t8.", " Show the most expensive product",
          "\n9.", " Show all phones in the store", "\t\t\t\t\t10.", "Show all laptops in the store",
          "\n11.", "Show the average phone price in the store", "\t\t12.",
          "Show the largest screen size in the store",
          "\n13.", "Show the most common camera in store", "\t\t\t14.", "Show most popular products in the store",
          "\n15.", "Show the shirts in the store", "\t\t\t\t\t16.", "Add new order"
                                                                    "\n17.", "Show all the orders", "\t\t\t\t\t\t\tB.",
          " Drill down to data of the store"
          , "\n\n 18.", "Restart(and reset the data)", "\n", "19." " Exit", "\n")


def print_products(store):
    store.print_products()


def print_clients(store):
    store.print_clients()


def remove_product(store):
    """Removes a product from the store"""
    product_id_to_remove = input("Enter the product id:")
    if store.remove_product(product_id_to_remove):
        print("The product has been removed from the store!")
    else:
        print("This item does not exist in stock!")


def add_new_product(store):
    """Adds new product + validation of the data"""
    new_product = Create_new_object.create_new_product()
    store += new_product


def add_new_client(store):
    """Adds new client + validation of the data"""
    new_client = Create_new_object.create_new_client()
    store += new_client


def remove_client(store):
    """Removes a client from the store"""
    client_id_to_remove = input("Enter the client id:")
    if store.remove_client(client_id_to_remove):
        print("The client has been removed!")
    else:
        print("This client does not exists!")


def print_all_under_price(store):
    """Prints all products under max price."""
    max_price = input("Enter the max price:")
    for product in store.get_all_by_price_under(max_price):
        product.print_me()


def print_most_expensive(store):
    """Prints the most expensive product in the store"""
    most_expensive_product = store.get_most_expensive_product()
    most_expensive_product.print_me()


def print_all_phones(store):
    """Prints all smartphones"""
    phone_list = store.get_all_phones()
    for phone in phone_list:
        phone.print_me()


def print_all_laptops(store):
    """Prints all laptops"""
    laptop_list = store.get_all_laptops()
    for laptop in laptop_list:
        laptop.print_me()


def print_avg_phone(store):
    """Prints the average phone price in the store"""
    print("The average price of a phone in the store is:", "%.2f" % store.phone_average_price())


def print_largest_screen(store):
    """Prints the largest screen size in the store"""
    print("The biggest screen size(in Inch) in the store is:", store.get_max_screen())


def print_most_cam_res(store):
    """Prints most common camera in store"""
    print("Most frequent camera resolution size(in MP) in the store is:", store.get_common_cam())


def print_most_popular(store):
    """Prints most popular products in the store"""
    phones = store.get_all_phones()
    laptops = store.get_all_laptops()
    for phone in phones:
        if phone.is_popular:
            phone.print_me()
    for laptop in laptops:
        if laptop.is_popular:
            laptop.print_me()


def print_shirts(shirts):
    """Prints all the shirts  in the store"""
    for shirt in shirts:
        if type(shirt) == Shirts:
            shirt.print_me()


def add_new_order(store):
    """A function that gets a store and generates new order from input of the user(with exceptions)"""
    is_ok = False
    while not is_ok:
        put_client_id = input("Enter the client id:")
        try:
            if not store.get_client(put_client_id) == "None":
                is_ok = True

            else:
                raise ClientNotFoundError

        except ClientNotFoundError as e:
            print(e)

    is_ok = False
    while not is_ok:
        put_product_id = input("Enter the product id:")
        try:
            if not store.get_product(put_product_id) == "None":
                is_ok = True

            else:
                raise ProductNotFoundError
        except ProductNotFoundError as e:
            print(e)

    is_ok = False
    while not is_ok:
        put_quantity = input("Enter the quantity:")
        if type(store.get_product(put_product_id)) == Shirts:
            try:
                if int(store.get_product(put_product_id).units_in_stock) >= int(put_quantity) > 0:
                    is_ok = True
                else:
                    raise ValueError
            except ValueError as e:
                print(e, f"The quantity of the order has to be bigger then 0 and smaller/equal to the stock of the "
                         f"store:",
                      store.get_product(put_product_id).units_in_stock)
        else:
            try:
                if int(put_quantity) == 1:
                    is_ok = True
                elif int(put_quantity) <= 0:
                    raise ValueError
                else:
                    raise ValueError
            except ValueError as e:
                print(e, f"The quantity of the order has to be bigger then 0 and smaller/equal to the stock of the "
                         f"store:", 1)
    store.add_order(put_client_id, put_product_id, put_quantity)


def print_menu_np():
    """A function that prints the drill down menu"""
    print("\n1.", "Show the most expensive shirt in the store",
          "\t\t\t\t2.Show client order details", " ", "\n3.", "Show all orders that cost more than the average",
          "\t\t\t4.Show all clients and their orders ", "\n5. Show a bar graph of clients vs orders count"
                                                        "\n\n6. Quit to the main menu")


def shirt_max_price(orders_csv, store):
    """A function that gets a csv file of orders and a store and prints most expensive shirt"""
    max_price_shirt_id, max_price_client_name, max_price_shirt_name, max_price = (
        most_expensive_shirt(shirt_orders_analysis(orders_csv, store), store))
    print("\nMost expensive shirt details:")
    print("\n\tShirt id:", max_price_shirt_id, "\n\tClient name:", max_price_client_name,
          "\n\tShirt name:"
          , max_price_shirt_name, "\n\tPrice:", max_price)


def client_order_details(orders_csv, store):
    """A function that gets a csv file of orders and a store and prints orders details about a client"""
    client_name, count_of_orders, sum_of_orders = client_orders_details(shirt_orders_analysis(
        orders_csv, store), store)
    print("\nThe client details are:")
    print("\n\tclient name:", client_name, "\n\tNumber of orders:", count_of_orders,
          "\n\tSum price of the orders:"
          , sum_of_orders)
