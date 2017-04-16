#coding:utf-8

#默认参数与位置参数的位置问题
# def power(x,n = 2):
	# s = 1
	# while n > 0:
		# n = n -1
		# s = s * x 
	# return s
# print(power(2))
# print(power(2,2))
# print(power(2,3))
# def power3(n = 2,x):
	# s = 1 
	# while n > 0:
		# n = n -1
		# s = s * x 
	# return s
# print(power3(2,2))
# print(power3(2))
# def infor(name,age=6,city='wuhan'):
	# print(name+str(age)+city)
# infor('didi')
# infor('didi',6,'wuhan')
# infor('didi',city='wuhan',age=6)


#默认参数与可变数据类型
# def add_end(L=[]):
    # L.append('END')
    # return L
# #正常调用
# print(add_end([4,3,9,6]))
# print(add_end([2,3,3]))
# #默认调用
# print(add_end())
# print(add_end())


#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# # person('Michael', 30)
# output: name: Michael age: 30 other: {}
# # person('Bob', 35, city='Beijing')
# output: name: Bob age: 35 other: {'city': 'Beijing'}
# # person('Adam', 45, gender='M', job='Engineer')
# output: name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

# # extra = {'city': 'Beijing', 'job': 'Engineer'}
# # person('Jack', 24, city=extra['city'], job=extra['job'])

def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')
#output Jack 24 Beijing Engineer
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
