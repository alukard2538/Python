from abc import ABC


class Product(ABC):
    Type = None
    product_list = []

    def __init__(self,
                 sku: int,
                 price: float,
                 name: str,
                 quantity: int,
                 brand: str):
        self.sku = sku
        self.price = price
        self.name = name
        self.quantity = quantity
        self.brand = brand
        self.addtolist()

    def getType(self):
        return Product.Type

    def addtolist(self):
        Product.product_list.append(self)


class TshirtProduct(Product):
    Type = 'Tshirt'

    def __init__(self,
                 sku: int,
                 price: float,
                 name: str,
                 quantity: int,
                 brand: str,
                 size: float,
                 color: str):
        super().__init__(sku, price, name, quantity, brand)
        self.size = size
        self.color = color

    def getType(self):
        return TshirtProduct.Type

    def addtolist(self):
        Product.product_list.append(self)


class SneakersProduct(Product):
    Type = 'Sneakers'

    def __init__(self,
                 sku: int,
                 price: float,
                 name: str,
                 quantity: int,
                 brand: str,
                 size: float,
                 color: str):
        super().__init__(sku, price, name, quantity, brand)
        self.size = size
        self.color = color

    def getType(self):
        return SneakersProduct.Type

    def addtolist(self):
        Product.product_list.append(self)


class CustomizableSneakersProduct(SneakersProduct):
    Type = 'Customizable_Sneakers'

    printOption = {'cat': 2000,
                   'dog': 1500,
                   'frog': 3000}

    lacesOption = {'white': 100,
                   'black': 200,
                   'grey': 300}

    def __init__(self,
                 sku: int,
                 price: float,
                 name: str,
                 quantity: int,
                 brand: str,
                 size: float,
                 color: str,
                 print_: str,
                 laces: str):
        super().__init__(sku, price, name, quantity, brand, size, color)
        self.print_ = print_
        self.laces = laces
        if self.print_ not in CustomizableSneakersProduct.printOption:
            raise ValueError('Unsupported option `{}`.'.format(self.print_))
        elif self.laces not in CustomizableSneakersProduct.lacesOption:
            raise ValueError('Unsupported option `{}`.'.format(self.laces))
        else:
            self.price = self.price + \
                         CustomizableSneakersProduct.printOption[self.print_] + \
                         CustomizableSneakersProduct.lacesOption[self.laces]

    def getType(self):
        return CustomizableSneakersProduct.Type

    def addtolist(self):
        Product.product_list.append(self)
