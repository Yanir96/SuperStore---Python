class ProductNotFoundError(Exception):
    def __str__(self):
        return super().__str__() + "There is no such a product in the store!"

