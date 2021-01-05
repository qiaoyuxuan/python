#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/10/23 10:18   乔誉萱

类的继承：
1、继承是为了重用已经存在的数据和行为，减少重复代码
2、子类可以继承父类的所有实例属性和方法，实例属性是可选的，可以继承，也可以不继承
3、子类继承父类的类属性是不可选的，默认继承
4、当子类重写了父类的方法，子类调用的就是自己的方法，父类方法不再调用（执行顺序是先子后父，自下而上的）
5、当子类没有重写父类方法，调用的则是父类方法（执行顺序是先父后子，自上而下）
'''

'''案例1：类的继承、实例属性的继承'''
class Father(object):
	def property(self):
		print('我是父类')

class Son(Father):
	def __init__(self,age):
		self.age = age
	
	def property(self):
		print('我是子类，我{0}岁了'.format(self.age))

class GrandSon(Son):
	# 如果此孙类没用init实例化属性，在需要继承父类属性时直接[self.变量名]即可,无需写Son.__init__(self,age)
	def __init__(self,age,sex):
		Son.__init__(self,age)  # 继承父类实例化属性
		self.sex = sex
	
	def property(self):
		print('我是孙类，我{0}岁了,我是{1}'.format(self.age,self.sex))

# 实例化父类
f = Father()
f.property()

# 实例化子类
s = Son(30)
s.property()

# 实例化孙类
gs = GrandSon(8,'男生')
gs.property()




'''案例2：类属性的继承'''
class ChinaPerson(object):
	china = '地球'
	print(china)

class UsaPerson(ChinaPerson):
	pass

u = UsaPerson()  # 实例化类
u.china  # UsaPerson类可以直接调用Person类的类属性


'''
案例3：多个类的继承。
1、遵循从左到右的原则，Son先去Mother类中找eat，若没有再去Father中找，若还没有则去Person中找
（虽然没有继承Person，但Person是Father的父类，若在Father类中未找到则会去父类Person中找)
2、被继承的父类是有书写顺序的，必须是从下到上，即下面案例中的Son子类若写成：class Son(Father,Mother)，程序会报错
'''

class Person(object):
	def eat(self):
		print('人都喜欢吃')

class Father(Person):
	def eat(self):
		print('爸爸喜欢吃肉')

class Mother(Father):
	def eat(self):
		print('妈妈喜欢吃菜')


class Son(Mother,Father):  #被继承的父类必须遵从从下到上的书写顺序，若这里的先写Father再写Mother，程序会报错
	pass

s=Son()
s.eat()

