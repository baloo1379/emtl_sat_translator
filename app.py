from src.bee import compile_and_solve, compile_and_save
from src.graph import Graph
from src.sol_to_dot import sol_to_dot
import click


def run(input_file):
    gr = Graph(input_file)
    filename = gr.save_file()
    compile_and_solve(filename)
    graph_name = 'A'
    sol_to_dot(filename, graph_name)

if __name__ == '__main__':
    run('test.dot')
