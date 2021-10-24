from typing import List


class Fruit():
    def __init__(self, id, name, price, quantity, orgin):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.orgin = orgin

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def getOrgin(self):
        return self.orgin

    def setQuantity(self, newQuantity):
        self.quantity = newQuantity

    def setId(self, newId):
        self.id = newId


class Order():
    def __init__(self):
        self.nameCus = str()
        self.cart = list()

    def getNameCus(self):
        return self.nameCus

    def getCart(self):
        return self.cart

    def addFruit(self, fruit):
        for fr in self.cart:
            if fr.getId() == fruit.getId() and fr.getName() == fruit.getName() and fr.getOrgin() == fruit.getOrgin() and fr.getPrice() == fruit.getPrice():
                fr.setQuantity(fr.getQuantity() + fruit.getQuantity())
                return
        self.cart.append(fruit)
        # print(self.cart[0].getName(),'=====')

    def setCusName(self, name):
        self.nameCus = name
