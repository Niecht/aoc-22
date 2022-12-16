
top_three = [0] * 3

def check_if_t3(elf_cal):
    pos = -1
    for i in top_three:
        if elf_cal < i:
            break
        else:
            pos += 1

    if pos >= 0:
        insert(elf_cal, pos)

def insert(elf_cal, pos):
    temp = elf_cal
    for i in range(pos, -1, -1):
        lower = top_three[i]
        top_three[i] = temp
        temp = lower



def main():
    elf_cal = 0
    while True:
        x = input()
        if x == "i":
            print(f"Maximus is {top_three[2]}")
            print(f"Top three is {top_three} and elf_cal is {top_three[0] + top_three[1] + top_three[2]}")
        elif x != "":
            elf_cal += int(x)
        else:
            check_if_t3(elf_cal)
            elf_cal = 0

if __name__ == "__main__":
    main()
    