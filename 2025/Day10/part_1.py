from pathlib import Path 
DIR = Path(__file__).parent 

import re 

def twoPassBFS(target:int, buttons:list) -> int:
    if target == 0:
        return 0 
    forward_visited = {0:0}
    backward_visited = {target:0}
    forward_queue = [0]
    backward_queue = [target]
    steps = 0
    while forward_queue and backward_queue:
        steps +=1 
        new_forward_queue = []
        for current_state in forward_queue:
            for btn in buttons:
                next_state = current_state ^ btn 
                if next_state not in forward_visited:
                    if next_state in backward_visited:
                        return steps + backward_visited[next_state]
                    forward_visited[next_state] = steps 
                    new_forward_queue.append(next_state)
        forward_queue = new_forward_queue
        new_backward_queue = []
        for current_state in backward_queue:
            for btn in buttons:
                next_state = current_state ^ btn 
                if next_state not in backward_visited:
                    if next_state in forward_visited:
                        return steps + forward_visited[next_state]
                    backward_visited[next_state] = steps 
                    new_backward_queue.append(next_state)
        backward_queue = new_backward_queue
    return -1 

def btnBitmask(btnWire:list, size:int) -> int:
    bitmask = 0
    for idx in btnWire:
        bitmask |= (1 << (size-1-idx))
    return bitmask 

def tgtBitmask(targetstr:str) -> int:
    targetls = [1 if w=='#' else 0 for w in targetstr]
    bitmask = 0
    for bit in targetls:
        bitmask = (bitmask << 1) | bit 
    return bitmask 

def parseFactoryLine(line:str) -> tuple:
    diagram = re.search(r'\[(.*?)\]', line).group(1)
    buttons = re.findall(r'\((.*?)\)', line)
    buttons = [[int(w) for w in btn.split(',')] for btn in buttons]
    joltage = re.search(r'\{(.*?)\}', line).group(1)
    joltage = [int(x) for x in joltage.split(',')]
    return diagram, buttons, joltage

def parseInput(input:str) -> int:
    lines = input.split('\n')
    count = 0
    for line in lines:
        diagram, buttons, joltage = parseFactoryLine(line)
        target_mask = tgtBitmask(diagram)
        button_masks = [btnBitmask(btn, len(diagram)) for btn in buttons]
        count += twoPassBFS(target_mask, button_masks)
    return count 

def main():
    with open(DIR / 'document.txt', 'r') as f:
        input = f.read() 
    ans = parseInput(input)
    print("Final answer = ", ans)

if __name__ == '__main__':
    main()
    