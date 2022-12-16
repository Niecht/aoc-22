#! /bin/python3

import fileinput

def range_to_set(intake):
    range_list = set()
    intake = intake.split("-")
    for i in range(int(intake[0]),int(intake[-1])+1):
        range_list.add(i)
    return range_list

def check_subset(part1, part2):
    if part1.issubset(part2) or part2.issubset(part1):
        return True
    else:
        return False

def check_contained(part1, part2):
    if part1 & part2:
        return True
    else:
        return False

contained = 0
for line in fileinput.input("/home/gus/python/advent_of_code_22/day4/input.txt"):
    elfs = line.rstrip().split(",")

    area_elf1 = range_to_set(elfs[0])
    area_elf2 = range_to_set(elfs[1])

    if check_contained(area_elf1, area_elf2):
        contained += 1

print(contained)
