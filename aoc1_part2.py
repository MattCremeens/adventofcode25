if __name__ == '__main__':
    f = open('./data/input1.txt')
    lines = f.readlines()
    pos = 50
    num_zeros = 0
    direction = None
    moves = 0
    for line in lines:
        direction = line[0]
        moves = int(line[1:])
        if direction == 'L':
            for i in range(moves):
                pos -= 1
                if pos < 0:
                    pos = 99
                if pos == 0:
                    num_zeros += 1
        else:
            for i in range(moves):
                pos += 1
                if pos > 99:
                    pos = 0
                if pos == 0:
                    num_zeros += 1
        # print(pos)


    print(num_zeros)