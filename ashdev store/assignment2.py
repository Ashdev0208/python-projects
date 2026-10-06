# assignment 1

def text_uppercaser(text):
    return text.upper()
def text_lowercase(text):
    return text.lower()

choice = int(input("1.uppercase to lowercase\n2.lowercase to uppercase\n"))

if choice == 1:
    result = input("enter your sentence: ")
    print(text_lowercase(result))
elif choice == 2:
    result = input("enter your sentence: ")
    print(text_uppercaser(result))
else:
    print("you have entered wrong number")


# assignment 2

def count_identifier(text = "Abdusalomov Shodiyor 18 years old".lower()):
   vowels = 0
   constanent = 0
   blank = text.count(" ")
   
   for char in text:
      if char in "aeuio":
        vowels += 1

   for char in text:
      if char not in "aeuio":
         constanent += 1
    
   return {"vowels": vowels, "constanent": constanent, "blank": blank, "length": len(text) + blank}

counter = count_identifier()

print(counter)

# in-class assignment 1

square = [x ** 2 for x in range(1, 21) if x % 2 == 0]

print(square)

# assignment 3 

# 1. The append() method appends an element to the end of the list.
# fruits = ['apple', 'banana', 'cherry']
# fruits.append("orange")
# ['apple', 'banana', 'cherry', 'orange']

# 2.The extend() method adds the specified list elements (or any iterable) to the end of the current list.
# fruits = ['apple', 'banana', 'cherry']

# cars = ['Ford', 'BMW', 'Volvo']

# fruits.extend(cars)

# ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# 3. The insert() method inserts the specified value at the specified position.
# fruits = ['apple', 'banana', 'cherry']

# fruits.insert(1, "orange")
# ['apple', 'orange', 'banana', 'cherry']
# 4. If there are more than one item with the specified value, the remove() method removes the first occurrence:

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)
# ['apple', 'cherry', 'banana', 'kiwi']

# 5.The pop() method removes the element at the specified position.

# fruits = ['apple', 'banana', 'cherry']

# fruits.pop(1)

# ['apple', 'cherry']

# 6. The clear() method removes all the elements from a list.

# fruits = ['apple', 'banana', 'cherry', 'orange']

# fruits.clear()

# []

# 7.The index() method returns the position at the first occurrence of the specified value.
# fruits = ['apple', 'banana', 'cherry']

# x = fruits.index("cherry")
# 2

# 8.The count() method returns the number of elements with the specified value. 
# fruits = ['apple', 'banana', 'cherry']

# x = fruits.count("cherry")
# 1

# 9. The sort() method sorts the list ascending by default.

# You can also make a function to decide the sorting criteria(s).

# cars = ['Ford', 'BMW', 'Volvo']

# cars.sort()

# ['BMW', 'Ford', 'Volvo']

# 10. The reverse() method reverses the sorting order of the elements.

# fruits = ['apple', 'banana', 'cherry']

# fruits.reverse()
# ['cherry', 'banana', 'apple']

# 11. The copy() method returns a copy of the specified list.

# fruits = ['apple', 'banana', 'cherry', 'orange']

# x = fruits.copy()

# ['apple', 'banana', 'cherry', 'orange']

# assignment 4

sortedList = []

print("Run example\n Commands: add <item>, remove <item>, show, done")

while True:
    commands = input("Write your Commands: ").split()
    if commands[0] == "add" and len(commands) > 1:
        sortedList.append(" ".join(commands[1:]))
    elif commands[0] == "remove" and len(commands) > 1:
        sortedList.remove(" ".join(commands[1:]))
    elif commands[0] == "show":
        print(f"Current list: {sortedList}")
    elif commands[0] == "done":
        print(f"Final list: {sortedList}")
        break
    else:
        print("please write right commands or enter commands right")


# Assignment 5 

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers 

user_list = int(input("Please enter series of numbers with space ")).split(" ")
final_result = bubble_sort(user_list)
print(f"here is Your sorted list: {final_result}")