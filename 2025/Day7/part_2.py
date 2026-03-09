from pathlib import Path 
DIR = Path(__file__).parent

import numpy as np

def countSplit(A:np.ndarray, row:int, col:int) -> int:
    leftPass = rightPass = False 
    if col>0 and A[row][col-1] == '.':
        leftPass = True 
    if col<(A.shape[1]-1) and A[row][col+1] == '.':
        rightPass = True 
    if not leftPass and not rightPass:
        A[row][col] = "&0"
        return 0
    leftCount = leftPass 
    rightCount = rightPass 
    if leftPass:
        nextRowSplit = np.where(A[row+1:, col-1]=='^')[0]
        nextRowCounted = np.where(np.char.startswith(A[row+1:, col-1], '&'))[0]
        if nextRowSplit.shape[0]>0:
            nextRowSplit = nextRowSplit[0] + row + 1
        else:
            nextRowSplit = A.shape[0]
        if nextRowCounted.shape[0]>0:
            nextRowCounted = nextRowCounted[0] + row + 1
        else:
            nextRowCounted = A.shape[0]
        nextRow = min(nextRowSplit, nextRowCounted)
        if nextRow < A.shape[0]:
            if A[nextRow][col-1]=='^':
                leftCount = countSplit(A, nextRow, col-1)
            else:
                leftCount = int(A[nextRow][col-1][1:])
    if rightPass:
        nextRowSplit = np.where(A[row+1:, col+1]=='^')[0]
        nextRowCounted = np.where(np.char.startswith(A[row+1:, col+1], '&'))[0]
        if nextRowSplit.shape[0]>0:
            nextRowSplit = nextRowSplit[0] + row + 1
        else:
            nextRowSplit = A.shape[0]
        if nextRowCounted.shape[0]>0:
            nextRowCounted = nextRowCounted[0] + row + 1
        else:
            nextRowCounted = A.shape[0]
        nextRow = min(nextRowSplit, nextRowCounted)
        if nextRow < A.shape[0]:
            if A[nextRow][col+1]=='^':
                rightCount = countSplit(A, nextRow, col+1)
            else:
                rightCount = int(A[nextRow][col+1][1:])
    count = leftCount + rightCount 
    A[row][col] = f"&{count}"
    if row==0:
        np.savetxt("matrix.csv", A, fmt='%s', delimiter=' ')
    return count 
        

def parseInput(input:str) -> int:
    lines = input.split('\n')
    matrix = np.array([list(line) for line in lines], dtype='U20')
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
