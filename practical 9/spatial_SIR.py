import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

grid_size = 100       
beta = 0.3           
gamma = 0.05         
time_steps = 100     

grid = np.zeros((grid_size, grid_size), dtype=int)

init_x = np.random.randint(0, grid_size)
init_y = np.random.randint(0, grid_size)
grid[init_x, init_y] = 1

neighbors = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),          (0, 1),
             (1, -1),  (1, 0), (1, 1)]

def update(frame):
    global grid
    new_grid = grid.copy()
    
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] == 1:
                for dx, dy in neighbors:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < grid_size and 0 <= y < grid_size:
                        if new_grid[x][y] == 0 and np.random.random() < beta:
                            new_grid[x][y] = 1
                
                if np.random.random() < gamma:
                    new_grid[i, j] = 2
    
    grid = new_grid
    im.set_array(grid)
    return im,

fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
cmap = plt.cm.colors.ListedColormap(['green', 'red', 'blue'])
im = ax.imshow(grid, cmap=cmap, vmin=0, vmax=2)

ax.set_title('2D Spatial SIR Model (100×100 Grid)', fontsize=14)
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='green', label='Susceptible'),
                   Patch(facecolor='red', label='Infected'),
                   Patch(facecolor='blue', label='Recovered')]
ax.legend(handles=legend_elements, loc='upper right')

ani = FuncAnimation(fig, update, frames=time_steps, interval=50, blit=True)

plt.savefig('spatial_SIR_final.png')
plt.show()