import numpy as np
import matplotlib.pyplot as plt


def draw_function_graph():
    x = np.arange(-10, 10.01, 0.01)
    plt.plot(x, x * x - x - 6)
    plt.show()


draw_function_graph()
