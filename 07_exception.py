# 예외처리
# [학습목표]
# - 파이썬의 예외 처리에 대해 이해할 수 있다.
# - 여러 가지 예외의 종류에 대해서 이해할 수 있다.
# - 사용자 정의 예외와 raise, assert의 사용법에 대해서 이해한다.

# 1. 예외 처리란
#---예외(Exception)란?
# 프로그램의 제어 흐름을 조정하기 위해 사용하는 이벤트
#   ⦿ 처리를 하지 않는 예외에 대하여 자동으로 에러(Error)가 발생하고 프로그램을 종료
# ---- example ----
print('---- 예외 처리 ----')
# a = [10, 20, 30]
# a[3]                      # 리스트의 크기를 넘어서는 인덱스 참조
#   ⦿ 처리되지 않은 예외(Inhandled Exception)
#     ☉ '0'으로 나누는 경우
#     ☉ 원격에 있는 데이터 베이스 접속시 연결되지 않는 경우
#     ☉ 파일을 열었는데 사용자에 의해서 삭제된 경우

#---구문 에러
#   ⦿ 오탈자, 들여쓰기의 실수로 발생
#   ⦿ 인터프리터에서 에러가 의심되는 부분을 개발자에게 알려줌
print('---- 구문 에러 ----')
# ---- example ----
# print("{0}, {1}.format(10, 20))           # 오탈자에 의한 구문 오류
# if a > 5 print('a is bigger than 5')      # 제어문 종료 ':' 구문 오류

#---예외의 몇 가지 종류
#   ⦿ NameError 선언하지 않은 변수 'a'에 접근
# print(a)
#   ⦿ ZeroDivisionError '0'으로 나눔
# a = 10 / 0
#   ⦿ IndexError 리스트의 접근 가능한 인덱스를 넘음
# a = [10, 20, 30]
# a[3]
#   ⦿ TypeError 지원하지 않는 연산(정수를 문자열로 나눔)
# a = 'Apple'
# 10 / a

#---내장 예외 클래스 계층구조
# 내장 예외는 exceptions 모듈에 미리 정의
#   ⦿ 프로그램 동작 중 자동적으로 발생
#   ⦿ 개발자가 명시적으로 예외 발생도 가능

# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning

#---주요 내장 예외
#           클래스 이름            |                내용
#          Exception                  모든 내장 예외의 기본 클래스 -사용자 정의 예외를 작성시 활용
#          ArithmeticError            수치 연산 예외의 기본 클랙스
#          LookupError                시퀀스 관련 예외의 기본 클래스
#          EnvironmentError           파이썬 외부 에러의 기본 클래스

# 2. 예외 처리의 종류
#---예외 처리
#   ⦿ try 구문
# try:
#   <예외 발생가능성이 있는 문장>
# except <예외 종류>:
#   <예외 처리 문장>
# except <예외1, 예외2>:
#   <예외 처리 문장>
# except <예외 as 인자>:
#   <예외 처리 문장>
# else:
#   <예외가 발생하지 않은 경우, 수행할 문장>
# finally:
#   <예외 발생 유무에 상관없이 try 블록 이후 수행할 문장>
# ---- example ----
print('--- try ~ except 예제 ----')
def divide(a, b):
  return a / b

try:
  c = divide(5, 0)
except:
  print('Exception is occured!!')

print('---- 다양한 예외 처리 ----')
try:
  c = divide(5, 'string')
except ZeroDivisionError:
  print('두번째 인자는 0이면 안됩니다')
except TypeError:
  print('모든 인수는 숫자이어야 합니다')
except:
  print('무슨 에러인지 모르겠어요')
  
print('---- else와 finally 예제 ----')
try:
  c = divide(5, 2)
except ZeroDivisionError:
  print('두번째 인자는 0이면 안됩니다')
except TypeError:
  print('모든 인수는 숫자이어야 합니다')
except:
  print('ZeroDivisionError, TypeError를 제외한 다른 에러')
else: # 예외가 발생하지 않은경우
  print('Result : {0}'.format(c))
finally: # 예외 발생 유무와 상관없이 수행
  print('항상 finally 블록은 수행됩니다!')

print('---- 예외에 대한 정보를 전달받는 예제 ----')
try:
  c = divide(5, 'af')
except TypeError as e: # 전달되는 예외 인스터스 객체를 e로 받아서 사용
  print('에러 : ', e.args[0])
except:
  print('무슨 에러인지 모르겠어요')

print('---- 예외를 묶어서 처리하는 예제 ----')
try:
  c = divide(5, 0)
except (ZeroDivisionError, OverflowError, FloatingPointError) as e: # 명시된 에러를 모두 처리
  print('수치 연산 관련 에러입니다  : ', e.args[0])
except TypeError:
  print('모든 인수는 숫자여야 합니다')
except:
  print('무슨 에러인지 모르겠어요')

print('---- 상위 예외 클래스를 처리하는 예제 ----')
try:
  c = divide(5, 0)
except ArithmeticError: # 상위 클래스를 처리시 하위 모든 클래스도 이 부분 에서 처리
  print('수치 연산 관련 에러입니다 ')
except TypeError:
  print('모든 인수는 숫자여야 합니다')
except:
  print('무슨 에러인지 모르겠어요')

print('---- try ~ finally ----')
FilePath = './test.txt'
try:
  f = open(FilePath, 'r')
  try:
    data = f.read(128)
    print(data)
  finally:
    f.close()
except IOError:
  print('Fail to open {0} file'.format(FilePath))

# 3. 사용자 정의 예외 및 기타 구문
#---rais 구문
#   ⦿ 명시적으로 예외 발생
# raise 구문형식
# - raise[Exception]
# - raise[Exception(data)]
# - raise
# ---- example ----
def RaiseErrorFunc():
  raise NameError # 내장 예외인 NameError 발생

try:
  RaiseErrorFunc()
except:
  print('NameError is Catched!')

# 내장 예외만으로 부족한 경우, 개발자가 직접 예외를 정의하여 사용 가능
#   ⦿ Exception 클래스나 그 하위 클래스를 상속받아서 구현
#   ⦿ 생성자에 클래스 멤버 변수를 이용하여 인자를 에러 처리부로 전달
# ---- example ----
print('---- 사용자 정의 예외 ----')
class NegativeDivisionError(Exception): # 사용자 정의 예외 정의
  def __init__(self, value):
    print('hello')
    self.value = value

def PositiveDivide(a, b):
  if (b < 0):
    raise NegativeDivisionError(b)
  return a / b

try:
  ret = PositiveDivide(10, 'string')
except NegativeDivisionError as e:      # 사용자 정의 예외인 경우
  print('Error - Second argument of PositiveDivide is ', e.value)
except ZeroDivisionError as e:          # 0으로 나누는 경우
  print('Error - ', e.args[0])
except BaseException as e:              # 그외 모든 에러
  print(e.args)

# assert 구문
# 표현식 Assert <조건식>, <관련 데이터>
# 인자로 받은 조건식이 거짓인 경우, AssertionError가 발생
#   ⦿ 개발과정에서 디버깅, 제약 사항 설정 등으로 사용
#   ⦿ __debug__가 True인 경우만 assert 구문 활성화
#     ☉ 명령 프롬프트에서 최적화 옵션(-O)을 설정하면 __debug__는 False로 설정됨
#     ☉ 다음 코드와 동일
# ---- example ----
print('---- assert ----')
if __debug__:
  if not 1 == 1:
    raise AssertionError('관련 데이터')

print('---- 예외에 대한 정보를 전달받는 예제 ----')
# def foo(x): # 받은 인자의 type이 정수형인지 검사
#   assert type(x) == int, 'Input value must be integer'
#   return x * 10
# ret = foo('a') # AssertionError가 발생
# print(ret)

print('---- 실용 예제 1 ----')
import glob, os.path

def traverse(dir, depth):
  for obj in glob.glob(dir + '/*'):
    if depth == 0:
      prefix = '|--'
    else:
      prefix = '|' + ' ' * depth + '+--'
    if os.path.isdir(obj):
      print(prefix + os.path.basename(obj))
      traverse(obj, depth + 1)
    elif os.path.isfile(obj):
      print(prefix + os.path.basename(obj))
    else:
      print(prefix + 'unknown object: ', obj)
if __name__ == '__main__':
  traverse('.', 0)



print('---- Raise를 활용한 응답방법 ----')

# def traverse_two(dir, depth):
#   for obj in glob.glob(dir + '/*'):
#     if depth == 0:
#       prefix = '|--'
#     else:
#       prefix = '|' + ' ' * depth + '+--'
#     if os.path.isdir(obj):
#       print(prefix + os.path.basename(obj))
#       traverse_two(obj, depth + 1)
#     elif os.path.isfile(obj):
#       print(prefix + os.path.basename(obj))
#     else:
#       print(prefix + 'unknown object: ', obj)
#       raise UnknownObjectError(obj)

# if __name__ == '__main__':
#   try:
#     traverse_two('.', 0)
#   except UnknownObjectError as e:
#     print('UnknownObjectError occurs: ', e.obj)
#   except:
#     exc, value, tb = sys.exc_info()
#     print(exc, value, tb)
#     traceback.print_exc()
  