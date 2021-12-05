import re
from collections import defaultdict

def sign(n):
    return (1 if n > 0 else -1) if n else 0

def solve(part=1):
    with open('input.txt') as file:
        data = [list(map(int, re.findall('\d+', line))) for line in file]

    grid = defaultdict(int)
    for x1, y1, x2, y2 in data:
        dx, dy = sign(x2 - x1), sign(y2 - y1)
        if part == 1:
            if dx and dy: continue  # comment this line out and rerun to solve part 2
        
        x, y = x1, y1
        while x != x2 or y != y2:
            grid[(x, y)] += 1
            x += dx
            y += dy
        grid[(x2, y2)] += 1

    return sum(count > 1 for count in grid.values())

print(solve())
print(solve(2))

