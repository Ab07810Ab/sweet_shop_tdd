from sweet import Sweet
from db_handler import DBHandler

class SweetShop:
    def __init__(self):
        self.db = DBHandler()

    def add_sweet(self, sweet):
        return self.db.insert_sweet(sweet)

    def update_sweet(self, sweet_id, price=None, quantity=None):
        self.db.update_sweet(sweet_id, price, quantity)

    def delete_sweet(self, sweet_id):
        return self.db.delete_sweet(sweet_id)

    def get_all_sweets(self):
        return [Sweet(*r) for r in self.db.get_all_sweets()]

    def search_by_name(self, name):
        return [Sweet(*r) for r in self.db.search_by_name(name)]

    def search_by_category(self, category):
        return [Sweet(*r) for r in self.db.search_by_category(category)]

    def search_by_price_range(self, min_p, max_p):
        return [Sweet(*r) for r in self.db.search_by_price_range(min_p, max_p)]

    def purchase(self, sweet_id, qty):
        self.db.purchase(sweet_id, qty)

    def restock(self, sweet_id, qty):
        self.db.restock(sweet_id, qty)
 

        
    
