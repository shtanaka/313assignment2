import random


class HotPotato:
    INF = 1234567

    def __init__(self, network):
        self.network = network
        self.num_transmissions = []
        for i in range(0, network.size):
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
                count += 1
                self.avg_shortest_paths += j
        self.avg_shortest_paths /= count

    last = -1

    def shortest_path(self, origin):
        shortest_path = []
        for i in range(0, self.network.size):
            if i == origin:
                shortest_path.append(0)
            else:
                shortest_path.append(self.INF)
        for destination in range(0, self.network.size):
            if destination != origin:
                self.last = origin
                shortest_path[destination] = self.find_path(origin, destination, origin)
        return shortest_path

    visited = []

    def find_path(self, origin, destination, main_origin, deeps=0):
        self.visited.append(origin)
        choice = random.choice(self.network.adjacency[origin])
        if choice == self.last and len(self.network.adjacency[origin]) > 1:
            c = choice
            while c == choice:
                choice = random.choice(self.network.adjacency[origin])
        if choice == destination:
            self.visited = []
            return deeps + 1
        else:
            if choice in self.visited:
                self.last = origin
                self.num_transmissions[main_origin] += 1
                return self.find_path(choice, destination, deeps)
            else:
                self.visited.append(choice)
                self.last = origin
                self.num_transmissions[main_origin] += 1
                deeps += 1
                return self.find_path(choice, destination, main_origin, deeps)

    def __str__(self):
        msg = " ==== HOTPOTATO 1 ==== \n"
        msg += "Average number of transmissions: "
        msg += str(self.avg_num_transmissions)
        msg += "\nAverage shortest paths length: "
        msg += str(self.avg_shortest_paths)
        msg += "\n"
        return msg


class HotPotato2:
    INF = 1234567

    def __init__(self, network):
        self.network = network
        self.num_transmissions = []
        for i in range(0, network.size):
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
                count += 1
                self.avg_shortest_paths += j
        self.avg_shortest_paths /= count

    last = -1

    def shortest_path(self, origin):
        shortest_path = []
        for i in range(0, self.network.size):
            if i == origin:
                shortest_path.append(0)
            else:
                shortest_path.append(self.INF)
        for destination in range(0, self.network.size):
            if destination != origin:
                self.last = origin
                shortest_path[destination] = self.find_path(origin, destination, origin)
        return shortest_path

    visited = []

    def find_path(self, origin, destination, main_origin, deeps=0):
        self.visited.append(origin)
        if destination in self.network.adjacency[origin]:
            self.visited = []
            self.num_transmissions[main_origin] += 1
            return deeps + 1
        else:
            choice = random.choice(self.network.adjacency[origin])
            if choice == self.last and len(self.network.adjacency[origin]) > 1:
                c = choice
                while c == choice:
                    choice = random.choice(self.network.adjacency[origin])
            if choice == destination:
                self.visited = []
                return deeps + 1
            else:
                if choice in self.visited:
                    self.last = origin
                    self.num_transmissions[main_origin] += 1
                    return self.find_path(choice, destination, deeps)
                else:
                    self.visited.append(choice)
                    self.last = origin
                    self.num_transmissions[main_origin] += 1
                    deeps += 1
                    return self.find_path(choice, destination, main_origin, deeps)

    def __str__(self):
        msg = " ==== HOTPOTATO 2 ==== \n"
        msg += "Average number of transmissions: "
        msg += str(self.avg_num_transmissions)
        msg += "\nAverage shortest paths length: "
        msg += str(self.avg_shortest_paths)
        msg += "\n"
        return msg




