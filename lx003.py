'''
题目003：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''
def tm003():
    ''' 
    note
    '''
    import math as m
    for i in range(1000):
        if m.sqrt(i+100)%1==0 and m.sqrt(i+100+168)%1==0:
            print(i)

tm003()

'''
题目004：输入某年某月某日，判断这一天是这一年的第几天:
'''

def tm004():
    ''' 
    利用time库的struct_time格式与格式化时间格式（strftime）之间的互相转化。strptime()把输入的格式化时间转成struct_time格式。
    '''
    import time
    date = input("请输入时间：（如2008年1月1日）")
    d = time.strptime(date,"%Y年%m月%d日")
    print(d.tm_yday)  #yday的属性就是计算当年的第几天
    print(d[7])       #yday元素位于日期元组的第8位


tm004()

'''
小结：
1.标准库的调用
2.time库中strptime的使用和时间格式的转化
'''