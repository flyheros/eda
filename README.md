# Python 기반 오픈소스 AI 관련 라이브러리 활용
## 1. AI를 위한 파이썬 핵심 리뷰
* 개발환경 구축
* 파이썬 리뷰 

<lambda 사용>
from collections import OrderedDict

#word_count 는 key, value 를 가진 dictionary 

od = OrderdDict(sorted(word_count.items(), key=lambda t:t[0])) #lambda란 t를 인수로 받고 return t[0] 하는 간단한 함수 호출시


---------------
<워드 카운팅> : list 로 만들어서 Counter 
from collections import Counter

text = list('Good morning everybody!!') 

c = Counter(text)# 문자 하나하나씩

------------

<list comprehensions>
  
**rst = [i for i in range(10)]
**rst = [i for i in range(10) if i % 2 ==0]
**rst = [ i if i%2==0 else 10  for i in range(10) ]

words = 'The quick brown fox jumps over the lazy dog'.split() #2차원 배열
rst=[[len(w), w.upper(), w.lower()]  for w in words]


s1 = 'abc'
s2 = '12'
# [['a1', 'b1', 'c1'], ['a2', 'b2', 'c2']]
rst = [[j+i for j in s1]  for i in s2 ]
------------
<enumerate> 리스트값에 인덱스를 붙여 출력: enumerate( ) 함수 
  
color = ['red', 'blue', 'white', 'black'] #각 값에 인덱스 달아 dictionary 로 
d_c = {i:j for i,j in enumerate(color) }

------------
<zip>: 리스트값을 묶어 출력
color = ['red', 'blue', 'white', 'black']
cnt = [6, 2, 3, 7]
# {'red': 6, 'blue': 2, 'white': 3, 'black': 7}
col_cnt = {i:j for i, j in zip(color,cnt)}
# [['red', 6], ['blue', 2], ['white', 3], ['black', 7]]
col_cnt = [[i, j] for i, j  in zip(color,cnt)]
  
------------
<reduce>
# reduce 함수 :이전계산값과 다음 인자를 동일하게 계산할때
from functools import reduce
num = [1, 2, 3, 4, 5]
reduce(lambda x,y:x+y, num)
  


## 2. 데이터 사용의 기초 Numpy
Numpy : 수치계산
Pandas: 테이블 데이터


