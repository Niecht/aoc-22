import fileinput

def read_input(file):
    line = fileinput.input(file).readline()
    return line

def find_comm_4char_package(datastream):
    startOfPacket = False

    for i in range(0, len(datastream)):
        if (datastream[i] in datastream[i+1:i+4] or
            datastream[i+1] in datastream[i+2:i+4] or
            datastream[i+1] in datastream[i] or
            datastream[i+2] in datastream[i+3] or
            datastream[i+2] in datastream[i:i+2] or
            datastream[i+3] in datastream[i:i+3]
            ):
            startOfPacket = False
        else:
            startOfPacket = True
            break

    if startOfPacket:
        return i+4
    else:
        return -1

def find_comm_14char_package(datastream):
    startOfPacket = False
    for i in range(0, len(datastream)):
        block = datastream[i:i+14]
        checker = set(block)
        #print(f"block is {block} with lenght {len(checker)} with index {i}")
        if len(checker) == 14:
            startOfPacket = True
            break
    
    if startOfPacket:
        return i+14
    else:
        return -1



datastream = read_input("/home/gus/python/aoc-22/day6/input.txt")
print(find_comm_14char_package(datastream))