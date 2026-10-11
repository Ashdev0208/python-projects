def automatic_teller_machine():
    from datetime import datetime
    print("it is in the test mode!\nso enter any kind of card number\n")
    personal_data = {"card_number": 0,"pin": 0,"balance":1000,"history": {}}



    def menu():
        print("1. Check Balance\n2. Withdraw\n3. Deposit\n4. Transfer\n5. Transaction History\n6. Exit")
        value = int(input("Enter the number: "))
        return value

    def historySaver(what):
        now = f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}:{datetime.now().microsecond}"
        personal_data['history'][now] = what

    def transfer():
        amount = 0
        
        while True:
            recipientNumber = input("Please enter a card number: ")
            if len(recipientNumber) < 6 or not recipientNumber.isdigit():
                print("Card number must contain at least 6 digits")
                continue
            value = int(input("please enter the amount: "))

            if personal_data['balance'] >= value and value > 0:
                personal_data["balance"] -= value
                amount = value
                break
            else:
                print("enter the amount that you have or positive numbers only")
        historySaver({"card number": recipientNumber,"Amount": amount})
        print(f"you have successfully transferred ({recipientNumber}: {amount})")

    def deposit():
        while True:
            print("warning: the amount must be higher than 10 and lower than 500")
            depositValue = int(input("please enter the deposit amount"))
            if 500 > depositValue > 10:
                personal_data["balance"] += depositValue
                print(f"you have successfully deposited ({depositValue})  into your balance")
                historySaver({"deposited Value": depositValue})
                break
            else:
                print("please follow the rule")
                continue

    def exit_handler():
        print("1.Menu --- 2.Dashboard")
        data = input("enter the number: ")
        if data == "1":
            hero_section()
        elif data == "2":
            return personal_data


    def withdraw():
        money = int(input("how much do you withdraw: "))
        if personal_data["balance"] < money:
            print("oops, you dont have enough money to widthraw")
            print("1. try again --- 2. menu")
            number = int(input("enter the number: "))
            if number == 1:
                withdraw()
            elif number == 2:
                hero_section()
            else:
                print("please enter those numbers")
        elif money < 0:
            print("please enter positive numbers")
            withdraw()
        else:
            personal_data["balance"] -= money
            historySaver({"withdrawed Amount": money})
            print(f"you have succesfully withdrawed the money ({personal_data['balance']})")


    def hero_section():

        while personal_data["card_number"] == 0 or personal_data["pin"] == 0:
                card_information = input("Please enter more than 6 numbers: ")
                card_pin = input("Please enter your Pin: ")
            
                if len(card_information) >= 6 and len(card_pin) >= 4 and card_information.isdigit() and card_pin.isdigit():
                    personal_data["card_number"] = card_information
                    personal_data["pin"] = card_pin
                    print("you have succesfuly entered your bank account")
                    break
                else:
                    print("please enter your information right")
                    personal_data["card_number"] = 0
                    continue
        command = menu()
        if command == 1:
            print(f"the balance is {personal_data['balance']};\n")
            exit_handler()
        elif command == 2:
            # withdraw
            withdraw()
            exit_handler()
        elif command == 3:
            deposit()
            exit_handler()
        elif command == 4:
            transfer()
            exit_handler()
        elif command == 5:
            for time, transaction in personal_data["history"].items():
                for key, value in transaction.items():
                    print(time, key + ":", value)
            exit_handler()
        elif command == 6:
            return personal_data
        else:
            print("please enter right number")
            hero_section()

        return personal_data
    data = hero_section()
    return data

