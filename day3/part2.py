#!/usr/bin/python3
import fileinput
from string import ascii_letters


sum_of_priorities = 0

def read_lines_to_list(f):
    lines = []
    with open(f) as intake:
        for line in intake:
            lines.append(line.strip("\n"))
    return lines

backpacks = read_lines_to_list('/home/gus/python/advent_of_code_22/day3/test.txt')
   
for group in range(0, len(backpacks), 3):
    backpack1 = backpacks[group].rstrip()
    backpack2 = backpacks[group+1].rstrip()
    backpack3 = backpacks[group+2].rstrip()

    same = set(backpack1) & set(backpack2) & set(backpack3)
    sum_of_priorities += ascii_letters.index(same.pop())+1

print(sum_of_priorities)

