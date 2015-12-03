#!/usr/bin/env python
#-*- coding:utf-8 -*-
import shuangseqiu

num=int(raw_input("双色球机选输入1；双色球手选请输入2:"))


if num == 1:
	shuangseqiu.jixuan_ssq()
elif num == 2:
    shuangseqiu.shouxuan_ssq()
else:
    print u"输入错误"
