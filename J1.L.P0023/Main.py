# import Utility as ul, datetime 
from view import View
from model import Fruit
# print("| %-16s | %-16s | %-16s | %-16s |" %("++ Item ++".center(16),"++ Fruit Name ++".center(16),"++ Origin ++".center(16),"++ Price ++".center(16)))
# # result = ul.getDate("Nhập ngày sinh của bạn: ")
# # print(result)

# # result = ul.getString("Chọn Y/N: ", False,"[YyNn]")
# print(datetime.datetime.today())

# x = dict()
# # x[input()] = input()
# # for k, v in x.items():
# #     print(k , "---", v )
v = View()
# v.createFruit()
v.addFr(Fruit(1,"Apple", 2, 100, "Vn"))
v.addFr(Fruit(2,"Apple", 2, 50, "Vn"))
v.addFr(Fruit(2,"Apple", 3, 100, "USA"))
v.option()