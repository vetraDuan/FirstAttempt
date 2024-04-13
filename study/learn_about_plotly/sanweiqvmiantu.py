#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :sanweiqvmiantu.py
# @Time      :2024/4/14 2:20
# @Author    :Vetra

import plotly.graph_objects as go
import numpy as np

# 生成x和y的值
x = np.linspace(-8, 8, 100)
y = np.linspace(-8, 8, 100)
# 生成网格点
x, y = np.meshgrid(x, y)
# 生成一个三维曲面图的z值
z = np.sin(np.sqrt(x**2 + y**2))
# 创建一个三维曲面图
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
# 设置标题和坐标轴标签
fig.update_layout(title='三维曲面图示例', scene=dict(xaxis_title='X-axis', yaxis_title='Y-axis', zaxis_title='Z-axis'))

fig.show()


if __name__ == "__main__":
    run_code = 0
