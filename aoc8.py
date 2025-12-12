import math
from operator import itemgetter
import itertools


if __name__ == '__main__':
    f = open('./data/input8_test.txt')
    lines = f.readlines()
    points = []
    
    for line in lines:
        points.append([int(x) for x in line.split(',')])
    
    pairs = []
    
    min_pairs = []
    for p1 in points:
        min_dist = 1e200
        min_pair = []
        for p2 in points:
            if p1 != p2:
                if math.dist(p1, p2) < min_dist:
                    min_dist = math.dist(p1, p2)
                    min_pair = [p1, p2, min_dist]
        if min_pair[2] not in [x[2] for x in min_pairs]:
            min_pairs.append(min_pair)
    
        
    min_pairs = sorted(min_pairs, key=itemgetter(2))
    #print(min_pairs)
    
    min_pairs = [[tuple(a), tuple(b)] for [a,b,c] in min_pairs]
    print(min_pairs)
    #merged_pair = min_pairs[0] + list(set(min_pairs[1]) - set(min_pairs[0]))
    #print(merged_pair)
    new_pair = min_pairs[4]
    #print(new_pair)
    for p in min_pairs:
        if p != new_pair and (new_pair[0] in p or new_pair[1] in p):
            new_pair = new_pair + list(set(p) - set(new_pair))
    print(new_pair)
        
    

                
                