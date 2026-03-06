from pathlib import Path 
DIR = Path(__file__).parent

from itertools import groupby
import math

def parse_input(input:str):
    rows = input.split("\n")
    cols = ["".join(col) for col in zip(*rows[:-1])]
    problems = []
    for active, group in groupby(cols, key = lambda x : x.strip() != ''):
        if active:
            problems.append(list(group))
    operators = rows[-1].split()
    total = 0 
    for p, o in zip(problems, operators):
        nums = [int(w.strip()) for w in p]
        if o == '+':
            total += sum(nums)
        else:
            total += math.prod(nums)
    return total 


def main():
    with open(DIR / "document.txt", 'r') as f:
        input = f.read()
    ans = parse_input(input)
    print("Final answer = ", ans)

if __name__ == "__main__":
    main() 