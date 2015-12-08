directions = open("input", 'r').read()

robocoordinates = [0, 0]
realcoordinates = [0, 0]
visitedhouses = []
uniquehouses = 0
currentsanta = "real"
coordinates = realcoordinates

def coordswap():
    global currentsanta, coordinates
    if currentsanta == "real":
        coordinates = robocoordinates
        currentsanta = "robo"
    else:
        coordinates = realcoordinates
        currentsanta = "real"

def addhouse(coordinates):
    global uniquehouses, currentsanta
    if not "{c[0]}, {c[1]}".format(c=coordinates) in visitedhouses:
        visitedhouses.append("{c[0]}, {c[1]}".format(c=coordinates))
        uniquehouses += 1
        print("New house at {c[0]}, {c[1]} for {}".format(currentsanta, c=coordinates))
    else:
        print("Duplicate house at {c[0]}, {c[1]} for {}".format(currentsanta, c=coordinates))

for i in directions:
    coordswap()
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