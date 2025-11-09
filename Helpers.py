def is_even(x):
	return x % 2 == 0
def is_odd(x):
	return x % 2 == 1

	
def goTo(x, y):
	yDistance = get_pos_y() - y # this will be positive if drone is north of target space
	xDistance = get_pos_x() - x # same idea
	halfWorldSize = get_world_size() / 2 # gives us a 'center' for lack of a better term
	while get_pos_y() != y:
		if yDistance >= halfWorldSize or (-halfWorldSize <= yDistance and yDistance < 0): # remember: yDistance will be positive if the drone is north of target
			move(North) 
		else:
			move(South)
	while get_pos_x() != x:
		if xDistance >= halfWorldSize or (-halfWorldSize <= xDistance and xDistance < 0): #same idea!
			move(East)
		else:
			move(West)
			
def goToNextTile(dir): # ideally call this recursively to traverse grid
	farmBoundary = get_world_size()
	farmHeight = farmBoundary # farm is always a square
	currentX = get_pos_x()
	currentY = get_pos_y()
	if ( dir == East ):
		if (currentX + 1 == farmBoundary):
			dir = North
	elif ( dir == West ):
		if ( currentX == 0):
			dir = North
	elif ( dir == North ):
		if ( currentX + 1 == farmBoundary ):
			dir = West
		elif ( currentX == 0 ):
			dir = East
	move(dir)
	return dir

def farmGrid(size, element):
	xArray = []
	for i in range(size):
		yArray = []
		for k in range (size):
			yArray.append(element)
		xArray.append(yArray)
	return xArray