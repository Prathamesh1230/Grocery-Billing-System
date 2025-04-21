from inventory import Inventory
from cart import Cart

inventory = Inventory()
cart = Cart()

while True:
    print("\n--- Grocery Store Billing System ---")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout and Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        inventory.list_products()

    elif choice == '2':
        pid = input("Enter Product ID: ")
        product = inventory.get_product(pid)
        if product:
            qty = int(input("Enter quantity: "))
            cart.add_item(product, qty)
            print("Added to cart.")
        else:
            print("Invalid Product ID.")

    elif choice == '3':
        pid = input("Enter Product ID to remove: ")
        if cart.remove_item(pid):
            print("Removed from cart.")
        else:
            print("Product not in cart.")

    elif choice == '4':
        cart.display()

    elif choice == '5':
        print("\nFinal Bill:")
        cart.display()
        print("\nThank you for shopping with us!")
        break

    else:
        print("Invalid choice.")