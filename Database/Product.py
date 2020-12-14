from abc import ABC
from enum import Enum, auto


class ProductType(Enum):
    Tshirt = auto()
    Sneakers = auto()
    CustomizableSneakers = auto()


class Product(ABC):

    def __init__(self,
                 sku: str,
                 price: float,
                 name: str,
                 quantity: int,
                 brand: str):
        self.sku = sku
        self.price = price
        self.name = name
        self.quantity = quantity
        self.brand = brand
        self.Type = None

    def get_type(self):
        return self.Type


class TshirtProduct(Product):
    def __init__(self,
                 sku: str,
                 price: float,
                 name: str,
                 quantity: int,
                 brand: str,
                 size: float,
                 color: str):
        super().__init__(sku, price, name, quantity, brand)
        self.size = size
        self.color = color
        self.Type = ProductType.Tshirt.name

    def get_type(self):
        return self.Type


class SneakersProduct(Product):
    def __init__(self,
                 sku: str,
                 price: float,
                 name: str,
                 quantity: int,
                 brand: str,
                 size: float,
                 color: str):
        super().__init__(sku, price, name, quantity, brand)
        self.size = size
        self.color = color
        self.Type = ProductType.Sneakers.name

    def get_type(self):
        return self.Type


class PrintOption(Enum):
    Dog = 1000
    Cat = 750
    Snake = 500


class LacesOption(Enum):
    Red = 100
    Green = 200
    Blue = 300


class CustomizableSneakersProduct(SneakersProduct):
    def __init__(self,
                 sku: str,
                 price: float,
                 name: str,
                 quantity: int,
                 brand: str,
                 size: float,
                 color: str,
                 print_: PrintOption,
                 laces: LacesOption):
        super().__init__(sku, price, name, quantity, brand, size, color)
        self.print_ = print_
        self.laces = laces
        self.Type = ProductType.CustomizableSneakers.name
        self.price = self.price + self.print_.value + self.laces.value

    def get_type(self):
        return self.Type
