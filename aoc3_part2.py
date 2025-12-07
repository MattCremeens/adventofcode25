import numpy as np
from geneticalgorithm import geneticalgorithm as ga


if __name__ == '__main__':
    jolt = ''
    def g(x):
        global jolt
        num = '0'
        pen = 0
        if np.sum(x) != 12:
            pen = 1e100 * np.sum(x)
        for i in range(len(x)):
            if x[i] == 1:
                num += jolt[i]
        return -int(num) + pen



    f = open('./data/input3.txt')
    lines = f.readlines()
    accum_jolt = 0

    algorithm_param = {'max_num_iteration': 3000,
                       'population_size': 2000,
                       'mutation_probability': 0.01,
                       'elit_ratio': 0.05,
                       'crossover_probability': 0.5,
                       'parents_portion': 0.3,
                       'crossover_type': 'uniform',
                       'max_iteration_without_improv': 300,
                       }
    for line in lines:

        nums = [i for i in line.replace('\n', '')]
        jolt = ''.join(nums)
        model = ga(function=g, dimension=100, variable_type='bool', algorithm_parameters=algorithm_param)
        model.run()
        solution = -int(model.output_dict['function'])
        accum_jolt += solution
        #break
    print('\n')
    print(accum_jolt)
