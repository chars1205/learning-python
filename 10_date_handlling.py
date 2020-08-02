# 날짜 다루기
# [학습목표]
# - 날짜 관련 기능들에 대해 이해하고 사용할 수 있다
# - time 모듈을 이해하고 사용할 수 있다
# - dateTime 모듈의 사용법을 숙지할 수 있다

# 1. 시간(time) 모듈
#----시간 표현 방법
#   ⦿ 타임스탬프(Time Stamp)
#   ⦿ UTC(Universal Time Coordinated, 협정세계시)
#   ⦿ 그리니치 평균시
#   ⦿ LST(Local Standard Time, 지방표준시)
#   ⦿ 일광절약 시간제(Daylight Saving Time, DTS)

#----struct_time 시퀀스 객체
#      속성         |        내용
#    tm_year              년도
#    tm_mon               월
#    tm_mday              일
#    tm_hour              시
#    tm_min               분
#    tm_sec               초
#    tm_wday              요일
#    tm_yday              누적 날짜

#----time 모듈
#   ⦿ 시간을 표현하는데 사용
#        함수                |              설명
#  time.time()                 1970년 1월 1일 자정 이후로 누적된 초를 float 단위로 반환
#  time.sleep(secs)            현재 동작 중인 프로세스를 주어진 초만큼 정지
#  time.gmtime([secs])         입력된 초를 변환하여, UTC 기준의 stuct_time 시퀀스 객체로 반환
#  time.localtime([secs])      입력된 초를 반환하여, 지방표준시 기준의 struct_time 시퀀스 객체를 반환
#  time.asctime([t])           struct_time 시퀀스 객체를 인자로 받아서 'Sun Jul 15 18:29:29 2020'과 같은 형태로 반환
#  time.mktime(t)              지방표준시인 struct_time 시퀀스 객체를 인자로 받아서 time()과 같은 누적된 초를 반환

#----time 모듈 사용예제 (1)
# ---- example ----
print('---- time 모듈 사용예제 ----')
import time
print(time.time())
print(time.gmtime())
print(time.localtime())

#----time 모듈 사용예제 (2)
t = time.gmtime(1234567890)
print(t)
print(t.tm_hour)
print(time.asctime(t))
print(time.mktime(t))

#----strptime, strftime
#   ⦿ 사용자가 직접 포맷을 지정하여 출력
#   ⦿ 함수원형
#     ☉ time.strftime(format[, t])
#     ☉ time.strptime(string[, format])
#   ⦿ 형식 지시자
#     ☉ %y     |   연도를 축약하여 표시
#     ☉ %Y     |   연도를 축약하지 않고 표시
#     ☉ %b     |   축약된 월 이름
#     ☉ %B     |   축약되지 않은 월 이름
#     ☉ %m     |   숫자로 표현한 월 (01 ~ 12)
#     ☉ %d     |   일(01 ~ 31)
#     ☉ %H     |   24시를 기준으로 한 시 (00 ~ 23)
#     ☉ %l     |   12시를 기준으로 한 시 (01 ~ 12)
#     ☉ %M     |   분 (00 ~ 59)
#     ☉ %S     |   초 (00 ~ 59)
#     ☉ %p     |   AM/PM
#     ☉ %a     |   축약된 요일 이름
#     ☉ %A     |   축약되지 않은 요일 이름
#     ☉ %W     |   요일을 숫자로 표시
#     ☉ %j     |   1월 1일부터 누적된 날짜 (001 ~ 366)

# ---- example ----
print('---- strftime ----')
from time import localtime, strftime
print(strftime('%B %dth %A %I:%M', localtime()))
print(strftime('%Y-%m-%d %I:%M', localtime()))
print(strftime('%y/%m/%d %H:%M:%S', localtime()))
print(strftime('%y/%m/%d %H:%M:%S'))

# ---- example ----
print('---- strptime ----')
from time import strptime
timestring = time.ctime(1234567890)
print(timestring)
print(strptime(timestring))
print(strptime(timestring, '%a %b %d %H:%M:%S %Y'))
try:
  print(strptime(timestring, '%a %b %d %H:%M:%S %y'))
except ValueError as e:
  print('e : ', e.args[0])

# 2. 날짜∙시간(datetime) 모듈
#----datetime 모듈이란?
#   ⦿ 기념일과 같은 날짜, 시간 연산을 위하여 사용

#----datetime 주요 클랙스
#   ⦿ datetime.date
#     ☉ 일반적으로 사용되는 그레고리안 달력(Gregorian Calendar)의 년, 월, 일을 표현
#   ⦿ datetime.time
#     ☉ 시간을 시, 분, 초, 마이크로 초, 시간대(Time zone)로 표현
#   ⦿ datetime.datetime
#     ☉ date 클랫와 time 클래스의 조합으로 구성
#   ⦿ datetime.timedate
#     ☉ 두 날짜 혹은 시간 사이의 기간을 표현

#----date 클래스
#   ⦿ 생성자
#     ☉ datetime.date(year, month, day)
#   ⦿ 입력인자의 조건
#     ☉ datetime.MINYEAR(1) <= year <= datetime.MAXYEAR(9999)
#     ☉ 1 <= month <= 12
#     ☉ 1 <= day <= 해당 월의 날짜

#----time 클래스
#   ⦿ 시, 분, 초와 같은 시간을 표시
#   ⦿ 생성자
#     ☉ datetime.time(hour[, minute,[, second[, microsecond[, tzinfo]]]])
#   ⦿ 시, 분, 초, 마이그로초, 시간대 정보를 입력 받아서 time 객체를 생성

#----timedelta 클랙스
#   ⦿ 두 날짜 혹은 시간 사이의 기간을 표현함
#   ⦿ 생성자
#     ☉ timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])

#----시간 연산 예제(1)
print('---- 시간 연산 ----')
from datetime import timedelta
tb_1 = timedelta(hours=7)
tb_2 = timedelta(days=-3)
print('tb_1 + tb_2 : ', tb_1 + tb_2)
print('tb_1 - tb_2 : ', tb_1 - tb_2)
print('tb_1 * 4 : ', tb_1 * 4)
print('tb_1 // 3 : ', tb_1 // 3)
print('abs(tb_2) : ', abs(tb_2))

print('tb_1 > tb_2 : ', tb_1 > tb_2)
print('tb_1 < tb_2 : ', tb_1 < tb_2)
tb_1 = timedelta(hours=24)
tb_2 = timedelta(seconds=86400)
print('tb_1 == tb_2 : ', tb_1 == tb_2)
