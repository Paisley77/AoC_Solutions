from pathlib import Path 
DIR = Path(__file__).parent

def solve_puzzle(textstr:str):
    pos = 50 
    count = 0 
    lines = textstr.strip().split('\n')
    for line in lines:
        if line=='':
            continue 
        direction = line[0]
        steps = int(line[1:])
        if direction == 'L':
            pos = (pos - steps) % 100
        else:
            pos = (pos + steps) % 100 
        if pos == 0:
            count += 1
    return count 

def main():
    with open(DIR / 'document.txt', 'r') as f:
        textstr = f.read()
    print(solve_puzzle(textstr))

if __name__ == '__main__':
    main() 