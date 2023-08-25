# -*- coding:utf-8 -*-
# author: vetra

# 递归函数
# 高斯求和问题，1+2+3+4+...+99+100
# 不使用递归
def sum_number(n):
    su = 0
    for i in range(1, n + 1):
        su += i
    return su


sum_number(100)


# 使用递归
def sum_number2(n):
    if n <= 0:
        return 0
    return n + sum_number2(n - 1)


sum_number2(100)
"""
每一个递归程序都遵循相同的基本步骤：
1. 初始化算法。递归程序通常需要一个开始时使用的种子值。可以向函数传递参数，或者提供一个入口函数，这个函数是非递归的，但可以为递归计算这是种子值。
2. 检查要处理的当前值是否已经与基线条件相匹配。如果匹配，则进行处理并返回值。
3. 使用更小的或更简单的子问题（或多个子问题）来重新定义答案。
4. 对子问题进行算法。
5. 将结果合并入答案的表达式。
6. 返回结果。
"""

