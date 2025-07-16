import sqlite3

class DBHandler:
    def __init__(self, db_name='sweetshop.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS sweets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price REAL,
            quantity INTEGER
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert_sweet(self, sweet):
        try:
            self.conn.execute("INSERT INTO sweets VALUES (?, ?, ?, ?, ?)", 
                              (sweet.id, sweet.name, sweet.category, sweet.price, sweet.quantity))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def update_sweet(self, sweet_id, price=None, quantity=None):
        if price is not None:
            self.conn.execute("UPDATE sweets SET price = ? WHERE id = ?", (price, sweet_id))
        if quantity is not None:
            self.conn.execute("UPDATE sweets SET quantity = ? WHERE id = ?", (quantity, sweet_id))
        self.conn.commit()

    def delete_sweet(self, sweet_id):
        cur = self.conn.execute("DELETE FROM sweets WHERE id = ?", (sweet_id,))
        self.conn.commit()
        return cur.rowcount > 0

    def get_all_sweets(self):
        return self.conn.execute("SELECT * FROM sweets").fetchall()

    def search_by_name(self, name):
        return self.conn.execute("SELECT * FROM sweets WHERE name LIKE ?", (f"%{name}%",)).fetchall()

    def search_by_category(self, category):
        return self.conn.execute("SELECT * FROM sweets WHERE category = ?", (category,)).fetchall()

    def search_by_price_range(self, min_p, max_p):
        return self.conn.execute("SELECT * FROM sweets WHERE price BETWEEN ? AND ?", (min_p, max_p)).fetchall()

    def purchase(self, sweet_id, qty):
        stock = self.conn.execute("SELECT quantity FROM sweets WHERE id = ?", (sweet_id,)).fetchone()
        if not stock:
            raise ValueError("Sweet not found")
        if stock[0] < qty:
            raise ValueError("Insufficient stock")
        self.conn.execute("UPDATE sweets SET quantity = quantity - ? WHERE id = ?", (qty, sweet_id))
        self.conn.commit()

    def restock(self, sweet_id, qty):
        self.conn.execute("UPDATE sweets SET quantity = quantity + ? WHERE id = ?", (qty, sweet_id))
        self.conn.commit()
         
        