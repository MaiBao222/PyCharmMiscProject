# lập trình hướng đối tượng trong Python
# Class: lớp
# Object: đối tượng
# Attribute: thuộc tính
# phương thức
# thụộc tính instance vs class
# class Student:
# # name mangling
#     __parent = "unknown"
# # thuoc tinh cua class neu co
#     name = "none"
#     age = 0
#     address = "none"
#     score = 0
#     _gender = "none"
# # ham khoi tao
#     def __init__(self, name, age, address, score, gender):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.score = score
#         self._gender = "None" # the hien gender la bien private - noi bo
# # cac phuong thuc, ham trong class
#     def run(self):
#         print("Student run")
#     def info(self):
#         print("Student info", self.name)
#         print("Student info", self.age)
#         print("Student info", self.address)
#         print("Student info", self.score)
#         print("Student info", self._gender)
#         print("--------------------------")
#     def quit(self):
#         print("Student quit")
#     def scoreTB(self):
#         print("Student score TB",self.score)
#     def displayparent(self):
#         print("Student parent",self.__parent)
#     def setParentInfo(self, parent):
#         self.__parent = parent
# # Object
# bao = Student("bao",20,"TP.HCM",100,"iuh")
# lananh = Student("lan anh",20,"TP.HCM",44,"ntt")
# bao.info()
# lananh.info()
# lananh.score = 100
# lananh.scoreTB()
# bao.score = 50
# bao.scoreTB()
#
# print(bao.__dict__) #dictionary
# # sau khi them bien gender = "none" ( chua thay doi, cap nhat gia tri moi)
# # thi trong dict khong chua bien gender
# # bien __dict__ chi chua cac "instance attribute"
# bao.setParentInfo("HN")
# bao.displayparent()
# print(bao.displayparent())

# class Calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def sum(self, a, b):
#         print("tong: ",a + b)
#     def sub(self, a, b):
#         print("hieu: ",a - b)
#     def mul(self, a, b):
#         print("tich: ",a * b)
#     def div(self, a, b):
#         print("thuong",a / b)
# print(Calculator(2,4).sum(2,3))
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_quantity(self):
        print("tong hang ton kho ",self.quantity)
    def update_stock(self, new_quantity):
        self.quantity = self.quantity + new_quantity
        print("So luong cap nhat: ", self.quantity)
    def stock_info(self):
        print("ten san pham: ", self.name)
    def to_dict(self):
        print("thong tin san pham: ",self.__dict__)
    def total_stock(self):
        print("gia san pham:  ",self.price)
dochoi = Product("xe o to", 100, 10)
dochoi.to_dict()
dochoi.stock_info()
dochoi.total_quantity()
dochoi.update_stock(5)
dochoi.total_stock()




