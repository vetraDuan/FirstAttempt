#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :sandiantu_color.py
# @Time      :2024/4/14 2:07
# @Author    :Vetra
import numpy as np
import plotly.express as px
import pandas as pd

# 创建一个示例数据集
np.random.seed(40)
# 创建一个包含50个随机点的数据集
df = pd.DataFrame({'X': np.random.rand(50), 'Y': np.random.rand(50), 'Size': np.random.rand(50) * 30})
# 创建一个包含50个随机点的数据集
fig = px.scatter(df, x='X', y='Y', size='Size', color='Size', title='Scatter Plot with Color Gradient', color_continuous_scale=px.colors.sequential.Plasma)
# 显示图形
fig.show()


if __name__ == "__main__":
    run_code = 0
