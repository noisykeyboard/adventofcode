directions = open("input", 'r').read()

coordinates = [0, 0]
visitedhouses = []
uniquehouses = 0

def addhouse(coordinates):
    global uniquehouses
    if not "{c[0]}, {c[1]}".format(c=coordinates) in visitedhouses:
        visitedhouses.append("{c[0]}, {c[1]}".format(c=coordinates))
        uniquehouses += 1
        print("New house at {c[0]}, {c[1]}".format(c=coordinates))
    else:
        print("Duplicate house at {c[0]}, {c[1]}".format(c=coordinates))

for i in directions:
    if i == "<":
        coordinates[0] -= 1
        addhouse(coordinates)
    elif i == ">":
        coordinates[0] += 1
        addhouse(coordinates)
    elif i == "^":
        coordinates[1] += 1
        addhouse(coordinates)
    else:
        coordinates[1] -= 1
        addhouse(coordinates)

print("Total unique houses: {}".format(uniquehouses))