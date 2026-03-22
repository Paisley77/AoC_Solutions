from pathlib import Path 
DIR = Path(__file__).parent 

import numpy as np

class Segment:
    def __init__(self, x:int, y_start:int, y_end:int):
        self.x = x
        self.y_start = y_start
        self.y_end = y_end

def mark_grid(A:list, xs:list, ys:list) -> np.ndarray:
    # pre: xs and ys have been sorted in ascending order 
    # post: grid[row][col] = 1 iff rect(xs[row], xs[row+1], ys[col], ys[col+1]) is inside loop
    grid_H = len(ys) - 1
    grid_W = len(xs) - 1
    grid = np.zeros((grid_H, grid_W))
    vertical_segments = []
    for i in range(len(A)):
        p1 = A[i]
        p2 = A[(i+1) % len(A)]
        if p1[0] == p2[0]:
            vertical_segments.append(Segment(p1[0], min(p1[1],p2[1]), max(p1[1],p2[1])))
    for row in range(grid_H):
        y_mid = (ys[row+1] + ys[row]) / 2
        crossing_x_coords = []
        for seg in vertical_segments:
            if seg.y_start <= y_mid <= seg.y_end:
                crossing_x_coords.append(seg.x)
        sorted_x = sorted(crossing_x_coords)
        for k in range(0, len(sorted_x)-1, 2):
            x_start = sorted_x[k]
            x_end = sorted_x[k+1]
            col_start = xs.index(x_start)
            col_end = xs.index(x_end)
            for col in range(col_start, col_end):
                grid[row][col] = 1
    return grid 

def compute_2D_prefix_sum(grid:np.ndarray) -> np.ndarray:
    H = grid.shape[0]
    W = grid.shape[1]
    S = np.zeros((H+1, W+1))
    for r in range(1, H+1):
        for c in range(1, W+1):
            S[r][c] = grid[r-1][c-1] + S[r][c-1] + S[r-1][c] - S[r-1][c-1]
    return S 

def get_sum(S:np.ndarray, r1:int, r2:int, c1:int, c2:int) -> int:
    return S[r2+1][c2+1] - S[r1][c2+1] - S[r2+1][c1] + S[r1][c1]

def rect_inside_loop(x1:int, y1:int, x2:int, y2:int, is_adj:bool, prefix_sum:np.ndarray, xs:list, ys:list) -> bool:
    # pre: x2>=x1; y2>=y1; xs and ys are sorted in ascending order
    ix1, ix2 = xs.index(x1), xs.index(x2)
    iy1, iy2 = ys.index(y1), ys.index(y2)
    if (ix1 == ix2 == len(xs)-1) or (iy1 == iy2 == len(ys)-1) or (ix1 == ix2 == 0) or (iy1 == iy2 == 0):
        return True if is_adj else False 
    if ix2 > ix1:
        ix2 -= 1
    if iy2 > iy1:
        iy2 -= 1
    expected_cells = (ix2 - ix1 + 1) * (iy2 - iy1 + 1)
    actual_cells = get_sum(prefix_sum, iy1, iy2, ix1, ix2)
    return expected_cells == actual_cells 

def search(A:list) -> float:
    xs, ys = set(), set()
    for x, y in A:
        xs.add(x)
        ys.add(y)
    xs = sorted(xs)
    ys = sorted(ys)
    grid = mark_grid(A, xs, ys)
    prefix_sum = compute_2D_prefix_sum(grid)
    best_area = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            xi, yi = A[i]
            xj, yj = A[j]
            x1, x2 = min(xi,xj), max(xi, xj)
            y1, y2 = min(yi,yj), max(yi, yj)
            if rect_inside_loop(x1, y1, x2, y2, (j-i)==1 or (i==0 and j==len(A)-1), prefix_sum, xs, ys):
                area = (x2-x1+1) * (y2-y1+1)
                best_area = max(best_area, area)
    return best_area 

def parse_input(input:str) -> float:
    coords = input.split('\n') # ["189,275", ...]
    coords = [w.split(',') for w in coords] # [['189', '275'], ...]
    coords = [[int(w) for w in u] for u in coords]
    return search(coords)

def main():
    with open(DIR/"document.txt", 'r') as f:
        input = f.read()
    ans = parse_input(input)
    print("Final answer = ", ans)

if __name__ == '__main__':
    main() 