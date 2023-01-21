class Product:
    def __init__(self, product_id, brand, model, year, price):
        self.product_id = product_id
        self.brand = brand
        self.model = model
        self.year = int(year)
        self.price = float(price)

    def print_me(self):
        """A method that prints the products objects."""
        print("\nid:", self.product_id, "\nBrand:", self.brand, "\nModel:", self.model, "\nYear:", self.year,
              "\nPrice:", self.price)

    def __str__(self):
        """A method that returns the product objects by string."""
        return f"{self.product_id},{self.brand},{self.model},{self.year},{self.price}"

    def __repr__(self):
        """A method that returns the product objects by string."""
        return str(self)

    def is_popular(self):
        return self.year > 2017 and self.price <= 3000
