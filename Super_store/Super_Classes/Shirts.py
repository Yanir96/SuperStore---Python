from Home_work_year_2.Super_store.Super_Classes.Product import Product


class Shirts(Product):
    def __init__(self, product_id, brand, model, year, price, product_name, units_in_stock):
        super().__init__(product_id, brand, model, year, price)
        self.product_id = product_id
        self.brand = "SuperStore"
        self.model = ""
        self.year = 2023
        self.price = price
        self.product_name = product_name
        self.units_in_stock = units_in_stock

    def print_me(self):
        """A method that prints the shirts objects."""
        print("\nid:", self.product_id, "\nBrand:", self.brand
              , "\nModel:", self.model, "\nYear:", self.year, "\nPrice:", self.price, "\nProduct name:",
              self.product_name,"\nUnits in stock:", self.units_in_stock)

    def __str__(self):
        """A method that returns the shirts objects by string."""
        return f"{self.product_id},{self.brand},{self.model},{self.year},{self.price}," \
               f"{self.product_name},{self.units_in_stock}"

    def __repr__(self):
        """A method that returns the shirts objects by string."""
        return str(self)



