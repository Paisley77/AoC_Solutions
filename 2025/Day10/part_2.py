from pathlib import Path 
DIR = Path(__file__).parent 

import numpy as np
import re 
from typing import Tuple 
from scipy.optimize import milp, LinearConstraint, Bounds

class ILPSolver:
    def __init__(self, A: np.ndarray, b: np.ndarray):
        self.A = A 
        self.b = b
        self.num_counters = len(A)
        self.num_buttons = A.shape[1]
        self.c = np.ones(self.num_buttons, dtype=int)

    def solve(self) -> int:
        constraints = LinearConstraint(self.A, self.b, self.b)
        bounds = Bounds(0, np.inf)
        integrality = np.ones_like(self.c)
        ans = milp(c=self.c, constraints=constraints, bounds=bounds, integrality=integrality)
        return ans.x.sum()
    
    
def build_indicator_matrix(buttons: list) -> np.ndarray:
    num_counters = max(max(btn) for btn in buttons) + 1 
    num_buttons = len(buttons)
    A = np.zeros((num_counters, num_buttons), dtype=int)
    for btn_idx, btn in enumerate(buttons):
        for cntr in btn:
            A[cntr][btn_idx] = 1 
    return A 

def parse_line(line:str) -> Tuple:
    """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"""
    diagram = re.search(r'\[(.*?)\]', line).group(1)
    buttons = re.findall(r'\((.*?)\)', line)
    buttons = [[int(w) for w in btn.split(',')] for btn in buttons]
    joltage = re.search(r'\{(.*?)\}', line).group(1)
    joltage = [int(x) for x in joltage.split(',')]
    return diagram, buttons, joltage 

def solve_line(line: str) -> int:
    diagram, buttons, joltage = parse_line(line)
    A = build_indicator_matrix(buttons)
    b = np.array(joltage, dtype=int)
    solver = ILPSolver(A, b)
    return solver.solve() 

def solve(input: str) -> int:
    lines = input.split('\n')
    total_count = 0
    for line in lines:
        total_count += solve_line(line)
    return total_count

def main():
    with open(DIR / 'document.txt', 'r') as f:
        input = f.read() 
    ans = solve(input)
    print("Final answer = ", ans)

if __name__ == '__main__':
    main()