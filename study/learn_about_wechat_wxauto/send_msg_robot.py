#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :send_msg_robot.py
# @Time      :2024/8/18 10:06
# @Author    :Vetra


import wxauto
import time
import random

wx = wxauto.WeChat()

lisen_list = [
    'vetrA'
]


for i in lisen_list:
    wx.AddListenChat(who=i, savepic=True)

# 持续监听消息，并且收到消息后回复“收到”
wait = 1  # 设置1秒查看一次是否有新消息
while True:
    msgs = wx.GetListenMessage()
    for chat in msgs:
        who = chat.who  # 获取聊天窗口名（人或群名）
        one_msgs = msgs.get(chat)  # 获取消息内容
        # 回复收到
        for msg in one_msgs:
            msgtype = msg.type  # 获取消息类型
            content = msg.content  # 获取消息内容，字符串类型的消息内容
            print(f'【{who}】：{content}')
            # ===================================================
            # 处理消息逻辑（如果有）
            #
            # 处理消息内容的逻辑每个人都不同，按自己想法写就好了，这里不写了
            #
            # ===================================================

            # 如果是好友发来的消息（即非系统消息等），则回复收到
            if msgtype == 'friend':
                chat.SendMsg('收到')  # 回复收到
    time.sleep(wait)

