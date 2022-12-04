import os
os.chdir("d:\Advent_of_code2022\Year-2022\Day4")
input = open("Day4_input.txt", "r")

count = 0
for line in input:
    splitlines = line.split(',')
    start1 = int(line.split(',')[0].split('-')[0])
    end1 = int(line.split(',')[0].split('-')[1])
    start2 = int(line.split(',')[1].split('-')[0])
    end2 = int(line.split(',')[1].split('-')[1])
    if (start1 <= start2 and start2 <= end1) or (start2 <= start1 and start1 <= end2):
        count += 1

print(count)