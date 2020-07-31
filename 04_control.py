# 제어문
# 학습목표
# - 파이썬의 제어문들에 대해 이해하고 사용할 수 있다
# - 리스트 내장을 이해하고 사용할 수 있다
# - 제어와 관련된 유요한 함수들의 사용법을 숙지한다

# 1. 제어문의 종류 및 사용법
#--- if 문
#   ⦿ 조건식을 평가하고 참인 경우만 구문이 수행
#   ⦿ 2개 이상의 구문은 들여쓰기로 블록을 지정
#     ☉ 함수와 동일
# -  들여쓰기의 정보는 파일 전체를 통틀어 일치해야함
# ---- expample ----
print('---- if ----')
value = 10
if value > 5:
  print('value is bigger then 5')

#--- elif, else
# 1. elif
#   ⦿ 2개 이상의 조건을 처리하는 경우
#   ⦿ if는 가장 처음에만 사용할 수 있는 방면에, elif는 필요한 만큼 사용가능

# 2. else 
#   ⦿ 어떠한 조건에도 해당하지 않는 경우
#   ⦿ 가장 마지막에만 사용가능
# ---- expample ----
# score = int(input('Input Score: ')) # 사용자로부터 정수값을 입력 받는다
print('---- elif, else ----')
score = 76
if 90 <= score <= 100:
  grade = 'A'
elif 80 <= score < 90:
  grade = 'B'
elif 70 <= score < 80:
  grade = 'C'
elif 60 <= score < 70:
  grade = 'D'
else:
  grade = 'F'

print('Grade is ', grade)

# 조건식의 참/거짓 판단
#   ⦿ 기본적으로 자료형의 bool 값과 동일함
#     ☉ True로 판명 : 10 > 0
#     ☉ False로 판명 : 5 > 10
#     False 인 경우 : 0, 0.0, (), [], {}, ''(빈문자열), None인 경우
#     True 인 경우 : False인 경우를 제외한 값이 할당된 경우
# ---- expample ----
print(bool(True))                 # bool 타입
print(bool(False))
print(bool(13))                   # 숫자 계열
print(bool(0.0))
print(bool('apple'))              # 문자열
print(bool(''))
print(bool(()))                   # 시퀀스 계열
print(bool([10, 20, 'Apple']))
print(bool({}))
print(bool(None))                 # None 타입

#---and/or
# 2개 이상의 논리식 판별을 위한 연산자
#    ⦿ 식의 왼쪽에서 오른쪽으로 판별함
# ---- expample ----
print('---- and -----')
score = 60
print(score > 70 and score <= 80) # 두가지 경우가 True일 경우 True
print('score : ', score)
print(score > 70 & score <= 80)   # 'and' 와 '&' 가 동일하게 수행되지않음
print('---- or -----')
math = 70
english = 89
print(math > 80 or english > 80)  # 두가지 경우중 하나라도 True인 경우 True
print(math > 80 | english > 80)   # 'or' 와 '|' 가 동일하게 수행되지않음

#---단축 평가
# Note] 단축 평가란?
# 조건식 전체를 판단하지 않고 순차적으로 진행하다 식 전체가 자명한 경우, 더 이상 수식을 평가하지 않는 방법
#   ⦿ 'and'와 'or'는 단축 평가로 수행되도록 보장
#     ☉ x and y: x가 False인 경우 y값은 평가하지 않음
#     ☉ x or y: x가 True인 경우 y값은 평가하지 않음

# ---- expample ----
a = 0
# 단축 평가 미적용
# if a & 10 / a:
#   print('a가 0입니다.')
# else:
#   print('에러없이 통과!')
# a가 0인 경우 조건식 'a & 10 / a'는 거짓
# 10 / a에 의하여 ZeroDivisionError 발생

# 단축 평가 적용
if a and 10 / a:
  print('a가 0입니다.')
else:
  print('에러없이 통과!')
# 단축 평가의 장점
#   ⦿ 조건식의 결과가 결정되는 시점 이후로 추가적인 판변 연산을 수행하지 않기 때문에 속도 향상
#   ⦿ RunTimeError 발생을 try ~ except 구문이 아닌 논리식으로 사전에 차단 가능

#---while문
# 조건식이 참(True)인 동안 내부 구문을 반복 수행
#   ⦿ 조건식은 구문이 수행되기 이전에 우선 평가
#   ⦿ 구문을 모두 수행이후 다시 조건식을 재평가
#   ⦿ 조건식이 거짓(False)이면 while문 구조를 벗어남
# ---- 사용방법 -----
# while <조건식>:
#     <구문>
print('---- while ----')
# ---- example ----
value = 5
while value > 0:
  print(value)
  value -= 1

#---for문
# 시퀀스형 객체를 순차적으로 순회
# ---- 사용방법 ----
# for <아이템 I> in <시퀀스형 객체 S>:
#     <구문>
#   ⦿ '시퀀스형 객체 S'의 각 아이템을 '아이템 I'에 할당
# ---- example ----
print('---- for ----')
l = ['Apple', 100, 15.23]
for i in l:
  print('value :', i, '| type : ', type(i))

d = {
  'Apple': 100,
  'Orange': 200,
  'Banana': 300
}
for k, v in d.items():
  print('key : ', k, '| value : ', v)

# for 문에서 사용할 수 있는 자료형
#   ⦿ 문자열, 리스트, 튜플, 사전
#   ⦿ 이터레이터, 제너레이터 객체
l = [10, 20, 30]
iterator = iter(l)
for i in iterator:
  print('value : ', i)
#   ⦿ 반복문은 2개 이상 중첩해서 사용 가능
for n in [1, 2]:
  print('-- {0} 단 --'.format(n))
  for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("{0} * {1} = {2}".format(n, i, n * i))
#---break
#   ⦿ break을 만나면 반복문 내부 블록을 벗어남
# ---- example ----
print('---- break ----')
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in L:
  if i > 5:
    break
  print('Item {0}'.format(i))
#---continue
#   ⦿ continue 이후 반복문 내부 블록을 수행하지 않고, 다음 아이템을 선택하여 내부 블록의 시작 지점으로 이동
# ---- example ----
print('---- continue ----')
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in L:
  if i % 2 == 0:
    continue
  print('Item {0}'.format(i))
#---else
#   ⦿ 반복문 수행 도중 break로 인하여 중간에 종료되지 않고 끝까지 수행되었을 때, else 블록이 수행
# ---- example ----
print('---- else ----')
# else 블록이 수행되는 경우
print('else블록이 수행되는 경우')
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in L:
  if i % 2 == 0:
    continue
  print('Item {0}'.format(i))
else:
  print('Exit without break.')
print('Always this is printed')

print('else블록이 수행되지 않는 경우')
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in L:
  if i > 5:
    break
  print('Item {0}'.format(i))
else:
  print('Exit without break.')
print('Always this is printed')

# 2. 리스트 내장
# [표현식] for <아이템> in <시퀀스 객체> (if <조건식>)]
#   ⦿ 기존 시퀀스 객체를 이용하여 추가적인 연산을 통하여 새로운 리스트 객체를 생성
# ---- example ----
print('---- 리스트내장 ----')
l = [1, 2, 3, 4, 5,]
print([i ** 2 for i in l])
t = ['orange', 'apple', 'banana']
print(len(i) for i in t)
#   ⦿ 조건식을 이용하여 원본 객체에서 조건을 만족하는 아이템만 선별
t = ['orange', 'apple', 'banana', 'kiwi']
print([i for i in t if len(i) > 5])
L_1 = [3, 4, 5]
L_2 = [1.5, -0.5, 4]
print([x * y for x in L_1 for y in L_2])

# 3. 유용한 함수들
# 제어문 관련 유용 함수
#---filter(<function> | None, 시퀀스 객체)
#   ⦿ 함수의 결과 값이 참인 시퀀스 객체의 이터레이터를 반환
#   ⦿ None이 오는 경우 필터링하지 않음
# ---- example ----
print('---- filter ----')
L = [10, 25, 30]
IterL = filter(None, L)
for i in IterL:
  print('Item: {0}'.format(i))

def getBiggerThan20(i):
  return i > 20
result = list(filter(getBiggerThan20, L))
print(result)
result2 = list(filter(lambda i : i > 20, L))
print(result2)

#---range(['시작값'], '종료값'[, '증가값'])
#   ⦿ 수열을 순회하는 이터레이터 객체를 반환
#   ⦿ 시작 값과 증가 값은 생략 가능하며, 이떄는 각 0, 1이 할당
# ---- example ----
print('---- range ----')
print(list(range(10))) # 종료값만 있는 경우 - 10은 포함되지 않음
print(list(range(5, 10))) # 시작값, 종료값이 있는 경우
print(list(range(10, 0, -1))) # 시작값, 종료값, 증가값이 있는 경우
print(list(range(10, 20, 2))) # 10부터 20까지 짝수만 출력

#---map(<function>, 시퀀스 객체, ...)
#   ⦿ 시퀀스 객체를 순회하며 function의 연산을 수행
#   ⦿ 함수의 인자 수만큼 시퀀스 객체를 전달
# ---- example ----
print('---- map ----')
L = [1, 2, 3]
def Add10(i):
  return i + 10
for i in map(Add10, L):
  print('Item: {0}'.format(i))

X = [1, 2, 3]
Y = [2, 3, 4]
print(list(map(pow, X, Y)))
