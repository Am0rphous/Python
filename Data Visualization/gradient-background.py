import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Definer fargekartet
colors = [(0, '#00ff00'), (0.4, '#ffff00'), (0.5, '#ffff00'), (1, '#ff0000')]
cmap = LinearSegmentedColormap.from_list('Custom', colors, N=2048)

# Lag gradient
gradient = np.linspace(0, 1, 2048)
gradient = np.vstack((gradient, gradient))

# Lag plottet med gradient som bakgrunn
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(gradient, aspect='equal', cmap=cmap, extent=[0, 10, 0, 10])

# Sett tittel og aksetekster
ax.set_title('Gradient bakgrunn')
ax.set_xlabel('X-akse')
ax.set_ylabel('Y-akse')

# Vis plottet
#plt.show()
plt.savefig('Gradient-background.png')