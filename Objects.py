# class Moblie:
#     def __init__(self,model,camera,processor,cooling_system):
#         self.model = model 
#         self.camera = camera 
#         self.processor = processor 
#         self.cooling_system = cooling_system 
#     def Make_game(self,Graphics):
#         print("Arendreo...{}".format(Graphics)) 
#     def another(self,processor):
#         self.processor = processor
# Mobile_obj = Moblie("IQOO 12","200 MP","8 gen3","6000MM2") 
# Mobile_obj.another("8 Elite")
# print(Mobile_obj.processor) #oops basics program and updating attributes 


# class CART:
#     def __init__(self):
#         self.items = {} 
#         self.price_items = {"Iqoo14":45000 ,"Iqoo13" : 50000}
#     def add_products(self,item_name,quantity):
#         self.items[item_name] = quantity 
#     def get_cart_items(self):
#         print(list(self.items.items()))
#     def delete_items(self,item_name):
#         del self.items[item_name] 
#     def update_item(self,item_name,quantity):
#         self.items[item_name] = quantity
#     def get_total_items(self):
#         total = 0 
#         for item , quantity in self.items.items():
#             total += quantity * self.price_items[item] 
#         print(total)
# CART_OBJ = CART() 
# CART_OBJ.add_products("Iqoo13",1) 
# CART_OBJ.get_cart_items()
# CART_OBJ.add_products("Iqoo14",1)
# CART_OBJ.add_products("Iqoo14",1)
# CART_OBJ.get_cart_items()
# CART_OBJ.get_total_items() 




# class Cart():
#     flat_discount = 0 
#     min_bill = 100 
#     def __init__(self):
#         self.items = {} 
#     def add_items(self,item_name,quantity):
#         self.items[item_name] = quantity 
#         self.display_items()
#     def display_items(self):
#         print(self.items)
# #         print(self)
# #     def print(self):
# #         print(Cart.min_bill)
# #     def print_updated(self):
# #         Cart.min_bill = 300
# #         return Cart.min_bill
# a = Cart() 
# a.add_items("Godofwar",2000)
# # b = Cart() 
# # Cart.min_bill = 2020
# # a.print()
# # b.print()
# # print(a.print_updated())
# # print(b.print_updated())


# class Product:
    
#     def __init__(self,name,price,deal_price,ratings):
#         self.name = name 
#         self.price = price 
#         self.deal_price = deal_price 
#         self.ratings = ratings 
#         self.you_save = price- deal_price 
#     def display_items(self):
#         print("product_name: {}".format(self.name))
#         print("Price: {}".format(self.price))
#         print("Deal_Price: {}".format(self.deal_price))
#         print("Ratings: {}".format(self.ratings))
#         print("You Save: {}".format(self.you_save)) 
#     def get_deal_price(self):
#         return self.deal_price

# class ElectronicItem(Product):
#     def set_warranty(self,warranty_in_months):
#         self.warranty_in_months = warranty_in_months 
#     def display_items(self):
#         super().display_items() 
#         print("Warrenty: {}".format(self.warranty_in_months))
# class Order():
#     def __init__(self,delivery_speed,delivery_address):
#         self.items_in_cart = [] 
#         self.delivery_speed = delivery_speed 
#         self.delivery_address = delivery_address 
#     def add_item(self,product,quantity):
#         self.items_in_cart.append((product,quantity)) 
#     def display_cart_items(self):
#         for product,quantity in self.items_in_cart:
#             product.display_items()
#             print("Quantity..{}".format(quantity))
#     def get_total_bill(self):
#         total_bill = 0 
#         for product,quantity in self.items_in_cart:
#             price = product.get_deal_price() * quantity 
#             total_bill += price 
#         print("total_bill: {}".format(total_bill))

# tv = ElectronicItem("LenovoThinkpad",40000,35000,4.5)
# tv.set_warranty(24) 

# O = Order("Amazon delivery","Chittoor") 
# O.add_item(tv,5)
# O.display_cart_items()
# O.get_total_bill()

# class Car:
    # def __init__(self, color, max_speed, acceleration, tyre_friction):
    #     self.color = color 
    #     self.max_speed = max_speed 
    #     self.acceleration = acceleration 
    #     self.tyre_friction = tyre_friction 
    #     self.is_engine_started = False 
    #     self.current_speed = 0 

    # def start_engine(self):
    #     self.is_engine_started = True

    # def stop_engine(self):
    #     self.is_engine_started = False

    # def accelerate(self):
    #     if self.is_engine_started:
    #         self.current_speed += self.acceleration 
    #         if self.current_speed > self.max_speed:
    #             self.current_speed = self.max_speed 
    #     else: 
    #         print( "Car has not started yet")
    #     return self.current_speed

    # def apply_brakes(self):
    #     self.current_speed -= self.tyre_friction 
    #     if self.current_speed < 0 :
    #         self.current_speed = 0 
    #     return self.current_speed
    # def sound_horn(self):
    #     if self.is_engine_started:
    #         print("Beep Beep") 
    #     else:
    #         print("Car has not started yet")


# def square(numbers):
#     for i in numbers:
#         st = int(i)
#         st = st**2
#     return st
# List = "1,2,3,4"

# str_obj = map(square,List.split(",")) 
# print(list(str_obj))



# List = "1,2,3,4,harsha"
# print(list(filter(int,List.split(","))))
# from functools import reduce

# def square(numbers,Num):
#     List = []
#     st = int(numbers)
#     st1 = int(Num)
#     return (st + st1)
# Numbers = "1,2,3,4"
# L = reduce(square,Numbers.split(","))
# print(L) 

# from math import pi as p

# print(round(p,2))

# import random 

# print(random.randint(1,10))
# print(random.choice(["a","b","c"]))






# print("harsha" //"vardhan") 


# from datetime import date 
# print(date.today())

# from datetime import time 
# Time_object = time(11,22,59)
# print(Time_object.hour)
# print(Time_object.minute)
# print(Time_object.second)

# from datetime import datetime 

# print(datetime())



# from datetime import datetime 

# dto = datetime.now()

# date = dto.strftime("%d %b %Y %I:%M:%S %p")
# print(date)



# from datetime import datetime 

# dto = "28 November, 2024"

# D = datetime.strptime(dto,"%d %B, %Y")
# print(D)











from datetime import datetime
class BankAccount:
    def __init__(self,name,account_number,amount):
        self.name = name 
        self.account_number = account_number 
        self.amount = amount 
    def deposite(self,amount):
        self.amount += amount 
    def debit(self,amount):
        if self.amount > 0:
            self.amount -= amount 
        else:
            raise ValueError("Insuffient Balance") 
    def get_details(self):
        print("="*50,"Account_Name:    {}".format(self.name),"======", "Date & Time {}".format(datetime.today()),"="*50)
        print("="*50,"Account_Number:  {}".format(self.account_number),"="*50)
        print("="*50,"Current Balance: {}".format(self.amount),"="*50) 

AccountName = input("Enter Your Name:")
AccountNumber = input("Enter Your AccountNumber:")
YourAmount = int(input())
AccountName1 = input("Enter AccHolder Name:")
AccountNumber1 = input("Enter Your AccHolder No:")
YourAmount1 = int(input())
Am = int(input())
def transefer(acc1,acc2,amount):
    try:
        User1.debit(amount)
        User2.deposite(amount)
        return " "*50, "TransactionSuccesful" ," "*50
    except:
        return " "*50, "TransactionFailure" ," "*50


User1 = BankAccount(AccountName,AccountNumber,YourAmount) 
User2 = BankAccount(AccountName1,AccountNumber1,YourAmount1)
User1.get_details()
User2.get_details()

print(transefer(User1,User2,Am))
print("="*50,"Transfering Amount {}".format(Am),"="*50)
User2.get_details()









