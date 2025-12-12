import numpy as np
from geneticalgorithm import geneticalgorithm as ga


if __name__ == '__main__':
    def generate_binary_strings(bit_count):
        binary_strings = []

        def genbin(n, bs=''):
            if len(bs) == n:
                binary_strings.append(bs)
            else:
                genbin(n, bs + '0')
                genbin(n, bs + '1')

        genbin(bit_count)
        return binary_strings
    
    diagram = []
    buttons = []
    def g(x):
        global diagram
        global buttons
        new_diagram = [0] * len(diagram)
        #print(new_diagram)
        for i in range(len(x)):
            if int(x[i]) % 2 != 0:
                if isinstance(buttons[i], int):
                    if new_diagram[buttons[i]] == 0:
                        new_diagram[buttons[i]] = 1
                    else:
                        new_diagram[buttons[i]] = 0
                else:
                    for j in buttons[i]:
                        if new_diagram[j] == 0:
                            new_diagram[j] = 1
                        else:
                            new_diagram[j] = 0
        if diagram == new_diagram:
            return sum([int(i) for i in x]), x
        return 0, x
    
    f = open('./data/input10.txt')
    lines = f.readlines()
    button_pushes = 0
    total_pushes = 0
    for line in lines:
        
        diagram = [1 if x == '#' else 0 for x in line.split()[0].replace('[', '').replace(']', '')]
        joltage = line.split()[-1]
        buttons = [eval(x) for x in line.split()[1:-1]]

        #print(buttons)
        #print(diagram)
        
        min_pushes = 1e6
        possible_button_pushes = [list(x) for x in generate_binary_strings(len(buttons))]
        for pushes in possible_button_pushes:
            a, b = g(pushes)
            if a > 0 and a < min_pushes:
                min_pushes = a
        total_pushes += min_pushes

    print('\n')
    print(total_pushes)
        