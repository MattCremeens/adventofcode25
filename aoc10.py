import numpy as np
from geneticalgorithm import geneticalgorithm as ga


if __name__ == '__main__':
    diagram = []
    buttons = []
    def g(x):
        global diagram
        global buttons
        new_diagram = [0] * len(diagram)
        #print(new_diagram)
        for i in range(len(x)):
            if x[i] % 2 != 0:
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
                    
        pen = 0
        #print(new_diagram)
        #print(diagram)
        if new_diagram != diagram:
            pen = 1e100
        return int(np.sum(x)) + pen


    algorithm_param = {'max_num_iteration': 4000,
                       'population_size': 3000,
                       'mutation_probability': 0.01,
                       'elit_ratio': 0.05,
                       'crossover_probability': 0.5,
                       'parents_portion': 0.3,
                       'crossover_type': 'uniform',
                       'max_iteration_without_improv': 700,
                       }
    
    f = open('./data/input10.txt')
    lines = f.readlines()
    button_pushes = 0
    for line in lines:
        
        diagram = [1 if x == '#' else 0 for x in line.split()[0].replace('[', '').replace(']', '')]
        joltage = line.split()[-1]
        buttons = [eval(x) for x in line.split()[1:-1]]

        #print(buttons)
        #print(diagram)

        model = ga(function=g, 
                   dimension=len(buttons), 
                   variable_type='bool', 
                   algorithm_parameters=algorithm_param)
        model.run()
        solution = int(model.output_dict['function'])
        button_pushes += solution
    print('\n')
    print(button_pushes)
        