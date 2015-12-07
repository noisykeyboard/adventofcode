floor = 0
for i in open("input", 'r').read():
	if i == "(":
		floor += 1
	else:
		floor -= 1

print(floor)