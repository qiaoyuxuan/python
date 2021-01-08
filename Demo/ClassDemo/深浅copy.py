#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2021/1/6 14:55
author：乔誉萱
说明：深copy和浅copy，第一次学习
:param 
:param 
'''
# 直接赋值，默认是浅拷贝，传递对象的引用而已，原始列表改变，被赋值的b也会做相同的改变--------------------------------------
alist = [1,2,3,['a','b']]
b = alist
alist.append('4')
print("直接赋值：原始对象alist：{0}，赋值对象：{1}".format(alist,b))

# 浅拷贝-----------------------------------------------------------------------------------------------------------
# 只copy最外面一层[1,2,3]，而对象中的子对象['a','b']不会拷贝。
# 所以当原始对象外层发生改变后，copy的对象不会发生变化；
# 但原始对象的子对象发生改变后，copy对象会发生变化'
import copy

alist = [1,2,3,['a','b']]  # 外层对象是[1,2,3]，子对象是['a','b']
c = copy.copy(alist)  # 浅拷贝
alist.append('copy')  # 原始对象改变外层，copy
print("浅copy：改变外层数据后原始对象alist:{0}，copy的对象c没有发生改变：{1}".format(alist,c))

alist[3].append('c')  # ['a','b']是alist的子对象，
print("浅copy：改变子对象后原始对象alist:{0}，copy的对象c的子对象发生了改变{1}".format(alist,c))


# 深拷贝，copy整个对象包括子对象，所以原始对象的改变不会改变深拷贝里任何元素----------------------------------------------
blist = [1,2,3,['a','b',['我是子对象']]]
dc = copy.deepcopy(blist)
blist.append(4)
blist[3].append('c')
blist[3][2].append('我是append的子对象')
print('深copy：改变子对象后原始对象blist：{0}，copy的对象dc没有发生任何改变{1}'.format(blist,dc))
