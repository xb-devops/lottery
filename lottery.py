#!/usr/bin/env python
#-*- coding:utf-8 -*-
import shuangseqiu

x=int(raw_input("双色球机选输入1；双色球手选请输入2:"))

if x == 1:
    range_ssq()
elif x == 2:
    zhiding_ssq()
else:
    print u"输入错误"
