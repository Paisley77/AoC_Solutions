from pathlib import Path
DIR = Path(__file__).parent

import numpy as np

def parse_input(input:str) -> int:
    lines = input.split('\n')
    table = [[int(w) for w in line.split()] for line in lines[:-1]]
    table = np.array(table)
    operators = np.array(lines[-1].split())
    sum_mask = operators == '+'
    prod_mask = operators == '*'
    ans = np.zeros(table.shape[1])
    ans[sum_mask] = table[:, sum_mask].sum(axis=0)
    ans[prod_mask] = table[:, prod_mask].prod(axis=0)
    return ans.sum()

def main():
    with open(DIR / 'document.txt', 'r') as f:
        input = f.read() 
    ans = parse_input(input)
    print("Final answer = ", ans)

if __name__ == '__main__':
    main() 