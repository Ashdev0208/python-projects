
# student grader application -----
# it includes -- login, password, adding informations and grading 
counter = 0
while True:
    login = input("Please enter your login: ")
    password = input("Please enter your password: ")

    if login == "pyCoding" and password == "py@Coding":

        print("You have successfully logged in")
        break

    else:
        counter += 1
        if login != "pyCoding" and len(login) > 1:
            print("You have entered the wrong login ID")
        else:
            print("please enter log in")

        if password != "py@Coding":

            if len(password) < 8:
                print("Password length is lower than 8 ande weak Password !")

            elif "@" not in password and "." not in password and "!" not in password and "?" not in password:
                print("Weak password has been entered")

            else:
                print("Wrong password has been entered")

        if counter >= 3: 
            print("enough attempts to log in")
            break 
        else:
            continue

# log in and password are done

number_of_students = int(input("please enter your number of students: "))


value = 0
students = ""
while True:
    value += 1
    if number_of_students < value:
        print("")
        print("you have entered all of students")
        break
    else:
        student_name = input(f"please your {value} student name: ")
        student_grade = input(f"please write your {value} student grade: ")
        students += f"{value} -- {student_name}: {student_grade}"
print(students)