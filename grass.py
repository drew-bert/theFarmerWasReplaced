while True: #main loop
    for i in range(get_world_size()):
        if can_harvest():
            harvest()
            plant(Entities.Grass)
        if i == get_world_size():
            move(East)
        else:
            move(North)