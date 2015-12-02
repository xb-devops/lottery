#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
这是一个随机生成双色球号码的程序

"""

import random

def range_ssq():
    i = 1
    ssq_redball = []
    ssq_blueball = []
    while i < 7 :
        ssq_redball.append(random.randint(1,33))
        i += 1
    if len(set(ssq_redball)) != 6:
        ssq_redball.append(random.randint(1,33))
    else :
        pass
    ssq_blueball.append(random.randint(1,14))
    print "随机生成一注双色球号码为:",sorted(set(ssq_redball)),ssq_blueball

def zhiding_ssq():
    i = 1
    ssq_redball = []
    ssq_sdsr_blueball = []
    while i < 7:
        ssq_sdsr_redball = int(raw_input("请输入选择[1..33]之间红球号码："))
        i += 1
        if  ssq_sdsr_redball <= 0 or ssq_sdsr_redball > 33:
            ssq_sdsr_redball = int(raw_input("请重新输入[1..33]之间红球号码："))
        else:
            pass
        ssq_redball.append(ssq_sdsr_redball)
    while len(set(ssq_redball)) != 6:
        ssq_sdsr_redball = int(raw_input("请输入选择[1..33]之间红球号码："))
        ssq_redball.append(ssq_sdsr_redball)
    else :
        pass
    ssq_sdsr_blueball = int(raw_input("请输入选择[1..14]之间红球号码："))
    if ssq_sdsr_blueball <= 0 or ssq_sdsr_redball > 14:
        ssq_sdsr_blueball = int(raw_input("请输入选择[1..14]之间红球号码："))
    else:
        pass
    print "手动选号结果为:",sorted(set(ssq_redball)),ssq_sdsr_blueball







x=int(raw_input("双色球机选输入1；双色球手选请输入2:"))

if x == 1:
    range_ssq()
elif x == 2:
    zhiding_ssq()
else:
    print "输入错误"
