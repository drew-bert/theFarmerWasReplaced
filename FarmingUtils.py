import Helpers

def use_water(water = 0.3): # 0.3 just seemed to be a good constant rn based on how much water a tile can take
	tileNotWatered = get_water() <= water
	isWaterAvailable = num_items(Items.Water) > 0
	if tileNotWatered and isWaterAvailable:
		use_item(Items.Water)
		
def Till(): # this is to replace the lame built in lowercase till 
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

def reset():
	Helpers.goTo(0,0)
	print('Reset time!')
	for x in range (get_world_size()):
		for y in range (get_world_size()):
			if can_harvest():
				harvest()
			move(East)
		move(North)
	print('All done!')
			