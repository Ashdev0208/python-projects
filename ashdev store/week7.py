# in class-assignment

# numbers = [1,2,3,4,5,6,7,8,9,10]

# cubes = [cube ** 3 for cube in numbers]

# print(cubes)

# words = ["hello", "hi","what's up"]

# key_words = {}

# for i in words:

#     key_words[i] = len(i)

# print(key_words)

# sentence = "hello my name is barry alen i am the fastestg man in alive"

# no_constant = {vowel for vowel in sentence.lower() if vowel in "aeiou"}
# print(no_constant)

# ASSIGNMENT 1


# sentence = input("Please enter a sentence: ").lower().split(" ")
# words = {}
# for x in sentence:
#     i = 0
#     for j in sentence:
#         if x == j:
#             i += 1
#     words[x] = i

# sorted_words = {x:words.get(x) for x in sorted(words)}


# print(sorted_words)


# ASSIGNMENT 2


# sentence = input("Please enter a sentence: ").lower()
# words = {}
# for x in sentence:
#     i = 0
#     for j in sentence:
#         if x == j:
#             i += 1
#     if x != " ":
#         words[x] = i

# sorted_words = {x:words.get(x) for x in sorted(words)}


# print(sorted_words)

# ASSIGNMENT 3

# 1. result = divmod(17,5) it divided by 5 and then result 3 and remainder is 2

# print(result)

# quotient, remainder = result

# print(quotient)
# print(remainder)

# #2 zip()
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

# If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.

# names = ["Ali", "John", "Sara"]
# ages = [20, 21, 19]

# for item in zip(names, ages):
#     print(item)

# 3. dict.items
# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

# The view object will reflect any changes done to the dictionary

# student = {
#     "name": "Ali",
#     "age": 20
# }

# for item in student.items():
#     print(item)


#4. dict.popitem()
# The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item.

# The removed item is the return value of the popitem() method, as a tuple

# student = {
#     "name": "Ali",
#     "age": 20
# }

# item = student.popitem()

# print(item)    
#5 split
# this returns a tuple
# sentence = "hi i am shodiyor".split(" ")

# print(sentence)