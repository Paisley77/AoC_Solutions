import numpy as np
from pathlib import Path 
DIR = Path(__file__).parent 

def computeJoltage(bank:str):
    bankList = list(bank)
    bankList = np.array([int(w) for w in bankList])
    A = np.max(bankList[:-1])
    i = np.argmax(bankList[:-1])
    B = np.max(bankList[i+1:])
    return A*10+B 

def parseInput(input:str):
    banks = input.split('\n')
    joltage = 0
    for bank in banks:
        joltage += computeJoltage(bank)
    return joltage 

def main():
    with open(DIR / 'document.txt', 'r') as f:
        input = f.read() 
    ans = parseInput(input)
    print("Final answer = ", ans)

if __name__ == '__main__':
    main() 