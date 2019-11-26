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

## 2. 데이터 사용의 기초 Numpy
