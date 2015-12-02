#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
双色球选号程序
"""
import random

ssq_list=[]
x=random.randint(1,33)
i = 1
while  x in range(1,34) and i <=6:
    ssq_list.append(x)
    i = i +1
    print ssq_list
