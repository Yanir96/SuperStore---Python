from Home_work_year_2.Super_store.Super_Classes.Smartphone import Smartphone
from Home_work_year_2.Super_store.Super_Classes.Laptop import Laptop
from Home_work_year_2.Super_store.Super_functions.Most_frequent import most_frequent
from Home_work_year_2.Super_store.Super_Classes.Client import Client
from Home_work_year_2.Super_store.Super_Classes.Product import Product
from Home_work_year_2.Super_store.Super_Classes.Shirts import Shirts
from Home_work_year_2.Super_store.Super_Classes.Order import Order


class SuperStore:

    def __init__(self, products, clients, orders):
        """An init method that gets 2 lists(products,clients,orders) """
        self.products = products
        self.clients = clients
        self.orders = orders

    def __iadd__(self, new):
        """An iadd method that gets a product/client
         and adds this instance to the list of products/clients. """
        if type(new) == Client:
            if self.add_client(new):
                print("The client has been added!")
            else:
                print("The client is all ready exists.")
        elif type(new) == Product or type(new) == Smartphone or type(new) == Laptop:
            if self.add_product(new):
                print("The product has been added!")
            else:
                print("The product is all ready exists in the store.")

        return self

    def print_products(self):
        """A method that prints the stores products."""
        for product in self.products:
            try:
                product.print_me()
            except AttributeError:
                pass

    def get_product(self, product_id_to_check):
        """A method that gets the products id and returns the product(if not in stock returns "none")"""
        for product in self.products:
            if type(product) == Product or type(product) == Smartphone or type(product) == Laptop or \
                    type(product) == Shirts:
                if product.product_id == str(product_id_to_check):
                    # print("Yes")
                    return product
        return "None"

    def get_shirt(self, shirt_id):
        """A method that gets the products id and returns the shirt(if not in stock returns "none")"""
        for shirt in self.products:
            if type(shirt) == Shirts:
                if shirt.product_id == str(shirt_id) or shirt.product_id == int(shirt_id):
                    return shirt
        return "None"

    def add_product(self, new_product):
        """A method that gets a product,if there is such a product(by id) - returns "False"
         else - it adds the product and returns "True"""
        if str(self.get_product(new_product.product_id)) == "None":
            self.products.append(new_product)
            return True
        else:
            return False

    def remove_product(self, product_id_to_remove):
        """A method thar gets a product,if there is such a product(by id) - returns "True" and remove this product
             # else -  returns "False"""
        if self.get_product(product_id_to_remove) == "None":
            return False
        else:
            product_to_remove = self.get_product(product_id_to_remove)
            self.products.remove(product_to_remove)
            return True

    def get_all_by_brand(self, brand_name):
        """A method that gets a brand name, returns a list of those brands products."""
        brands_products = []
        for product in self.products:
            if brand_name == product.brand:
                brands_products.append(product)
        return brands_products

    def get_all_by_price_under(self, max_price):
        """A method that gets a max price,returns a list of the products that under that price."""
        products_under_max_price = []
        for product in self.products:
            try:
                if float(max_price) > float(product.price):
                    products_under_max_price.append(product)
            except:
                pass
        return products_under_max_price

    def get_all_by_price_upper(self, min_price):
        """A method that gets a max price,returns a list of the products that under that price."""
        products_upper_min_price = []
        for product in self.products:
            if float(min_price) < float(product.price):
                products_upper_min_price.append(product)
        return products_upper_min_price

    def get_most_expensive_product(self):
        """A method that returns the most expensive product."""
        max_price = 0
        for product in self.products:
            try:
                if int(product.price) > int(max_price):
                    most_expensive_product = product
                    max_price = most_expensive_product.price
            except AttributeError:
                pass
        return most_expensive_product

    def print_clients(self):
        """A method that prints the stores clients."""
        for client in self.clients:
            client.print_me()

    def get_client(self, client_id_to_check):
        """A method that gets the clients id and returns the client(if not in exist returns "none")"""
        check = False
        for client in self.clients:
            if client.client_id == str(client_id_to_check):
                return client
        return "None"

    def add_client(self, new_client):
        """ A method that gets a client,if there is such a client(by id) - returns "False"
        else - it adds the client and returns "True" """
        if str(self.get_client(new_client.client_id)) == "None":
            self.clients.append(new_client)
            return True
        else:
            return False

    def remove_client(self, client_id_to_remove):
        """A method thar gets a client,if there is such a client(by id) - returns "True" and remove this client
         else -  returns "False """
        if self.get_client(client_id_to_remove) == "None":
            return False
        else:
            client_to_remove = self.get_client(client_id_to_remove)
            self.clients.remove(client_to_remove)
            return True

    def get_all_phones(self):
        """A method that returns a list with all Smartphones type."""
        list_of_phones = []
        for product in self.products:
            if type(product) is Smartphone:
                list_of_phones.append(product)
        return list_of_phones

    def get_all_laptops(self):
        """A method that returns all Laptop type."""
        list_of_laptops = []
        for product in self.products:
            if type(product) is Laptop:
                list_of_laptops.append(product)
        return list_of_laptops

    def phone_average_price(self):
        """A method that calculates the average price of all Smartphones type."""
        list_of_phones = self.get_all_phones()
        sum_of_price = 0
        for phone in list_of_phones:
            sum_of_price += phone.price
        return sum_of_price / len(list_of_phones)

    def get_max_screen(self):
        """A method that returns the largest screen in the store."""
        list_of_laptops = self.get_all_laptops()
        max_screen = 0
        for laptop in list_of_laptops:
            if laptop.screen > max_screen:
                max_screen = laptop.screen
        return max_screen

    def get_common_cam(self):
        """A method that returns the most common cam_res"""
        list_of_phones = self.get_all_phones()
        list_of_cam = []
        for phone in list_of_phones:
            list_of_cam.append(phone.cam_res)
        most_frequent_cam = most_frequent(list_of_cam)
        return most_frequent_cam

    def get_max_order_id(self):
        """"A method that returns the highest order id number """
        return self.orders[-1].order_id

    def add_order(self, client_id, product_id, quantity):
        """A method that gets order details and adds the order to the orders list"""
        order_id = int(self.get_max_order_id()) + 1
        new_order = Order(order_id, client_id, product_id, quantity)
        self.orders.append(new_order)
        print("Order has been added!")

    def print_orders(self):
        """A method that prints the stores orders."""
        for order in self.orders:
            order.print_me()

    def get_all_clients(self):
        """A method that returns a dict with all Clients with empty values."""
        dict_of_clients = {}
        for client in self.clients:
            dict_of_clients[client.client_id] = ""
        return dict_of_clients


