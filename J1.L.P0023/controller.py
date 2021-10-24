from model import Fruit, Order


class Controller():
    def __init__(self):
        self.fruitLst = list()
        self.Orders = dict()

    def addFruit(self, fruit):
        if fruit == None:
            return
        if(len(self.fruitLst) != 0):
            for i in self.fruitLst:
                if(fruit.getName() == i.getName() and fruit.getPrice() == i.getPrice() and fruit.getOrgin() == i.getOrgin()):
                    i.setQuantity(i.getQuantity() + fruit.getQuantity())
                    return
        self.fruitLst.append(fruit)


    def addOrder(self, order):
        if order == None: return
        self.Orders[order.getNameCus()] = order.getCart()

    def delSoldItProduct(self, fruit):
        self.fruitLst.remove(fruit)
        newID = 1
        for x in self.fruitLst:
            x.setId(newID)
            newID += 1

    def getCusName(self, key):
        return str(key).split('$')[0]

    def getCusCart(self, key):
        return self.Orders.get(key)
