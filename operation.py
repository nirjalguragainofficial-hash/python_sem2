from read import readingfile
from write import make_sales_bill, make_restock_bill

def apply_markup(items):
    """Set selling price to 200% higher than the cost price (2x cost price)."""
    for item in items:
        item["selling_price"] = item["cost_price"] * 2
    return items
    
def load_items():
    items = readingfile("products.txt")
    return apply_markup(items)

items_in_stock = load_items()
def save_items():
    """Save updated stock back to an text file."""
    
    try:
        with open("products.txt", "w") as f:
            for item in items_in_stock:
                line = f"{item['name']}, {item['brand']}, {item['quantity']}, {int(item['cost_price'])}, {item['origin']}\n"
                f.write(line)
                
    except Exception as e:
        print("Error saving data to file:", e)

def show_items():
    products = readingfile("products.txt")
    if products:
        # Apply markup to display correct selling prices
        products = apply_markup(products)
        print("\nPRODUCT LIST:\n" + "-" * 40)
        for p in products:
            print(f"• {p['name']} ({p['brand']})")
            print(f"  Stock: {p['quantity']}, Cost: Rs.{p['cost_price']}, Selling Price: Rs.{p['selling_price']}")
            print("-" * 40)
    else:
        
        print("No products available.")
def process_sale(items, item_name, qty_needed):
    """Handle item sale with free item offer, stock update, and cost calculation."""
    for item in items:
        if item["name"].lower() == item_name.lower():
            free_units = qty_needed // 3
            total_units = qty_needed + free_units

            if total_units > item["quantity"]:
                print(f"Not enough stock to provide {qty_needed} + {free_units} free units.")
                return None
                
            subtotal = qty_needed * item["selling_price"]
            vat = subtotal * 0.13
            total_due = subtotal + vat
            item["quantity"] -= total_units

            return {
                "name": item["name"],
                "brand": item["brand"],
                "quantity_requested": qty_needed,
                "free_items": free_units,
                "Total_item": total_units,
                "total_cost": round(subtotal, 2),
                "VAT": round(vat, 2),
                "Total_bill": round(total_due, 2)
            }

    print("Item not found!")
    return None

def process_restock(items, item_name, added_qty, new_price=None):
    """Update stock quantity and optionally update cost price."""
    for item in items:
        if item["name"].lower() == item_name.lower():
            item["quantity"] += added_qty
  
            if new_price is not None:
                item["cost_price"] = new_price
                item["selling_price"] = new_price * 2  # 100% higher than cost price
            return {
                "name": item["name"],
                "brand": item["brand"],
                "quantity_added": added_qty,
                "cost_price": item["cost_price"],
                "origin": item["origin"]
            }
    print("Item not found during restock.")
    return None

def sell_items():
    while True:
        name = input("Customer name: ").strip()
        if name.replace(" ", "").isalpha():
            break
        print("Please enter a valid name using letters only.")

    while True:
        show_items()

        while True:
            item_name = input("Enter item to buy: ")
            if any(i['name'].lower() == item_name.lower() for i in items_in_stock):
                break
            print("Item not available. Please choose again.")

        while True:
            try:
                qty = int(input("Quantity to purchase: "))
                if qty > 0:
                    break
                print("Quantity must be more than zero.")
            except ValueError:
                print("Enter a valid number.")

        result = process_sale(items_in_stock, item_name, qty)
        if result:
            make_sales_bill(name, result)
            print("*" * 60)
            print("Stock after transaction:")
            for item in items_in_stock:
                print(f"{item['name']} - {item['quantity']}")
            save_items()

        again = input("Buy another item? Type 'yes' to continue: ").strip().lower()
        if again != "yes":
            print("Thanks for shopping with us!")
            break

def restock_items():
    while True:
        supplier = input("Enter supplier name: ").strip()
        if supplier.replace(" ", "").isalpha():
            break
        print("Invalid name. Use letters only.")

    while True:
        item_name = input("Item name: ").strip()
        found = next((i for i in items_in_stock if i['name'].lower() == item_name.lower()), None)

        if found:
            while True:
                try:
                    qty = int(input("Add quantity: "))
                    if qty > 0:
                        break
                    print("Quantity must be positive.")
                except ValueError:
                    print("Enter a number.")

            price_input = input("New cost price? (press Enter to skip): ").strip()
            updated_price = float(price_input) if price_input else None

            found['quantity_added'] = qty
            result = process_restock(items_in_stock, item_name, qty, updated_price)
            if result:
                make_restock_bill(supplier, [result])
                save_items()

        else:
            add_new = input("Item not found. Add it as new? (yes/no): ").strip().lower()
            if add_new == "yes":
                brand = input("Enter brand: ").strip()
                while True:
                    try:
                        qty = int(input("Quantity: "))
                        if qty > 0:
                            break
                        print("Must be more than 0.")
                    except ValueError:
                        print("Invalid number.")
                while True:
                    try:
                        cp = float(input("Cost price: "))
                        break
                    except ValueError:
                        print("Enter a valid price.")
                origin = input("Origin: ").strip()

                new_entry = {
                    "name": item_name,
                    "brand": brand,
                    "quantity": qty,
                    "cost_price": cp,
                    "origin": origin,
                    "selling_price": cp * 2,  # 100% higher than cost price
                    "quantity_added": qty
                }

                items_in_stock.append(new_entry)
                make_restock_bill(supplier, [new_entry])
                save_items()
            else:
                print("Item not added. Returning to menu.")
                return

        more = input("Restock another item? (yes/no): ").strip().lower()
        if more != "yes":
            print("*" * 60)
            print("Restocking completed. Thanks for managing inventory.")
            print("*" * 60)
            return
