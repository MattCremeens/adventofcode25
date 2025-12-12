import numpy as np


if __name__ == '__main__':
    data = np.genfromtxt('./data/input7.txt', dtype='str', delimiter=1)

    #print(data)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i,j] == 'S':
                data[i+1,j] = '|'
            elif data[i,j] == '^':
                data[i,j-1] = '|'
                data[i,j+1] = '|'
            elif data[i,j] == '.' and data[i-1,j] == '|':
                data[i,j] = '|'
                
    print('\n')            
    print(data)    
    pipe_cnt = 0
    for i in range(data.shape[0]-1):
        for j in range(data.shape[1]):
            if data[i,j] == '|' and data[i+1,j] == '^':
                pipe_cnt += 1
    print(pipe_cnt)





