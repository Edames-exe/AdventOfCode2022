import os
print(os.getcwd())
input = open("Day5_input.txt", "r")
array = []
i = 1
for line in input:
    print(line)
    while i < 35:
        print(i)
        i += 4
