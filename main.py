from operation import (
    load_items, save_items, show_items,
    apply_markup, process_sale, process_restock,
    sell_items, restock_items
)
from write import make_sales_bill, make_restock_bill
def start_wecare():
    while True:
        print("*" * 60)
        print("      WELCOME TO THE WECARE BEAUTY & SKINCARE SHOP")
        print("Please select an Option:")
        print("1. Display Products")
        print("2. Sell Product")
        print("3. Add Stock")
        print("4. Quit")
        print("*" * 60)
        
        selection = input("Your choice: ")

        if selection == '1':
            show_items()
        elif selection == '2':
            sell_items()
        elif selection == '3':
            restock_items()
        elif selection == '4':
            print("We're grateful for your visit. See you again soon!")
            break
        else:
            print("Oops! That wasn't a valid choice. Please try 1, 2, 3, or 4.")

if __name__ == '__main__':
    start_wecare()

    
