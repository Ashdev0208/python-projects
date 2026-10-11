# made by Shodiyor
from studentGrader import student_grader
from guessNumber import guess_number
from ATM import automatic_teller_machine

# important function
def greeting():
    print("\n\nWelcome to AshDev playground")

def get_info(information):
   info = input(f"please enter {information}: ")
   return info

def login(user):
    print(" 1.register -- 2.login")
    login_data = get_info("number")
    password, name = user["password"],user["name"]
    if len(name) != 0 and login_data == "2":
        verification = {"name": get_info("name"),"password": get_info("password")}
        if verification["name"] == name and verification["password"] == password:
            greeting()
            print("you have succuesfully logged in ")
            dashboard()
        else: 
            print("please remember your login and password or refresh to restart the store")
            login(user)
    elif login_data == "1": 
        if len(name) ==0:
            input_name = get_info("your name")
            input_password = get_info("your password")
            if len(input_name) < 2 or len(input_password) < 5:
                if len(input_name) < 2:
                    print("name must be longer than 2 characters")
                if len(input_password) < 5:
                    print("password must be longer than 5 characters")
                print("don't hurry up please fill the form or log in")
                login(user)
            else:
                print("you have succesfully registered ")
                user["name"] = input_name
                user["password"] = input_password
                dashboard()
                
        else:
            print("\n\nplease login because you have registered")
            login(user)

    else:
        print("you have entered wrong number\nor please register if you don't have an account\n")
        login(user)
def iterator(value):
    count = 0
    for key, i in value:
        count += 1
        print(f"{count}.Name: {key}; Grade: {i}")
def resume():
    resume_input = input("     1. Menu ----------  2. log out: ")
    if resume_input == "1":
        dashboard()
    elif resume_input == "2":
        print("you have logged out\n to login please enter 2")
        login(user)
    else:
        print("please enter those numbers to use")
        resume()

greeting()

# register 

user = {"name": "","password": "", "apps": {"ATM":0,"student_grader": 0,"guess": [],"typing":0}}
choice = 0





# dashboard

# app includes ATM , student grade Application, guessing numbers, and typing word 


def dashboard():
    print("please choose the application: \n1.Student grade manager\n2.ATM simulator\n3.Guessing Game\n4.show result\n5.log out")
    choice = get_info("right number to use an application")
    app = user["apps"]
    if choice == "1":
       app["student_grader"] = student_grader(user["name"],user["password"])
       print("Here is list")
       iterator(user["apps"]["student_grader"])
       resume()
    elif choice == "2":
        app["ATM"] = automatic_teller_machine()
        resume()
    elif choice == "3":
        app["guess"].append(guess_number())
        resume()
    elif choice == "4":
        print("\n\nHere is your all student status")
        if app["student_grader"]:
            iterator(user["apps"]["student_grader"])
        else:
            print("student grader Manager: 0")
        if app["ATM"] != 0:
            print("ATM")
            for key, value in app["ATM"].items():
                if key == "history":
                    for key2, value2 in value.items():
                        for key3, val3 in value2.items():
                            print(f"in {key2}, {key3}: {val3}")
                else:
                    print(f"{key}: {value}")
        else:
            print("ATM: empty")
        if app["guess"] == 0:
            print("guessing Number: empty")
        else:
            
            print(app["guess"])
            for i in app['guess']:
                print(f"Guessing numbers: the number is {i['random_number'] } in the {i['counter']} attempts")
        resume()

    elif choice == "5":
        print("you have logged out\n to login please enter 2")
        login(user)
    else:
        print("please enter right number to use an application \n")
        dashboard()

login(user)

