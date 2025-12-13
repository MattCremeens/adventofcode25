import numpy as np
from geneticalgorithm import geneticalgorithm as ga


if __name__ == '__main__':
    
    joltage = []
    buttons = []
    def g(x):
        global joltage
        global buttons
        new_joltage = [0] * len(joltage)
        #print(new_joltage)
        #print(joltage)
        #print(buttons)
        #print(x)
        #print(buttons)
        for i in range(len(x)):
            if isinstance(buttons[i], int):
                new_joltage[buttons[i]] += x[i]
            else:
                for j in buttons[i]:
                    new_joltage[j] += x[i]
        #print(new_joltage)
        pen = 0
        if joltage != new_joltage:
            pen = 1e6#sum([1e6 * abs(joltage[i] - new_joltage[i]) for i in range(len(joltage))])
            #print(x)
            #print(new_joltage)
            #print(joltage)
        return sum([abs(joltage[i] - new_joltage[i]) for i in range(len(joltage))]) + int(np.sum(x)) + pen


    algorithm_param = {'max_num_iteration': 3000,
                       'population_size': 2000,
                       'mutation_probability': 0.01,
                       'elit_ratio': 0.05,
                       'crossover_probability': 0.5,
                       'parents_portion': 0.3,
                       'crossover_type': 'uniform',
                       'max_iteration_without_improv': 600,
                       }
    
    f = open('./data/input10.txt')
    lines = f.readlines()
    total_pushes = 0
    for line in lines:
        diagram = [1 if x == '#' else 0 for x in line.split()[0].replace('[', '').replace(']', '')]
        joltage = [x for x in eval(line.split()[-1].replace('{', '').replace('}', ''))]
        buttons = [eval(x) for x in line.split()[1:-1]]
        #print(joltage) 
        #print(buttons)
        #print(diagram)
        varbound = np.array([[0, max(joltage)]] * len(buttons))
        model = ga(function=g,
                   dimension=len(buttons),
                   variable_type='int',
                   variable_boundaries=varbound,
                   algorithm_parameters=algorithm_param)
        model.run()
        solution = int(model.output_dict['function'])
        total_pushes += solution
        # break
    print('\n')
    print(total_pushes)
        