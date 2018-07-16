# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 08:43:31 2018

@author: DELL
"""

'''
题目005：输入三个整数x,y,z，请把这三个数由小到大输出。
'''

def tm005():
    ls = input("输入三个数字例如：123 \n")
    new_ls = sorted(ls)
    print(new_ls)

tm005()

'''
题目006：斐波那契数列。0、1、1、2、3、5、8、13、21、34、……。
'''

def tm006():
    a = [0,1]
    for i in range(2,100):
        a.append(a[i-1]+a[i-2])
import time
t1 = time.clock()
tm006()
escaped = time.clock() - t1
print("运行时间是%f"%escaped)

'''
题目007：将一个列表的数据复制到另一个列表中。
'''
def tm007():
    a = [1,2,3]
    b = a 
    c = a[:]
    print(id(a),id(b),id(c))
tm007()
# 可以看到b和a的地址是相同的，而c与a的地址不同，所以b操作只是改名，c操作才是复制。
    
    
    
    
    
    
    




