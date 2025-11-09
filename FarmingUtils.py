import Helpers
import Constants

def use_water(water = Constants.WATER_GAIN_RATE): 
	tileNotWatered = get_water() <= water
	isWaterAvailable = num_items(Items.Water) > 0
	if tileNotWatered and isWaterAvailable:
		use_item(Items.Water)
		
def Till(): # this is to replace the lame built in lowercase till 
	if can_harvest():
		harvest()
	if get_entity_type() == Entities.Dead_Pumpkin:
		till()
	if get_ground_type() == Grounds.Grassland:
		till()
   
def TillEverything():
	sizeX = get_world_size()
	sizeY = sizeX # farm is always square?
	nextDirection = North
	for i in range(sizeX * sizeY):
		till()
		nextDirection = Helpers.goToNextTile(nextDirection)
  
def is_over(entity):
	return get_entity_type() == entity


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
				

def reset():
	Helpers.goTo(0,0)
	print('Reset time!')
	HarvestAll()
	print('All done!')
