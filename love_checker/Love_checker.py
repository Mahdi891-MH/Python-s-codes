#This progarm check the compatibility between two names and find the love's score.
#Mahdi Hussaini

name1 = (input("Enter your name: ")).lower()
name2 = (input("Enter her/his name: ")).lower()
names = name1+name2


def check(name, word):
    counter = 0
    for i in word:
        for j in name:
            if i == j:
                counter += 1
    return counter


love_score = str(check(names, "true"))+str(check(names, "love"))
print(love_score)
