#Jack Amos
#CS2300-002
#10/04/2019
#Project 2
#using Python 3.7


def print_coordinates(filename):

	with open(filename,'r') as file:
		contents = file.read()

	#get each value in string an convert it to integer
	# [llx,lly,d,p1,p2,v1,v2]
	coord_values = [int(x) for x in contents.split()]

	#sets scale of "screen"
	dimension = 2*coord_values[2]
	
	#2d array that will be printed
	screen = [[" "]*dimension for x in range(dimension)]

	implicit = get_implicit(coord_values)

	#plot box 1st point
	y_point = dimension - abs(coord_values[1])
	x_point = abs(coord_values[0])

	#exists to make array index not all = 0
	index = 0
	for n in screen:
		screen[index][index] = "w"
		index += 1

	r1 = range((y_point-coord_values[2]+1),y_point+1)
	index = x_point

	#make actual box
	for n in screen:
		if screen.index(n) in r1:
			n[x_point] = "*"
			n[x_point+coord_values[2]] = "*"
		if screen.index(n) == y_point or screen.index(n) == (y_point-coord_values[2]+1):
			while index < (x_point+coord_values[2]):
				n[index] = "*"
				index+=1
			index = x_point
		
	#draw line
	for n in screen:
		for i in n:
			if (implicit[0]*screen.index(n)+implicit[1]*n.index(i)+implicit[2]) == 0:
				screen[screen.index(n)][n.index(i)] = "*"


	row = 0
	screen_string = ""

	while row < dimension:
		#adds row of values to output string plus newline char
		screen_string += "|" + str(screen[row]) + "\n"
		#increment by column number so vars are at the start and end of next row
		row+=1

	#adds x axis to the bottom of the graph
	x_axis = ["_"]*dimension
	screen_string+= "|" + str(x_axis)

	#removes unneeded chars for beautification
	screen_string = screen_string.replace(",","").replace("[","").replace("]","").replace("'","").replace("w"," ")	



	#print final graph
	print(screen_string)
	print("\n")
	print("Implicit Form:	"+str(implicit[0])+"x+"+str(implicit[1])+"x+"+str(implicit[2])+"=0")




def get_implicit(coord_values):
	
	#[a,b,c]
	implicit_values = []

	#a
	implicit_values.append(-1*coord_values[5])
	#b
	implicit_values.append(coord_values[6])
	#c
	implicit_values.append(-1*(coord_values[6]*coord_values[3]+(-1*coord_values[5]*coord_values[4])))

	return implicit_values




print_coordinates("exfile.txt")






