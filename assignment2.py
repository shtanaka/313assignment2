import sys
from bin.network import Network
from algorithm.linkstate import LinkState
from algorithm.distvector import DistanceVector

if __name__ == '__main__':

    fl = open(sys.argv[1])
    vector = []
    for i in fl:
        vector.append(i)

    network = Network(vector)
    link_state = LinkState(network)
    distance_vector = DistanceVector(network)

    print link_state
    print link_state.num_transmissions
    print link_state.shortest_paths

    print distance_vector
    print distance_vector.num_transmissions
    print distance_vector.shortest_paths
