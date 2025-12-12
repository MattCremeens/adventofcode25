import numpy as np
import networkx as nx


if __name__ == '__main__':
    data = np.genfromtxt('./data/input7.txt', dtype='str', delimiter=1)
    G = nx.DiGraph()
    #print(data)
    s_pos = 0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i,j] == 'S':
                s_pos = j
                data[i+1,j] = '|'
            elif data[i,j] == '^':
                data[i,j-1] = '|'
                data[i,j+1] = '|'
            elif data[i,j] == '.' and data[i-1,j] == '|':
                data[i,j] = '|'
                
    print('\n')            
    #print(data)  
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i,j] in ('|', 'S'):
                G.add_node((i,j))

    for n1 in G.nodes:
        for n2 in G.nodes:
            if n1 != n2 and \
                    abs(n2[1] - n1[1]) <= 1 and \
                    n2[0] - n1[0] == 1 and \
                    data[n2[0], n1[1]] == '^':                
                G.add_edge(n1, n2)
            if n1 != n2 and \
                n2[0] - n1[0] == 1 and \
                n2[1] == n1[1]:
                G.add_edge(n1, n2)
            
                
    
    paths = 0
    for i in range(data.shape[0]-1):
        #print(i)
        if G.has_node((data.shape[0]-1,i)):
            #for path in nx.all_shortest_paths(G, source=(0,s_pos), target=(data.shape[0]-1,i)):
            paths += len(list(nx.all_shortest_paths(G, source=(0, s_pos), target=(data.shape[0] - 1, i))))
            print(paths)
                #paths += 1
                #print(paths)
                #sorted_path = sorted(path)
                #if sorted_path not in paths:
                #paths.append(path)
    
    print(paths)
    #print(len(G.edges))
    #print(len(G.nodes))
    #print(paths)
    
    





