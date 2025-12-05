if __name__ == '__main__':
    f = open('./data/input5.txt')
    lines = f.readlines()
    id_ranges = []
    ids = []
    for line in lines:
        if '-' in line:
            id_ranges.append(line.replace('\n', ''))
        elif line != '\n':
            ids.append(line.replace('\n', ''))

    num_fresh = []
    for id in ids:
        for id_range in id_ranges:
            left_endpoint = int(id_range.split('-')[0])
            right_endpoint = int(id_range.split('-')[1])
            int_id = int(id)
            if int_id <= right_endpoint and int_id >= left_endpoint:
                num_fresh.append(int_id)

    num_fresh = set(num_fresh)
    print(len(num_fresh))
