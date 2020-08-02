# 파일 시스템
# [학습목표]
# - os.path 모듈에 대해 이해하고 사용할 수 있다
# - glob 모듈을 이해하고 사용할 수 있다
# - glob과 os.path를 활용한 프로젝트인 tree를 이해한다

# 1. os.path
#   ⦿ os.path.abspath(path) 절대 경로를 반환
from os import path
import os
print(path.abspath('tmp'))
#   ⦿ os.path.basename(path) 입력받은 경로의 기본 이름을 반환
print(path.basename('/Users/chars/workspace/study'))
#   ⦿ os.path.dirname(path) 입력받은 파일/디렉터리의 경로를 반환
print(path.dirname('/Users/chars/workspace/study/learning-python/test.txt'))
#   ⦿ os.path.exists(path) 입력받은 경로가 존재하면 True를 반환하고, 존재하지 않는 경우에는 False를 반환
print(path.exists('/Users/Local'))
print(path.exists('/Users/chars'))
#   ⦿ os.path.expanduser(path) 입력받은 경로안의 "~"를 현재 사용자 디렉터리의 절대 경로로 대체
print(path.expanduser('~/test'))
#   ⦿ os.path.expandvars(path) path 안에 환경 변수가 있다면 확장
print(path.expandvars('~/temp'))
#   ⦿ os.path.getatime(path) 입력받은 경로에 대한 최근 접근 시간을 반환
print(path.getatime('/Users/chars/workspace/study/learning-python/test.txt'))
#   ⦿ os.path.getmtime(path) 입력받은 경로에 대한 최근 변경 시간을 반환
print(path.getmtime('/Users/chars/workspace/study/learning-python/test.txt'))
#   ⦿ os.path.getctime(path) 입력받은 경로에 대한 생성 시간을 반환
print(path.getctime('/Users/chars/workspace/study/learning-python/test.txt'))
#   ⦿ os.path.getsize(path) 입력받은 경로에 대한 바이트 단위의 파일 크기를 반환
print(path.getsize('/Users/chars/workspace/study/learning-python/test.txt'))
#   ⦿ os.path.isabs(path) 경로가 절대 경로이면 True를 반환하고, 그 외의 경우에는 False를 반환
print(path.isabs('/Users/chars/workspace/study/learning-python/test.txt'))
#   ⦿ os.path.isfile(path) 경로가 파일인지 검사 파일인 경우 True 반환 그이외의 경우에는 False 반환
print(path.isfile('/Users/chars/workspace/study/learning-python/test.txt'))
#   ⦿ os.path.isdir(path) 경로가 디렉터리인지 검사 디렉터리인 경우 True 반환 그이외의 경우에는 False 반환
print(path.isdir('/Users/chars/workspace/study/learning-python/test.txt'))
#   ⦿ os.path.join(path1,[, path2[,...]]) 해당 OS 형식에 맞도록 입력받은 경로를 연결
print(path.join('Users/chars', 'workspace', 'study'))
#   ⦿ os.path.normcase(path) 해당 OS에 맞도록 입력받은 경로의 문자열을 정규화함
print(path.normcase('/Users/chars/workspace'))
#   ⦿ os.path.normpath(path) 입력받은 경로를 정규화함
print(path.normpath('/Users/chars/workspace/study/learning-python/test.txt'))
#   ⦿ os.path.split(path) 입력받은 경로를 디렉터리 부분과 파일 부분으로 나눔
print(path.split('/Users/chars/workspace/study/learning-python/test.txt'))
#   ⦿ os.path.spltdrive(path) 입력받은 경로를 드라이브 부분과 나머지 부분으로 나눔
print(path.splitdrive('/Users/chars/workspace/study/learning-python/test.txt'))
#   ⦿ os.path.splittext(path) 입력받은 경로를 확장자 부분과 그 외의 부분으로 나눔
print(path.splitext('/Users/chars/workspace/study/learning-python/test.txt'))

# 2. glob
#----glob.glob(path)
#   ⦿ path 경로에 대응되는 모든 파일 및 디렉터리의 리스트를 반환
#   ⦿ 경로를 주는 방식에 따라절대 경로롤 결과가 나오게 할 수도 있음
import glob
print(glob.glob('test.*'))
print(glob.glob('test[0-9].*'))
print(glob.glob('*.sh'))
print(glob.glob(path.abspath('.') + '/'))

#----glob.iglob(path)
#   ⦿ glob과 동일한 동작을 수행하지만, 리스트로 결과를 반환하는 것이 아니라 이터레이터를 반환함
print(glob.iglob('*'))
for i in glob.iglob('*'):
  print(i)

# 3. tree 만들기
#----tree란?
#   ⦿ tree는 하위 디렉터리 구조를 보여주는 툴
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