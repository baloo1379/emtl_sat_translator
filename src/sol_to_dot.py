import re
import random
import pydot

def int_generator(seed):
    random.seed(seed)
    number = str(hex(random.randint(255, 16777215))).replace('0x', '')
    while len(number) < 6:
        number = '0' + number
    value = '#' + number
    return value


def split_vertexes(vertexes):
    content = []
    for data in vertexes:
        data = data.replace('v', '').replace(' ', '')
        separated_vertexes = data.split("=")
        # print(separated_vertexes)
        text = 'node [shape=circle,style=filled,color="' + int_generator(separated_vertexes[1]) + '",label='+separated_vertexes[1]+'] ' + \
               separated_vertexes[0]
        content.append(text)
    # print(content)
    return content


def split_edges(edges):
    content = []
    for data in edges:
        data = data.replace(' ', '').replace('e', '').replace('n', ' ').replace('=', ' ')
        separated_edges = data.split(" ")
        try:
            text = separated_edges[0] + ' -- ' + separated_edges[1] + ' [label="' + \
                   separated_edges[2] + '",color="' + int_generator(
                separated_edges[2]) + '"];'
            content.append(text)
        except:
            print("Out of labels")

    return content


def save_to_file(vertexes, edges, graph_name):
    file_name = f"{graph_name}_solved.dot"
    file = open(file_name, "w")
    data = 'graph ' + graph_name + ' {\n'
    for vertex in vertexes:
        data = data + vertex + "\n"

    for edge in edges:
        data = data + edge + "\n"
    data = data + "}"

    file.write(data)
    file.close()
    return file_name


def sol_to_dot(filename):
    with open(f"{filename}.sol") as file:
        file_contents = file.read()
        # print(file_contents)
    vertexes = split_vertexes(re.findall("v[0-9]+\s=\s[0-9]+", file_contents))
    edges = split_edges(re.findall("e[0-9]n[0-9]+\s=\s[0-9]+", file_contents))
    file = save_to_file(vertexes, edges, filename)
    return file


def create_png_from_dot(dot_file, png_file="graph"):
    (g,) = pydot.graph_from_dot_file(dot_file)
    g.write_png(f"{png_file}.png")


'''if __name__ == '__main__':
    print(sol_to_dot("../test.sol", 'A'))'''

