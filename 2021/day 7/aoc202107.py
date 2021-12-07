# aoc_template.py
'''
Note : this template was created during day 7 2021,
so some days may not use this template
'''
import pathlib
import sys
def nFuel(data,add_fuel = False):
    fuel = []
    current_fuel = 0
    possible_alingn = list(range(0,max(data) + 1))
    #print(possible_alingn)
    for pos in possible_alingn:
        current_fuel = 0
        for crab_pos in data:
            #print((pos,crab_pos))
            if pos < crab_pos:
                if not add_fuel:
                    current_fuel += crab_pos - pos
                    #print((pos,crab_pos,crab_pos - pos))
                else:
                     
                     range_needed = crab_pos - pos
                     current_fuel += sum(range(1,range_needed + 1))
                
            else:
                if not add_fuel:
                    current_fuel += pos - crab_pos
                else:
                    range_needed = pos - crab_pos
                    current_fuel += sum(range(1,range_needed + 1))
                    
                #print((pos,crab_pos,pos - crab_pos))
                
        #print(current_fuel)
                
        fuel.append(current_fuel)
    
    #print(min(fuel))
    #print(fuel)
    return min(fuel)

def parse(puzzle_input):
    """Parse input"""
    return [int(data) for data in puzzle_input.split(',')]

def part1(data):
    """Solve part 1"""
    return nFuel(data)
        


    

def part2(data):
    """Solve part 2"""
    return nFuel(data,True)
    

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
