import operator
from itertools import accumulate
import math


if __name__ == '__main__':
    f = open('./data/input6.txt')
    lines = f.readlines()
    operators = lines[-1].split()
    digits_1 = lines[0].split()
    digits_2 = lines[1].split()
    digits_3 = lines[2].split()
    digits_4 = lines[3].split()
    widths = []
    num_space = 1
    for c in reversed(lines[-1]):
        if c in ('+', '*'):
            widths.append(num_space)
            num_space = 1
        else:
            num_space += 1
    #widths.append(0)
    widths = widths[::-1]
    
    accumulated_widths = [0] + list(accumulate(widths, operator.add))
    accumulated_widths = accumulated_widths[:-1]
    
    #print(widths)
    #print(accumulated_widths)
    operator = ''
    grand_total = 0
    for j in range(len(accumulated_widths)):
        nums = []
        for i in range(widths[j]):
            num = ''
            for line in lines:
                #print(line[i+4])
                if line[i+accumulated_widths[j]] not in (' ', '*', '+'):
                    num += line[i+accumulated_widths[j]]
                elif line[i+accumulated_widths[j]] in ('*', '+'):
                    operator = line[i+accumulated_widths[j]]
                    
            nums.append(num)
        # print(nums)
        total = 0
        if operator == '+':
            total = sum([int(x) for x in nums if x != ''])
        elif operator == '*':
            total = math.prod([int(x) for x in nums if x != ''])
        grand_total += total
    print(grand_total)
            
        
            
                    
                
            
                
            