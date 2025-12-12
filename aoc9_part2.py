from shapely import Polygon, points


if __name__ == '__main__':
    f = open('./data/input9_test.txt')
    lines = f.readlines()
    
    points = []
    for l1 in lines:
        x1 = int(l1.split(',')[0])
        y1 = int(l1.split(',')[1])
        points.append((x1, y1))
        
    polygon = Polygon(points)
    ch = polygon.convex_hull
    largest_area = 0
    print(polygon.boundary.coords)
    for c in polygon.boundary.coords:
        print(c)
                
    
        
        