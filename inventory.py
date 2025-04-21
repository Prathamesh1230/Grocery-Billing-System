from product import Product

class Inventory:
    def __init__(self):
        self.products = {
            "101": Product("101", "Rice", 50.0),
            "102": Product("102", "Wheat", 40.0),
            "103": Product("103", "Oil", 150.0),
            "104": Product("104", "Sugar", 45.0),
            "105": Product("105", "Salt", 20.0),
        }

    def list_products(self):
        print("\nAvailable Products:")
        for p in self.products.values():
            print(p)

    def get_product(self, pid):
        return self.products.get(pid, None)