# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:22:34 2019

@author: shkim
"""

"""
# 키워드 인수 (keyward arguments)
"""
#%%
def print_something(my_name, your_name):
    print("Hello {},   My name is {}".format(your_name, my_name))

print_something("kim", "lee")
print_something("lee", "kim")
print_something( your_name="kim", my_name="lim" )

#%%
def kwargs_test(**kwargs ):  #dictionary point 개념
    print(type(kwargs))
    print("First value is {first}".format(**kwargs))
    print("Second value is {second}".format( **kwargs ))
    print("Third value is {third}".format( **kwargs ))

kwargs_test(first = 3, second = 4, third = 5, a=10)
#kwargs_test(n1 = 3, n2 = 4, n3 = 5)  # error

#%%
def kwargs_test(*kwargs ):  #tuple 개념
    print(type(kwargs))
    print("First value is {0}".format(*kwargs))
    print("Second value is {2}".format( *kwargs ))
    print("Third value is {1}".format(*kwargs ))

kwargs_test(3, 4,  5)
#kwargs_test(n1 = 3, n2 = 4, n3 = 5)  # error

#%%
def kwargs_test(kwargs ):  #tuple 개념
    print(type(kwargs))
    print("First value is {}".format(kwargs))
    print("Second value is {}".format(kwargs ))
    print("Third value is {}".format(kwargs ))

kwargs_test([3, 4,  5])
#kwargs_test(n1 = 3, n2 = 4, n3 = 5)  # error
#%%
"""
# 디폴트 인수 (default arguments)
"""
#%%
def print_something(my_name, your_name='park'):
    print("Hello {}, My name is {}".format(your_name, my_name))

print_something("kim", "lee")
print_something(my_name="lim")




#%%
"""
# 가변 인수 (variable arguments)
"""
#%%
def vararg_test(a, b,*args ):
    print(args[1])
    print(args)

print(vararg_test(1, 2, 3, 4, 5))  # 3,4,5


#%%
def vararg_test(a, b, *args ):  #args 는 tuple형식(값을 못바꿔)
    c=[*args] # tuple -->list 로 c 에 저장
    
    d=c
    print(d.__addr__)
    c[1]=44
    print(c)

print(vararg_test(1, 2, 3, 4, 5))  # 3,4,5


