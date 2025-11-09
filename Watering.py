import Helpers

def use_water(water = 0.3): # 0.3 just seemed to be a good constant rn based on how much water a tile can take
	tileNotWatered = get_water() <= water
	isWaterAvailable = num_items(Items.Water) > 0
	if tileNotWatered and isWaterAvailable:
		use_item(Items.Water)
		
def Till(): # this is to replace the lame built in lowercase till 
	if get_ground_type() == Grounds.Grassland:
		till()
   
