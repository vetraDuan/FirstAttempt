#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :qipaotu.py
# @Time      :2024/4/14 2:28
# @Author    :Vetra

import plotly.express as px

# 读取数据
df = px.data.gapminder().query('year==2007')
# 绘制地图
fig = px.scatter_geo(df, locations='iso_alpha', size='pop', hover_name='country', title='Burnaby map')
# 设置地图投影
fig.show()


if __name__ == "__main__":
    run_code = 0
