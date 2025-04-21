from product import Product

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.pid in self.items:
            self.items[product.pid][1] += quantity
        else:
            self.items[product.pid] = [product, quantity]

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            return True
        return False

    def total(self):
        return sum(p.price * q for p, q in self.items.values())

    def display(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("\nItems in Cart:")
            for p, q in self.items.values():
                print(f"{p.name} - Rs.{p.price} x {q} = Rs.{p.price * q:.2f}")
            print(f"Total Amount: Rs.{self.total():.2f}")

