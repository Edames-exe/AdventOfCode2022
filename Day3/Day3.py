import os
os.chdir("d:\Advent_of_code2022\Day3")

priorities = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}
answer = 0
#get file
input = open("Day3_input.txt", "r")
count2 = 0
#read first lin
for line in input:
    #split in half
    index = int((len(line) -1)/2)
    string1 = line[:index]
    string2 = line[index:]
    #for each letter in a check each letter in b
    isfound = False
    for value1 in string1:
        for value2 in string2:
            if value1 == value2:
                #look at map for value
                answer = answer + priorities[value1]
                count2 += 1
                isfound = True
                break
        if isfound == True:
            break


print("answer: ", answer)
print("number of answers: ", count2)