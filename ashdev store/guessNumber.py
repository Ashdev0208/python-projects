import random 

def guess_number():
    counter = 0
    number = random.randint(1,100)
    result = {}

    while True:
        guess = int(input("Guess the number starts from 1 to 100: "))
        counter += 1
        if guess < number:
            print("cold")
        elif guess > number:
            print("hot")
        elif guess <= 0 and guess > 100:
            print("follow the rules")
            continue
        else: 
            print(f"woooww, you have found the Number({number}) in the {counter} attempts")
            result["random_number"] = number
            result["counter"] = counter
            break
    return result
