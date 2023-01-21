class Client:
    def __init__(self, client_id, name, email, address, number, gender):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.address = address
        self.number = number
        self.gender = gender

    def print_me(self):
        """A method that prints the clients objects."""
        print("Client ID:", self.client_id, "\nName:", self.name
              , "\nEmail:", self.email, "\nAddress:", self.address, "\nNumber:", self.number, "\nGender:", self.gender)

    def __str__(self):
        """A method that returns the clients objects by string."""
        return f"{self.client_id}, {self.name}, {self.email}, {self.address}, {self.number}, {self.gender}"

    def __repr__(self):
        """A method that returns the clients objects by string."""
        return str(self)
