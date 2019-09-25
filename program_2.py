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
	
	#2d array that will be printed
	screen = [["*"]*30]*30
	y_axis = "|"
	x_axis = "_"

	implcit = get_implicit(coord_values)


	row = 0
	screen_string = ""

	while row < 30:
		#adds row of values to output string plus newline char
		screen_string += str(screen[row]) + "\n"
		#increment by column number so vars are at the start and end of next row
		row+=1

	#removes commas and brackets for beautification
	screen_string = screen_string.replace(",","").replace("[","").replace("]","").replace("'","")
	print(screen_string)
	





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






