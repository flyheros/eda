# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:22:15 2019
@author: shkim
"""

"""
cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white', 'pupple']
"""



color1 = ["red", "blue", "green"]
color1[1]=color1[2]


len(color1)

type(color1)



cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
cities[0:2]
cities[3:-2]
cities[0:len(cities)]

cities[:8]
cities[5:]

cities



#%% 
#append 와 extend의 차이점

color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white', 'pupple']

color1.append(color2)
color1.remove("orange")
color1
#%%

color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white', 'pupple']

color1.extend(color2)

color1
#%%
color1 = ['red', 'blue', 'green']
color1
color1.remove("red")

color1.remove("green")

print(color2)
