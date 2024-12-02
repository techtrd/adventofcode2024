leftList = []
rightList = []

with open('aoc_data.txt') as f:
    data = f.read()

# Split the data
for line in data.strip().split("\n"):
    left, right = map(int, line.split())

    leftList.append(left)
    rightList.append(right)

# sort ascending
leftList.sort()
rightList.sort()

# compare and measure distance
# We know both lists are the same size so we can just work with the length of one list
differences = []

for leftVal, rightVal in zip(leftList, rightList):
    difference = abs(leftVal - rightVal)
    differences.append(difference)

print(sum(differences))