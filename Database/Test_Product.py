import pytest
import Product


def test_tshirt():
    print('tshirt_test')
    tshirt = Product.TshirtProduct(sku='0001', price=500.0, name="Kolobaza",
                                   quantity=25, brand='Nike', size=36, color='red')
    tshirt_type = tshirt.get_type()
    assert tshirt_type == Product.ProductType.Tshirt.name


def test_sneakers():
    print('sneakers_test')
    sneakers = Product.SneakersProduct(sku='0001', price=500.0, name="Kolobaza",
                                       quantity=25, brand='Nike', size=36, color='red')
    sneakers_type = sneakers.get_type()
    assert sneakers_type == Product.ProductType.Sneakers.name


def test_customizable_sneakers():
    print('customizable_sneakers_test')
    sneakers = Product.CustomizableSneakersProduct(sku='0001', price=500.0, name="Kolobaza",
                                                   quantity=25, brand='Nike', size=36, color='red',
                                                   print_=Product.PrintOption.Cat, laces=Product.LacesOption.Green)
    sneakers_type = sneakers.get_type()
    assert sneakers_type == Product.ProductType.CustomizableSneakers.name
    assert 1450 == sneakers.price
