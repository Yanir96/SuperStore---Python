import numpy as np
import matplotlib.pyplot as plt

from Home_work_year_2.Super_store.Exceptions_Classes.ClientNotFoundError import ClientNotFoundError
from Home_work_year_2.Super_store.Super_Classes.Order import Order


def shirt_orders_analysis(orders_csv, store):
    """A method that gets csv file of orders and a store and returns the orders(np array)  """
    orders = np.genfromtxt(orders_csv, delimiter=",", skip_header=1, dtype="int32")
    quantity_column = orders[:, 3:4]
    orders = np.append(orders, orders[:, 2:3], axis=1)
    price_column = orders[:, 4:5]
    count = 0
    for price in price_column:
        this_shirt = store.get_shirt(int(price))
        if this_shirt != "None":
            this_price = this_shirt.price
            price_column[count, :] = int(this_price)
            count += 1
    price_column = price_column * quantity_column
    orders[:, 4:5] = price_column
    return orders


def most_expensive_shirt(orders_np, store):
    """A method that gets orders array(np type) and a store and returns details about the max price order"""
    max_price = 0
    place = 0
    place_of_max = 0
    for i in orders_np[:, 4]:
        if int(i) > max_price:
            max_price = int(i)
            place_of_max = place
        place += 1
    max_price_shirt_id = int(orders_np[place_of_max:place_of_max + 1, 0:1])
    max_price_client_name = store.get_client(int((orders_np[place_of_max:place_of_max + 1, 1:2]))).name
    max_price_shirt_name = store.get_shirt(int(max_price_shirt_id)).product_name
    return max_price_shirt_id, max_price_client_name, max_price_shirt_name, max_price


def client_orders_details(orders_np, store):
    """A method that gets an orders array(np type) and a store and returns details about this client orders"""
    is_ok = False
    while not is_ok:
        client_id = input("Enter clients id:")
        try:
            if store.get_client(client_id) == "None":
                raise ClientNotFoundError
            else:
                client_name = store.get_client(client_id).name
                is_ok = True
        except ClientNotFoundError as e:
            print(e)
    count_of_orders = 0
    this_row = 0
    sum_of_orders = 0
    for order in orders_np[:, 1:2]:
        if str(order) == "[" + client_id + "]":
            count_of_orders += 1
            sum_of_orders += orders_np[this_row, 4:5]
        this_row += 1
    return client_name, count_of_orders, int(sum_of_orders)


def orders_above_price_avg(orders_np):
    """A function that gets orders array(np) and prints the orders that their price is above the mean"""
    place = 0
    avg_of_orders = orders_np[:, 4].mean(axis=0)
    print("\nThe orders mean price is:", avg_of_orders)
    for price in orders_np[:, 4]:
        if price > avg_of_orders:
            a = (orders_np[place, :])
            Order(a[0], a[1], a[2], a[3]).print_me()
        place += 1


def orders_clients_dict(orders_np, store):
    """A function that gets orders array(np) and a store and returns a dict(key - client , value - [orders,
    count of orders]) """
    dict_of_clients = store.get_all_clients()
    for client_id in dict_of_clients.keys():
        place = 0
        count_of_orders = 0
        new_value = []
        for order in orders_np[:, 1]:
            if str(order) == client_id:
                count_of_orders += 1
                new_value.append((orders_np[place, 0]))
                dict_of_clients[client_id] = new_value
            place += 1
        new_value.append("Count of orders is:")
        new_value.append(count_of_orders)
        dict_of_clients[client_id] = new_value
    return dict_of_clients


def orders_per_client_graph(dict_of_clients):
    """A function that prints a graph of count of orders per client"""
    list_of_clients = []
    list_of_counts = []
    for key in dict_of_clients:
        list_of_clients.append(key)
        list_of_counts.append(dict_of_clients[key][-1])

    plt.bar(list_of_clients, list_of_counts)
    plt.title("Clients VS Count of Orders", fontdict={"fontname": "Comic Sans MS", "fontsize": 20})
    plt.xlabel("Clients(by id)")
    plt.ylabel("Count of orders")
    plt.show()
