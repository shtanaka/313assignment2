import utils


class DistanceVector:
    INF = 1234567

    def __init__(self, network):
        self.network = network
        self.num_transmissions = []
        for i in range(0, network.size):
            self.num_transmissions.append(0)
        self.paths = []
        self.what_sees = [[]]
        self.shortest_paths = []
        self.avg_shortest_paths = 0.0
        self.avg_num_transmissions = 0.0
        self.create_paths()

    def create_paths(self):
        for origin in range(0, self.network.size):
            self.shortest_paths.append(self.init_shortest_path(origin))
        for origin in range(0, self.network.size):
            self.shortest_paths[origin] = self.ask_neighbor(origin, self.shortest_paths[origin])
        for origin in range(0, self.network.size):

            k = []
            for i in self.shortest_paths[origin]:
                k.append(i)
            while self.INF in self.shortest_paths[origin]:
                self.shortest_paths[origin] = self.ask_neighbor(
                        origin,
                        self.shortest_paths[origin],
                        utils.get_max(k))
                k[utils.get_max(k)] = self.INF
                all_inf = True
                for i in k:
                    if i < self.INF:
                        all_inf = False
                if all_inf:
                    k = []
                    for i in self.shortest_paths[origin]:
                        k.append(i)

        for i in self.num_transmissions:
            self.avg_num_transmissions += i
        self.avg_num_transmissions /= len(self.num_transmissions)
        count = 0
        for i in self.shortest_paths:
            for j in i:
                count += 1
                self.avg_shortest_paths += j
        self.avg_shortest_paths /= count

    def init_shortest_path(self, origin):
        shortest_path = []
        for i in range(0, self.network.size):
            if i == origin:
                shortest_path.append(0)
            elif i in self.network.adjacency[origin]:
                shortest_path.append(1)
            else:
                shortest_path.append(self.INF)
        return shortest_path

    def ask_neighbor(self, origin, shortest_path, point=None):
        if point is None:
            point = origin
        for neighbor in self.network.adjacency[point]:
            self.num_transmissions[origin] += 1
            for neighbor_of_neighbor in self.network.adjacency[neighbor]:
                if shortest_path[neighbor_of_neighbor] >= shortest_path[neighbor] + 1:
                    shortest_path[neighbor_of_neighbor] = shortest_path[neighbor] + 1
        return shortest_path

    def __str__(self):
        msg = " ==== DISTANCE VECTOR ==== \n"
        msg += "Average number of transmissions: "
        msg += str(self.avg_num_transmissions)
        msg += "\nAverage shortest paths length: "
        msg += str(self.avg_shortest_paths)
        msg += "\n"
        return msg
