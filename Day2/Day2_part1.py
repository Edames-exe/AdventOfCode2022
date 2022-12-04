import os
os.chdir("d:\Advent_of_code2022\Day2")
outcomes = {
    "A X": "Draw",
    "A Y": "Win",
    "A Z": "Loose",
    "B X": "Loose",
    "B Y": "Draw",
    "B Z": "Win",
    "C X": "Win",
    "C Y": "Loose",
    "C Z": "Draw",
}
points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "Win": 6,
    "Loose": 0,
    "Draw": 3,
}
input = open("Day2_input.txt", "r")
score = 0
for line in input:
    outcome = outcomes[line.strip("\n")]
    print(outcome)
    score += int(points[outcome])
    score += int(points[line[2]])
print(score)
