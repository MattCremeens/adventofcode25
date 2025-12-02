if __name__ == '__main__':
    f = open('./data/input2.txt')
    line = f.readline()
    ranges = line.split(',')
    id_sum = 0
    for r in ranges:
        endpoints = r.split('-')
        left_endpoint = int(endpoints[0])
        right_endpoint = int(endpoints[1])
        for num in range(left_endpoint, right_endpoint+1):
            str_num = str(num)
            for i in range(1, len(str_num)+1):
                if str_num[:i] == str_num[i:]:
                    id_sum += int(str_num)
    print(id_sum)



