


class Cars():
     def __init__(self,CAR_NAME,CAR_MODEL,CAR_COLOR,CAR_ENGINE,CAR_PRICE):
         self.A=CAR_NAME
         self.B=CAR_MODEL
         self.C=CAR_COLOR
         self.D=CAR_ENGINE
         self.E=CAR_PRICE
     def SUZUKI_CARS(self):
         print('-'*35, 'HEARTLY WELCOMES YOU','-'*35)
         print("CAR NAME:",self.A)
         print("CAR MODEL:",self.B)
         print("CAR COLOR:",self.C)
         print("CAR ENGINE:",self.D)
         print("CAR PRICE:",self.E)
         print('-'*30,'THANKYOU FOR VISTING OUR SHOWROOM','-'*35)
while True:
    name=input("Enter the carname:")
    model=input("Enter the model:")
    color=input("Enter the color:")
    engine=input("Enter the enginetype:")
    price=float(input("Enter the price:"))   
    C=Cars(name,model,color,engine,price)
    C.SUZUKI_CARS()






































