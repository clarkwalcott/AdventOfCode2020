import re

passwords = open("input.txt", "r").read().split("\n")

for password in passwords:
    pair = password.split(" ")
    char_range = int(pair[0].split("-")[0]), int(pair[0].split("-")[1])
    char = pair[1][0]
    pswd = pair[2]
    print(char_range, char, pswd)