import matplotlib.pyplot as plt

def plot(xdata, ydata):
    """ Plot a range of ydata (on y-axis) against xdata (on x-axis) """
    
    plt.plot(xdata, ydata)
    plt.show()

def plot_many(xdata, ydatas):
    """ Plot a sequence of ydatas (on y-axis) against xdata (on x-axis) """
    
    for ydata in ydatas:
        plt.plot(xdata, ydata)
    plt.show()


if __name__ == "__main__":
    xdata = [100, 200, 400, 800, 1000]
    ydata = [117, 483, 1920, 7823, 12395]
    plot(xdata, ydata)