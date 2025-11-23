import itertools

class ACESSLibrary:
    def __init__(self, csa_graph):
        self.G = csa_graph

    def generate(self, max_len=5):
        sequences = []

        for start in self.G.nodes:
            paths = itertools.product(self.G.nodes, repeat=max_len)
            for p in paths:
                sequences.append(p)

        return sequences
