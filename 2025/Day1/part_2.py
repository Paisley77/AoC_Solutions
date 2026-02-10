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
            raw_pos = pos - steps
            count += (-(raw_pos//100))
            if raw_pos % 100 == 0:
                count += 1
            if pos == 0:
                count -= 1 
        else:
            raw_pos = pos + steps
            count += (raw_pos//100)
        pos = raw_pos % 100 
    return count 

def main():
    with open(DIR / 'document.txt', 'r') as f:
        textstr = f.read()
    print(solve_puzzle(textstr))

if __name__ == '__main__':
    main() 