with open('input.txt') as f:
    data = f.read().split('\n')

data = [str(d).split(' ') for d in data]


#print(data)

def part_1(data):
    horizontal = 0
    dept = 0
    for movement_data in data:
        if movement_data[0] == 'forward':
            horizontal += int(movement_data[1])
            #print(horizontal)
        elif movement_data[0] == 'down':
            dept += int(movement_data[1])
            #print(dept)
        elif movement_data[0] == 'up':
            dept -= int(movement_data[1])
            #print(dept)

    return horizontal * dept


def part_2(data):
    horizontal = 0
    dept = 0
    aim = 0
    for movement_data in data:
        if movement_data[0] == 'forward':
            horizontal += int(movement_data[1])
            dept += int(movement_data[1]) * aim
            #print(horizontal)
        elif movement_data[0] == 'down':
            aim += int(movement_data[1])
            #print(dept)
        elif movement_data[0] == 'up':
            aim -= int(movement_data[1])
            #print(dept)
            
    return horizontal * dept

print(part_1(data))
print(part_2(data))


