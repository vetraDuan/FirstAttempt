# -*- coding:utf-8 -*-
# author: vetra

# 实现字符串反转，以逗号作为切割符，切割的子串以单词作为单元反转
# 输入：hello world, god bless you
# 输出：world hello, you bless god
res_str = 'hello world, god bless you'


def reverse_test(res_str):
    res_list = res_str.split(',')
    new_str = ''
    for i in res_list:
        li = i.split(' ')
        li.reverse()
        new_str += ' '.join(li) + ', '
    new_str = new_str.rstrip(', ')
    print(new_str)


if __name__ == '__main__':
    reverse_test(res_str)