import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

def plot_matrix(rm, title='Robot World', cmap=plt.cm.Blues):
    plt.imshow(rm,'inferno', interpolation='nearest')
    plt.title(title)
    plt.tight_layout()
    plt.show()

cmap = colors.ListedColormap(['k','b','y','g','r'])
rm = np.random.randint(0,4,(5,5))
plot_matrix(rm,cmap=cmap)