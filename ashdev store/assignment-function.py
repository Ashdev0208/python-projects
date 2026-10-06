import math

def rootsQEq():
    print("this program finds the real solutions to a quadratic. \n")


    a = eval(input("Enter the value of coefficient a: "))
    b = eval(input("Enter the value of coefficient b: "))
    c = eval(input("Enter the value of coefficient c: "))

    s_root_val = math.sqrt(b*b - 4 * a * c)
    root1 = (-b + s_root_val)/(2*a)
    root2 = (-b - s_root_val)/(2*a)

    print("\n","the solutions are: ", root1, root2)

rootsQEq()

def c_to_f(c):
    return (9/5)*c + 32
def f_to_c(f):
    return 5/9 * (f - 32)

def main():
    choice = int(input("1.do you prefer to change celsius to fahrenheit\n or 2.celsius to fahrenheit \n please write numbers to choose? \n"))
    if choice == 1:
        celsius = int(input("please enter today's weather in celsius mode: "))
        c = c_to_f(celsius)
        print(c)
    elif choice == 2:
        celsius = int(input("please enter today's weather in fahrenheit mode: "))
        f = f_to_c(celsius)
        print(f)
main()

# third assignment

def Calculate_Compund_Interest(p,r,n):
    return p*(1+r)**n
def calculate_interest(p,r,n,t):
    return principal * (1 + rate/period) ** years*period - principal
principal = 10000
rate = 5 / 100
years = 1
period = 1
starting_amount = principal


# this is for assignment version 2

# while years <= 7:
#     result = Calculate_Compund_Interest(principal,rate,years)
#     interest = calculate_interest(principal,rate, years, period)
#     print(f"Year: {years}  starting balance: {starting_amount}      Interest: {interest}     Ending Balance: {result}\n")
#     starting_amount = result
#     years += 1


# assignment 3 version 3

result = Calculate_Compund_Interest(principal,rate,years)

print("\n\nPrincipal: " , principal , "₩") # \n this helps to separate line
print("Interest rate: " , rate * 100 , "%")
print("Years: " , years)
print("(A) Final Amount: " , result , "₩")
