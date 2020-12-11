import Product
import psycopg2

DB_NAME = "products"
DB_USER = "postgres"
DB_PASSWORD = "30101990gG"
DB_HOST = "localhost"
DB_PORT = "5432"


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def add_tshirt(connection, tshirt: Product.TshirtProduct):
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO TSHIRTS (SKU, PRICE, NAME, QUANTITY, BRAND, SIZE, COLOR) 
                        VALUES ({tshirt.sku}, {tshirt.price}, 
                                {tshirt.name}, {tshirt.quantity},     
                                {tshirt.brand}, {tshirt.size}, 
                                {tshirt.color})
                        """)


def add_sneakers(connection, sneakers: Product.SneakersProduct):
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO SNEAKERS (SKU, PRICE, NAME, QUANTITY, BRAND, SIZE, COLOR) 
                        VALUES ({sneakers.sku}, {sneakers.price},
                                {sneakers.name}, {sneakers.quantity},
                                {sneakers.brand}, {sneakers.size},
                                {sneakers.color})""")


def add_customizable_sneakers(connection, customizable_sneakers: Product.CustomizableSneakersProduct):
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO SNEAKERS (SKU, PRICE, NAME, QUANTITY, BRAND, SIZE, COLOR, PRINT, LACES) 
                        VALUES ({customizable_sneakers.sku}, {customizable_sneakers.price},
                                {customizable_sneakers.name}, {customizable_sneakers.quantity},
                                {customizable_sneakers.brand}, {customizable_sneakers.size},
                                {customizable_sneakers.color}, {customizable_sneakers.print_}, 
                                {customizable_sneakers.laces})""")


def add_product(connection, product: Product):
    product_type = product.getType()
    if product_type == 'Tshirt':
        add_tshirt(connection, product)
    if product_type == 'Sneakers':
        add_sneakers(connection, product)
    if product_type == 'Customizable_Sneakers':
        add_customizable_sneakers(connection, product)


def delete_product(connection, table: str, sku: str):
    table = table.upper()
    cursor = connection.cursor()
    try:
        cursor.execute(f'DELETE FROM {table} WHERE SKU={sku}')
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")


def main():
    connection = create_connection(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)


if __name__ == '__main__':
    main()
