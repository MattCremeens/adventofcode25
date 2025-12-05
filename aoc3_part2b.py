from gadapt.ga import GA
import numpy as np


if __name__ == '__main__':
    jolt = ''


    def g(x):
        global jolt
        num = '0'
        pen = 0
        #print(x)
        if np.sum(x) > 12:
            pen = 1e100 * np.sum(x)
        elif np.sum(x) < 12:
            pen = 1e100 * max(np.sum(x), 1)
        for i in range(len(x)):
            if x[i] == 1:
                num += jolt[i]
        return -int(num) + pen


    f = open('./data/input3.txt')
    lines = f.readlines()
    accum_jolt = 0

    for line in lines:

        nums = [i for i in line.replace('\n', '')]
        jolt = ''.join(nums)

        ga = GA(cost_function=g,
                population_size=200,
                population_mutation="cost_diversity,parent_diversity",
                #number_of_mutation_chromosomes=0,
                #number_of_mutation_genes=0,
                gene_mutation="normal_distribution",
                exit_check="min_cost",
                max_attempt_no=500,
                logging=True,
                timeout=3600)

        for i in range(len(nums)):
            ga.add(0, 1, 1)

        results = ga.execute()
        print(results)
        break