import Farm
import FarmingUtils
import Helpers
import Debug

Helpers.goTo(0,0) # start at beginning
while True: #main loop
	
	Farm.farm(get_world_size(), Entities.Grass, False)