import Helpers
import FarmingUtils

def farm(size, entity, water):
	for x in range(size):
		for y in range(size):
			if can_harvest():
				harvest()
			if entity == Entities.Tree:
				if shouldPlantTree(x, y):
					plant(Entities.Tree)
				else:
					print('plant tree is: ', shouldPlantTree(x,y))
			if entity == Entities.Carrot:
				FarmingUtils.Till()
				plant(entity)
			if entity == Entities.Grass:
				plant(entity)
			if entity == Entities.Bush:
				plant(entity)
			if entity == Entities.Pumpkin:
				print('PUMPKINS LOL')
			if (water == True):
				FarmingUtils.use_water()
		move(North)
	move(East)

def shouldPlantTree(x,y):
	if Helpers.is_even(x) == Helpers.is_odd(y):
		return True
	else:
		return False

def HarvestAll():
	size = get_world_size()
	i = 0
	for x in range(size):
		for y in range(size):
			if can_harvest():
				i += 1
				harvest()
			else:
				FarmingUtils.Till()
			move(East)
		move(North)
	print('Harvested all! Harvested ', i, ' times!')
				

# pumpkinssss
# start at 0,0. 
# define a 2d grid
# grid start at all 0, move tile by tile and set grid to 1 (plant)
# once all grid is 1, go back to start (0,0) set all to 0 (harvest)
# need helper function to eval what phase it is.  ideally the whole grid will either be false or true but can never promise that lol
# 	set a flag at beginning of loop
#	walk through the grid by x,y range and if the value is true, go to that tile.
#	if it isnt a pumpkin, plant a pumpkin
#	if you can harvest it, DONT, instead set that tile to false (harvest)
#	at the end of the x/y loop, set the shouldcheck to true so it doesnt loop forever
# then just harvest by default in the main pumpkin function - the grid should be entirely planted with pumpkins after the fill



def fillRemainingTiles(size,entity,grid):
	shouldCheck = True # flag to see if we should continue to check
	while shouldCheck: # loop for checker
		anyLeft = False # false to avoid infinite loop
		for x in range(size): # x loop
			for y in range(size): # y loop
				if grid[x][y] == True: # True = need planting
					anyLeft = True # if ANYTHING needs planting, it should hit this flag
					Helpers.goTo(x,y) # go to the fucker that needs planting
					if not FarmingUtils.is_over(entity): # if youre already over a live pumpkin, dont fuck around
						FarmingUtils.Till() # murder that ground
						plant(entity) # plant that bitch
					elif can_harvest(): # if its good to harvest
						grid[x][y] = False # DO NOT HARVEST, set the grid value to false (harvest)
		if anyLeft == False: # this should only be false after the drone checks the whole grid
			shouldCheck = False # this will stop the loop

def plantPumpkins(size, entity):
	grid = Helpers.farmGrid(size,False)

	for z in range(2): # control loop
		for x in range(size): # x loop (outer)
			for y in range(size): # y loop (inner)
				if not FarmingUtils.is_over(entity):
					FarmingUtils.Till()
					plant(entity)
					if z > 0:
						grid[x][y] = True
				else:
					grid[x][y] = False
			move(North)
		move(East)
	fillRemainingTiles(size,entity,grid)
	Helpers.goTo(0,0)