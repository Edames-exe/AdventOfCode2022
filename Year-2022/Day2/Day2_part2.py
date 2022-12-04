import os
os.chdir("d:\Advent_of_code2022\Day2")
outcomes = {
    "X": "Loose",
    "Y": "Draw",
    "Z": "Win",
}
Win = {
    "A": 8, #paper is worth 2
    "B": 9, #scissors is worth 3
    "C": 7, #rock is worth 1
}
Draw = {
    "A": 4, #rock is woth 1
    "B": 5, #paper is worth 2
    "C": 6, #scissors is woth 3
}
Loose = {
    "A": 3, #scissors is worth 3
    "B": 1, #rock is worth 1
    "C": 2, #paper is worth 2
}
input = open("Day2_input.txt", "r")
score = 0
for line in input:
    outcome = outcomes[line[2]]
    if outcome == "Win":
        score += Win[line[0]]
    if outcome == "Draw":
        score += Draw[line[0]]
    if outcome == "Loose":
        score += Loose[line[0]]
print(score)
