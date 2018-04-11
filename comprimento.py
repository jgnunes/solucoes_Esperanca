from math import sqrt
# p = [x1, y1]
# q = [x2, y2]

def comprimento(p, q):
    delta_x = p[0] - q[0]
    delta_y = p[1] - q[1]
    distancia = sqrt((delta_x**2) + (delta_y)**2)
    return distancia

if __name__ == '__main__':
    print(comprimento([1,1],[4,5]))
