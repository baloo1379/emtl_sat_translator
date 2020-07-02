from src.bee import compile_and_solve, compile_and_save
from src.graph import Graph
from src.sol_to_dot import sol_to_dot, create_png_from_dot
import argparse


def run(input_file, save=False, image=False):
    graph = Graph(input_file)
    filename = graph.save_file()
    if save:
        compile_and_save(filename)
        print(f"Files {filename}.ctf and {filename}.map have been created")
        return
    compile_and_solve(filename)
    result = sol_to_dot(filename)
    print(f"File {result} has been created")
    if image:
        create_png_from_dot(result, filename)
        print(f"File {filename}.png has been created")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='emtl_sat_translator')
    parser.add_argument('filename', metavar='F', type=str,
                        help='a graph file in DOT format (Graphviz)')
    parser.add_argument('-s', '--save', action='store_true',
                        help="save CTF formulas to files instead of solving")
    parser.add_argument('-i', '--save-image', action='store_true', dest='save_image',
                        help="save solved graph to png image (takes no effect while -s is set)")

    args = parser.parse_args()

    if args.save and args.save_image:
        print("Cannot save image while saving CTF formulas")
    else:
        run(args.filename, args.save, args.save_image)
