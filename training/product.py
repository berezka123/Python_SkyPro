class Product:
    def __init__(self, name, price):
        self.productName = name
        self.productPrice = price
    

    def displayName(self):
        print("Продукт называется", self.productName)
    

    def displayPrice(self):
        print("Цена продукта", self.productPrice)
    

    def displayNamePrice(self):
        print("Продукт", self.productName, ", цена", self.productPrice)
