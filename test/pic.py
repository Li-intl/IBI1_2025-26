# 导入绘图库和数值计算库
import matplotlib.pyplot as plt
import numpy as np

# ===================== 1. 定义实验数据 =====================
# 植物名称（x轴标签）
plant_names = [
    'Banana',
    'Garlic',
    'Cabbage'
]
# 生植物速率 Raw rate
raw_rate = [0.048, 0.190, 0.440]
# 熟植物速率 Cooked rate
cooked_rate = [0.000, 0.001, 0.005]

# ===================== 2. 设置柱状图分组位置 =====================
x = np.arange(len(plant_names))  # 植物的坐标位置
width = 0.35  # 柱子宽度

# ===================== 3. 绘制分组柱状图 =====================
plt.bar(x - width/2, raw_rate, width, label='Raw rate (cm³/s)', color='lightgreen')
plt.bar(x + width/2, cooked_rate, width, label='Cooked rate (cm³/s)', color='salmon')

# ===================== 4. 添加图表标题和轴标签 =====================
plt.title('Enzyme Activity of Raw vs Cooked Plant Extracts')
plt.xlabel('Plant Species')
plt.ylabel('Reaction Rate (cm³/s)')

# ===================== 5. 设置x轴刻度和图例 =====================
plt.xticks(x, plant_names)
plt.legend()  # 显示图例

# ===================== 6. 保存图片 + 显示图表 =====================
plt.tight_layout()  # 自动调整布局，防止文字重叠
plt.savefig('plant_rate_bar_chart.png', dpi=300)  # 保存高清图片
plt.show()