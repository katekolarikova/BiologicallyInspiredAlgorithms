import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib; matplotlib.use("TkAgg")

def PrintPlot(current_pop):

    # current_pop = current_pop[-1]
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='2d')
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')

    # add color bar to p

    fig, ax = plt.subplots()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    def update(t):

        ax.clear()
        history = current_pop[t]

        x = [history[i].location[0] for i in range(len(history))]
        y = [history[i].location[1] for i in range(len(history))]

        plt.scatter(x, y, marker='o', color='red', label='Města')
        plt.plot(x, y, linestyle='-', color='blue', label='Optimální cesta')

        # point  = point_history[t]
        # ax.scatter(point[0], point[1], point[2], c='blue', marker='o')

    # Creating the Animation object
    num_frames = len(current_pop)
    print(num_frames)
    ani = FuncAnimation(fig=fig, func=update, frames=num_frames, repeat=False)



    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Problém obchodního cestujícího')
    plt.grid(True)
    plt.show()