import networkx as nx


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
    num_paths = 0
    for path in nx.all_simple_paths(G, source='you', target='out'):
        num_paths += 1
        
    print(num_paths)
        






