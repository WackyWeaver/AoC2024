# Day 1 of 2024 Advent of Code
# Written by WackyWeaver

from collections import Counter

def getList(inputFile):
    with open(inputFile, 'r') as content:
        content = content.read()
        lines = content.split('\n')
        leftList = []
        rightList = []
        for pair in lines:
            pairing = pair.split("   ")
            rightList.append(int(pairing[1]))
            leftList.append(int(pairing[0]))
        leftList = sorted(leftList)
        rightList = sorted(rightList)
        
    return leftList, rightList

def totalDifference(pairList):
    total = 0
    for left, right in pairList:
        total += abs(left - right)
    return total

def totalSimilarity(leftList, rightList):
    total = 0
    rightCount = Counter(rightList)
    for line in leftList:
        if line in rightCount:
            similarity = rightCount[line] * line
            total += similarity
    return total

def main():
    leftList, rightList = getList("Day 1/input.txt")
    pairList = zip(leftList, rightList)
    print("Part 1 Solution: ", totalDifference(pairList))
    print("Part 2 Solution: ", totalSimilarity(leftList, rightList))
    
if __name__ == "__main__":
    main()