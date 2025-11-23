import networkx as nx

class CSASynthesizer:
    def build(self, subsystems):
        G = nx.DiGraph()

        for idx, s in enumerate(subsystems):
            G.add_node(idx, **s)

        # naïve transitions: allow switching if stability is satisfied
        for i in G.nodes:
            for j in G.nodes:
                if i != j:
                    G.add_edge(i, j, guard=lambda t, mdadt=0: t >= mdadt)

        return G
