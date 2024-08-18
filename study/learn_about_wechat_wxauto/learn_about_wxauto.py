#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :learn_about_wxauto.py
# @Time      :2024/8/18 9:58
# @Author    :Vetra

from wxauto import *


# 获取当前微信客户端
wx = WeChat()


# 获取会话列表
wx.GetSessionList()

# 向某人发送消息（以`文件传输助手`为例）
msg = '你好~'
who = '文件传输助手'
wx.SendMsg(msg, who)  # 向`文件传输助手`发送消息：你好~


# 向某人发送文件（以`文件传输助手`为例，发送三个不同类型文件）
files = [
    'C:/Users/vetra/Pictures/SnipasteToPycharm.png',
    # 'D:/test/pic.png',
    # 'D:/test/files.rar'
]
who = '文件传输助手'
wx.SendFiles(filepath=files, who=who)  # 向`文件传输助手`发送上述三个文件


# 下载当前聊天窗口的聊天记录及图片
msgs = wx.GetAllMessage(savepic=True, savefile=True)   # 获取聊天记录，及自动下载图片
print(msgs)  # 打印聊天记录