

user="harsha"
password='5555'
username=input("Enter the username:")
pass_word=input("Enter the password:")
H='''
1.credit
2.debit
3.statement
4.exit'''
Amount=10000
if user==username  and password==pass_word:
 while True:
    print(H)
    option=int(input("Enter option:"))
    if option==1:
         creditamount=float(input("Enter amount:"))
         print("Amount after credit",Amount+creditamount)       
    elif option==2:
         debitamount=float(input("Enter amount:"))
         print("After the debit",Amount-debitamount)
    elif option==3:
         print("### Statemant Amount###:",Amount)
    elif option==4:
           break
else:
     print("Invalid Information")




















