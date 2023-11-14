import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib; matplotlib.use("TkAgg")





# this function print 3D plot of given function, and add points found by blind search to it

def Print3DPlot(func, algorithm):
    r_min, r_max = -32.768, 32.768 # range of values for x and y
    x = np.linspace(r_min, r_max, 1500) # return array of evenly spaced values
    y = np.linspace(r_min, r_max, 1500)
    X, Y = np.meshgrid(x, y) #create X, Y grid from x, y arrays
    Z = func(X, Y) #compute Z value for each point of grid (func represents given type of plot)

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='hot', alpha=0.3) # create a plot
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # add color bar to plot
    fig.colorbar(surf)

    # find by blind search
    st_dev_x = np.std(x)
    st_dev_y = np.std(y)
    print("Standard deviation of x: ", st_dev_x)
    print("Standard deviation of y: ", st_dev_y)
    pointsHistory = algorithm(func, 1, r_min, r_max, r_min, r_max, st_dev_x, st_dev_y)
    def update(t):

        point = pointsHistory[t]
        ax.scatter(point[0], point[1], point[2], c='blue', marker='o')




    # Creating the Animation object
    num_frames = len(pointsHistory)
    ani = FuncAnimation(fig=fig, func=update, frames=num_frames, interval=100)

    plt.show()
