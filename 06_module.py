# 모듈
# [학습목표]
# - 모듈의 정의와 사용법에 대해 이해할 수 있다
# - 직접 모듈을 만들 수 있다
# - 모듈의 동작과 패키지를 이해한다

# 1. 모듈이란
# Tip!] 모듈이란?
# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일

#---모듈
#   ⦿ 현재 파이썬 3.0 버전에서는 대략 200개가 넘는 모듈을 지원, 간단하게 모듈을 사용할 수 있음
#     ☉ 문자열(string), 날짜(date), 시간(time), 십진법(decimal), 랜덤(random)
#     ☉ 파일(file), os, sqlite3, sys, xml, email, http 등등
#   ⦿ 어떠한 조건에도 해당하지 않는 경우
#   ⦿ 모듈을 사용하는 이유
#     ☉ 코드의 재 사용성
#     ☉ 코드를 이름공간으로 구분하고 관리 할 수 있음
#     ☉ 복잡하고 어려운 기능을 포함하는 프로그램을 간단하게 만들 수 있음

#---모듈 import
#   ⦿ import: 모듈을 현재 이름 공간으로 가져오는 역할
# ---- example ----
print('---- module import ----')
import math
print(math.pow(2, 10))
print(math.pi)
#   ⦿ math 모듈은 삼각함수, 제곱근, 로그함수 등 수학과 관련된 기능이 들어 있는 내장 모듈
#   ⦿ dir() 함수를 이용해 모듈에 어떠한 함수 혹은 데이터가 들어 있는지 알 수 있음
print(dir(math))

#---간단한 FTP 프로그램
#   ⦿ FTP로 서버에 접근해 파일 리스트를 가져오는 프로그램
# from ftplib import FTP
# ftp = FTP('ftp.cwi.nl')
# ftp.login()
# ftp.retrlines('LIST')
# ftp.quit()

# 2. 모듈 만들기
#---모듈 만들기
#   ⦿ 사용자가 직접 모듈을 만들 수 있음
#   ⦿ 큰 프로젝트의 경우 모듈 단위로 일을 진행하기도 함
#   ⦿ 모듈은 일반적으로 <모듈이름>.py 으로 지정

#---Simpleset 모듈 만들기
#   ⦿ 텍스트 에디터를 이용해 교집합, 차집합, 합집합 함수를 만듦
#   ⦿ simpleset.py 이름으로 저장하고 simplesret.py를 파이썬 라이브러리 디렉터리에 옮김
#   ⦿ import 명령을 이용해 simpleset 모듈을 가지고 옴

#---모듈의 경로
#   ⦿ 모듈을 임포트 했을 대 모듈의 위치를 검색하는 경로
#     ☉ sys.path에 저장되어 있는 디렉토리를 검색
#   ⦿ 모듈의 경로 밖의 모듈은 이포트 할 수 없음
#   ⦿ 모듈 경로 탐색 순서
#     ☉ 프로그램이 실행된 디렉터리
#     ☉ PYTHONPATH 환경 변수에 등록된 위치
#     ☉ 표준 라이브러리 디렉터리

#---모듈 임포트
#   ⦿ 모듈 안의 어트리뷰트 (함수, 데이터)들을 사용하려면 임포트를 해야함
#   ⦿ import 구문은 어디에서나 사용 가능
#     ☉ 함수, 제어문 내부에서도 import를 할 수 있음
#   ⦿ import <모듈이름>
#     ☉ 기본적인 임포트 방법
#     ☉ 모듈. 이름 형식으로 모듈 안의 데이터나 함수를 사용 할 수 있음
#     ☉ 모듈은 임포트 하는 방법은 import 모듈 이름 방법 이외에도 다른 방법이 있음

#---모듈 임포트 방법
#   ⦿ from <모듈> import <어트리뷰트>
# ---- example ----
# from simpleset import union
# union([1, 2, 3], [3], [3,4])
#   ⦿ from <모듈> import *
#   ⦿ import <모듈> as <별칭>
#     ☉ 모듈 이름을 <별칭>으로 변경하여 임포트

# 3. 모듈의 고급 사용법
#---모듈 임포트 파헤치기
#   ⦿ 임포트를 할 대, 해당 모듈의 바이트 코드가 있으면 이를 임포트함
#   ⦿ 모듈을 임포트 하면 해당 모듈의 코다가 실행
#   ⦿ 모듈이 임포트 되면 메모리에 모듈 코드가 로딩되면 프로그램이나 파이썬 인터프리터가 끝나기 전까지 변경되지 않음

#---바이트 코드
#   ⦿ 모듈의 임포트를 빠르게 해주는 역할
#   ⦿ 바이트 코드가 이미 있으면: 모듈을 인터프리팅(InerPreting) 하지 않고 바로 바이트 코 로딩
#   ⦿ 바이트 고드가 없으면: 모듈을 인터프리팅 해서 바이트 코드를 생성
#   ⦿ 바이트 코드가 생성된 모습 => pyc 파일

#---모듈이 메모리에 로딩 될 때
#   ⦿ 모듈의 코드가 실행 됨
# ---- example ----
print('---- 모듈이 메모리에 로딩 될 때 ----')
# _*_ coding: cp949 _*_
print('test module')
defaultvalue = 1
def prinDefaultValue():
  print(defaultvalue)
#   ⦿ 처음 임포트 할 때 'print' 구문이 실행
#   ⦿ 한 번 메모리에 로딩된 모듈은 끝나기 전 까지 변하지 않음

#---유용한 팁
# 모듈이 직접 실행 혹은 다른 곳에서 임포트 되었는지를 구분해 줄 수 있는 __name__ 어트리뷰트
#   ⦿ 모듈이 임포트 되었을때 __name__은 모듈 자기 자신의 이름
#   ⦿ 모듈이 직접 실행 되었을 때 __name__은 '__main__'
# ---- example ----
print('---- 유용한 팁 ----')
print('my module')
if __name__ == '__main__':
  print('모듈을 직접 실행하셨네요')
else:
  print('임포트 하셨네요')

#---패키지
# 모듈의 모음
#   ⦿ 파이썬의 모듈 이름 공간을 구조화 하는 한 방법
#   ⦿ 파이썬 내장 라이브러리중 XML 패키지의 디렉터리 구조
# |--- __init__.py
#     +--- dom
#         +--- __init__.py
#         +--- domreg.py
#         +--- expatbuilder.py
#         ...
#     +--- etree
#         +--- __init__.py
#         +--- cElementTree.py
#         ...

#---__init__.py 내부
# __all__ = ['dom', 'parsers', 'sax', 'etree']
# __version__ = '$Revision: 41660 $'.split()[-2:][0]
# _MINIMUM_XMLPLUS_VERSION = (0, 8, 4)
# try:
# import _xmlplus
# except ImportError:
#   pass

#---모듈 임포트 예제
# python3 를 실행후 아래 예제를 따라한다
# >>> from xml import *
# >>> etree
# <module 'xml.etree' from '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/xml/etree/__init__.py'>
# >>> dom
# <module 'xml.dom' from '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/xml/dom/__init__.py'>
# >>> import xml.dom
# >>> xml.dom
# <module 'xml.dom' from '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/xml/dom/__init__.py'>



