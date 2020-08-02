# 숫자 다루기
# [학습목표]
# 파이썬의 수학 관련 모듈에 대해 이해하고 사용할 수 있다
# 분수와 랜덤 모듈을 이해하고 사용할 수 있다
# 부동 소수점 방식과 문제점에 대해서 이해할 수 있다

# 1. 수학(Math) 모듈
#----내장함수
#   ⦿ 특별한 모듈 임포트 없이 사용 가능
#           함수명              |            설명  
#   sum(iterable[, start])          순회 가능한(iterator)객체의 총 합계를 반화
#   max(iterable)                   순회 가능한 객체의 최대값을 반환
#   min(iterable)                   순회 가능한 객체의 최소값을 반환
#   abs(x)                          x의 절대값을 반환
#   pow(x, y [z])                   x의 y 제곱 값을 반환
#   pow(x, y [z])                   x의 y 제곱 값을 반환
#   round(x[, n])                   x의 반올림 결과를 반환
#   divmod(a, b)                    'a/b'의 몫과 나머지를 튜플 형태로 변환

# ---- example ----
l = list(range(0, 10))
print(sum(l))
print(max(l))
print(min(l))
print(abs(-11))
print(pow(2, 10))

#----math 모듈의 수치 연산 함수들
#             함수            |                   설명
#        match.ceil(x)               'N >= x'를 만족하는 가장 작은 정수 N을 반환
#        match.floor(x)              'N <= x'를 만족하는 가장 큰 정수 N을 반환
#        match.trunc(x)              x의 정수 부분만을 반환
#        match.copysign(x)           y의 부호만 x에 복사하여 반환
#        matc.fabs(x)                x의 절대값을 반환
#        match.factoria(x)           x의 계승(factorial, x!) 값을 반환
#        match.fmod(x)               나머지 연산을 수행
#        match.fsub(x)               입력받은 값의 합계를 반환
#        match.modf(x)               입력받은 x의 순수 소수부분과 정수 부분으로 분리하여 튜플로 반환

# ---- example ----
print('---- 수치연산 ----')
import math
print(math.ceil(3.14))
print(math.floor(3.14))
print(math.trunc(3.14))
print(math.fmod(5.5,3)) # 피제수와 제수의 부호가 같은 경우 
print(math.fmod(-5.5,3)) # 피제수와 제수의 부호가 다은 경우

#----지수, 로그 연산
#             함수            |                   설명
#      match.pow(x,y)               'N >= x'를 만족하는 가장 작은 정수 N을 반환
#      match.sqrt(x)                'N <= x'를 만족하는 가장 큰 정수 N을 반환
#      match.exp(x)                 x의 정수 부분만을 반환
#      match.log(x[, base])         y의 부호만 x에 복사하여 반환

#----삼각함수 연산
#             함수            |                   설명
#      match.degrees(x)             라디안으로 표현된 각도를 60분법으로 변환
#      match.radians(x)             60분뻐으로 표현된 각도를 라디안으로 변환
# math.sin(x), math.asin(x), math,cosh(x), math.cos(x), match.atan(x), math.sinh(x), math.atanh(x), match.tan(x), math.acos(x), math.tanh(x), math.acosh(x)

# 2. 분수 모듈
#----Fraction 클래스
#   ⦿ 유리수와 관련된 연산을 효율적으로 처리할 수 있는 분수(fractions) 모듈
#   ⦿ Fraction 클래스의 생성자
#     ☉ function Fraction(분자 = 0, 분모 = 1)
#     ☉ function Fraction(Fraction 객체)
#     ☉ function Fraction(문자열)
# ---- example ----
print('---- fraction ----')
from fractions  import Fraction
print(Fraction(4, 16))
print(Fraction(3))
print(Fraction('3.14'))

#----지원 메소드
#   ⦿ 기본적인 연산 및 floor, ceil, round도 사용 가능하며, 최대공약수를 반환하는 클래스 메소드도 존재
print('---- 지원 메소드 ----')
f = Fraction.from_float(3.14)
print(f.__floor__())
import math
print(math.floor(f))
print(math.ceil(f))
print(round(f))


# 3. 십진법 모듈
#----부동 소수점 표현 방식
#   ⦿ 정수 : 고정 소수점 방식
#   ⦿ 실수 : 부동 소수점 방식
#     ☉ 소수점의 위치를 고정하지 않고, 그 위치를 나타내는 수를 따로 적는 방식
#     ☉ 유효숫자를 나타내는 가수와 소수점의 위치를 풀이한느 지수로 나누어서 표현
#     ☉ '[가수] * [밑수][지수]'와 같은 형태
#     ☉ 컴퓨터 시스템은 밑수를 2로 하고, 부호를 나타내는 하나의 비트를 추가하여 세 부분으로 나누어서 실수를 표현
#       부호(1)       지수부(8)       기수부(23)

#----부동 소수점의 문제
#   ⦿ 결합법칙 예제
print('---- 부동 소수점의 문제 ----')
print((1234.567 + 45.67844) + 0.00004)
print(1234.567 + (45.67844 + 0.00004))

#----Decimal 객체 생성
#   ⦿ 생성자
#     ☉ decimal.Decimal([value[, context]])
# ---- example ----
print('---- decimal 객체 ----')
import decimal

print(decimal.Decimal(3))                             # 정수
print(decimal.Decimal('1.1'))                         # 문자열
print(decimal.Decimal((0, (3, 1, 3), -2)))            # 튜플
print(decimal.Decimal('-infinity'))                   # 음수의 무한대
print(decimal.Decimal('NaN'))                         # NaN(Not a Number)

#----Decimal 객체의 연산
#   ⦿ 모든 수치 연산과 내장 함수의 인자로 전달 가능
# ---- example ----
print('---- deciaml 객체 연산 ----')
a, b = decimal.Decimal('3.14'), decimal.Decimal('.04')
print('a + b : ', a + b)
print('a - b : ', a - b)
print('a * b : ', a * b)
print('a / b : ', a / b)
print('a ** b : ', a ** b)
rawData = '3.45|5.3|1.65|9|-1.28'
l = [decimal.Decimal(x) for x in rawData.split('|')]
print('l : ', l)
print(max(l))
print(min(l))
print(sum(l))
print(sorted(l))

# 4. 랜덤 모듈
#----여러가지 random 메소드
#                       메소드                  |                      설명
#   random.seed([x])                                   임의 숫자 생성기의 초기화 작업을 함
#   random.random()                                    '0.0 <= F < 1.0' 사이의 임의의 float 숫자를 반환
#   random.uniform(a, b)                               인자로 받은 두 값 사이의 임의의 float 숫자를 반환
#   random.gauss(m, sb)                                가우스 분포의 난수를 반환
#   random.randrange([star t], stop[, step])           내장 함수인 range()의 아이템 중에서 임의로선택하여 반환
#   random.randint(a, b)                               'a <= N <= b'인 임의의 정수 N을 반환
#   random.choice(seq)                                 입력받은 시퀀스 객체의 임의의 아이템을 반환
#   random.shuffle(x[, random])                        입력받은 시퀀스 객체를 섞음

#----임의의 실수 생성
# ---- example ----
print('---- 임의의 실수 생성 ----')
import random
print(random.random())
print(random.random())
print(random.uniform(3, 4))
for i in range(3):
  print(random.gauss(1, 1.0))

#----임의의 정수 생성
# ---- example ----
print('---- 임의의 정수 생성 ----')
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20), 10))

#----임의의 시퀀스
# ---- example ----
print('---- 임의의 시퀀스 ----')
l = list(range(10))
print(l)
print([random.choice(l) for i in range(3)])
print(random.sample(l, 3))
l2 = list(range(10))
print(l2)
random.shuffle(l2)
print(l2)