from inventory_manager import *
import sys
# ask the user whether the are check or login the stock
# if the user is login the stock the return successfully login or not
# if the user is check the stock return the quantity, name and the id of the item in a list
def menu():
    while True:
        print("1. Add inventory 2. View inventory 3. Exit or Done")
        try:
            choice = input("Select: ")
            if choice == "1":
                item_name = input("Item Name: ").strip().title()
                item_id = input("Item Id: ").strip()
                while True:
                    try:
                        item_quantity = int(input("Item quantity: ").strip())
                        if item_quantity <= 0:
                            print("Quantity cannot be negative or 0.")
                        else:
                            break 
                    except ValueError:
                        print("Invalid input")
                
                inventories.append(Inventory(item_name,item_id,item_quantity))
                save_to_all(inventories)
            elif choice == "2":
                print("\n --- INVENTORY LIST ---")
                for item in inventories:
                    print(f"Item name: {item.name}\nItem Id: {item.id}\nItem quantity: {item.quantity}")
                    item.check_low_stock()
            elif choice == "3":
                print({"Exiting the inventory manager"})
                sys.exit()
            else:
                print("Invalid selection")
        except ValueError:
            print("Error: please enter a valid number for quantity")
        
if __name__ == "__main__":
    menu()