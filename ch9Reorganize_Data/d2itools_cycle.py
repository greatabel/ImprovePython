import itertools


shape_list = ["square", "triangle", "circle", "pentagon", "star", "octagon"]
g = itertools.cycle(shape_list)
for i in range(18):
    if i % len(shape_list) == 0:
        print('')
    shape = next(g)
    print("Drawing",shape)