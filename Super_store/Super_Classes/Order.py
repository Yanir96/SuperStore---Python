class Order:
    def __init__(self, order_id, client_id, product_id, quantity):
        self.order_id = order_id
        self.client_id = client_id
        self.product_id = product_id
        self.quantity = quantity

    def print_me(self):
        """A method that prints the order objects."""
        print("\nId:", self.order_id, "\nClient id:", self.client_id, "\nProduct id:", self.product_id,
              "\nQuantity:", self.quantity)

    def __str__(self):
        """A method that returns the order objects by string."""
        return f"{self.order_id},{self.client_id},{self.product_id},{self.quantity}"

    def __repr__(self):
        """A method that returns the Order objects by string."""
        return str(self)


