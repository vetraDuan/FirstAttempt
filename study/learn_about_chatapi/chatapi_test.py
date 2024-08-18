#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :chatapi_test.py
# @Time      :2024/8/18 19:08
# @Author    :Vetra

# from openai import OpenAI
#
# client = OpenAI(
#     # defaults to os.environ.get("OPENAI_API_KEY")
#     api_key="sk-b6LIcMHykEPw5ciYlvrLzcVfrmlStKRXajAH0Krc2SpW1SDP",
#     base_url="https://api.chatanywhere.tech"
#     # base_url="https://api.chatanywhere.cn/v1"
# )

'''
curl https://api.chatanywhere.tech/v1/chat/completions
  -H 'Content-Type: application/json'
  -H 'Authorization: sk-b6LIcMHykEPw5ciYlvrLzcVfrmlStKRXajAH0Krc2SpW1SDP'
  -d '{
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": "Say this is a test!"}],
  "temperature": 0.7
}'
'''

import http.client
import json
import time

headers = {
       'Authorization': 'sk-b6LIcMHykEPw5ciYlvrLzcVfrmlStKRXajAH0Krc2SpW1SDP',
       'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
       'Content-Type': 'application/json'
    }


def chat_with_robot(message_send):
    conn = http.client.HTTPSConnection("api.chatanywhere.tech")
    payload = json.dumps({
       "model": "gpt-3.5-turbo",
       "messages": [
          {
             "role": "user",
             "content": message_send
          }
       ]
    })

    conn.request("POST", "/v1/chat/completions", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))['choices'][0]['message']['content']


def listen_chat():
    wait = 1
    while True:
        message = input("请输入：")
        if message == 'exit':
            break
        print(chat_with_robot(message))
        time.sleep(wait)


if __name__ == '__main__':
    listen_chat()