import heapq
import utils


class LinkState:
    INF = 1234567

    def __init__(self, network):
        self.network = network
        self.num_transmissions = []
        for i in range (0, network.size):
            self.num_transmissions.append(0)
        self.paths = []
        self.visited = []
        self.shortest_paths = []
        self.avg_shortest_paths = 0.0
        self.avg_num_transmissions = 0.0
        self.create_paths()

    def create_paths(self):
        for origin in range(0, self.network.size):
            self.shortest_paths.append(self.shortest_path(origin))
        for i in self.num_transmissions:
            self.avg_num_transmissions += i
        self.avg_num_transmissions /= len(self.num_transmissions)
        count = 0
        for i in self.shortest_paths:
            for j in i:
                count+=1
                self.avg_shortest_paths += j
        self.avg_shortest_paths /= count

    def shortest_path(self, origin):
        heap = []
        shortest_path = []
        for i in range(0, self.network.size):
            if i == origin:
                shortest_path.append(0)
                heapq.heappush(heap, (i, 0))
            else:
                shortest_path.append(self.INF)
                heapq.heappush(heap, (i, self.INF))
        while len(heap) > 0:
            u, heap = utils.get_min(heap)
            for adjacent in self.network.adjacency[u[0]]:
                if utils.is_present(heap, adjacent):
                    self.num_transmissions[origin] += 1
                    if shortest_path[adjacent] > u[1] + 1:
                        shortest_path[adjacent] = u[1] + 1
                        heap = utils.set_value(adjacent, u[1] + 1, heap)
        return shortest_path

    def __str__(self):
        msg = " ==== LINKSTATE ==== \n"
        msg += "Average number of transmissions: "
        msg += str(self.avg_num_transmissions)
        msg += "\nAverage shortest paths length: "
        msg += str(self.avg_shortest_paths)
        msg += "\n"
        return msg
