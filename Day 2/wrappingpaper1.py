packages = open("input", 'r').readlines()
total = 0

for i in packages:
    h, w, l = [int(num) for num in i.split('x')]
    sides = sorted([h, w, l])
    side1 = sides[0]
    side2 = sides[1]
    area = l*w*h

    package = side1*2 + side2*2 + area
    total += package

    print("package: ", package)

print("total: ", total)   