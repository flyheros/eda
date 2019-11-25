# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:52:25 2019

@author: shkim
"""

......
    print('\naddr_eggs1:', .... )
    print('spam_eggs1:', .... )
    eggs.append(1)      # 기존 객체의 주솟값에 1[] 추가
    eggs = [2, 3]       # 새로운 객체 생성
    print('\naddr_eggs2:', ..... )
    print('spam_eggs2:', eggs)


ham = [0]
print('-->main_addr_ham:', .... )
spam(ham)
print('\nmain_ham:', ham)



#%%
def spam(eggs):
    print(eggs.__add__)
    eggs.append(1)
    print(eggs.__add__)
    eggs=[2,4]  ##함수 내에서 새롭게 값을 지정하면 다른 객체인 지역변수 생성
    print(eggs.__add__)
    
    print(eggs)
    

ham=[0]
print ("ddd")
print ("ham address:" , ham.__add__)



spam(ham)
ham