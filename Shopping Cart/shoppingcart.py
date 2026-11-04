
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
BILL_FILE = BASE_DIR / "shopping_bill.txt"

cart = {}

def add_item():
    food = input("\nEnter food name: ").strip().title()
    if not food:
        print("Food name cannot be empty.")
        return
    try:
        price = float(input("Enter price: $"))
        if price <= 0:
            print("Price must be greater than zero.")
            return
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
    except ValueError:
        print("Please enter valid numeric values.")
        return
    if food in cart:
        cart[food]["quantity"] += quantity
        cart[food]["price"] = price
        print(f"{food} quantity updated successfully.")
    else:
        cart[food] = {
            "price": price,
            "quantity": quantity
        }

        print(f"{food} added to cart successfully.")

def view_cart():
    print("\n========== YOUR SHOPPING CART ==========")
    if not cart:
        print("Your cart is empty.")
        return
    print(f"{'Item':<15}{'Price':<12}{'Qty':<8}{'Subtotal'}")
    print("-" * 50)
    for index, (food, details) in enumerate(cart.items(), start=1):
        price = details["price"]
        quantity = details["quantity"]
        subtotal = price * quantity

        print(
            f"{index}. {food:<12}"
            f"${price:<11.2f}"
            f"{quantity:<8}"
            f"${subtotal:.2f}"
        )

    print("-" * 50)

    total_items = sum(item["quantity"] for item in cart.values())
    total = calculate_subtotal()

    print(f"Total items: {total_items}")
    print(f"Cart subtotal: ${total:.2f}")

def calculate_subtotal():
    total = 0
    for details in cart.values():
        total += details["price"] * details["quantity"]
    return total
def remove_item():
    if not cart:
        print("\nYour cart is empty.")
        return
    view_cart()
    food = input("\nEnter item name to remove: ").strip().title()
    if food in cart:
        del cart[food]
        print(f"{food} removed successfully.")
    else:
        print("Item not found in your cart.")

def update_quantity():
    if not cart:
        print("\nYour cart is empty.")
        return
    view_cart()
    food = input("\nEnter item name: ").strip().title()
    if food not in cart:
        print("Item not found.")
        return
    try:
        quantity = int(input("Enter new quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        cart[food]["quantity"] = quantity
        print(f"{food} quantity updated successfully.")
    except ValueError:
        print("Please enter a valid quantity.")

def apply_discount(subtotal):

    print("\n========== DISCOUNT COUPONS ==========")
    print("SAVE10 - 10% discount")
    print("SAVE20 - 20% discount")
    print("NO - Skip discount")

    coupon = input("\nEnter coupon code: ").strip().upper()

    if coupon == "SAVE10":
        discount = subtotal * 0.10

    elif coupon == "SAVE20":
        discount = subtotal * 0.20

    elif coupon == "NO":
        discount = 0

    else:
        print("Invalid coupon. No discount applied.")
        discount = 0

    return discount

def generate_bill():
    if not cart:
        print("\nYour cart is empty. Add items first.")
        return
    subtotal = calculate_subtotal()
    discount = apply_discount(subtotal)
    discounted_total = subtotal - discount
    gst_rate = 0.05
    gst = discounted_total * gst_rate
    final_total = discounted_total + gst
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    bill = []

    bill.append("\n========== SHOPPING BILL ==========")
    bill.append(f"Date: {current_time}")
    bill.append("-" * 45)
    bill.append(f"{'Item':<15}{'Price':<10}{'Qty':<6}{'Total'}")
    bill.append("-" * 45)

    for food, details in cart.items():

        price = details["price"]
        quantity = details["quantity"]
        item_total = price * quantity

        bill.append(
            f"{food:<15}${price:<9.2f}{quantity:<6}${item_total:.2f}"
        )

    bill.append("-" * 45)
    bill.append(f"Subtotal:       ${subtotal:.2f}")
    bill.append(f"Discount:       -${discount:.2f}")
    bill.append(f"GST (5%):       ${gst:.2f}")
    bill.append(f"Final Total:     ${final_total:.2f}")
    bill.append("=" * 45)
    bill.append("Thank you for shopping!")

    print("\n" + "\n".join(bill))

    # Save bill to text file
    with open(BILL_FILE, "a") as file:
        file.write("\n".join(bill))
        file.write("\n\n")

    print(f"\nBill saved successfully at: {BILL_FILE}")


def main():

    while True:

        print("\n========== SHOPPING CART ==========")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Update quantity")
        print("5. Generate bill")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                add_item()
            elif choice == 2:
                view_cart()
            elif choice == 3:
                remove_item()
            elif choice == 4:
                update_quantity()
            elif choice == 5:
                generate_bill()
            elif choice == 6:
                print("\nThank you for shopping!")
                break
            else:
                print("Invalid choice. Select between 1 and 6.")
        except ValueError:
            print("Please enter a valid menu number.")

if __name__ == "__main__":
    main()
