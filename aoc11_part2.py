import networkx as nx
import matplotlib.pyplot as plt


if __name__ == '__main__':
    
    G = nx.DiGraph()
    f = open('./data/input11.txt')
    lines = f.readlines()
    for line in lines:
        source = line.split(':')[0]
        destinations = line.split(':')[1].split()
        for destination in destinations:
            G.add_edge(source, destination)
    
    # print(G.edges)
    #print(nx.has_path(G, source='dac', target='fft')) # False
    #print(nx.has_path(G, source='svr', target='dac')) # True
    #print(nx.has_path(G, source='svr', target='fft')) # True
    #print(nx.has_path(G, source='fft', target='dac')) # True
    #print(nx.has_path(G, source='dac', target='out')) # True
    #print(nx.has_path(G, source='fft', target='out')) # True
    
    # Must follow:
    # svr --> fft --> dac --> out
    
    # Pruning
    print(len(G.nodes))
    candidate_removals = [x for x in G.nodes]
    for node in candidate_removals:
        if not (nx.has_path(G, source=node, target='fft') or nx.has_path(G, source='fft', target=node)):
            G.remove_node(node)
    candidate_removals = [x for x in G.nodes]
    for node in candidate_removals:
        if not (nx.has_path(G, source=node, target='dac') or nx.has_path(G, source='dac', target=node)):
            G.remove_node(node)

        
    candidate_removals = [x for x in G.nodes]
    for node in candidate_removals:
        if not (nx.has_path(G, source='svr', target=node) or nx.has_path(G, source=node, target='out')):
            G.remove_node(node)
        
    print(len(G.nodes))
    #nx.draw(G)
    #plt.show()
    
    num_paths = 0
    for path in nx.all_simple_paths(G, source='svr', target='out'):
        if 'dac' in path and 'fft' in path:
        #if 'fft' in path:
            #print(path)
            num_paths += 1
        #num_paths += 1
    print(num_paths)
    






