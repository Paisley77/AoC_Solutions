from pathlib import Path 
import math 
DIR = Path(__file__).parent 

def numOfDigits(N:int) -> int:
    return math.floor(math.log10(N)) + 1 

def computeDouble(A:int) -> int:
    N = numOfDigits(A)
    return A * 10**N + A 

def sumInvalid(N:int, M:int) -> int:
    """
    Precondition: N <= M
    Returns the sum of integers between NN and MM (inclusive) of the form X_1...X_nX_1...X_n
    """
    lenN = numOfDigits(N)
    lenM = numOfDigits(M)
    total = 0
    start = N
    for n in range(lenN, lenM+1):
        end = min(10**n-1, M)
        S = ((start+end) * (end-start+1)) // 2
        total += (S * 10**n + S)
        start = 10**n 
    return total 

def parseRange(rangestr: str) -> int:
    digitstrs = rangestr.split('-')
    firststr = digitstrs[0]
    laststr = digitstrs[1]
    if len(firststr) % 2 == 0:
        first = int(firststr)
    else:
        first = 10 ** (len(firststr))
    if len(laststr) % 2 == 0:
        last = int(laststr)
    else:
        last = 10 ** (len(laststr)-1) - 1
    if first > last:
        return 0
    N1 = numOfDigits(first)
    N2 = numOfDigits(last)
    A = first // (10**(N1//2))
    B = last // (10**(N2//2))
    AA = computeDouble(A)
    BB = computeDouble(B) 
    if AA<first:
        A +=1
    if BB>last:
        B -=1
    if A>B:
        return 0 
    return sumInvalid(A,B)

def parseInput(textstr: str) -> int:
    ranges = textstr.strip().split(',')
    count = 0
    for range in ranges:
        count += parseRange(range)
    return count 

def main():
    with open(DIR / "document.txt", 'r') as f:
        textstr = f.read() 
    print("Final Answer: ", parseInput(textstr))

if __name__ == '__main__':
    main() 
        
    