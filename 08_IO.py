# 입출력
# [학습목표]
# - 파이썬의 입출력 방법들에 대해 이해하고 사용할 수 있습니다
# - 화면 뿐만 아니라 파일의 입출력을 이해하고 사용할 수 있다
# - 입출력과 관련된 유용한 함수들의 사용법을 숙지한다

# 1. 입출력
#---출력
#   ⦿ 화면으로 출력할 때는 print() 함수 사용
#     ☉ 파이썬 버전 2.x 때는 print가 함수가 아니었지만 3,x 에서는 함수로 바뀜
#   ⦿ print 함수의 입력인자로 다음과 같이 구분자(sep), 끝라인(end), 출력(file)을 지정해 줄 수 있음
#   ⦿ 예제와 같이 file을 이용해서 출력을 표준오류(StandardError)로 변경하거나 파일로 바꿀 수 있음
# --- example ---
print('---- print ----')
import sys
print('welcomto', 'python', sep = '~', end = '!', file = sys.stderr)

#--포매팅(formatting)
#   ⦿ Print만으로는 출력이 좀 불편하다고 느낄 수 있으나 format() 메소드를 사용하면 문자열을 그 이상으로 자유롭게 다룰 수 있음
#   ⦿ 문자열 내에서 어떤 값이 들어가길 원하는 곳은 {}로 표시함
#   ⦿ {} 안의 값들은 숫자로 표현할 수 있으며, format 인자들의 인덱스를 사용함
#   ⦿ {} 안의 값을 지정할 때는 format의 인자로 키(key)와 값(value)을 준다
#   ⦿ ** 기호를 사용하면 dictionary를 입력으로 받은 것으로 판단하고 인자를 하나만 받게됨
#   ⦿ 불필요한 index를 생략 가능함
#   ⦿ '!' 기호를 사용해서 문자열 변환을 사용할 수 있음
#     ☉ 파이썬 버전 2.x 때는 print가 함수가 아니었지만 3,x 에서는 함수로 바뀜
#   ⦿ ':' 기호를 이용하여 보다 정교하게 정렬, 폭, 부호, 공백처리, 소수점, 타입 등을 지정할 수 있다
#     ☉ 정렬에 사용되는 기호
#       - '>' 오른쪽 기준
#       - '<' 왼쪽기준
#       - '^' 가운데 기준
#       - '=' 부호와 상관이 있음
#       - '='가 사용되면 공백문자들 앞에 부호가 표시됨. 사용되지 앟으면 공백문자들 뒤, 즉, 숫자 바로 앞에 부호가 표시됨
#     ☉ 부호를 나타내는 기호
#       - '+' 플러스 부호를 나타내라는 뜻
#       - '-' 마이너스 값만 마이너스 부호를 나타내라는 뜻
#       - ' ' 마이너스 값에는 마이너스 부호를 나타내고 플러스일 때는 공백을 표시하라는 뜻
#   ⦿ 정수 이외에 실수에 대한 변환도 제공되며, 'e'는 지수표현을, 'f'는 일반적인 실수 표현을, '%'는 퍼센트 표현을 의미
#   ⦿ 실수에서는 소수점 몇 번째 자리까지 표현할 것인지를 지정 가능
# --- example ---
print('---- formatting ----')
print('{0} is {1}'.format('apple', 'red'))                        # Index 사용
print('{item} is {color}'.format(item = 'apple', color = 'red'))  # Key 사용
dic = { 'item': 'banana', 'color': 'yellow' }
print('{0[item]} is {0[color]}'.format(dic))                      # dictionary를 입력으로 받는경우
print('{item} is {color}'.format(**dic))                          # ** 사용
print('{item!s} is {color!s}'.format(**dic))                      # !s => str() 를 실행한 결과와 동일
print('{item!r} is {color!r}'.format(**dic))                      # !r => repr() 를 실행한 결과와 동일
print('{item!a} is {color!a}'.format(**dic))                      # !a => ascii() 를 실행한 결과와 동일
print('{0:$>-5}'.format(-10))                                     # 마이너스 값만 부호를 나타내라는 뜻
print('{0:b}'.format(10))                                         # 2진수로 변경하여 표현
print('{0:o}'.format(10))                                         # 8진수로 변경하여 표현
print('{0:c}'.format(65))                                         # ascii code 문자열로 표현 
print('{0:#x}, {0:#o}, {0:#b}'.format(10))                        # 16진수, 8진수, 2진수로 표시
print('{0:e}'.format(4 / 3))                                      # e는 지수표현
print('{0:f}'.format(4 / 3))                                      # f는 실수 표현
print('{0:%}'.format(4 / 3))                                      # %는 퍼센트 표현
print('{0:.3f}'.format(4 / 3))                                    # .3f는 실수 세자리까지 표현

#---입력
#   ⦿ 사용자로부터 입력은 다음과 같이 input()함수를 이용해서 받을 수 있음
#   ⦿ input의 입력 인자로는 화면에 출력할 프로프트(prompt)를 줄 수 있으며, 생략 가능
#   ⦿ 결과값으로는 문자열 객체를 반환함
# a = input('insert any keys : ')
# print(a)

# 2. 파일 입출력
#---파일 입출력 - open
#   ⦿ 파일 입출력 제어를 보다 세밀하게 하기 위해서는 open() 함수를 통해서 파일을 연 후, 파일 전용 함수들을 이용해서 작업하는 것이 일반적
#   ⦿ 기본형: 파일객체 = open(file, mode)
#   ⦿ open 함수의 마지막 인자인 mode는 파일을 열 때의 속성을 의미하며, 다음 속성들의 조합으로 사용이 가능함
#     ☉ r: 읽기 모드 (default)
#     ☉ w: 쓰기 모드
#     ☉ a: 쓰기 + 이어쓰기 모드
#     ☉ b: 바이너리 모드
#     ☉ +: 읽기 + 쓰기 모드
#     ☉ t: 텍스트 모드 (default)

#---파일 입출력 - write, close
#   ⦿ 파일로부터 읽고 쓰기 위해서 파일로부터 모든 데이터를 읽는 read() 함수와 문자열을 쓰는 write() 함수가 제공됨
#   ⦿ 또한 파일을 열고 할 일을 모두 완료했을 경우 파일객체를 닫아주는 close() 함수가 있음
# ---- example ----
print('---- 파일 입출력 - write, close ----')
f = open('test.txt', 'w')
f.write('plow deep\nwhile sluggards sleep')
f.close()

#---파일 입출력 - read
#   ⦿ 텍스트 모드에서는 일반 문자열과 같이 encoding이 적용되기 때문에, 바이너리 데이터(binary data)를 다룰 때에는 오류가 발생함
#   ⦿ 바이너리 데이터를 다룰 때에는 반드시 바이너리 모드를 사용해야함!
# ---- example ----
print('---- 파일 입출력 - read ----')
f = open('test.txt', 'r')
print(f.read())
f.close()
print(f.closed)

#---파일 입출력 - readline, readlines, tell, seek
#   ⦿ 파일 입출력 관련 함수들
#     ☉ readline() 함수 : 호출할 때 마다 한 줄씩 읽은 문자열을 반환함
#     ☉ readlines() 함수 : 파일의 모든 내용을 줄 단위로 잘라서 리스트를 반환함
#     ☉ tell() 함수 : 현재파일에서 어디까지 읽고 썼는지 위치를 반환함
#     ☉ seek 함수 : 사용자가 원하는 위치로 포인터를 이동함
#   ⦿ with ~ as 구문
# ---- example ----
print('---- with ~ as 구문 ----')
with open('test.txt') as f:
  print(f.readlines())
  print(f.closed)
  f.close()
  print(f.closed)

#---pickle
#   ⦿ pickle로 파일에 쓰거나 읽을 떄는 반드시! 바이너리 모드로 파일을 열어야함!
#   Q. 문자열의 경우에는 배운 방법을 사용하여 쉽게 다룰 수 있지만, 리스트나 클래스 등을 저장할 때는 어떻게 해야 할까요?
#   Q. 내용을 모두 분해해서 파일에 저장한 후, 다시 읽어 들일 때는 구분해서 다시 값을 설정해야 할까요?
#   A. 파이썬에서는 이러한 일들을 쉽게 할 수 있도록 도와주는 pickle이라는 모듈이 있음
#---pickle - 쓰기
#   ⦿ pickle 모듈의 dump 함수를 사용하면, 쉽게 파일에 저장 가능
# ---- example ----
import pickle
colors = ['red', 'green', 'blue']
f = open('colors', 'wb')
pickle.dump(colors, f)
f.close()

#---pickle - 읽기
#   ⦿ clolors를 삭제한 후, load 함수를 이용해서 리스트를 읽어 들임
del colors
f = open('colors', 'rb')
colors = pickle.load(f)
f.close()
print(colors)

#---pickle - 사용자 정의 클래스
#   ⦿ pickle로 저장할 수 있는 대상은 파이썬 객체라면 거의 모두 가능
#   ⦿ 기본 자료형은 물론이고 사용자가 정의한 클래스 객체도 pickle이 가능
class test:
  var = None
a = test()
a.var = 'Test'
f = open('test', 'wb')
pickle.dump(a, f)
f.close()
f = open('test', 'rb')
b = pickle.load(f)
f.close()
print(b.var)