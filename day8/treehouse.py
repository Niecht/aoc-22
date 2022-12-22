import fileinput
import numpy as np

def read_file_to_lines(inputfile):
    lines = []
    for line in fileinput.input(inputfile):
        lines.append(line.rstrip())
    return lines

def create_2d_array(inputfile):
    forest = np.zeros([len(inputfile), len(inputfile[0])])
    y_index = 0
    for line in inputfile:
        x_index = 0
        for i in line:
            forest[y_index][x_index] = i
            x_index += 1
        y_index += 1
    return forest

def get_visible_trees(forest):
    visible = np.full(forest.shape, True)
    visible[1:-1,1:-1] = False

    # from top
    for y in range(len(forest)):
        for x in range(len(forest[y])):
            #print(forest[y][:x])
            #print(forest[y][x])
            #print(forest[y][x+1:])
            back = any(tree >= forest[y][x] for tree in forest[y][x+1:])
            front = any(tree >= forest[y][x] for tree in forest[y][:x])
            #print(f"higher trees before = {front}, higher trees after = {back}")
            if any(tree >= forest[y][x] for tree in forest[y][:x]) and any(tree >= forest[y][x] for tree in forest[y][x+1:]):
                continue
            else:
                visible[y][x] = True

    # from left
    flip_forest = forest.T
    for y in range(len(flip_forest)):
        for x in range(len(flip_forest[y])):
            #print(flip_forest[y][:x])
            #print(flip_forest[y][x])
            #print(flip_forest[y][x+1:])
            back = any(tree >= flip_forest[y][x] for tree in flip_forest[y][x+1:])
            front = any(tree >= flip_forest[y][x] for tree in flip_forest[y][:x])
            #print(f"higher trees before = {front}, higher trees after = {back}")
            if any(tree >= flip_forest[y][x] for tree in flip_forest[y][:x]) and any(tree >= flip_forest[y][x] for tree in flip_forest[y][x+1:]):
                continue
            else:
                visible.T[y][x] = True

    return visible


def calculate_scenic_score(forest):
    sceneScore = np.zeros(forest.shape)
    # ignore edges
    for y in range(1, len(forest)-1):
        for x in range(1, len(forest[y])-1):
            right = 0
            walker = x + 1
            while walker < len(forest[y]):
                if forest[y][walker] < forest[y][x]:
                    right += 1
                    walker += 1
                else:
                    right += 1
                    break

            left = 0
            walker = x - 1
            while walker > -1:
                if forest[y][walker] < forest[y][x]:
                    left += 1
                    walker -= 1
                else:
                    left += 1
                    break

            up = 0
            walker = y - 1
            while walker > -1:
                if forest[walker][x] < forest[y][x]:
                    up += 1
                    walker -= 1
                else:
                    up += 1
                    break

            down = 0
            walker = y + 1
            while walker < len(forest):
                if forest[walker][x] < forest[y][x]:
                    down += 1
                    walker += 1
                else:
                    down += 1
                    break
            
            sceneScore[y][x] = up * down * left * right
    return sceneScore


lines = read_file_to_lines("/home/gus/python/aoc-22/day8/input.txt")
matrix = create_2d_array(lines)
visible = get_visible_trees(matrix)

scenic_score = calculate_scenic_score(matrix)

print(f"amount of visible trees: {np.count_nonzero(visible == True)}")
print(f"most scenic tree: {int(scenic_score.max())}")