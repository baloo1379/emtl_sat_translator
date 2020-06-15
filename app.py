from src.bee import compile_and_solve, compile_and_save
from src.graph import Graph
import click


def run(input_file):
    gr = Graph(input_file)
    filename = gr.save_file()
    compile_and_solve(filename)


if __name__ == '__main__':
    run('test.dot')
