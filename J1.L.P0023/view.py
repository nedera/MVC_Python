from model import Fruit, Order
from controller import Controller
import Utility as ul
import datetime


class View():
    def __init__(self):
        self.ctrl = Controller()

    def createFruit(self):
        # print("Enter fruit's name: ", end="")
        frName = ul.getString("Enter fruit's name: ", False, "")
        # print("Enter fruit's price: ", end="")
        frPrice = ul.getInt("Enter fruit's price: ", 0, 0)
        # print("Enter fruit's quantity: ", end="")
        frQuantity = ul.getInt("Enter fruit's quantity: ", 0, 0)
        # print("Enter fruit's origin: ", end="")
        frOrigin = ul.getString("Enter fruit's origin: ", False, "")
        if(str(ul.getString("Do you want to continue (Y/N)? ", False, '[YyNn]')).lower() == 'y'):
            return Fruit(len(self.ctrl.fruitLst) + 1, frName, frPrice, frQuantity, frOrigin)

    def addFr(self, fruit):
        self.ctrl.addFruit(fruit)

    def addAnorder(self, order):
        self.ctrl.addOrder(order)

    def Shopping(self):
        o = Order()
        if len(self.ctrl.fruitLst) == 0:
            print("No product! come back later.")
            return
        while(True):
            View.printFruitsInShop(self)
            # chọn fruit trong list
            pointer = self.ctrl.fruitLst[ul.getInt(
                "Enter number of fruit: ", 0, len(self.ctrl.fruitLst)) - 1]
            print("You selected:", pointer.getName())
            # chọn số lượng
            quantity = ul.getInt("Quantity(%s - %s): " %
                                 (0, pointer.getQuantity()), 0, pointer.getQuantity())
            pointer.setQuantity(pointer.getQuantity() - quantity)
            if(pointer.getQuantity() == 0):         # xóa các mặt hàng đã bán hết
                self.ctrl.delSoldItProduct(pointer)
            # check xem người dùng chọn nhưng có cho vào giỏ hàng của mình hay không?
            if(quantity != 0):
                o.addFruit(Fruit(pointer.getId(), pointer.getName(),
                           pointer.getPrice(), quantity, pointer.getOrgin()))
            # in tất cả fruit trong list
            View.printFruitInCart(self, o.getCart())
            # hỏi người dùng có thanh toán hay không
            choice = ul.getString(
                "Do you want to order now (Y/N)? ", False, "[YyNn]")
            # thanh toán
            # Chọn thanh toán và có product trong giỏ
            if(str(choice).lower() == "y" and len(o.getCart()) != 0):
                nameCus = ul.getString(
                    "Your name: ", False, "") + '$' + str(datetime.datetime.today())
                o.setCusName(nameCus)
                # self.ctrl.addOrder(o.getNameCus(), o.getCart())
                break
            # Không thanh toán tiếp tục mua
            elif(str(choice).lower() == "n"):
                if len(self.ctrl.fruitLst) == 0:
                    print(
                        ">> Sorry! Don't have any product. And you need to pay your invoice. Thank you and come back later...")
                    nameCus = ul.getString(
                        "Your name: ", False, "") + '$' + str(datetime.datetime.today())
                    o.setCusName(nameCus)
                    # self.ctrl.addOrder(o.getNameCus(), o.getCart())
                    break
                continue
            else:                                                     # Chọn thanh toán nhưng không có product trong giỏ
                print("You don't have any product!")
                o = None
                break
        return o

    def printFruitsInShop(self):
        print("| %-16s | %-16s | %-16s | %-16s | %-16s |" % ("++ Item ++".center(16),
              "++ Fruit Name ++".center(16), "++ Origin ++".center(16), "++ Price ++".center(16), "++ Quantity ++".center(16)))
        for fruit in self.ctrl.fruitLst:
            print("| %-16s | %-16s | %-16s | %-16s | %-16s |" % (str(fruit.getId()).center(16),
                  fruit.getName().center(16), fruit.getOrgin().center(16), ("$" + str(fruit.getPrice())).center(16), str(fruit.getQuantity()).center(16)))

    def printFruitInCart(self, fruitLst):
        if len(fruitLst) == 0:
            print(">>> You don't have any fruit...")
            return
        print("| %-16s | %-16s | %-16s | %-16s | %-16s |" % ("Product".center(16), "Origin".center(16),
                                                             "Quantity".center(16), "Price".center(16), "Amount Coconut".center(16)))
        total = 0                                                     
        for fruit in fruitLst:
            total += fruit.getQuantity() * fruit.getPrice()
            print("  %-16s   %-16s   %-16s   %-16s   %-16s" % (str(fruit.getName()).center(16), str(fruit.getOrgin()).center(16),
                                                               str(fruit.getQuantity()).center(16), ("$" + str(fruit.getPrice())).center(16), ("$" + str((fruit.getQuantity() * fruit.getPrice()))).center(16)))
        print("------------------------------------------------------------------------------------------------")                                                       
        print("  %-16s   %-16s   %-16s   %-16s   %-16s" %(">>> Total".ljust(15),"","","", ("$" + str(total)).center(16) ))
    def printOders(self):
        if len(self.ctrl.Orders) == 0:
            print(">>> You don't have any order...")
            return
        for k, v in self.ctrl.Orders.items():
            print("Name customer: ", self.ctrl.getCusName(k))
            View.printFruitInCart(self, v)

    def option(self):
        while(True):
            print('''>>> FRUIT SHOP SYSTEM <<<
    1.	Create Fruit
    2.	View orders
    3.	Shopping (for buyer)
    4.	Exit
    (Please choose 1 to create product, 2 to view order, 3 for shopping, 4 to Exit program).
    ''')
            choice = ul.getInt(">> Your choice: ", 1, 4)
            if(choice == 1):
                View.addFr(self, View.createFruit(self))
            elif choice == 2:
                View.printOders(self)
            elif choice == 3:
                View.addAnorder(self, View.Shopping(self))
            elif choice == 4:
                break
            else:
                continue
