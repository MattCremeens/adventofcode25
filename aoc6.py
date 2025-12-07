if __name__ == '__main__':
    f = open('./data/input6.txt')
    lines = f.readlines()
    operators = lines[-1].split()
    digits_1 = lines[0].split()
    digits_2 = lines[1].split()
    digits_3 = lines[2].split()
    digits_4 = lines[3].split()
    grand_total = 0
    for i in range(len(operators)):
        if operators[i] == '+':
            grand_total += int(digits_1[i]) + int(digits_2[i]) + int(digits_3[i]) + int(digits_4[i])
        else:
            grand_total += int(digits_1[i]) * int(digits_2[i]) * int(digits_3[i]) * int(digits_4[i])

    print(grand_total)