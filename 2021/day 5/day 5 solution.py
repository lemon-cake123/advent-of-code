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
##with open('input.txt') as f:
##    raw_data = f.read().strip().split('\n')
##
##
###print(raw_data)
##data = [d.split(' -> ') for d in raw_data]
###print(data)
##data = [[c[0].split(',') for c in data],[c[1].split(',') for c in data]]
###print(data)
##test_data = """
##0,9 -> 5,9
##8,0 -> 0,8
##9,4 -> 3,4
##2,2 -> 2,1
##7,0 -> 7,4
##6,4 -> 2,0
##0,9 -> 2,9
##3,4 -> 1,4
##0,0 -> 8,8
##5,5 -> 8,2"""
##test_data = test_data.strip().split('\n')
##test_data = [d.split(' -> ') for d in test_data]
###print(data)
##test_data = [[c[0].split(',') for c in test_data],[c[1].split(',') for c in test_data]]
##def part_1(data):
##    beginning_coords,ending_coords = data[0],data[1]
##    beginning_x_coords = beginning_y_coords=ending_x_coords=ending_y_coords = []
##    for x,y in beginning_coords:
##        beginning_x_coords.append(x)
##        beginning_y_coords.append(y)
##        
##    for x,y in ending_coords:
##        ending_x_coords.append(x)
##        ending_y_coords.append(y)
##
##    for i in range(len(beginning_x_coords)):
##        if beginning_x_coords[i] != ending_x_coords[i]:
##            if beginning_y_coords[i] != ending_y_coords[i]:
##                print('popped')
##                beginning_x_coords.pop(i)
##                beginning_y_coords.pop(i)
##                ending_x_coords.pop(i)
##                ending_y_coords.pop(i)
##            
##    covered_x_coords = []
##    covered_y_coords = []
##    overlap = 0
##    for i in range(len(ending_coords)):
##        x = beginning_x_coords[i]
##        
##        if x in covered_x_coords:
##                overlap += 1
##                
##        covered_x_coords.append(x)
##        
##            
##    
##    for i in range(len(ending_coords)):
##        y = beginning_y_coords[i]
##        
##        if y in covered_y_coords:
##                overlap += 1
##                
##        covered_y_coords.append(y)
##
##    return overlap
##
##print(part_1(test_data))
