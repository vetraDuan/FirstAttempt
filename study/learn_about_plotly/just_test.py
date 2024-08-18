#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :just_test.py
# @Time      :2024/4/23 20:57
# @Author    :Vetra


size = {'101001':{'data':{u'test':{u'volue_size':u'-2'}}},'101003':{'data':{u'test':{u'volue_size':u'null'}}}}
all_size = dict()

for ip, ip_data in size.items():
    code = ip_data.get('code')
    if code == '1':
        for key, value in ip_data.get('data').items():
            if all_size.has_key(key) and all_size[key].get('bucker_size') == 'null':
                all_size[key] = value
            elif not all_size.has_key(key):
                all_size[key] = value
            else:
                continue



if __name__ == "__main__":
    run_code = 0
