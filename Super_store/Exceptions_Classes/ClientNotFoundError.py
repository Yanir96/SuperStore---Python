class ClientNotFoundError(Exception):
    def __str__(self):
        return super().__str__() + "There is no such a client in the store!"
