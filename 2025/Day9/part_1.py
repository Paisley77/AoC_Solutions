from pathlib import Path
DIR = Path(__file__).parent 

import time

def compute_area(i:int, j:int) -> int:
    x1, y1 = coords[i]
    x2, y2 = coords[j]
    return (abs(x1-x2)+1) * (abs(y1-y2)+1)

def search() -> int:
    bestArea = 0
    N = len(coords)
    for i in range(N):
        x_i = coords[i][0]
        if (x_max - x_i + 1) * max_height <= bestArea:
            break
        for j in range(N-1, i, -1):
            x_j = coords[j][0]
            if (abs(x_j - x_i)+1)*max_height <= bestArea:
                break
            area = compute_area(i,j)
            if area > bestArea:
                bestArea = area
    return bestArea

def parse_input(input:str) -> int:
    global coords, x_max, max_height
    coords = input.split('\n') # ["189,275", ...]
    coords = [w.split(',') for w in coords] # [['189', '275'], ...]
    coords = [[int(w) for w in u] for u in coords]
    coords.sort() 
    x_max = max(coords, key=lambda point: point[0])[0]
    y_max = max(coords, key=lambda point: point[1])[1]
    y_min = min(coords, key=lambda point: point[1])[1]
    max_height = y_max - y_min + 1
    return search() 

def main():
    start_time = time.perf_counter()
    with open(DIR/"document.txt", 'r') as f:
        input = f.read()
    ans = parse_input(input)
    print("Final answer = ", ans)
    end_time = time.perf_counter()
    print("Time used = ", end_time-start_time)

if __name__ == '__main__':
    main() 
