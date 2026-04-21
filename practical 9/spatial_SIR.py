import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------- 模型参数 -------------------
grid_size = 100       # 100x100的网格空间
beta = 0.3           # 感染率
gamma = 0.05         # 恢复率
time_steps = 100     # 模拟步数

# 网格状态定义：0=易感(S), 1=感染(I), 2=恢复(R)
grid = np.zeros((grid_size, grid_size), dtype=int)

# 随机初始化1个感染者（核心要求）
init_x = np.random.randint(0, grid_size)
init_y = np.random.randint(0, grid_size)
grid[init_x, init_y] = 1

# 8邻域坐标偏移（上下左右+四个斜角）
neighbors = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),          (0, 1),
             (1, -1),  (1, 0), (1, 1)]

# ------------------- 模拟函数 -------------------
def update(frame):
    global grid
    # 复制当前网格，避免更新时覆盖原始数据
    new_grid = grid.copy()
    
    # 遍历所有网格点
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