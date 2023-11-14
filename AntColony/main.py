import print_plot
from ant_colony import AntColonyClass

if __name__ == "__main__":
    algo = AntColonyClass(20)
    tmp_p = algo.ant_colony()
    print_plot.PrintPlot(tmp_p)

