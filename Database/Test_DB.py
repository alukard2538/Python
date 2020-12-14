import pytest
import Product
import DB

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "30101990gG"
DB_HOST = "localhost"
DB_PORT = "5432"

connection = DB.create_connection(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)

tshirt = Product.TshirtProduct(sku='0001', price=500.0, name="Tshirt",
                               quantity=25, brand='Nike', size=36, color='red')

sneakers1 = Product.SneakersProduct(sku='0121', price=600.0, name="Kolobaza",
                                    quantity=25, brand='Abibas', size=36, color='red')

sneakers2 = Product.SneakersProduct(sku='6230', price=5000.0, name="Pegasus",
                                    quantity=1, brand='Nike', size=25, color='blue')

sneakers3 = Product.SneakersProduct(sku='8924', price=200.0, name="Prikol",
                                    quantity=15, brand='Asics', size=42, color='green')

customizable_sneakers = Product.CustomizableSneakersProduct(sku='3021', price=750.0,
                                                            name="Customizable Kolobaza",
                                                            quantity=25, brand='Puma',
                                                            size=36, color='red',
                                                            print_=Product.PrintOption.Cat,
                                                            laces=Product.LacesOption.Green)


def test_add_and_show_and_sort_product():
    DB.add_product(connection, tshirt)
    DB.add_product(connection, sneakers1)
    DB.add_product(connection, sneakers2)
    DB.add_product(connection, sneakers3)
    DB.add_product(connection, customizable_sneakers)
    table = DB.read_table(connection, 'TSHIRTS')
    assert len(table) == 1
    print('Table - TSHIRTS')
    for row in table:
        print(row)
    table = DB.read_table(connection, 'SNEAKERS', sort_by='price')
    assert len(table) == 4
    print('Table - SNEAKERS')
    for row in table:
        print(row)
    DB.delete_product(connection, 'SNEAKERS', sneakers3.sku)
    table = DB.read_table(connection, 'SNEAKERS', sort_by='price')
    assert len(table) == 3


