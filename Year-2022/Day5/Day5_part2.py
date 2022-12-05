input = open("Day5_input.txt", "r")
#put file in to array of lines
lines = input.readlines()

verticalArray = [] #Holds all items as seen in the input

#create array of items
for x in range(0, 8, 1):
    innerArray = []
    for y in range(1, 35, 4):
        innerArray.append(lines[x][y])
    verticalArray.append(innerArray)

bigBoiArray = []
#look at collumn
for collumn in range(0, 9, 1):
    innerArray = []
    # look at item in bottom row
    for row in range(0, len(verticalArray), 1):
        # add item to new array
        if verticalArray[row][collumn] != ' ':
            innerArray.append(verticalArray[row][collumn])
    bigBoiArray.append(innerArray[::-1])
def printArray(array):
    for z in array:
        print(z)

printArray(bigBoiArray)

for command in range(10, len(lines), 1):
    splitLine = lines[command].split(' ')
    num = int(splitLine[1])
    start = int(splitLine[3])
    end = int(splitLine[5])
    for loop in range(1, num+1, 1):
        bigBoiArray[end-1].append(bigBoiArray[start-1].pop())

print("------------")

printArray(bigBoiArray)
