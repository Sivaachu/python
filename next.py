bal = 500
while True:
    print("1.Deposit","2.Withdraw","3.Balance","4.Exit",sep='\n')   
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = int(input("Enter a amount: "))
        bal += amount
        print("Rs.",amount,"sucessfully credited..!")
    elif choice == 2:
        amount = int(input("Enter an amount to withdraw : "))
        if bal > amount:
            bal = bal - amount
            print("Rs.",amount,"successfully Withdrwan")
        else:
            print("Invalid Balance")
    
    elif choice == 3:
        print("Current balance Rs.",bal)
    elif choice == 4:
        print("Thanks ")
        break
else:
    print("Invalid choice, Choose from 1 to 4")