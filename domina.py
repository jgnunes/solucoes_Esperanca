# a = [x1, y1]
# b = [x2, y2]

def domina(a, b):
    if a[0] > b[0] and a[1] > b[1]:
        return True
    else:
        return False

if __name__ == "__main__":
    print(domina([5,5],[0,0]))
    print(domina([5,0], [0,0]))