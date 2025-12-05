from pulp import *


if __name__ == '__main__':

    f = open('./data/input3.txt')
    lines = f.readlines()
    for line in lines:

        nums = [i for i in line.replace('\n', '')]

        prob = LpProblem("Jolt Problem", LpMaximize)

        x = pulp.LpVariable.dicts(
            "x", range(len(nums)), lowBound=0, upBound=1, cat=LpInteger
        )
        prob += lpSum([int(nums[i])*x[i] for i in range(len(nums))])
        prob += lpSum([x[i] for i in range(len(nums))]) == 12
        prob.solve()
        # Print the status of the solution
        print("Status:", LpStatus[prob.status])

        # Print the value of the objective function
        print("Objective value:", pulp.value(prob.objective))

        # Print the value of the decision variables
        ans = ''

        for i in range(len(nums)):
            for v in prob.variables():
                #print(v.name, "=", v.varValue)
                if v.varValue == 1 and v.name == 'x_' + str(i):
                    ans += nums[i]

        print(ans)
        prob.writeLP("jolt.lp")
        break
