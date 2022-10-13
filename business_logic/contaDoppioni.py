import os



ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def read_from_file_and_place_in_list(path):
    lines = []
    with open(path) as f:
        for line in f.readlines():
            if line != '\n':
                lines.append(line)

    return lines

if __name__ == '__main__':
    nodes = read_from_file_and_place_in_list(ROOT_DIR+'/all-nodes.txt')
    res = {}

    for key in nodes:
        if(nodes.count(key)>1):
         res[key.split(';')[0]] = nodes.count(key)

    print(res)


