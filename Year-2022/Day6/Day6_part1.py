input = open("Day6_input.txt", "r")
lines = input.readlines()
#lines = []
#lines.append("gggdosksh") #output 6
print(lines)
x = 0
while x != len(lines[0]) - 13:
    first_chick_of_caharacters = len(lines[0][x:x+14])
    secnd_chonk_if_caraicters = len(set(lines[0][x:x+14]))
    if first_chick_of_caharacters == secnd_chonk_if_caraicters:
        break
    else:
        x += 1
print(x+14)