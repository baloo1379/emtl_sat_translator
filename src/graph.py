from numpy import *
import pydot


class Graph:
    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = self.filepath.split('.')[0]

        (g,) = pydot.graph_from_dot_file(self.filepath)

        # Edge object, to get source/destination use get_source()/get_destination()
        # ex. self.edges[0].get_source()
        self.edges = g.get_edges()
        # List of nodes [1,2,3] etc.
        self.nodes = self.get_node_list(g.get_node_list())
        # List of 'bee' edges [e1n2, e2n3] etc.
        self.edges_bee = []
        # List of 'bee' nodes [v1, v2, v3] etc.
        self.nodes_bee = []

    def get_edges(self):
        return self.edges

    def get_nodes(self):
        return self.nodes

    def get_node_list(self, nodes):
        arr = []
        for n in range(int(len(nodes) / 2), len(nodes)):
            node = str(nodes[n])
            arr.append(node[0])
        return arr

    # Creates predicate new_int for Node
    def create_node(self, vertex, mini, maxi):
        label = f"v{vertex}"
        self.nodes_bee.append(label)
        return f"new_int({label},{mini},{maxi})\n"

    # Creates all predicates based on class nodes
    def create_all_nodes(self, mini, maxi):
        predicates = ""
        for n in self.nodes:
            predicates += self.create_node(n, mini, maxi)
        return predicates

    # Creates predicate new_int for edge connection
    def create_edge(self, src, dest, mini, maxi):
        label = f"e{src}n{dest}"
        self.edges_bee.append(label)
        return f"new_int({label},{mini},{maxi})\n"

    # Creates all predicates for edge connection based on class edges
    def create_all_edges(self, mini, maxi):
        predicates = ""
        for edge in self.edges:
            src = edge.get_source()
            dest = edge.get_destination()
            predicates += self.create_edge(src, dest, mini, maxi)
        return predicates

    # Creates predicate new_int for constant k
    def magic_constant(self, mini, maxi):
        return f"new_int(k,{mini},{maxi})\n"

    # Creates predicate int_array_plus for node-node connection
    def int_array_plus(self, array):
        return ("int_array_plus(%s, k)" % (array)).replace("'", "")

    # Returns int_array_plus predicates for all connections
    def int_array_plus_all(self):
        predicates = ""
        self.edges.reverse()
        for e in self.edges:
            arr = self.get_node_connections(e)
            predicates += self.int_array_plus(arr) + "\n"
        return predicates

    # Returns array of all connections to single node
    def get_node_connections(self, e):
        edge_label = f"e{e.get_source()}n{e.get_destination()}"
        arr = [edge_label, f"v{e.get_source()}", f"v{e.get_destination()}"]
        return arr

    # All diff predicate
    def int_array_allDiff(self):
        self.nodes_bee.reverse()
        total = self.nodes_bee + self.edges_bee
        return f"int_array_allDiff({total})".replace("'", "")

    # Returns solve clause
    def add_solve_clause(self):
        return "solve satisfy"

    def save_file(self):
        with open(self.filename+'.bee', 'w+') as file:
            file.write(self.create_all_nodes(1, 100))
            file.write('\n')
            file.write(self.create_all_edges(1, 100))
            file.write('\n')
            file.write(self.magic_constant(1, 100))
            file.write('\n')
            file.write(self.int_array_plus_all())
            file.write('\n')
            file.write(self.int_array_allDiff())
            file.write('\n')
            file.write(self.add_solve_clause())
            return self.filename


if __name__ == '__main__':
    path = "../test.dot"
    graph = Graph(path)
    graph.save_file()
