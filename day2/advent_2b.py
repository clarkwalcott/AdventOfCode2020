import re

passwords = open("input.txt", "r").read().split("\n")

num_valid = 0
for password in passwords:
    pair, char, pswd = password.split(" ")
    a, b = int(pair.split("-")[0]), int(pair.split("-")[1])
    print(a, b, char, pswd, end=": ")
    checka = pswd[a-1] == char[0]
    checkb = pswd[b-1] == char[0]
    if not(checka and checkb) and (checka or checkb):
        print("Good")
        num_valid += 1
    else:
        print("Bad")
print(num_valid)