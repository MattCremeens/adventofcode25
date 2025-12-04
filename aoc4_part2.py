import numpy as np
import networkx as nx


if __name__ == '__main__':
    data = np.genfromtxt('./data/input4.txt', dtype='str', delimiter=1)
    G = nx.Graph()

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            G.add_node((i,j), char=str(data[i,j]))

    for n1 in G.nodes:
        for n2 in G.nodes:
            # Chebyshev distance
            if max(abs(n2[0] - n1[0]), abs(n2[1] - n1[1])) == 1:
                G.add_edge(n1, n2)
    total_rolls_accessed = 0
    while True:
        rolls_accessed = 0
        for n in G.nodes():
            num_rolls = 0
            if G.nodes[n]['char'] == '@':
                num_rolls = 0
                for neighbor in G.neighbors(n):
                    if G.nodes[neighbor]['char'] == '@':
                        num_rolls += 1
                if num_rolls < 4:
                    G.nodes[n]['char'] = '.'
                    rolls_accessed += 1
        if rolls_accessed == 0:
            break
        else:
            total_rolls_accessed += rolls_accessed
    print(total_rolls_accessed)






