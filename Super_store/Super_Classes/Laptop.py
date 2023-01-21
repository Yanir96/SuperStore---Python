from Home_work_year_2.Super_store.Super_Classes.Product import Product


class Laptop(Product):
    def __init__(self, product_id, brand, model, year, price, cpu, hard_disk, screen):
        super().__init__(product_id, brand, model, year, price)
        self.cpu = str(cpu)
        self.hard_disk = int(hard_disk)
        self.screen = float(screen)

    def print_me(self):
        """A method that prints the laptop objects."""
        print("\nid:", self.product_id, "\nBrand:", self.brand
              , "\nModel:", self.model, "\nYear:", self.year, "\nPrice:", self.price, "\nCpu name:", self.cpu
              , "\nHard disk size:", self.hard_disk, "\nScreen size:", self.screen)

    def __str__(self):
        """A method that returns the laptop objects by string."""
        return f"{self.product_id},laptop,{self.brand},{self.model},{self.year},{self.price}," \
               f"{self.cpu},{self.hard_disk},{self.screen}"

    def __repr__(self):
        """A method that returns the laptop objects by string."""
        return str(self)
