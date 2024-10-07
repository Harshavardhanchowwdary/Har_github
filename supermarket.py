from datetime import datetime

name=input("Enter your name:")


lists='''
1.Rice   Rs 30/kg
2.Oil    Rs 120/litre
3.Salt   Rs 20/kg
4.Maggi  Rs 50/kg
5.Sugar  Rs 30/kg
6.Panner Rs 100/kg
'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]
finalamount=0

items={'Rice':30,
'Oil':120,
'Salt':20,
'Maggi':50,
'Sugar':30,
'Panner':100}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry the item is not available in stock")
    else:
        print("you entered the wrong number")
    inp=input("can i bill the item yes or no:")
    if inp=='no':
            break
    elif inp=="yes":
            pass
            if finalamount!=0:
                print(25*"=","HUNGER SUPERMARKET",25*"=")
                print(30*"=","CHITTOOR",30*"=")
                print("Name:",name,30*" ","Date:",datetime.now())
                print(75*"-")
                print("sno",8*" ",'items',8*" ",'Quantity',4*" ",8*' ','price')
                for i in range(len(pricelist)):
                    print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
                    print(75*"-")
                    print(50*" ",'TotalAmount:','Rs',totalprice)
                    print("gst amount",50*" ",'Rs',gst)
                    print(75*"-")
                    print(50*" ",'FinalAmount:','Rs',finalamount)
                    print(75*"-")
                    print(25*" ","Thankyou For Visiting Our Supermarket")
                    print(75*"-")





