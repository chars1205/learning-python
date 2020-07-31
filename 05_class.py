# 클래스
# [학습목표]
# - 클래스에 대해 이해 할 수 있다.
# - 클래스와 인스턴스와의 관계, 생성자와 소멸자를 이해한다.
# - 연산자 중복 및 상속에 대해 이해한다.

# 1. 클래스의 기본
# Tip!] 클래스란?
# - 데이터와 데이터를 변형하는 함수를 같은 공간으로 작성
# - 메소드(Method), 인스턴스(Instance), 정보 은닉(Information Hiding), 추상화(Abstraction)
class Person:               # 클래스 정의
  Name = 'Default Name'     # 멤버 변수
  def Print(self):          # 멤버 메소드
    print('My Name is {0}'.format(self.Name))

p1 = Person()               # 인스턴스 객체 생성
p1.Print()                  # 멤버 변수값을 출력

#---클래스와 인스턴스 이름 공간
# p1(인스턴스) -> Person(클래스)
# 검색순서 : 인스턴스 객체 영역 -> 클래스 객체 영역 -> 전역 영역
# ---- example ----
print('---- class & instance name space ----')
p1 = Person()               # 인스턴스 객체 생성    
p2 = Person()
print('--- 변경전 ----')
print('p1 name: ', p1.Name)
print('p2 name: ', p2.Name)
p1.Name = '김연아'                # 인스턴스의 'name' 속성을 변경
print('--- 변경후----')
print('p1 name: ', p1.Name)
print('p2 name: ', p2.Name)

# 클래스와 인스턴스에 멤버 데이터 추가
Person.title = 'New Title'      # 클래스 객체에 새로운 멤버 변수 title 추가
p1.age = 20                     # p1 객체에만 age 멤버 변수를 추가
print('p1 title : ', p1.title)
print('p2 title : ', p2.title)

print('p1 age : ', p1.age)
# print('p2 age : ', p2.age)

#---클래스와 인스턴스 관계
# isinstance(인스턴스객체 클래스 객체)
#   ⦿ 인스턴스 객체가 어떤 클래스로 부터 생성되었는지 확인
#   ⦿ 불린 형태로 결과 반환
# ---- example ----
print('---- isinstance ----')
class User:
  pass
class Bird:
  pass
class Student(User):
  pass

u, s = User(), Student()
print('u is instance of User : ', isinstance(u, User))
print('s is instance of User : ', isinstance(s, User))
print('u is instance of object : ', isinstance(u, object))
print('u is instance of Bird : ', isinstance(u, Bird))

# 2. 인스턴스, 생성자/소멸자
#---생성자와 소멸자
# Note] 생성자
#   - 생성시 초기화 작업을 수행
#   - 인스턴스 객체가 생성될 떄 자동으로 호출
#   - __init__()
# Note] 소멸자
#   - 소멸시 종료 작업을 수행
#   - 인스턴스 객체의 참조 카운터가 '0'이 될 때 호출
#   - __del__()
# ---- example ----
print('---- 생성자와 소멸자 ----')
class MyClass:
  def __init__(self, value):            # 생성자 메소드
    self.Value = value
    print('Class is created! Value = ', value)
  def __del__(self):                    # 소멸자 메소드
    print('Class is deleted!!')

def foo():
  d = MyClass(10) # 함수 foo 블록안에서만 인스턴스 객체 d가 존재
foo()

#--- 메소드 확장
# Note] 정적(static) 메소드
#   ⦿ 인스턴스 객체를 통하지 않고, 클래스를 통해 직접 호출할 수 있는 메소드
#     ☉ 인스턴스 객체를 참조하는 self 인자가 필요하지 않음
#     형식 : <호출할 메소드 이름> staticmethod(클래스내 정의한 메소드 이름)
# Note] 클래스(class) 메소드
#   ⦿ 클래스 영역의 데이터에 직접 접근할 수 있는 메소드
#     ☉ 암시적으로 첫 인자로 클래스 객체가 전달
#     형식 : <호출할 메소드 이름> classmethod(클래스내 정의한 메소드 이름)

# 3. 연산자 중복, 상속
#---연산자 중복
#   ⦿ 사용자 정의 객체에서 필요한 연산자를 내장 타입과 형태와 동작이 유사하도록 재정의
#   ⦿ 연산자 중복을 위하여 두 개의 밑줄 문자가 앞뒤로 있는 메소드를 미리 정의함
# ---- example ----
print('---- 연산자 중복 ----')
class GString:
  def __init__(self, init = None):
    self.content = init
  def __sub__(self, str):   # '-' 연산자 중복 정의
    for i in str:
      self.content = self.content.replace(i, '')
      print(self.content)
    return GString(self.content)
  def Remove(self, str):
    return self.__sub__(str)

stringClazz = GString('hello')
print(stringClazz.Remove('l'))
# 수치 연산자
#            메소드                         연산자                      사용예
#     __add__(self, other)                +(이항)                 A + B, A += B
#     __sub__(self, other)                -(이항)                 A - B, A -= B
#     __mul__(self, other)                  *                    A * B, A *= B
#     __truediv__(self, other)              /                    A / B, A /= B (python 3이상 지원, 그 이하 버전에서는 __div__가 사용됨)
#     __floordiv__(self, other)            //                    A // B, A //= B
#     __mod__(self, other)                  %                    A % B, A %= B
#     __divmod__(self, other)             divmod()               divmod(A, B)
#     __pow__(self, other[, modulo])      pow(), **              pow(A, B), A ** B
#     __lshift__(self, other)                <<                  A << B, A <<= B

#---상속
#   ⦿ 부모 클래스의 모든 속성(데이터, 메소드)를 자식 클래스로 물려줌
#   ⦿ 클래스의 공통된 속성을 부모 클래스에 정의
#   ⦿ 하위 클래스에서는 특화된 메소드와 데이터를 정의
# * 장점
#   - 각 클래스마다 동잃한 코드가 작성되는 것을 방지
#   - 부모 클래스에 공통된 속성을 두어 코드의 유지 보수가 용이
#   - 각 개별 클래스에 특화된 기능을 공통된 인터페이스로 접근 가능
# ---- example ----
print('---- 상속 ----')
class School:
  def __init__(self, name, phoeNumber):
    self.Name = name
    self.PhoneNumber = phoeNumber

class Teacher(School):
  def __init__(self, name, phoeNumber, subject, studentID):
    self.Name = name
    self.PhoneNumber = phoeNumber
    self.Subject = subject
    self.StudentID = studentID

# 클래스 간의 관계 확인
#   ⦿ 상속 관계인 두 클래스 간의 관계를 확인
#     -issubclass(자식 클래스, 부모 클래스)
print(issubclass(Teacher, School))

#---다중 상속
#   ⦿ 2개 이상의 클래스를 상속받는 경우
#   ⦿ 두 클래스의 모든 속성(변수와 메소드)을 전달받음
# ---- example ----
print()
class Tiger:
  def Jump(self):
    print('호랑이처럼 멀리 점프하기')
class Lion:
  def Bite(self):
    print('사자처럼 한입에 꿀꺽하기')
class Liger(Tiger, Lion): # 다중상속
  def Play(self):
    print('라이거만의 사육사와 놀이')

#---클래스 상속과 이름 공간
#   ⦿ 클래스 객체 간 상속을 통한 영역 (자식 클래스 영역, 부모 크래스 영역)
#   ⦿ 전역 영역
# ---- example ----
print('---- 클래스 상속과 이름 공간 ----')
class SuperClass:                         # 부모 클래스
  x = 10
  def printX(self):
    print(self.x)
class SubClass(SuperClass):               # 자식 클래스
  y = 20
  def printY(self):
    print(self.y)

s = SubClass()
s.a = 30
print(s.a)
s.printX()
s.printY()
