# -*- coding:utf-8 -*-
# author: vetra


# mysql数据库基本操作

import pymysql


connection = pymysql.connect(user='root', password='111111', db='first_test')
cursor = connection.cursor()
cursor.execute("select title, con from duanzixing limit 10;")

di = {}
for i in cursor.fetchall():
    print("标题：" + i[0])
    print("内容：" + i[1] + '\n')
connection.close()