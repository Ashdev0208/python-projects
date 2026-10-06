print("it is in the test mode!\nso enter any kind of card number\n")
personal_data = {"card_number": 0,"pin": 0,"balance":1000,"history": 0}

def menu():
    print("1. Check Balance\n2. Withdraw\n3. Deposit\n4. Transfer\n5. Transaction History\n6. Exit")
    value = input("Enter the number: ")
    return value
def withdraw():
    money = input("how much do you withdraw: ")
    if personal_data["balance"] < money:
        print("oops, you dont have enough money to widthraw")
        print("1. deposit --- 2. transfer ---- 3. exit")
        number = input("enter the number: ")
        if number == 1:
            pass
        elif number == 2:
            pass
        elif number == 3:
            pass
        else:
            print("please enter those numbers")
    else:
        personal_data["balance"] = personal_data["balance"] - money
        print(f"you have succesfully withdrawed the money ({personal_data['balance']})")
while True:
    card = input("Please enter more than 6 numbers: ")
    personal_data["pin"] = input("Please enter your Pin: ")
    if len(card) >= 6:
        print("you have succesfuly entered your bank account\nMenu:")
        command = menu()
        if command == 1:
            print(personal_data["balance"])
        elif command == 2:
            # withdraw
            withdraw()
        elif command == 3:
            # deposit
            pass
        elif command == 4:
            #trasfer
            pass
        elif command == 5:
            #Transaction History
            pass
        elif command == 6:
            #Exit
            pass
        else:
            print("please enter right number")

        break
    else:
        print("please follow the rule")

