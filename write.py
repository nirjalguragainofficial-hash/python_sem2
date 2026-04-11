import datetime

def make_sales_bill(buyer_name, sale_info):
    time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"{buyer_name}_{time_stamp}.txt"

    with open(filename, 'w') as file:
        file.write(f"Customer Name: {buyer_name}\n")
        file.write(f"Date & Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        file.write(f"Item: {sale_info['name']} ({sale_info['brand']})\n")
        file.write(f"Bought: {sale_info['quantity_requested']}\n")
        file.write(f"Free Units: {sale_info['free_items']}\n")
        file.write(f"Total Units Received: {sale_info['Total_item']}\n")
        file.write(f"Amount (Without VAT): Rs. {sale_info['total_cost']}\n")
        file.write(f"VAT (13%): Rs. {sale_info['VAT']}\n\n")
        file.write(f"Final Amount to Pay: Rs. {sale_info['Total_bill']}\n")

    with open(filename, 'r') as file:
        print("\n" + file.read())

    print("-" * 60)
    print("Sale completed! Thanks for shopping with us.")


def make_restock_bill(supplier_name, items_restocked):
    time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"{supplier_name}_{time_stamp}.txt"

    with open(filename, 'w') as file:
        file.write(f"Supplier: {supplier_name}\n")
        file.write(f"Date & Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for item in items_restocked:
            amount = item['quantity_added'] * item['cost_price']
            vat_amount = amount * 0.13
            total_cost = amount + vat_amount

            file.write(f"Item: {item['name']} ({item['brand']})\n")
            file.write(f"Units Added: {item['quantity_added']}\n")
            file.write(f"Cost per Unit: Rs. {item['cost_price']}\n")
            file.write(f"Subtotal: Rs. {amount}\n")
            file.write(f"VAT (13%): Rs. {vat_amount}\n")
            file.write(f"Total with VAT: Rs. {total_cost}\n\n")

    with open(filename, 'r') as file:
        print("\n" + file.read())
