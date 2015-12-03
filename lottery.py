#!/usr/bin/env python
#-*- coding:utf-8 -*-
print u"""#*******************************\n
这是一个随机生成双色球号码的程序\n
*******************************#


"""

import random



def range_ssq():
#定义自动选号函数
    i = 1
    ssq_redball = []
    ssq_blueball = []
    while i < 7 :
        ssq_redball.append(random.randint(1,33))
        #从1-33中随机生成一个数字
        i += 1
    if len(set(ssq_redball)) != 6:
        #判断生成的6个数字中有没有重复的
        ssq_redball.append(random.randint(1,33))
        #如果有重复的继续生成至6个
    else :
        pass
    ssq_blueball.append(random.randint(1,14))
    #从1-14中生成一个数字
    print "随机生成一注双色球号码为:",sorted(set(ssq_redball)),ssq_blueball
    #打印一组双色球（红球+篮球）号码

def zhiding_ssq():
#定义手动选号函数
    i = 1
    ssq_redball = []
    ssq_sdsr_blueball = []
    while i < 7:
        ssq_sdsr_redball = int(raw_input("请输入选择[1..33]之间红球号码："))
        #手动输入一个红球号码
        i += 1
        if  ssq_sdsr_redball <= 0 or ssq_sdsr_redball > 33:
        #判断该红球号码是否<=0或者大于33
            ssq_sdsr_redball = int(raw_input("请重新输入[1..33]之间红球号码："))
        #输入的红球号码不在范围内，就重新输入
        else:
            pass
        ssq_redball.append(ssq_sdsr_redball)
    while len(set(ssq_redball)) != 6:
        ssq_sdsr_redball = int(raw_input("请输入选择[1..33]之间红球号码："))
        #判断输入的红球是否有重复的，有重复的需要重新输入
        ssq_redball.append(ssq_sdsr_redball)
    else :
        pass
    ssq_sdsr_blueball = int(raw_input("请输入选择[1..14]之间蓝球号码："))
    #输入一个1-14之间的篮球号码
    if ssq_sdsr_blueball <= 0 or ssq_sdsr_redball > 14:
    #判断篮球号码是否在1-14之间
        ssq_sdsr_blueball = int(raw_input("请输入选择[1..14]之间红球号码："))
        #不在范围之内，需要重新输入
    else:
        pass
    print "手动选号结果为:",sorted(set(ssq_redball)),ssq_sdsr_blueball
    #输出一组手动选号双色球（红球+篮球）号码   






x=int(raw_input("双色球机选输入1；双色球手选请输入2:"))

if x == 1:
    range_ssq()
elif x == 2:
    zhiding_ssq()
else:
    print u"输入错误"
