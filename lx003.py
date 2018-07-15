  1 '''
  2 题目003：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
  3 '''
  4 def tm003():
  5     '''
  6     note
  7     '''
  8     import math as m
  9     for i in range(1000):
 10         if m.sqrt(i+100)%1==0 and m.sqrt(i+100+168)%1==0:
 11             print(i)
 12 
 13 tm003()
 14 
 15 '''
 16 题目004：输入某年某月某日，判断这一天是这一年的第几天:
 17 '''
 18 
 19 def tm004():
 20     '''
 21     利用time库的struct_time格式与格式化时间格式（strftime）之间的互相转化。strptime()把输入的格式化时间转>    成struct_time格式。
 22     '''
 23     import time
 24     date = input("请输入时间：（如2008年1月1日）")
 25     d = time.strptime(date,"%Y年%m月%d日")
 26     print(d.tm_yday)  #yday的属性就是计算当年的第几天
 27     print(d[7])       #yday元素位于日期元组的第8位
 28 
 29 
 30 tm004()
