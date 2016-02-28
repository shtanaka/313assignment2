class Network:

    size = 0
    adjacency = []

    def __init__(self, vector):

        self.size = int(vector[0])
        self.make_adjacency(vector)

    def make_adjacency(self, vector):
        for adj in vector[1:]:
            aux = adj.split(" ")
            neighbors = []
            for neighbor in aux:
                neighbors.append(int(neighbor))
            self.adjacency.append(neighbors)
