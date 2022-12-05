input = open("Day1_input.txt", "r")
calories = 0
elves = []
for line in input:
    if line != "\n":
        calories += int(line)
    else:
        elves.append(calories)
        calories = 0
elves.sort(reverse=True)
top3 = elves[0] + elves[1] + elves[2]
print(top3)