# 운영체제 관련 기능
# [학습목표]
# - 파이썬의 제공하는 os 모듈에 대해서 이해하고 사용할 수 있다
# - sys 모듈의 기능을 이해하고 사용할 수 있다
# - 스레드에 대한 개념을 이해하고, threading 모듈을 사용할 수 있다


# 1. os 모듈
#----os.getcwd(), os.chdir(path)
#   ⦿ chdir() 함수는 현재 작업 디렉터리 위치를 변경하며, getcwd() 함수는 현재 작업 디렉터리의 위치를 가져올 때 쓰임
# ---- example ----
print('---- os.getcwd, os.chdir ----')
from os import *
print(getcwd())
# print(chdir('Tools'))
print(getcwd())

#----os.access(path, mode)
#   ⦿ 입력받은 <path>에 대해서 <mode>에 해당하는 작업이 가능한 지의 여부를 반환
# ---- example ----
print('---- os.access ----')
print(access('.', F_OK))
print(access('.', W_OK | X_OK | R_OK))

#----os.listdir(path)
#   ⦿ 해당 경로(path)에 존재하는 파일과 디렉터리들의 리스트를 반환
# ---- example ----
print('---- listdir ----')
print(listdir('.'))

#----os.mkdir(path[, mode])
#   ⦿ <path>에 해당하는 디렉터리를 생성
# ---- example ----
print('---- mkdir ----')
print(mkdir('test1'))
# print(listdir('.'))

#----os.makedirs(path[, mode])
#   ⦿ 인자로 전달된 디렉터리를 재귀적으로 생성
makedirs('test2/sub1/sub2/leaf') 
# print(listdir('test2/sub1/sub2'))
# makedirs('test2/sub1/sub2/leaf')

#----os.remove(path), os.unlink(path)
#   ⦿ 파일을 삭제
# remove('test')
# unlink('test.db')

#----os.rmdir(path)
#   ⦿ 디렉터리를 삭제
print('---- rmdir ----')
rmdir('test1')

#----os.removedirs(path)
#   ⦿ 디렉터리를 순차적으로 삭제
print('---- removedirs ----')
removedirs('test2/sub1/sub2/leaf')

#----os.rename(src, dst)
#   ⦿ src를 dst로 이름을 변경하거나 이동
print('---- rename ----')
rename('test.txt', 'test2.txt')
rename('test2.txt', 'test.txt')

#----os.utime(path, times)
#   ⦿ 경로에 해당하는 파일에 대해 액세스 시간(access time)과 수정 시간(modified time)을 <times>로 수정
print('---- utime ----')
print(stat('test.txt'))
utime('test.txt', None)
print(stat('test.txt'))

#----os.walk(top[, topdown = True[, onerror=None[, fllowlinks=False]]])
#   ⦿ top으로 지정된 디렉터리를 순회하며 경로, 디렉터리 명을 순차적으로 반환
print('---- walk ----')
for path, dirs, files, in walk('./'):
  print(path, dirs, files)

#----os.pipe()
#   ⦿ 파이프를 생성
print('---- pipe ----')
# pipe()(5, 6)

#----os.fdopen(fd[, mode[, bufsize]])
#   ⦿ 파일 디스크립터를 이용해 파일 객체를 생성
print('---- fdopen ----')
r, w = pipe()
rd = fdopen(r)
print(rd)

#----os.popen(command[, mode[, bufsize]])
#   ⦿ 인자로 전달된 command를 수행하며 파이프를 생성
p = popen('dir', 'r')
print(p.read())

#----os.system(command)
#   ⦿ <command>를 실행하며, 성공한 경우 0을 반환
print('---- system ----')
print(system('ls -al'))

#----os.startfile(path[, operation])
#   ⦿ <path>를 os에서 지정된 프로그램으로 실행
print('---- startfile ----')
# startfile('README.txt')

#----os.execl(path, arg0, arg1, ...)
#   ⦿ 현재 프로세스에서 새로운 프로그램을 수행
# execl('.', 'python', '-v')

# 2. sys 모듈
#----sys.argv
#   ⦿ 파이썬 스크립트로 넘어온 입력 인자(argument)들의 리스트
import sys
print('argv size : ', len(sys.argv))
for i, arg in enumerate(sys.argv):
  print(i, arg)

#----sys.exc_info()
#   ⦿ 현재 발생한 예외 정보를 튜플로 반환
sys.exc_info()

try:
  1 / 0
except:
  exc_class, val, tb_ob = sys.exc_info()
  print(exc_class)
  print(val)
  print(tb_ob)

#----sys.exit([arg])
#   ⦿ 프로세스를 종료
# sys.exit()

#----sys.path
#   ⦿ 모듈을 찾을 때 참조하는 경로를 나타냄
print('---- path ----')
print(sys.path)


# 3. threading 모듈
#----Thread 객체
#   ⦿ Thread.start()            |   스레드를 시작할 때 사용
#   ⦿ Thread.run()              |   스레드의 주요 동작을 정의
#   ⦿ Thread.join([timeout])    |   스레드가 종료되기를 기다림

#----Lock 객체
#   ⦿ Lock, unlocked의 2가지 상태를 제공
#     ☉ 제공 메소드
#       - acquire() : locked 상태로 바뀜
#       - release() : unlocked 상태로 바뀜

