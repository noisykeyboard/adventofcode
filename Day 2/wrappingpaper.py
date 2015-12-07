packages = open("input", 'r').readlines()
total = 0

for i in packages:
    h, w, l = [int(num) for num in i.split('x')]
    side1 = h*w
    side2 = h*l
    side3 = w*l

    extra = min(side1, side2, side3)

    package = side1*2 + side2*2 + side3*2 + extra
    total += package

    print("package: ", package)

print("total: ", total)