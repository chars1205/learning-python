# 문자열 다루기
# [학습목표]
# - 파이썬의 문자열 메소드들에 대해 이해하고 사용할 수 있다
# - 정규식의 문법을 이해할 수 있다
# - 정규식 함수들의 사용법을 이해하고 사용할 수 있다


# 1. 문자열 클래스
#---str
#   ⦿ 문자열을 다루는 기본 클래스
#   ⦿ 특별한 모듈을 import할 필요가 없음(내장 클래스)
print(dir(str))

#---capitalize()
#   ⦿ 문자열의 첫문자만 대문자로 변경해주고 나머지 문자들은 소문자로 변환시켜 준다
# ---- example ----
print('---- capitalize ----')
print('PYTHON'.capitalize())
print('python is powerful'.capitalize())

#---count(keyword, [start,[end]])
#   ⦿ 문자열에서 키워드에 해당하는 문자를 카운트하여 보여준다
# ---- example ----
print('---- count ----')
print('python is powerful'.count('p'))
print('python is powerful'.count('p', 5))                  # [5:]으로 슬라이싱하고 count한 결과와 동일
print('python is powerful'.count('p', 0, -1))              # [0:-1]으로 슬라이싱하고 count한 결과와 동일

#---encode([encoding, [errors]])
# ---- example ----
print('---- encode ----')
print('가나다'.encode('cp949'))                               # 윈도우에서 사용하는 'CP949'로 변환
print('가나다'.encode('UTF-8'))                               # 'UTF-8'로 변환
# print('가나다'.encode('latin1', 'strict'))                  # UnicodeDecodeError 예외 발생
print('가나다abc'.encode('latin1', 'ignore'))                 # 유니코드 결과에서 문자를 그냥 생략
print('가나다abc'.encode('latin1', 'replace'))                # U+FFFD REPLACEMENT CHATACTER 사용 하여 치환
print('가나다abc'.encode('latin1', 'xmlcharrefreplace'))      # XML 문자 참조 삽입
print('가나다abc'.encode('latin1', 'backslashreplace'))       # unicoe 값으로 치환

#---endswith(postfix, [start, [end]])
print('---- endswith ----')
print('python is powerful'.endswith('ful'))
print('python is powerful'.endswith('ful', 5))               # [5:]으로 슬라이싱하고 endswit한 결과와 동일
print('python is powerful'.endswith('ful', 5, -1))           # [5: -1]으로 슬라이싱하고 endswit한 결과와 동일
print('python is powerful'.endswith(('m', 'l')))             # 문자열의 끝이 인자로 들어온 값에 부합할 경우 True 반환

#---expandtabs([tabsize])
print('---- expandtabs ----')
print('python\tis\tpowerful')
print('python\tis\tpowerful'.expandtabs())
print('python\tis\tpowerful'.expandtabs(1))                  # 탭간격 조정

#----find(keyword, [start, [end]])
print('---- find ----')
print('python is powerful'.find('p'))
print('python is powerful'.find('p', 5, -1))                 # [5:-1]으로 슬라이싱하고 find한 결과와 동일
print('python is powerful'.find('pa'))                       # 키워드를 문자열에서 찾지 못하는 경우 -1 반환

#----index(keyword, [start, [end]])
print('python is powerful'.index('p'))
print('python is powerful'.index('p', 5, -1))                # [5:-1]으로 슬라이싱하고 index한 결과와 동일
try:
  print('python is powerful'.index('pa'))                    # 키워드를 문자열에서 찾지 못하는 경우 ValueError 발생
except ValueError as e:
  print('e : ', e.args[0])

#----isalnum()
print('---- isalnum ----')
print('python'.isalnum())
print('python30000'.isalnum())
print('python3.8'.isalnum())                                 # 문자열에 '.'이 존재 할 경우 False 반환

#----isalpha()
print('---- isalpha ----')
print('python'.isalpha())
print('python30000'.isalpha())                              # 문자열에 알파벳을 제외한 문자가 존재할 경우 False 반환 

#----isupper()
print('---- isupper ----')
print('Python'.isupper())
print('PYTHON'.isupper())
print('PYTHON3.2'.isupper())                                # 문자열에서 문자들이 대문자 인지 판단

#----islower()
print('---- islower ----')
print('python'.islower())
print('pyThon'.islower())                                   # 문자열에 대문자 존재할 경우 False 반환
print('python3.8'.islower())

#----isspace()
print('---- isspace ----')
print(' '.isspace())                                        # 스페이스 문자 True 반환
print('\t\n '.isspace())                                    # 탭, 개행, 스페이스 문자 True 반환
print('\thi\n'.isspace())                                   # 탭, 개행, 스페이스 문자를 제외한 문자 포함시 False 반환

#----istitle()
print('---- istitle ----')
print('python is powerful'.istitle())
print('PYTHON IS POWERFUL'.istitle())
print('Python Is Powerful'.istitle())
print('Python is powerful'.istitle())                       # 문자열에서 시작되는 문자열이 대문자인지 판단하여 True, False 반환

#----isdecimal(), isdigit()
#   ⦿ 문자열은 소수점 문자가 포함 된 경우 true, 그렇지 않은경우는 false를 반환합니다.
print('---- isdecimal, isdigit ----')
print('2580'.isdecimal())
print('\u0669', '\u0669'.isdecimal())
print('\u00bc', '\u00bc'.isdecimal())

#----isnumeric()
print('---- isnumeric ----')
print('\u00bc', '\u00bc'.isdecimal())
print('\u00bc', '\u00bc'.isnumeric())

#----join(sequence)
print('---- sequence ----')
print('.'.join('BTS'))
print('\t'.join(['python', 'is', 'powerful']))

#----lower()
print('---- lower ----')
print('Python3.2'.lower())

#----lower()
print('---- upper ----')
print('Python3.2'.upper())

#----rstrip(['chars'])
print('---- rstrip ----')
print('python \t'.rstrip())
print('>>> python is powerful <<<'.rstrip('<> '))

#----lstrip(['chars'])
print('---- lstrip ----')
print('\t python'.lstrip())
print('>>> python is powerful'.lstrip('> '))

#----maketrans(x,[y,[z]])
# 이 함수는 translate()함수에 쓰일 번역용 맵을 반환함
# 입력인자가 하나인 경우에 사전을 입력으로 주어야 하며, 두개인 경우에는 길이가 같은 문자열을 입력으로 받아야 하고, 입력인자가 셋인경우에는 길이가 같은 문자열 둘과 마지막 인자로 None으로 대체될 문자열을 입력받는다.
print('---- maketrans ----')
print(str.maketrans('p', 'P'))
transmap = str.maketrans({'p' : 'P'})                       # 입력인자가 하나인 경우
print('python is powerful'.translate(transmap))
transmap = str.maketrans('poieu', 'P0129')                  # 입력인자가 둘인 경우
print('python is powerful'.translate(transmap))
transmap = str.maketrans("p", "P", "!")                     # 입력인자가 셋인 경우
print('python is powerful!!!!!!!!!'.translate(transmap))

#----partition(separator)
print('---- partition ----')
print('python is powerful'.partition('is'))

#----replace(old, new, [count])
print('---- replace ----')
print('python is powerful'.replace('p', 'P'))
print('python is powerful'.replace('p', 'P', 1))

#----rfind(keyword, [start, [end]])
print('---- rfind ----')
print('python is powerful'.rfind('p'))
print('python is powerful'.rfind('p', 0, 9))
print('python is powerful'.rfind('pa'))

#----rindex(keyword, [start, [end]])
print('---- rindex ----')
print('python is powerful'.rindex('p'))
print('python is powerful'.rindex('p', 0, 9))
try:
  print('python is powerful'.rindex('pa'))
except ValueError as e:
  print('e : ', e.args[0])

#----rpartion(separtor)
print('---- rpartion ----')
print('python is powerful'.rpartition('p'))

#-----split(sparator, [maxsplit])
print('---- split ----')
print('python is powerful'.split())
print('python is powerful'.split(' ', 1))

#-----rsplit(sparator, [maxsplit])
print('---- rsplit ----')
print('python is powerful'.rsplit())
print('python is powerful'.rsplit(' ', 1))

#----splitlines([keep])
print('---- splitlines ----')
print('python\r\nis\npowerful'.splitlines())
print('python\r\nis\npowerful'.splitlines(True))

#----startwith(prefix, [start,[end]])
print('---- startwith ----')
print('python is powerful'.startswith('py'))
print('python is powerful'.startswith('py', 5))
print('python is powerful'.startswith('py', 0, 5))
print('python is powerful'.startswith(('p', 'm')))

#----strip([chars])
print('---- strip ----')
print('\t python \t'.strip())
print('>>> python is powerful <<<'.strip('<> '))

#----swapcase()
print('---- swapcase ----')
print('Python3.2'.swapcase())

#----title()
print('---- title ----')
print('python is powerful'.title())

# 2. 정규표현식 모듈
#----정규표현식(Regular expression)
#   ⦿ 특정한 규칙을 가진 문자열을 표현하는데 사용되느 형식 언어
#   ⦿ 주어진 패턴으로 문자열을 검색/치환하는데 사용
#   ⦿ vi, grep 등 프로그램에서 널리 사용

#----정규표현식 문법
#   ⦿ 문자나 문자의 패턴을 나타내기 위한 특수 문자들
#    문법   |             의미
#     .         개행 문자를 제외한 1자를 의미
#     ^         문자열의 시작
#     $         문자열의 종료
#     []        문자의 집합
#     |         OR
#     ()        괄호 안의 정규식을 그룹으로 만듦
#     *         문자가 0회 이상 반복
#     +         문자가 1회 이상 반복
#     ?         문자가 0 혹은 1회 반복
#    {m}        문자가 m회 반복
#   {m,n}       문자가 m회부터 n회까지 반복되는 모든 경우
#    {m,}       문자가 m회부터 무한 반복되는 모든 경우

#----정규표현식 예제
#     정규식        |                   예제    
#    'app.e'          'apple', 'appLe', 'app-e', 'app4e', 'app e'등 이 매치된다
#    '^app'           'apple and orange'등 'app'으로 시작하는 문자열이 매치된다
#    'ple$'           'orange and apple'과 같이 'ple'로 끝나는 문자열이 매치된다
#    'appl[a-z]'      'applz', 'appll'과 같이 마지막에 소문자가 오는 경우에만 매치된다
#    'appl[^a-z]'     'appl!', 'applE'와 같이 마지막에 소문자가 오는 경우를 제외한 모든 경우에 매치된다
#    'apple|E'        'apple', 'applE'인 경우 매치된다

#---- esacape 문자열
#     종류       |             설명
#     \w           밑줄과 표현 가능한 문자
#     \W           밑줄과 표현 가능한 문자를 제외한 나머지 문자
#     \d           0-9를 포함하는 모든숫자
#     \D           숫자를 제외한 모든 문자
#     \s           공백 문자
#     \S           공백 문자를 제외한 모든 문자
#     \\           역스래쉬(\) 문자 자체를 의미

#----re 모듈
#                 메소드                             |                             설명
#     search(pattern, string[, flags])                  string 전체에 대해서 pattern이 존재하는지 검사하여 MatchObject 인스턴스를 반환
#     match(pattern, string[, flags])                   string 시작부분부터 pattern이 존재하는지 검사하여 MatchObject 인스턴스를 반환
#     split(pattern, string[, maxsplit=0])              pattern을 구분자로 string을 분리하여 리스트로 반환함
#     findall(pattern, string[, flags])                 string에서 pattern과 매치되는 모든 경우를 찾아 리스트로 반환
#     sub(pattern, repl, string[, count])               string에서 patter과 일치하는 부분에 대하여 repl로 교체하여 결과 문자열을 반환

# ---- example ----
print('---- re 모듈 ----')
import re
re_match = re.match('[0-9]*th', '35th')                          # 결과로 Match 객체를 반환
print('re_match : ', re_match)
print(bool(re.match('[0-9]*th', '35th')))                        # 불린으로 결과를 확인
print(bool(re.match('ap', 'This is an apple')))                  # 문자열의 시작부터 검색한다
print(bool(re.search('[0-9]*th', '35th')))

print(bool(re.match('ap', 'This is an apple')))                  # 문자열의 시작부터 검색한다
print(bool(re.search('ap', 'This is an apple')))                 # 문자열의 전체에 대해서 \검색한다

print(re.findall('app\w*', 'application orange apple banana'))
print(re.findall('king\w*', 'application orange apple banana'))

print(re.sub('-', '', '901225-1234567'))                          # 주민등록번호 형식을 변경한다
print(re.sub('[:,|\s]', ',', 'Apple: Orange, Banan|Tomato'))      # 필드 구분자를 통일한다



