import sqlite3


class Database:

    URI = "become_qa_auto.db"

    def __init__(self) -> None:
        self.__connection = sqlite3.connect(Database.URI)
        self.__cursor = self.__connection.cursor()

    def test_connection(self):
        sqlite_select_query = "SELECT sqlite_version();"
        self.__cursor.execute(sqlite_select_query)
        record = self.__cursor.fetchone()
        print(f"Connected successfully. SQLite Database version is {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.__cursor.execute(query)
        records = self.__cursor.fetchall()
        return records

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.__cursor.execute(query)
        records = self.__cursor.fetchall()
        return records

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.__cursor.execute(query)
        self.__connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.__cursor.execute(query)
        records = self.__cursor.fetchall()
        return records

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity)\
             VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.__cursor.execute(query)
        self.__connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.__cursor.execute(query)
        self.__connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, "\
                "products.description, orders.order_date "\
                "FROM orders "\
                "JOIN customers ON orders.customer_id = customers.id "\
                "JOIN products ON orders.product_id = products.id"
        self.__cursor.execute(query)
        records = self.__cursor.fetchall()
        return records
