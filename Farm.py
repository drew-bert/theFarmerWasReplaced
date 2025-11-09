import Helpers
import FarmingUtils
import Pumpkins

def farm(size, entity, water):
	if entity == Entities.Tree:
		chop(size, entity, water, False)
	if entity == Entities.Pumpkin:
		Pumpkins.plantPumpkins(size, entity)
	else:
		for x in range(size):
			for y in range(size):
				if can_harvest():
					harvest()
				if entity == Entities.Carrot:
					FarmingUtils.Till()
					plant(entity)
				elif entity == Entities.Grass:
					plant(entity)
				elif entity == Entities.Bush:
					plant(entity)
				if (water == True):
					FarmingUtils.use_water()
			move(North)
		move(East)

def chop(size, entity, water, fertilize = False):
	for x in range(size):
		for y in range(size):
			if can_harvest():
				harvest()
			if shouldPlantTree(x,y):
				FarmingUtils.Till()
				plant(entity)
			else:
				plant(Entities.Bush)
			move(North)
		move(East)
			

def shouldPlantTree(x,y):
	return x%2 == y%2

