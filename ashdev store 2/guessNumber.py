import random 

def guess_number():
    counter = 0
    number = random.randint(1,100)
    result = {}

    while True:
        guess = input("please enter a number from 1 to 100: ")
        if guess.isdigit():
            guess_to_number = int(guess)
        else:
            print("please enter number only between 1 to 100")
            continue
        counter += 1
        if guess_to_number <= 0 or guess_to_number > 100:
            print("follow the rules")
            continue
        elif guess_to_number < number:
            print("cold")
        elif guess_to_number > number :
            print("hot")
        else: 
            print(f"woooww, you have found the Number({number}) in the {counter} attempts")
            result["random_number"] = number
            result["counter"] = counter
            break
    return result