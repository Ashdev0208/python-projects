# made by Shodiyor
from studentGrader import student_grader
from guessNumber import guess_number

# important function
def greeting():
    print("\n\nWelcome to AshDev playground")

def get_info(information):
   info = input(f"please enter {information}: ")
   return info

def login(user):
    print(" 1.register -- 2.login")
    login_data = get_info("number")
    if len(user["name"]) != 0 and login_data == "2":
        verification = {"name": get_info("name"),"password": get_info("password")}
        if verification["name"] == user["name"] and verification["password"] == user["password"]:
            greeting()
            print("you have succuesfully logged in ")
            dashboard()
        else: 
            print("please remember your login and password or refresh to restart the store")
            login(user)
    elif login_data == "1":
        if len(user["name"]) ==0:
            user["name"] = get_info("your name")
            user["password"] = get_info("your password")
            if len(user["name"]) != 0 and len(user["password"]) != 0:
                print("you have succesfully registered ")
            else:
                print("dont hurry up please fill the form or log in")
                login(user)
        else:
            print("\n\nplease login because you have registered")
            login(user)

    else:
        print("you have entered wrong number\nor please register if you don't have an account\n")
        login(user)
def iterator(value):
    count= 0
    for key, i in value:
        count+=1
        print(f"{count}.Name: {key}; Grade: {i}")
def resume():
    resume = input("     1. Menu ----------  2. log out: ")
    if resume == "1":
        dashboard()
    elif resume == "2":
        print("you have logged out\n to login please enter 2")
        login(user)

greeting()

# register 

user = {"name": "","password": "", "apps": {"ATM":0,"student_grader": 0,"guess": 0,"typing":0}}
choice = 0


login(user)

print(user)


# dashboard

# app includes ATM , student grade Application, guessing numbers, and typing word 


def dashboard():
    print("please choose the application: \n1.Student grade manager\n2.ATM simulator\n3.Guessing Game\n4.typing game\n5. show result\n6.log out")
    choice = int(get_info("right number to use an application"))
    if choice == 1:
       user["apps"]["student_grader"] = student_grader(user["name"],user["password"])
       print("Here is list")
       iterator(user["apps"]["student_grader"])
       resume()
    elif choice == 2:
        pass
    elif choice == 3:
        user["apps"]["guess"] = guess_number()
        resume()
    elif choice == 4:
        pass
    elif choice == 5:
        print("\n\nHere is your all status")
        if user["apps"]["student_grader"] != 0:
            iterator(user["apps"]["student_grader"])
        else:
            print("student grader Manager: 0")
        print(f"atm: 0\nguess: {user['apps']["guess"]}\ntyping: 0\n\n")
        resume()

    elif choice == 6:
        print("you have logged out\n to login please enter 2")
        login(user)
    else:
        print("please enter right number to use an application \n")
        dashboard()


dashboard()
