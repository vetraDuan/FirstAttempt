#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :chatapi_test2.py
# @Time      :2024/8/18 19:35
# @Author    :Vetra
import time

from openai import OpenAI

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



def listen_chat():
    wait = 1
    messages = []
    while True:
        msg = input("请输入：")
        if msg == 'exit':
            break
        data = {'role': 'user', 'content': msg}
        messages.append(data)
        gpt_35_api_stream(messages)
        print(content_about_robot)
        print(content_about_robot[-1])

        time.sleep(wait)


if __name__ == '__main__':
    listen_chat()