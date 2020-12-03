import re

passwords = open("input.txt", "r").read().split("\n")

num_valid = 0
for password in passwords:
    pair = password.split(" ")
    char_range = int(pair[0].split("-")[0]), int(pair[0].split("-")[1])
    char = pair[1][0]
    pswd = pair[2]
    print(char_range, char, pswd, end=": ")
    count = 0
    for letter in pswd:
        if letter == char:
            count += 1
    if count >= char_range[0] and count <= char_range[1]:
        print("Good")
        num_valid += 1
    else:
        print("Bad")
print(num_valid)