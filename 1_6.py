#coding:utf-8

#参数检查
# def my_abs(x):
    # if x >= 0:
        # return x
    # else:
        # return -x
# print(my_abs(4))
# print(my_abs(-2))  #到这里都能成功执行，因为传入的参数可以与0进行判断
# print(my_abs(a))   #此时将会报错，因为str类型无法与int类型进行比较
#对此，我们应该在自定义代码中添加对传入参数的检查代码

# def my_abs(x):
    # if not isinstance(x,(int,float)):
        # raise TypeError('bad operand type')
    # if x >= 0:
        # return x 
    # else:
        # return -x 


#自定义函数quadratic(a,b,c)
def quadratic(a,b,c):
    import math
    delta = b**2 - 4*a*c
    if delta < 0:
        raise TypeError("No answer")
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    return x1,x2

