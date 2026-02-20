from typing import List
import numpy as np
from pathlib import Path 
DIR = Path(__file__).parent 

def findNextDigit(low:int, high:int, ls:List, digits:List, seq:List) -> List:
    if high==len(digits):
        return seq 
    for i in range(0, len(ls)):
        if ls[i]>=low and ls[i]<=high:
            seq.append(digits[ls[i]])
            break
    return findNextDigit(ls[i]+1, high+1, ls, digits, seq)

def computeJoltage(N:int, digits:List) -> int:
    ls = sorted(range(len(digits)), key=lambda i:digits[i], reverse=True)
    seq = findNextDigit(0, len(digits)-N, ls, digits, [])
    return int("".join(map(str,seq)))
    
def parseInput(input:str) -> int:
    banks = input.split('\n')
    total = 0 
    for bank in banks:
        digits = [int(w) for w in bank]
        total += computeJoltage(12, digits)
    return total 

def main():
    with open(DIR/'document.txt', 'r') as f:
        input = f.read() 
    ans = parseInput(input)
    print("Final answer = ", ans)

if __name__=='__main__':
    main() 
