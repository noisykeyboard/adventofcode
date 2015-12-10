floor = 0
position = 0
for i in open("input", 'r').read():
	position += 1
	if i == "(":
		floor += 1
	else:
		floor -= 1
	
	if floor == -1:
		print("position: ", position)

print("floor: ", floor)