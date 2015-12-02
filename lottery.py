#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
这是一个生成双色球号码的程序
'''



import random
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
print sorted(ssq_redball),ssq_blueball

