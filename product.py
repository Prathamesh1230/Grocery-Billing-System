class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.pid} - {self.name} - Rs.{self.price:.2f}"