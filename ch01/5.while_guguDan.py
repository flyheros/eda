# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:48:40 2019

@author: shkim
"""

dan = 1
while(dan):

........

print("구구단 게임을 종료합니다.")

#%%

#i = int(input("number:"))



for i in range(1,10):
  for j in range(1,10):
    print(i, '*', j, '=', j*i)
    if(j==9) :
        print ("-------")
        
        
        
#%%
        
dan=1
while(dan):
    dan=input("number")
    dan=int(dan)
    if not (1<=dan<10):
        print("incorrect number")
        continue
    
    else:        
        print(dan, "dd")
        for i in range(1,10):
            print(i, '*', dan, '=', dan*i)