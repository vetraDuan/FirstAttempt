#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :zhexiantu.py
# @Time      :2024/4/14 1:58
# @Author    :Vetra

import plotly.graph_objects as go
import numpy as np

# 创建一个简单的折线图
x = np.linspace(0, 10, 100)
y = np.sin(x)
# 创建一个图形对象
fig = go.Figure(data=go.Scatter(x=x, y=y))
# 设置标题和坐标轴标签
fig.update_layout(title="Sin Wave", xaxis_title="x", yaxis_title="sin(x)")
# 显示图形
fig.show()


if __name__ == "__main__":
    run_code = 0
