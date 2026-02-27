from scipy import signal 
import numpy as np
from pathlib import Path 
DIR = Path(__file__).parent 

def parseMatrix(A:np.ndarray, count:int) -> int:
    kernel = np.ones((3,3))
    kernel[1,1] = 0
    B = signal.convolve2d(A ,kernel, mode='same', boundary='fill', fillvalue=0)
    B = np.where(B<4, 1, 0)
    C = (A==1) & (B==1)
    if C.sum() == 0:
        return count 
    return parseMatrix(A-C, count + C.sum())

def processMatrix(input:str) -> int:
    rows = input.split('\n')
    nested = [[1 if row[i]=='@' else 0 for i in range(len(rows))] for row in rows]
    A = np.array(nested)
    return parseMatrix(A, 0)

def main():
    with open(DIR/'document.txt', 'r') as f:
        input = f.read() 
    ans = processMatrix(input)
    print('Final answer = ', ans)

if __name__ == '__main__':
    main() 
