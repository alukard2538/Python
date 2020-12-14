import Product
import psycopg2

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "30101990gG"
DB_HOST = "localhost"
DB_PORT = "5432"


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    connection = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
    )
    print("Connection to PostgreSQL DB successful")
    return connection


def add_tshirt(connection, tshirt: Product.TshirtProduct):
    table = 'TSHIRTS'
    check_sku(connection, tshirt, table)
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO {table} (SKU, PRICE, NAME, QUANTITY, BRAND, SIZE, COLOR) 
                                                    VALUES ('{tshirt.sku}', {tshirt.price}, 
                                                            '{tshirt.name}', {tshirt.quantity}, 
                                                            '{tshirt.brand}', {tshirt.size}, 
                                                            '{tshirt.color}')""")


def add_sneakers(connection, sneakers: Product.SneakersProduct):
    table = 'SNEAKERS'
    check_sku(connection, sneakers, table)
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO SNEAKERS (SKU, PRICE, NAME, QUANTITY, BRAND, SIZE, COLOR) 
                        VALUES ('{sneakers.sku}', {sneakers.price},
                                '{sneakers.name}', {sneakers.quantity},
                                '{sneakers.brand}', {sneakers.size},
                                '{sneakers.color}')""")


def add_customizable_sneakers(connection, customizable_sneakers: Product.CustomizableSneakersProduct):
    table = 'SNEAKERS'
    check_sku(connection, customizable_sneakers, table)
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO SNEAKERS (SKU, PRICE, NAME, QUANTITY, BRAND, SIZE, COLOR, PRINT, LACES) 
                        VALUES ('{customizable_sneakers.sku}', {customizable_sneakers.price},
                                '{customizable_sneakers.name}', {customizable_sneakers.quantity},
                                '{customizable_sneakers.brand}', {customizable_sneakers.size},
                                '{customizable_sneakers.color}', '{str(customizable_sneakers.print_.name)}', 
                                '{str(customizable_sneakers.laces.name)}')""")


def add_product(connection, product: Product):
    product_type = product.get_type()
    if product_type == Product.ProductType.Tshirt.name:
        add_tshirt(connection, product)
    elif product_type == Product.ProductType.Sneakers.name:
        add_sneakers(connection, product)
    elif product_type == Product.ProductType.CustomizableSneakers.name:
        add_customizable_sneakers(connection, product)
    connection.commit()
    print('Product added')


def delete_product(connection, table: str, sku: str):
    table = table.upper()
    cursor = connection.cursor()
    cursor.execute(f"""DELETE FROM {table} WHERE SKU='{sku}'""")
    connection.commit()


def check_sku(connection, product, table):
    cursor = connection.cursor()
    cursor.execute(f"""SELECT * FROM {table} WHERE SKU='{product.sku}'""")
    cursor.fetchall()
    if cursor.rowcount > 0:
        delete_product(connection, table, product.sku)


def read_table(connection, table, sort_by=None, selected_feature=None):
    if selected_feature is None:
        selected_feature = '*'
    if sort_by is None:
        sort_by = ""
    else:
        sort_by = f' ORDER BY {str(sort_by)}'

    cursor = connection.cursor()
    cursor.execute(f"""SELECT {selected_feature} FROM {table}{sort_by}""")
    return cursor.fetchall()


def main():
    pass


if __name__ == '__main__':
    main()
