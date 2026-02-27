from pathlib import Path 
DIR = Path(__file__).parent 

def merge(A:list[list]) -> list:
    if len(A) <= 1:
        return A
    if A[0][1] >= A[1][0]:
        mergedPair = []
        mergedPair.append(A[0][0])
        mergedPair.append(max(A[0][1], A[1][1]))
        del A[:2]
        A = [mergedPair] + A 
        return merge(A)
    else:
        return [A[0]] + merge(A[1:])

def sortRangeLower(ranges:list[list]) -> list[list]:
    ranges.sort(key=lambda pair : pair[0])
    return ranges 

def parseInput(input:str) -> int:
    freshRanges, IDs = input.split("\n\n")
    freshRanges = freshRanges.split("\n")

    def parseRange(rangestr:str):
        lower, upper = rangestr.split('-')
        rangels = []
        rangels.append(int(lower))
        rangels.append(int(upper))
        return rangels 
    
    freshRanges = [parseRange(rangestr) for rangestr in freshRanges]
    freshRanges = sortRangeLower(freshRanges)
    freshRanges = merge(freshRanges)

    count = 0 
    for pair in freshRanges:
        count += (pair[1]-pair[0]+1)
    
    return count 

def main():
    with open(DIR / 'document.txt', 'r')  as f:
        input = f.read() 
    ans = parseInput(input)
    print("Final answer: ", ans)

if __name__ == "__main__":
    main() 


