import collections
import numpy as np

def nfish(days):
    c = collections.Counter([eval(x)for x in open('input.txt')][0])
    for day in range(days-1):
        c2=collections.Counter()
        for k,v in c.items():
            if k==0:
                k=7
            elif k==1:
                c2[9]+=v
            c2[k-1]+=v
        c=c2
    print(sum(c.values()))

def part_one():
    return nfish(80)

def part_two():
    return nfish(256)

print(part_one())
print(part_two())
