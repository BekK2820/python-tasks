import sys
import math

def read_circle_file(circle_file):
    with open(circle_file, 'r') as f:
        center_x, center_y = map(float, f.readline().strip().split())
        radius = float(f.readline().strip())
    return (center_x, center_y), radius

def read_points_file(points_file):

    points = []
    with open(points_file, 'r') as f:
        for line in f:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

def check_point_position(center, radius, point):

    dist_squared = (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2
    radius_squared = radius ** 2

    if dist_squared < radius_squared:
        return 1  
    elif dist_squared == radius_squared:
        return 0
    else:
        return 2

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]


    center, radius = read_circle_file(circle_file)
    points = read_points_file(points_file)


    for point in points:
        result = check_point_position(center, radius, point)
        print(result)