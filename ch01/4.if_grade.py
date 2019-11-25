# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:58:39 2019

@author: shkim
"""

score = int(input ("your score:"))

if score >= 90:
    grade = 'A'
if 90> score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)


#%%

for looper in [1,2,3,4,5] :
    print (looper)
    
    
for looper in range(100):
    print(looper)
    
for i in "abcef":
    print(i)
    
for i in ["abc", "def"]:
    print(i)

#%%
for j in range(1,10,2):
    print(j)
    
    
        