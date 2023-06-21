import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
x = np.random.random(200)
y = np.random.random(200)
classes = np.random.randint(0,3,200)
colors = ["red","orange","yellow","blue"]
custom_cmap =
matplotlib.colors.LinearSegmentedColormap.from_list("customer",colors)
custom_cmap = matplotlib.colors.ListedColormap(colors)
plt.scatter(x,y,c=classes, cmap=custom_cmap)
plt.colorbar()
plt.show()
