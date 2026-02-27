from pathlib import Path 
DIR = Path(__file__).parent 
import bisect 
from copy import deepcopy

def sortRangeLower(ranges:list[list]) -> list[list]:
    ranges.sort(key=lambda pair : pair[0])
    return ranges 

def sortRangeUpper(ranges:list[list]) -> list[list]:
    ranges.sort(key=lambda pair : pair[1])
    return ranges 

def contains(x:int, A:list[list]) -> bool:
    a = deepcopy(A)
    glb = bisect.bisect_right(a, x , key=lambda pair:pair[0])
    if glb == 0:
        return False 
    del a[glb:]
    a = sortRangeUpper(a)
    lub = bisect.bisect_left(a, x, key=lambda pair:pair[1])
    if lub == len(a):
        return False 
    return True 

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

    IDs = IDs.split("\n")
    IDs = [int(id) for id in IDs]
    count = 0
    for id in IDs:
        count += contains(id, freshRanges)

    return count 

def main():
    with open(DIR / 'document.txt', 'r')  as f:
        input = f.read() 
    ans = parseInput(input)
    print("Final answer: ", ans)

if __name__ == "__main__":
    main() 



