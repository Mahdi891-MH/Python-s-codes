#Mahdi Hussaini
#This program can generate strong password

import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
characters = ['@', '$', '^', '&', '*', '#', '%', '!']
letter = int(input("How letters would you like in your password: "))
number = int(input("How numbers would you like in your password: "))
char = int(input("How characters would you like in your password: "))

pass_list = []
for i in range(letter):
    index = random.randint(0, len(letters)-1)
    pass_list.append(letters[index])

for i in range(number):
    index = random.randint(0, len(numbers)-1)
    pass_list.append(str(numbers[index]))

for i in range(char):
    index = random.randint(0, len(characters)-1)
    pass_list.append(characters[index])

print(pass_list)

indexes = []

while len(indexes) < len(pass_list):
    index = random.randint(0, len(pass_list)-1)
    b = 1
    for i in indexes:
         if i == index:
            b = 0
            break
    if b == 1:
        indexes.append(index)
password = ''
for i in indexes:
    password += pass_list[i]

print(password)




