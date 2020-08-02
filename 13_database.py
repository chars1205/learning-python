# 데이터 베이스
# [학습목표]
# - SQLite3에서 제공되는 기능들에 대해서 이해하고 사용할 수 있다
# - SQL 문과 SQLite3를 함께 사용하는 법에 대해서 숙지할 수 있다
# - 배운 기능들을 모두 활용하여 간단한 프로젝트를 만들어 봅시다!

# 1. SQLite3의 기본
#----sqlite3 란?
#   ⦿ 디스크 기반의 가벼운 데이터베이스 라이브러리
#   ⦿ 서버가 필요치 않음
#   ⦿ 모바일 디바이스에 기본적으로 사용되고 있음
#   ⦿ 파이썬에도 기본적으로 포함되어 있음

#----모듈 함수
#                                      함수                                                |                              설명
#     sqlite3. connect(database[timeout, isolation_level, detect_types, factory])                 SQLite3 DB에 연결
#     sqlite3.complete_statement(sql)                                                             SQL 문장에 대해서 True를 반환
#     sqlite3.register_adapter(type, callable)                                                    사용자 정의 파이썬 자료형을 SQLite3에서 사용하도록 등록
#     sqlite3.register_converter(typename, callable)                                              SQLite3에 저장된 자료를 사용자 정의 자료형으로 변환하는 함수를 등록


#----Connection 클래스
#                           메소드                                        |                     설명          
#     Connection.cursor()                                                     Cursor 객체 생성
#     Connection.commit()                                                     현재 트랜잭션의 변경내역을 DB에 반영(commit)함
#     Connection.rollback()                                                   가장 최근의 commit() 이후 지금까지 작업한 내용에 대해서 되돌림
#     Connection.close()                                                      DB 연결을 종료
#     Connection.isolation_level()                                            트랜잭션의 격리 수준 (isolation level)을 확인/설정
#     Connection.execute(sql[, parameters]) 
#     Connection.executemany(sql[, parameters])                               임시 Cursor 객체를 생성하여 해당 execute 계열 메서드를 수행
#     Connection.executescript(sql_script)                        
#     Connection.create_aggregate(name, num_params, aggregate_class)          사용자 정의 집계(aggregate) 함수를 생성
#     Connection.create_collation(name, callable)                             문자열 정렬시 SQL 구문에서 사용될 이름(name) 과 정렬 함수를 지정
#     Connection.iterdump()                                                   연결된 DB의 내용을 SQL 질의로 형태로 출력

#----Cursor 클래스
#                     메소드                                    |                     설명          
#     Cursor.execute(sql[, parameters])                               SQL 문장을 실행
#     Cursor.executemany(sql, seq_of_ parameters)                     동일한 SQL 문장을 파라미터만 변경하며 수행
#     Cursor.executescript(sql_script)                                세미콜론으로 구분된 연속된 SQL 문장을 수행
#     Cursor.fetchone()                                               조회된 결과(Record Set)로부터 데이터 1개를 반환
#     Cursor.fetchmany([size=cursor. arraysize])                      조회된 결과로부터 입력받은 size 만큼의 데이터를 리스트 형태로 반환
#     Cursor.fetchall()                                               조회된 결과 모두를 리스트 형태로 반환

# 2. SQLite3의 사용법
#----데이터베이스 연결
#   ⦿ 실제 파일을 이용한 connection 객체 생성
import sqlite3
# con = sqlite3.connect('test.db')
#   ⦿ 메모리를 이용한 connection 객체 생성
con = sqlite3.connect(':memory:')

#----SQL문 수행
#   ⦿ Cursor.execute 메소드를 이용하여 SQL문을 수행
cur = con.cursor()
cur.execute('CREATE TABLE phone_book(name text, phone_number text);')
cur.execute("INSERT INTO phone_book VALUES('Pan', '010-1234-5678');")
name = 'Sing'
phoneNumber = '010-8520-5678'
cur.execute("INSERT INTO phone_book VALUES(?, ?);", (name, phoneNumber))

#   ⦿ 딕셔너리를 이용한 인자 전달
cur.execute("INSERT INTO phone_book VALUES(:inputName, :inputPhoneNumber);", {"inputName": name, "inputPhoneNumber": phoneNumber})

#   ⦿ 동일한 문장을 매개변수만 바꾸며 연속적으로 수행하는 경우
datalist = (('Tom', '010-0987-3123'), ('DSP', '010-8775-1234'))
cur.executemany('INSERT INTO phone_book VALUES(?, ?)', datalist)

#----레코드 조회
#   ⦿ fetch를 이용한 레코드 조회
cur.execute('SELECT * FROM phone_book;')
for row in cur:
  print('row: ', row)

#   ⦿ fetchone, fetchmany를 이용한 레코드 조회
# cur.execute('SELECT * FROM phone_book;')
# print('fetchone : ', cur.fetchone())
# print('fetchmany', cur.fetchmany(2))
#----트랜잭션 처리
#   ⦿ 작업한 내용이 커밋되지 않는 예제
# print('fetchall : ', cur.fetchall())

# con = sqlite3.connect('./commit.db')
# cur = con.cursor()
# cur.execute('CREATE TABLE phone_book(name text, phone_number text);')
# cur.execute("INSERT INTO phone_book VALUES('Pan', '010-1234-5678');")
# con.commit()

cur.execute("SELECT * FROM phone_book;")
print(cur.fetchall())

#----레코드 정렬
#   ⦿ ORDER BY 사용 예제
cur.execute("SELECT * FROM phone_book ORDER BY name")
print([r for r in cur])
cur.execute("SELECT * FROM phone_book ORDER BY name DESC")
print([r for r in cur])

#   ⦿ 사용자 임의로 정렬 방식을 변경하는 경우
def OrderFunc(str1, str2):                                  # 대소문자 구별 없이 정렬하는 함수
  s1 = str1.upper()
  s2 = str2.upper()
  return (s1 > s2) - (s1 < s2)
con.create_collation('myordering', OrderFunc)               # SQL 구문에서 호출할 이름과 함수를 등록
cur.execute("SELECT * FROM phone_book ORDER BY name COLLATE myordering")
print([r for r in cur])

#----내장/집계 함수
#       함수      |             설명
#   abs(x)            절대값을 반환
#   length(x)         문자열의 길이를 반환
#   lowerx)           소문자로 변환해서 반환
#   upper(x)          대문자로 변환해서 반환
#   min(x)            최소값을 반환
#   max(x)            최대값을 반환
#   random(x)         임의의 정수를 반환
#   count(x)          Null이 아닌 튜플의 개수를 바환
#   count(*)          튜블의 개수를 반환
#   sum(x)            합을 반환

#----자료형
#   ⦿ SQLite3 자료형과 그에 대응되는 파이썬의 자료형
#    SQLite3 자료형    |      파이썬 자료형
#      NULL                   None
#      INTEGER                int
#      REAL                   float
#      TEXT                   str
#      BLOB                   buffer

#----데이터베이스 덤프 만들기
for l in con.iterdump():
  print(l)