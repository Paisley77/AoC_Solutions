from pathlib import Path
DIR = Path(__file__).parent 

from disjoint_set_union import DSU 
import numpy as np

dsu = DSU(1)

def search(pairs:list, low:int, high:int, rollback:bool) -> int:
    if low > high:
        return -1 
    mid = (low+high)//2
    if not rollback:
        for i in range(low, mid+1):
            dsu.union(pairs[i][0], pairs[i][1])
    else:
        for i in range(mid+1, high+2):
            dsu.rollback(pairs[i][0], pairs[i][1])
    if dsu.numComponents == 1:
        index = search(pairs, low, mid-1, True)
        return index if index>=0 else mid 
    return search(pairs, mid+1, high, False)

def parseInput(input:str) -> int:
    # Extract coordinates
    points = input.split('\n')
    points = [coord.split(',') for coord in points]
    points = [[int(w) for w in coord] for coord in points]
    points = np.array(points)
    # Build distance matrix 
    N = len(points)
    D = np.zeros((N, N))
    for i in range(N):
        for j in range(i+1, N):
            D[i][j] = eucDist(points[i], points[j])
    # create list of pairs sorted by distance
    row_indices, col_indices = np.triu_indices_from(D, k=1)
    distances = D[row_indices, col_indices]
    sorted_indices = np.argsort(distances)
    pairs = []
    for idx in sorted_indices:
        row_idx = row_indices[idx]
        col_idx = col_indices[idx]
        pairs.append([row_idx, col_idx])
    # declare the DSU instance
    global dsu 
    dsu = DSU(N)
    # find the first pair creating connectivity 
    index = search(pairs, 0, len(pairs)-1, False)
    return points[pairs[index][0]][0] * points[pairs[index][1]][0] 

def eucDist(p1:np.ndarray, p2:np.ndarray):
    return np.linalg.norm(p1-p2)

def main():
    with open(DIR/"document.txt", 'r') as f:
        input = f.read()
    ans = parseInput(input)
    print("Final answer = ", ans)

if __name__ == '__main__':
    main() 