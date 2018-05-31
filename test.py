#%%
import networkx as nx
import matplotlib.pyplot as plt
def read_graph(in_file):
    """ Read in the graph from the data file.  The graph is stored
    as a dictionary, where the keys are the nodes, and the values
    are a list of pairs (d, c), where d is a node and c is a number.
    If (d, c) is in the list for node n, then d can be reached from
    n at cost c.
    """
    graph = {}
    infile = open(in_file)
    for line in infile:
        elements = line.split(',')
        node = elements.pop(0)
        graph[node] = []
        if node != 'node99':
            for element in elements:
                destination, cost = element.split()
                graph[node].append((destination, float(cost)))
    infile.close()
    return graph

graph = read_graph('06-Dynamic-Programming/graph.txt')
G = nx.Graph()

graph

G.add_nodes_from([*graph])

G


down vote
import networkx as nx
import matplotlib.pyplot as plt

G=nx.cycle_graph(10)
nx.draw(G)
plt.show()
