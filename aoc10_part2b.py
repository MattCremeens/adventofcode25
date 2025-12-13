from pulp import *


if __name__ == '__main__':

    f = open('./data/input10.txt')
    lines = f.readlines()
    total_pushes = 0
    for line in lines:
        diagram = [1 if x == '#' else 0 for x in line.split()[0].replace('[', '').replace(']', '')]
        joltage = [x for x in eval(line.split()[-1].replace('{', '').replace('}', ''))]
        buttons = [eval(x) for x in line.split()[1:-1]]
        buttons = [(x, ) if isinstance(x, int)  else x for x in buttons]
        print(joltage) 
        print(buttons)
        #print(diagram)
        prob = LpProblem("MinimizePushes", LpMinimize)
        num_pushes = [LpVariable(f"x{button}", lowBound=0, cat='Integer') for button in range(len(buttons))]
        prob += lpSum(num_pushes)
        for i in range(len(joltage)):
            prob += lpSum([num_pushes[j] for j in range(len(buttons)) if i in buttons[j]]) == joltage[i]

        prob.solve()
        # print("Status:", LpStatus[prob.status])
        for v in prob.variables():
            # print(v.name, "=", v.varValue)
            total_pushes += v.varValue
        
    print('\n')
    print(total_pushes)
        