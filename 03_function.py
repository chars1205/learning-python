# 함수
# 함수는 여러개의 문장(statement)을 하나로 묶어줌
# 이미 정의되어 있는 함수를 사용하거나 필요한 함수를 정의
# 한 번 혹은 여러번 호출될 수 있으며 함수 종료 시 결과 값을 전달
# 프로그램을 구조적, 논리적으로 만들어줌

# 함수의 정의
# 함수의 선언은 def로 시작하고 콜론(:)으로 끝남
# 함수의 시작과 끝은 코드의 들여쓰기로 구분
# 시작과 끝을 명시해 줄 필요가 없음
# 헤더(header)파일, 인터페이스(interface), 구현(implementation) 같은 부분으로 나누지 않음

def Times(a, b):
  return a * b

print(Times(10, 10))

#@함수 선언
# 함수를 선언하면 메모리에 함수 객체가 생성
# 함수 객체를 가리키는 레퍼런스가 생성
# 함수 레퍼런스를 통해서 함수를 사용하게 됨
# - 함수 레퍼런스는 다른 변수에 할당할 수 있음

# return
# 함수를 종료시키고 호출한 곳으로 돌아가게 함
# return은 어떠한 객체로돌려줄 수 있음
# - 여러 개의 값을 튜플로 묶어서 값을 전달할 수 있음
def swap(x, y):
  return y,x
print(swap(1,2))
# return을 사용하지 않거나 return만 적을 때도 함수가 종료됨 
# 리턴값으로 None을 리턴
def setValue(newValue):
  x = newValue                    # 반환값이 없는 경우
retval = setValue(10)
print(retval)
#-- 파이썬 함수에서 인수 전달
# 파이썬에서 함수 이수는 레퍼런스를 이용해 전달
# 함수의 인수는 호출자 내부 객체의 레퍼런스
a = 10
def isZero(arg1):
  return arg1 == 0
print(isZero(a))
# 호출자가 전달하는 변수의 타입에 따라 다르게 처리
# 변경 가능 변수(mutable)
# 불가능 변수(immutable)

# 변경 불가능 변수 예제
a = 10
b = 20
def sum1(x, y):
  return x + y
print(sum1(a, b))
x = 10
def sum2(x, y):
  x = 1 # 해당 부분에서 값이 1인 객체가 생성되고 x에 레퍼런스를 할당
  return x + y
print(sum2(x, b)) # x를 인수로 전달
print(x) # 함수 내부에서 변경한 사항이 외부에 영향을 미치지 않는다

# - 변경가능한 변수를 인수로 전달
def change(x):
  x[0] = 'H' # list x의 첫번째 아이템을 H로 변경
wordlist = ['J', 'A', 'M']
change(wordlist)
print(wordlist) # change가 호출자의 객체에 영향을 미친다
def change2(x):
  x = x[:] #
  x[0] = 'H'

# 3-2 스코핑룰 (Scoping rule)
# 이름공간(Name Space)
# 변수의 이름이 저장되어 있는 장소
# 함수 내부의 이름 공간, 지역 영역(Local Scope)
# 함수 밖의 영역, 전역 영역(Global Scope)
# 파이썬 자체에서 정의한 내용에 대한 영역, 내장 영역(Built-in Scope)

# LGB 규칙
# Local scope -> Golobal scope -> Built-in Scope 순서로 찾음
# 지역 영역에서 전역 영역의 이름을 접근할때 globaldmf dldyd
x = 1
def func(a):
  return a + x
print(func(1))
def func2(a):
  x = 2
  return a + x
print(func2(1))

# 파이썬에서 인수 모드
# 기본인수값
# 함수를 호출할 대 인수를 지정해 주지 않아도 기본 값이 할당 되도록 하는 방법
def Times2(a = 10, b = 20):
  return a * b
print(Times2())
print(Times2(5))
# 키워드 인수
# 인수 이름으로 값을 전달하는 방식
# 변수의 이름으로 특정 인수를 전달할 수 있음
def connectURI(server, port):
  str = 'http://' + server + ':' + port
  return str
print(connectURI("test.com", '8080'))
print(connectURI(port = '8080', server = 'cocoa.com'))
# 가변인수 리스트
# 인수의 개수가 정해지지 않은 가변 이수를 전달
# *를 사용하며 인수는 튜플 형식으로 전달 됨
def union2(*ar):
  res = []
  for item in ar:
    print('item : ', item)
    for x in item:
      print('x : ', x)
      if not x in res:
        res.append(x)
        print('res : ', res)
  return res
print(union2('HAM', 'EGG', 'SPAM'))
# 정의되지 않은 인수 처리하기
# **를 사용하면 정의되지 않은 인수를 딕셔너리 형식으로 전달
def userURIBuilder(server, port, **user):
  str = 'http://' + server + ':' + port + '/?'
  for key in user.keys():
    str += key + '=' + user[key] + '&'
  return str
print(userURIBuilder('test.com', '9090', id='userId', passwd='1234'))
print(userURIBuilder('naver.com', '80', id='userId', passwd='1234', name='mike', age='20'))
# 람다(lambda) 함수
# 이름이 없는 1줄짜리 함수
# Lambda 인수 <구문>
# 한 줄의 간다한 함수가 필요한 경우
# 프로그램의 가독성을 위해서
# 함수를 인수로 넘겨 줄 때
g = lambda x, y : x * y
print(g(2,3))
print((lambda x: x * x)(3))
# 재귀적(recursive) 함수 호출
# 함수 내부에서 자기 자신을 계속 호출하는 방법
# 변수를 조금씩 변경하면서 역속적으로 반복된 연산을 할 때 유용
def factorial(x):
  if x == 1:
    return 1
  print('x : ', x)
  return x * factorial(x - 1)
print(factorial(10))
# pass 구문(statement)
# 아무 일도 하지 않음
# while True:
#   pass
#아무것도 하지 않는 함, 모둘, 클래스를 만들어야 할 경우가 있는데 이때 pass가 사용될 수 있음
def sample():
  print('sample')
  pass
print(sample())

# __doc__ 속성과 help 함수
# help 함수를 이용해 함수의 설명을 볼 수 있음
# help(print)         # 주석 제거후 테스트 해야함!
def plus(a, b):
  return a + b
# 사용자가 만든 함수도 help를 사용해 설명을 볼 수 있음
help(plus)          # 주석 제거후 테스트
plus.__doc__ = 'return the sum of parameter a,b'
help(plus)          # 

# 이터레이터(iIterater)
# 순회 가능한 객체의 요소를 순서대로 접근할 수 있는 객체
# 내부 반목분을 관리해 주는 객체
# 이터레이터 안의 __next__()를 이용해 순회 가능한 객체의 요소를 하나씩 접근할 수 있음
s = 'abc'
it = iter(s)
print(s)
print(next(it))
print(next(it))
print(it.__next__())
print(next(it)) # 마지막 인덱스를 초과 호출하여 오류 발생 

#--제너레이터(Generator)
# return 대신 yield라는 구문을 이용해 함수 객체를 유지한 체 값을 호출자에게 넘겨줌
# 값을 넘겨준 후 함수 객체는 그대로 유지
# 함수의 상태를 그대로 유지하고 다시 호출할 수 있기 때문에 순회 가능한 객체를 만들 대 매우 편리함
# 예제1)
def reverse(data):
  for index in range(len(data) - 1, -1, -1):
    yield data[index]

for char in reverse('golf'):
  print(char)
# 예제2)
def abc():
  data = 'abc'
  for char in data:
    yield char
print(abc)
print(abc())
it = iter(abc())
print(next(it))
print(next(it))
print(next(it))