users='Harshavardhan'
password='5555'

Amount=120000

user_name=input("Enter the username:")
user_password=input("Enter the password:")
if users==user_name and password==user_password:
    def menu():
        print("1.credit")
        print("2.debit")
        print("3.deposite")
        print("4.balance")
        print("5.exit")

    def option():
        return input("Enter The option:")
    
    def credit():
        creditamount=float(input("Enter the creditAmount:"))
        if creditamount<=0:
            print("Enter a positive amount")
        elif creditamount>=Amount:
            print("insufficient balance")
        else:
            print('-'*70)
            print("Amount after credited",Amount+creditamount)

    def debit():
        debitamount=float(input("Enter the debitAmount:"))
        if debitamount<=0:
            print("Enter a positive amount")
        elif debitamount>=Amount:
            print("insufficient balance")
        else:
            print('-'*70)
            print("Amount after debited",Amount-debitamount)

    def deposite():
        depositeamount=float(input("Enter the depositeAmount:"))
        if depositeamount<=0:
            print("Enter a positive amount")
        elif depositeamount>=Amount:
            print("insufficient balance")
        else:
            print('-'*70)
            print("Amount after deposited",Amount+depositeamount)

    def balance():
        print('-'*70)
        print("your balance is",Amount)
        print('-'*70)
    def exit():
        print('-'*70)
        print("Thank you for visiting ,Have a beautiful day")
        print('-'*70)


    def main():
        while True:
            menu()
            choice=option()
            if choice=="1":
                credit()
            elif choice=="2":
                debit()
            elif choice=="3":
                deposite()
            elif choice=="4":
                balance()
            elif choice=="5":
                exit()
            break
        else:
            print("Enter the correct user details")
main()


