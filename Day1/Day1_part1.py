import os
os.chdir("d:\Advent_of_code2022\Day1")
input = open("Day1_input.txt", "r")
calories = 0
elves = []
for line in input:
    if line != "\n":
        calories += int(line)
    else:
        elves.append(calories)
        calories = 0
print(max(elves))