from pathlib import Path
DIR = Path(__file__).parent 

import numpy as np
from collections import defaultdict

k = 1000

def BFS(graph: dict) -> list:
    classes = []
    visited = []
    while graph:
        component = []
        queue = []
        v0 = next(iter(graph))
        queue.append(v0)
        visited.append(v0)
        visited.sort()
        while queue:
            v0 = queue.pop(0)
            component.append(v0)
            for v in graph[v0]:
                if not v in visited:
                    queue.append(v)
                    visited.append(v)
                    visited.sort() 
            del graph[v0]
        classes.append(component)
    classes.sort(key=len, reverse=True)
    return classes 

def createGraph(points:np.ndarray) -> dict:
    # create distance matrix
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
    # extract first k and sort by first element
    pairs = pairs[:k]
    pairs.sort(key=lambda x : x[0])
    # create graph
    graph = defaultdict(list)
    for u,v in pairs:
        graph[u].append(v)
        graph[v].append(u)
    return graph 

def parseInput(input:str) -> int:
    points = input.split('\n')
    points = [coord.split(',') for coord in points]
    points = [[int(w) for w in coord] for coord in points]
    points = np.array(points)
    graph = createGraph(points)
    classes = BFS(graph)
    numClasses = len(classes)
    prod = 1 
    for i in range(min(3,numClasses)):
        prod *= len(classes[i])
    return prod 

def eucDist(p1:np.ndarray, p2:np.ndarray):
    return np.linalg.norm(p1-p2)

def main():
    with open(DIR/"document.txt", 'r') as f:
        input = f.read()
    ans = parseInput(input)
    print("Final answer = ", ans)

if __name__ == '__main__':
    main() 