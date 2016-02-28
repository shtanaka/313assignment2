import sys
from distvector import Network
from linkstate import LinkState

if __name__ == '__main__':

    file = open(sys.argv[1])
    vector = []
    for i in file:
        vector.append(i)

    network = Network(vector)
    linkState = LinkState(network)
    print linkState
    #print linkState.network.adjacency
    #print linkState.visited


