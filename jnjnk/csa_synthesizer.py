import networkx as nx

class CSASynthesizer:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_state(self, name, period, skips, mdadt):
        self.graph.add_node(name, period=period, skips=skips, mdadt=mdadt)

    def add_transition(self, src, dest, guard_fn):
        self.graph.add_edge(src, dest, guard=guard_fn)

    def generate_acess_library(self, depth=5):
        sequences = []
        for path in nx.all_simple_paths(self.graph, source='start', target='end', cutoff=depth):
            sequences.append(path)
        return sequences
