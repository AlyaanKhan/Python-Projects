import pandas as pd
import sqlite3
print("WELCOME TO CUSTOMER ORDER MANAGEMENT SYSTEM! \n")
def open_a_connection():
    connection_established = sqlite3.connect('customer_order_management_system.db')
    print("Connection to database is live right now")
    return connection_established
def close_a_connection(connection_established):
    if connection_established:
            connection_established.close()
            print("Connection closed Succesfully!")
def generating_tables(connection_established):
    query_cursor = connection_established.cursor()
    query_cursor.execute('''CREATE TABLE IF NOT EXISTS customers_details (
                            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            customer_name TEXT NOT NULL,
                            customer_gender TEXT NOT NULL,
                            customer_phone_no TEXT NOT NULL,
                            customer_address TEXT NOT NULL,
                            customer_favorite_food_genere TEXT NOT NULL)''')
    query_cursor.execute('''CREATE TABLE IF NOT EXISTS product_details (
                            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            product_name TEXT NOT NULL,
                            product_description TEXT NOT NULL,
                            product_price REAL NOT NULL,
                            product_stock INTEGER NOT NULL)''')
    query_cursor.execute('''CREATE TABLE IF NOT EXISTS order_details (
                            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            cus_id INTEGER NOT NULL,
                            pro_id INTEGER NOT NULL,
                            quantity INTEGER NOT NULL,
                            FOREIGN KEY(cus_id) REFERENCES customers_details(customer_id),
                            FOREIGN KEY(pro_id) REFERENCES product_details(product_id))''')
    connection_established.commit()

class Customer:
    def __init__(self, customer_name, customer_gender, customer_phone_no, customer_address, customer_favorite_food_genere):
        self.customer_name = customer_name
        self.customer_gender = customer_gender
        self.customer_phone_no = customer_phone_no
        self.customer_address = customer_address
        self.customer_favorite_food_genere = customer_favorite_food_genere
    def save_customer_info_to_db(self, connection_established):
        query_cursor = connection_established.cursor()
        query_cursor.execute('''INSERT INTO customers_details (customer_name, customer_gender, customer_phone_no, customer_address, customer_favorite_food_genere)
    VALUES (?, ?, ?, ?, ?)''', (self.customer_name, self.customer_gender, self.customer_phone_no, self.customer_address, self.customer_favorite_food_genere))
        connection_established.commit()
class Product:
    def __init__(self, product_name, product_description, product_price, product_stock):
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_stock = product_stock
    def save_product_info_to_db(self, connection_established):
        query_cursor = connection_established.cursor()
        query_cursor.execute('INSERT INTO product_details (product_name, product_description, product_price, product_stock) VALUES (?, ?, ? ,?)', 
                             (self.product_name, self.product_description, self.product_price, self.product_stock))
        connection_established.commit()
class Order:
    def __init__(self, cus_id, pro_id, quantity):
        self.cus_id = cus_id
        self.pro_id = pro_id
        self.quantity = quantity
    def save_order_info_db(self, connection_established):
        query_cursor = connection_established.cursor()
        query_cursor.execute('INSERT INTO order_details (cus_id, pro_id, quantity) VALUES (?, ?, ?)', (self.cus_id, self.pro_id, self.quantity))
        connection_established.commit()
def generate_detailed_order_reports(connection_established):
    query_to_fetch = '''SELECT customers_details.customer_name AS Customer_Name, product_details.product_name AS Product_Name,
                               order_details.quantity AS Quantity, product_details.product_price * order_details.quantity AS Total_Bill 
                        FROM order_details
                        JOIN customers_details ON order_details.cus_id = customers_details.customer_id
                        JOIN product_details ON order_details.pro_id = product_details.product_id'''
    data_frame = pd.read_sql_query(query_to_fetch, connection_established)
    return data_frame
def csv_generation(connection_established):
    data_frame_customers = pd.read_sql_query('SELECT * FROM customers_details', connection_established)
    data_frame_products = pd.read_sql_query('SELECT * FROM product_details', connection_established)
    data_frame_order = pd.read_sql_query('SELECT * FROM order_details', connection_established)
    data_frame_customers.to_csv('customers_data.csv', index = False)
    data_frame_products.to_csv('products_data.csv', index = False)
    data_frame_order.to_csv('order_data.csv', index = False)
    print("Generating CSV...........")
    print("Files Generated Successfully!")

def user_interface_menu():
    connection_established = open_a_connection()
    generating_tables(connection_established)
    while True:
        print('''
                 Press 1 to Add a Customer
                 Press 2 to Add a Product
                 Press 3 to Place a Order
                 Press 4 to Generate Report
                 Press 5 to Generate csv files
                 Press 6 to Exit the System \n ''')
        user_choice = int(input("Enter your choice: "))
        
        print("__________________________________________________________________________________________________")
        if user_choice == 1:
            customer_name = input("Enter Customer's name: ")
            customer_gender = input(f"Enter {customer_name}'s gender: ")
            customer_phone_no = input(f"Enter {customer_name}'s contact number: ")
            customer_address = input(f"Enter {customer_name}'s Address: ")
            customer_favorite_food_genere = input(f"Enter {customer_name}'s Favorite Food Genere: ")
            customer_details = Customer(customer_name, customer_gender, customer_phone_no, customer_address, customer_favorite_food_genere)
            customer_details.save_customer_info_to_db(connection_established)
            print("Adding Customer to Database.........")
            print("Added Succesfully! ")
            print("__________________________________________________________________________________________________")
        elif user_choice == 2:
            product_name = input("Enter Product name: ")
            product_description = input(f"Enter {product_name} description: ")
            product_price = float(input(f"Enter {product_name} price: "))
            product_stock = int(input(f"Enter {product_name} stock: "))
            product_details = Product(product_name, product_description, product_price, product_stock)
            product_details.save_product_info_to_db(connection_established)
            print("Adding Product to Database.........")
            print("Added Succsfully! ")
            print("__________________________________________________________________________________________________")
        elif user_choice == 3:
            cus_id = int(input("Enter Customer's ID: "))
            pro_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter number of quantity: "))
            order_details = Order(cus_id, pro_id, quantity)
            order_details.save_order_info_db(connection_established)
            print("Placing Order...........")
            print("Order Placed Succesfully ")
            print("__________________________________________________________________________________________________")
        elif user_choice == 4:
            gen_report = generate_detailed_order_reports(connection_established)
            print("The Report is: ")
            print(gen_report)
            print("__________________________________________________________________________________________________")
        elif user_choice == 5:
            csv_generation(connection_established)
            print("Exporting........")
            print("Data Exported to CSV Succesfully!")
            print("__________________________________________________________________________________________________")
        elif user_choice == 6:
            print("Exiting.........")
            print("Exited Succesfully! ")
            break
        else:
            print("Invalid Choice! ")
    close_a_connection(connection_established)
if __name__ == "__main__":
    user_interface_menu()
