import sys
import plotly
import plotly.graph_objs as go

from bin.network import Network
from algorithm.linkstate import LinkState
from algorithm.distvector import DistanceVector
from algorithm.hotpotato import *

if __name__ == '__main__':
    fl = open(sys.argv[1])
    vector = []
    for i in fl:
        vector.append(i)

    network = Network(vector)
    link_state = LinkState(network)
    distance_vector = DistanceVector(network)
    hot_potato = HotPotato(network)
    hot_potato2 = HotPotato2(network)

    print link_state
    print distance_vector
    print hot_potato
    print hot_potato2
