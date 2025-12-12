if __name__ == '__main__':
    f = open('./data/input9.txt')
    lines = f.readlines()
    
    largest_area = 0
    p1 = []
    p2 = []
    for l1 in lines:
        x1 = int(l1.split(',')[0])
        y1 = int(l1.split(',')[1])
        for l2 in lines:
            x2 = int(l2.split(',')[0])
            y2 = int(l2.split(',')[1])
            new_area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if new_area > largest_area:
                largest_area = new_area
                
                
    print(largest_area)
                
    
                
            
        