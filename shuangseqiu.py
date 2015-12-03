#!/usr/bin/env python
#-*- coding:utf-8 -*-
print u"""#*******************************\n
这是一个随机生成双色球号码的程序\n
********************************#
"""

import random


#定义自动选号函数
def jixuan_ssq():
    i = 1
    ssq_hongqiu = []
    ssq_lanqiu = []
    while i < 7 :
	    #从1-33中随机生成一个数字 
        ssq_hongqiu.append(random.randint(1,33))
        i += 1
		#判断生成的6个数字中有没有重复的,如果有重复的继续生成至6个
    if len(set(ssq_hongqiu)) != 6:
        ssq_hongqiu.append(random.randint(1,33))
    else :
        pass
	#从1-14中生成一个数字
    ssq_lanqiu.append(random.randint(1,14))
	#打印一组双色球（红球+篮球）号码
    print u"随机生成一注双色球号码为:",sorted(set(ssq_hongqiu)),ssq_lanqiu




#定义手动选号函数
def shouxuan_ssq():
    i = 1
    ssq_hongqiu = []
    ssq_lanqiu = None
    while i < 7:
	    #手动输入一个红球号码
        ssq_sdsr_hongqiu = int(raw_input("请输入选择[1..33]之间红球号码："))
		#判断输入的红球号码是否在范围（1-34）之内
        if ssq_sdsr_hongqiu in [x for x in range(1,34)]:
            ssq_hongqiu.append(ssq_sdsr_hongqiu)
            i += 1
			#判断输入的6个数字是否有重复的
            if len(set(ssq_hongqiu)) == 6:
                break
    while True:
        #手动输入一个篮球号码
        ssq_lanqiu = int(raw_input("请输入选择[1..16]之间蓝球号码："))
	    #判断输入的篮球号码是否在范围（1-16）之内
        if ssq_lanqiu in [x for x in range(1,17)]:
            break
    #输出一组手动选号双色球（红球+篮球）号码   
    print u"手动选号结果为:",sorted(set(ssq_hongqiu)),ssq_lanqiu

