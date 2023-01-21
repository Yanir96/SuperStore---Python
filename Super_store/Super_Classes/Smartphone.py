from Home_work_year_2.Super_store.Super_Classes.Product import Product


class Smartphone(Product):
    def __init__(self, product_id, brand, model, year, price, cell_net, num_cores, cam_res):
        super().__init__(product_id, brand, model, year, price)
        self.cell_net = str(cell_net)
        self.num_cores = int(num_cores)
        self.cam_res = float(cam_res)

    def print_me(self):
        """A method that prints the smartphone objects."""
        print("\nid:", self.product_id,  "\n""Brand:", self.brand, "\nModel:", self.model,
              "\nYear:",
              self.year, "\nPrice:", self.price, "\nCpu name:", self.cell_net, "\nHard disk size:", self.num_cores,
              "\nScreen size:", self.cam_res)

    def __str__(self):
        """A method that returns the smartphone objects by string."""
        return f"{self.product_id},Smartphone,{self.brand},{self.model},{self.year},{self.price},{self.cell_net},{self.num_cores},{self.cam_res}"

    def __repr__(self):
        """A method that returns the smartphone objects by string."""
        return str(self)
