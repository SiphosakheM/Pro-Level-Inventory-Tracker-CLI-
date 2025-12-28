import json
import csv

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
        return {"item name" : self.name, "Item Id": self.id, "Item quantity": self.quantity }
    
    def to_csv(self):
        return [self.name , self.id, self.quantity]
    
def save_to_all(inventories):
    with open("inventory.json", "w") as j_file:
        json.dump([inventory.to_json for inventory in inventories], j_file, indent=4)
        
    with open("stock.csv", "w", newline="") as c_file:
        writer = csv.writer(c_file)
        writer.writerow(["Item name", "Item Id", "Item quantity"])
        writer.writerows([inventory.to_csv for inventory in inventories])
        
