# 자료형 및 연산자

friend = 10
Friend = 1
print(friend)
print(Friend)
print(10)
print(0x10)
print(0o10)
print(0b10)
print(type(3.14), type(314e-2))
x = 3 - 4j
print(x)
print(type(x), x.imag, x.real, x.conjugate())
print('string', "string")
print("""줄바꿈도
그대로 적용됩니다""")
print("hellow \n123\0null")
print('py''thon')
print('py' * 3)
print('python'[0])
print('python'[5])
print('python'[1:4])
print('python'[-2:])
# 모든 문자열(string)이 기본적으로 유니코드임
# 유니코드 이외의 인코딩이 있는 문자열은 bytes로 표현
print(type('가'))
print('가'.encode('utf-8'))
print(type('가'.encode('utf-8')))
print(type('uA23'.encode('utf-8')))
# 리스트는 쉽게 값드의 나열이라고 생각됨
# 또한, 인덱싱과 슬라이싱도 가능
colors = ['red', 'green', 'gold']
print(colors)
colors.append('blue')
print(colors)
colors.insert(1, 'black')
print(colors)
colors.extend(['white', 'gray'])
print(colors)
print(colors + ['purple'])
print(colors.index('red'))
print("colors.index('red', 0) : ", colors.index('red', 0))
print("colors.index('gold', 0, 6) : ", colors.index('gold', 0, 6))
print(colors.index('gold', 0))
colors = ['red', 'black', 'green', 'gold', 'blue', 'white', 'gray', 'red']
print(colors.count('red'))
print('colors.pop() : ', colors.pop())
print(colors)
print(colors.remove('gold'))
print(colors)
colors.sort()
print(colors)
a = {1, 2, 3}
b = {3, 4, 5}
unionA = a.union(b)
print(unionA)
intersectionA = a.intersection(b)
print(intersectionA)

# 튜플
# 튜플은 리스트와 유사하나, 읽기전용임
# 읽기 전용인 만큼 제공되는 함수도 리스트에 비해 적지만, 속도는 그만큼 빠름
# 튜플에서 제공되는 메소드는 count, index 정도임
a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)

# 딕셔너리
# 딕셔너리는 Object와 같이 키와 값의 쌍으로 이루어져 있다 
d = dict(a = 1, b = 3, c = 5)
print(d)
color = { 'apple': 'red', 'banana': 'yellow'}
color["cherry"] = "red"
print(color)
color["apple"] = "green"
print(color)
# 딕셔너리의 내용을 얻기 위해서는 다음과 같이 items(), keys(), values() 메소드를 사용하면됨
# items()는 딕셔너리의 모든키와 값을 튜플로 묶어서 반환하며, keys()는 키만, values()는 값만 반환
for k, v in color.items():
  print(k, v)
print(color.items())
print(color.keys())
print(color.values())
# 삭제는 del을 이용할 수 도 있으며 clear를 이용해 한 번에 삭제할 수도 있음
del color['cherry']
print(color)
color.clear()
print(color)
# 부울 (bool)
# 부울은 참과 거짓을 나타내는 자료형으로, 가능한 값은 True와 False뿐
# 주로 부울은 부울 값들 간의 논리연산이나, 수치들 간의 비교연상의 결과로 사용

# 비교 연산자 '크다(>)', '작다(<)', '같다(==)', '다르다(!=)', '같거나크다(>=)', '같거나작다(<=)'가 있음
# 논리 연산자 'and(&)', 'or(|)', 'not'이 있음
print(not 1 == 2)

# 얕은 복사 vs 깊은 복사
# 변수에는 객체의 주소를 저장
one = [1, 2, 3]
two = one
print(one[0])
print(one)
print(two)
print(id(one), id(two))
# 얕은 복사 : 주소가 복사되어 객체를 공유하는 경우
# 깊은 복사 : 객체를 공유하지 않는 경우
arr_one = [1, 2, 3]
arr_two = arr_one[:]
print(id(arr_one), id(arr_two))
arr_one[0] = 38
print(arr_one)
print(arr_two)
