from pathlib import Path 
DIR = Path(__file__).parent

import numpy as np

def countSplit(A:np.ndarray, row:int, col:int) -> int:
    leftPass = rightPass = False 
    if col>0 and not A[row][col-1] in ['^', 'v']:
        leftPass = True 
    if col<(A.shape[1]-1) and not A[row][col+1] in ['^', 'v']:
        rightPass = True 
    if not leftPass and not rightPass:
        return 0 
    A[row][col] = 'v'
    if row==A.shape[0]-1:
        return 1 
    leftCount = rightCount = 0
    if leftPass:
        nextRow = np.where(A[row+1:, col-1]=='^')[0]
        if nextRow.shape[0] > 0:
            nextRow = nextRow[0] + row + 1 
            if not np.any(A[row+1:nextRow, col-1]=='v'):
                leftCount = countSplit(A, nextRow, col-1)
    if rightPass:
        nextRow = np.where(A[row+1:, col+1]=='^')[0]
        if nextRow.shape[0] > 0:
            nextRow = nextRow[0] + row + 1
            if not np.any(A[row+1:nextRow, col+1]=='v'):
                rightCount = countSplit(A, nextRow, col+1)
    return 1 + leftCount + rightCount 
        

def parseInput(input:str) -> int:
    lines = input.split('\n')
    matrix = np.array([list(line) for line in lines])
    SRow = 0
    while not (matrix[SRow]=='S').any():
        SRow += 1
    SCol = np.where(matrix[SRow]=='S')[0][0]
    startRow = np.where(matrix[SRow+1:, SCol]=='^')[0][0]
    return countSplit(matrix[startRow+SRow+1:], 0, SCol)

def main():
    with open(DIR / "document.txt", 'r') as f:
        input = f.read()
    ans = parseInput(input)
    print("Final answer = ", ans)

if __name__ == "__main__":
    main() 
