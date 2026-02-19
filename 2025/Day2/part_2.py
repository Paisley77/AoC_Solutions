from pathlib import Path 
import math 
from typing import List
DIR = Path(__file__).parent 

def numOfDigits(N:int) -> int:
    return math.floor(math.log10(N)) + 1 

def firstN(n:int, N:int) -> int:
    num = numOfDigits(n)
    assert num>=N, "Invalid number of digits."
    return n//10**(num-N)

def repeatN(n:int, N:int) -> int:
    num = numOfDigits(n)
    return n * sum10(num, N)

def sum10(n:int, N:int) -> int:
    return (10**(n*N)-1) / (10**n-1)

def computeFactors(n:int) -> List[int]:
    factors = [1]
    for i in range(2, math.isqrt(n)+1):
        if n%i == 0:
            factors.append(i)
            if n//i != i:
                factors.append(n//i)
    factors.sort()
    return factors 

def sumNRepeat(N:int, M:int, duplicateSum:int, nRepeat:int):
    numN = numOfDigits(N)
    numM = numOfDigits(M)
    assert numN==numM, "Number of digits should be equal."
    S = ((N+M)*(M-N+1))//2 
    return (S-duplicateSum) * sum10(numN, nRepeat)

def sumAllRepeat(N:int, M:int) -> int:
    numN = numOfDigits(N)
    numM = numOfDigits(M)
    assert numN==numM, "Number of digits should be equal."
    if numN==1:
        return 0 
    factors = computeFactors(numN)
    total = 0
    for fac in factors:
        nRepeat = numN // fac
        A = firstN(N, fac)
        ARepeat = repeatN(A, nRepeat)
        if (ARepeat < N):
            A = A + 1 
        B = firstN(M, fac)
        BRepeat = repeatN(B, nRepeat)
        if (BRepeat > M):
            B = B - 1
        if A > B:
            continue
        duplicateSum = sumAllRepeat(A,B)
        total += sumNRepeat(A,B,duplicateSum, nRepeat)
    return total 

def sumRange(N:int, M:int) -> int:
    total = 0
    start = N 
    numN = numOfDigits(N)
    numM = numOfDigits(M)
    for num in range(numN, numM+1):
        end = min(10**num-1, M)
        total += sumAllRepeat(start, end)
        start = 10**num 
    return total 

def parseInput(textstr: str) -> int:
    ranges = textstr.strip().split(',')
    total = 0
    for rangestr in ranges:
        digitstrs = rangestr.split('-')
        first = int(digitstrs[0])
        last = int(digitstrs[1])
        total += sumRange(first, last)
    return total 

def main():
    with open(DIR / 'document.txt', 'r') as f:
        textstr = f.read() 
    ans = parseInput(textstr)
    print("Final answer = ", ans)

if __name__ == '__main__':
    main() 
        


