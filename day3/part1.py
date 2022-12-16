#!/usr/bin/python3
import fileinput
from string import ascii_letters


sum_of_priorities = 0
for line in fileinput.input('/home/gus/python/advent_of_code_22/day3/input.txt'):
    compartment1 = line[:len(line)//2].rstrip()
    compartment2 = line[len(line)//2:].rstrip()

    same = set(compartment1) & set(compartment2)
    sum_of_priorities += ascii_letters.index(same.pop())+1

print(sum_of_priorities)

