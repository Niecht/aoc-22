#!/usr/bin/python3
from enum import IntEnum

class Score(IntEnum):
    X = 1 # Rock
    Y = 2 # Paper
    Z = 3 # Scissors
    LOSS = 0
    TIE = 3
    WIN = 6

def read_lines_to_list(f):
    lines = []
    with open(f) as intake:
        for line in intake:
            lines.append(line.strip("\n"))
    return lines

def calc_points(battle):
    #ROCK
    if battle == "A X":
        return Score.LOSS + Score.Z
    elif battle == "A Y":
        return Score.TIE + Score.X
    elif battle =="A Z":
        return Score.WIN + Score.Y
    #PAPER
    elif battle =="B X":
        return Score.LOSS + Score.X
    elif battle =="B Y":
        return Score.TIE + Score.Y
    elif battle =="B Z":
        return Score.WIN + Score.Z
    #Scissors
    elif battle =="C X":
        return Score.LOSS + Score.Y
    elif battle =="C Y":
        return Score.TIE + Score.Z
    elif battle =="C Z":
        return Score.WIN + Score.X

def main():
    lines = read_lines_to_list("input.txt")
    total_score = 0
    for battle in lines:
        total_score += calc_points(battle)
        print(total_score)


if __name__ == "__main__":
    main()
    
        


    