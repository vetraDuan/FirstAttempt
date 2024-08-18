#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :wxauto_with_chatapi.py
# @Time      :2024/8/18 20:17
# @Author    :Vetra

import wxauto
import time

from openai import OpenAI

wx = wxauto.WeChat()

client = OpenAI(
    api_key="",
    base_url="https://api.chatanywhere.tech/v1"
)


content_about_robot = []


# 非流式响应
def gpt_35_api(messages: list):
    """为提供的对话消息创建新的回答

    Args:
        messages (list): 完整的对话消息
    """
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    print(completion.choices[0].message.content)


def gpt_35_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
    """
    stream = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        stream=True,
    )
    data = ''
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            data += chunk.choices[0].delta.content
            # 将data信息添加到content_about_robot列表中
    content_about_robot.append(['{}'.format(data)])


# def listen_chat():
#     wait = 1
#
#
#         time.sleep(wait)


def wechat_with_gpt():
    # 监听好友消息
    lisen_list = [
        'vetrA',
        '王璐瑶',
        '王旭东'
    ]
    for i in lisen_list:
        wx.AddListenChat(who=i)
    # 持续监听消息
    messages = []
    # wait = 1  # 设置1秒查看一次是否有新消息
    while True:
        msgs = wx.GetListenMessage()
        for chat in msgs:
            who = chat.who  # 获取聊天窗口名（人或群名）
            one_msgs = msgs.get(chat)  # 获取消息内容

            for msg in one_msgs:
                msgtype = msg.type  # 获取消息类型
                content = msg.content  # 获取消息内容，字符串类型的消息内容
                print(f'【{who}】：{content}')

                data = {'role': 'user', 'content': content}
                messages.append(data)
                gpt_35_api_stream(messages)
                # print(content_about_robot)
                result = content_about_robot[-1][0]


                # 如果是好友发来的消息则回复
                if msgtype == 'friend':
                    chat.SendMsg(result)  # 回复
        # time.sleep(wait)


if __name__ == '__main__':

    wechat_with_gpt()

