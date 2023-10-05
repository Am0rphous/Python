import matplotlib.pyplot as plt
import numpy as np

# Lag en tilfeldig matrise
data = np.random.rand(10, 10)

# Lag start-punktet for heatmap
fig, ax = plt.subplots()
im = ax.imshow(data, cmap='coolwarm', extent=[0, 10, 0, 10], vmin=0, vmax=1)

# Lag fargebar
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Verdier', rotation=-90, va="bottom")

# Sett tittel og aksetekster
ax.set_title('Heatmap')
ax.set_xlabel('X-akse')
ax.set_ylabel('Y-akse')

# Vis plottet
#plt.show()
plt.savefig('Standard_seaborn_heatmap.png')