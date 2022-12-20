import fileinput
import treelib

currentNode = None

AVAILABLE = 70000000
UPDATESIZE = 30000000

class FilesystemElement:
    def __init__(self, obj_type, size):
        self.obj_type = obj_type
        self.size = size
    def update_size(self, update):
        self.size += update

filesystem = treelib.Tree()

filesystem.create_node("/", "/", data=FilesystemElement("dir", 0))

def cd(command):
    global currentNode
    if command == "..":
        currentNode = filesystem.get_node(currentNode.bpointer)
    elif command == "/":
        currentNode = filesystem.get_node("/")
    else:
        identifier = currentNode.identifier + "_" + command
        if identifier in currentNode.fpointer:
            currentNode = filesystem.get_node(identifier)

def add_directory(properties):
    # create unique name with parent node _ new dir
    identifier = currentNode.identifier + "_" + properties
    node = treelib.Node(properties, identifier, data=FilesystemElement("dir", 0))
    filesystem.add_node(node, currentNode)

def add_file(properties):
    size, name = properties.split(" ")
    identifier = currentNode.identifier + "_" + name
    size = int(size)
    node = treelib.Node(name, identifier, data=FilesystemElement("file", size))
    filesystem.add_node(node, currentNode)
    update_tree(size)

def update_tree(size):
    currentNode.data.update_size(size)
    tempNode = currentNode
    while not tempNode.is_root():
        tempNode = filesystem.get_node(tempNode.bpointer)
        tempNode.data.update_size(size)

def sum_of_dir_smaller100000(tree_list):
    sum = 0
    for i in tree_list:
        if i.data.obj_type == "dir" and i.data.size < 100000:
            sum += i.data.size

    return sum

def find_appropriate_dir(tree_list, clear):
    temp = filesystem.get_node("/").data.size
    for i in tree_list:
        size = i.data.size
        if i.data.obj_type == "dir" and size > clear and size < temp:
            temp = size
    return temp



for line in fileinput.input("/home/gus/python/aoc-22/day7/input.txt"):
    line = line.rstrip()
    if line[0:4] == "$ cd":
        cd(line[5:])
    elif line[0:4] == "$ ls":
        ...
    elif line[0:3] == "dir":
        add_directory(line[4:])
    else:
        add_file(line)

filesystem.show(idhidden= False, data_property="size")

print(sum_of_dir_smaller100000(filesystem.all_nodes()))

used = filesystem.get_node("/").data.size
free = AVAILABLE - used
need = UPDATESIZE - free
print(f"space free:{free}")
print(f"need {need}")

print(f"Clear directory of size {find_appropriate_dir(filesystem.all_nodes(), need)}")


