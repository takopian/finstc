import sqlite3


class DB:
    @staticmethod
    def add_car(name):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO car(name) VALUES(?)", (name,)).fetchone()
            cursor.execute('SELECT last_insert_rowid()')
            return cursor.fetchall()

    @staticmethod
    def get_car_by_id(car_id):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM car WHERE id = ?", (car_id,)).fetchone()
            return result

    @staticmethod
    def get_car_info_by_id(car_id):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute('''SELECT dealer.name, price, quantity FROM dealer_car JOIN dealer
                                         ON (dealer_car.dealer_id = dealer.id) WHERE car_id = ?''',
                                    (car_id,)).fetchall()
            return result

    @staticmethod
    def delete_car(car_id):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM car WHERE id = ?", (car_id,)).fetchall()

    @staticmethod
    def update_car(car_id, car_name):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE car SET name = ? WHERE id = ?", (car_name, car_id)).fetchall()

    @staticmethod
    def add_dealer(dealer_name):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO dealer(name) VALUES(?)''',
                           (dealer_name,))
            cursor.execute('SELECT last_insert_rowid()')
            return cursor.fetchall()

    @staticmethod
    def delete_dealer(dealer_id):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM dealer WHERE id = ?", (dealer_id,))
            cursor.fetchall()

    @staticmethod
    def get_dealer_by_id(dealer_id):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM dealer WHERE id = ?''',
                           (dealer_id,))
            result = cursor.fetchone()
            return result

    @staticmethod
    def update_dealer(dealer_id, dealer_name):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE dealer SET name = ? WHERE id = ?", (dealer_name, dealer_id)).fetchall()

    @staticmethod
    def get_dealer_info_by_id(dealer_id):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT car.name, price, quantity FROM dealer_car JOIN car
                                         ON (dealer_car.car_id = car.id) WHERE dealer_id = ?''',
                           (dealer_id,))
            result = cursor.fetchall()
            return result

    @staticmethod
    def get_dealer_car_info(dealer_id, car_id):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT car.name, price, quantity FROM dealer_car JOIN car
                                             ON (dealer_car.car_id = car.id) WHERE dealer_id = ? AND car_id = ?''',
                           (dealer_id, car_id))
            result = cursor.fetchone()
            return result

    @staticmethod
    def add_dealer_car_info(dealer_id, car_id, quantity, price):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO dealer_car(dealer_id, car_id, price, quantity) VALUES(?, ?, ?, ?)''',
                           (dealer_id, car_id, price, quantity))
            cursor.fetchall()

    @staticmethod
    def delete_dealer_car_info(dealer_id, car_id):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM dealer_car WHERE dealer_id = ? AND car_id = ?''',
                           (dealer_id, car_id))
            cursor.fetchone()

    @staticmethod
    def update_dealer_car_info(dealer_id, car_id, quantity=None, price=None):
        if quantity is None and price is None:
            return
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            sqlString = '''UPDATE dealer_car SET '''
            if price is not None:
                sqlString += f"price = {price}"
            if quantity is not None:
                sqlString += f", quantity = {quantity}"
            sqlString += " WHERE dealer_id = ? AND car_id = ?"
            cursor.execute(sqlString,
                           (dealer_id, car_id))
            cursor.fetchall()