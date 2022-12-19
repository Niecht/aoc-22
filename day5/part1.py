#! /bin/python

import fileinput

def read_stacks(stack_file):
    # create empty stack with correct dimensions
    stacks = []

    # create correct ammount of stacks
    for i in range(0, int(stack_file[-1][-1])):
        stacks.append([])

    # add items to stacks bottom up
    for i in range(len(stack_file)-2, -1, -1):
        for j in range(0, len(stack_file[i]), 4):
            item = stack_file[i][j+1]
            # if item is not a space
            if item != " ":
                stacks[j//4].append(item)
    return stacks

def read_moves(instructions):
    moves_array = []
    for i in range( 0, len(instructions)):
        split_string = instructions[i].split(" ")
        moves_array.append([int(split_string[1]), int(split_string[3]), int(split_string[5])])
    return moves_array

def read_input(file):
    lines = []
    for line in fileinput.input(file):
        lines.append(line.rstrip())
    # split stack from instructions
    stacks = lines[0:lines.index("")]
    instuctions = lines[lines.index("")+1:]
    return stacks, instuctions

def perfom_move_on_stack(amount, origin, target, stack):
    for i in range(0, amount):
        stack[target].append(stack[origin].pop())

    return stack

def get_top_of_stacks_string(stacks):
    tops = ""
    for i in stacks:
        tops += i[-1]

    return tops 


stacks, instructions =read_input("/home/gus/python/aoc-22/day5/input.txt")
stacks = read_stacks(stacks)
moves_array = read_moves(instructions)

for i in moves_array:
    stacks = perfom_move_on_stack(i[0], i[1]-1, i[2]-1, stacks)


print(get_top_of_stacks_string(stacks))
