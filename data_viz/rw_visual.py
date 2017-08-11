import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True: 
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    #alter size to fill screen
    plt.figure(figsize=(10,6))
    
    #vary each point from light blue to dark blue (gradient)
    point_numbers = list(range(rw.num_points))
    plot.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
        edgecolor='none', s=1)
    
    #emphasize first and last points
    plt.scatter(0,0, c='green', edgecolors='none', s=100)
    plot.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #remove axes
    plot.axes().get_xaxis().set_visible(False)
    plot.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running=='n':
        break
