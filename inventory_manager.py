import json
import csv

JSON_PATH = "data/inventory.json"
CSV_PATH = "data/stock.csv"

# i will use oop to mke thing easy for me 
# i will have  a class inventory
# i should have self name , self id self quantity 
# i should have a function that will check the inventory and notify the owner if the stock if less than 5 unit
# should have a function that ables the user to check items using an id or name
# have a function that save the items on the json file
# be abel to read a json file to get items from it 
# have the condition that checks the user input
# based on the users input then check that is valid

class Inventory:
    def __init__(self, item_name , item_id , item_quantity):
        self.name = item_name
        self.id = item_id
        self.quantity = item_quantity
        
    def to_json(self):
        return {"name" : self.name, "Id": self.id, "quantity": self.quantity }
    
    def to_csv(self):
        return [self.name , self.id, self.quantity]
    def check_low_stock(self):
        """Notifies the owner if stock is less than 5 units."""
        if self.quantity < 5:
            print(f" LOW STOCK ALERT: {self.name} (ID: {self.id}) has only {self.quantity} units left!")
    
def save_to_all(inventories):
    with open(JSON_PATH, "w") as j_file:
        json.dump([inventory.to_json() for inventory in inventories], j_file, indent=4)
        
    with open(CSV_PATH, "w", newline="") as c_file:
        writer = csv.writer(c_file)
        writer.writerow(["name", "Id", "quantity"])
        writer.writerows([inventory.to_csv() for inventory in inventories])
        
def load_from_json():
    try:
        with open(JSON_PATH, "r") as file:
            data = json.load(file)
            return [Inventory(d["name"], d["Id"], d["quantity"])for d in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

inventories = load_from_json()