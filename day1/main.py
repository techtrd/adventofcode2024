def main():
    data = "aoc_data.txt"
    leftList, rightList = processData(data)
    print(part_one(leftList, rightList))
    print(part_two(leftList, rightList))

def processData(file):
    leftList = []
    rightList = []

    with open(file) as f:
        data = f.read()

    # Split the data
    for line in data.strip().split("\n"):
        left, right = map(int, line.split())

        leftList.append(left)
        rightList.append(right)

    # sort ascending
    leftList.sort()
    rightList.sort()

    return leftList, rightList

def part_one(leftList, rightList):
    # compare and measure distance
    # We know both lists are the same size so we can just work with the length of one list
    differences = []

    for leftVal, rightVal in zip(leftList, rightList):
        difference = abs(leftVal - rightVal)
        differences.append(difference)

    return sum(differences)

def part_two(leftList, rightList):
    similarities = 0
    for number in leftList:
        occurences = rightList.count(number)
        similarities = similarities + (number * occurences)
        
    return similarities
if __name__ == "__main__":
    main()