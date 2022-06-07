# 파이썬 기본_1
## 1. 자료형
- 1. 숫자형
- 2. 문자열
- 3. list
- 4. tuple
- 5. 딕셔너리
- 6. 집합
- 7. 불린

> 1. 숫자형
- 정수(integer), 실수(float), 8진수(Octal), 16진수(Hexadecimal)
- 정수
```python
print(4+3)
print(4/3) # 나누기
print(4**3) # 제곱
print(4%3) # 나머지
print(4//3) # 몫
```
> 2. 문자열
- "문자" , '문자' ,"""문자""",'''문자'''
- 문자열 안에 작은따옴표나 큰 따옴표를 포함시키고 싶기떄문에 여러개의 문자열 표현이 존재
- 여러줄인 문자열을 변수로 대입하고 싶을때
```python
mulitline='''
life
is 
too
short
'''
print(mulitline)
```
|코드|설명|
|---|---|
|\n|문자열 안에서 줄을 바꿀때 사용|
|\t|문자열 사이의 탭간격 |
| \\\\ | \\를 그대로 사용하고싶을떄|
|\'|작은따옴표 사용|
|\"|큰따옴표 사용|



> 문자열의 연산
- 더하기는 연결하기
- 곱하기는 반복 
- len(a) 문자열 길이 구하기

> 문자열 인덱싱
- 파이썬은 0 부터 숫자를 센다
- a[시작번호 : 끝번호]
- a[:] 전체
- a[-1] 맨뒤
---문자열은 요솟값을 바꿀 수 없는 값이 아니다!!! 문자열 자료형은 immutable한 자료형이다. ---
> 문자열 포맷팅
``` python
a=3.5
print("I eat %d apples" %a) # 숫자 바로대입
print("I eat %s apples" %a) # string으로 대입
b=5.6
print("I eat %f apples and %f ham" %(a,b)) # 변수 두개 넣기

```
| 코드 | 설명 |
|----|---|
| %s | string |
| %c | 문자열1개 |
| %d | 정수 |
| %f | 부동소수점 |
| %o | 8진수 |
| %x | 16진수|
| %% | 문자열 자체 %쓸떄 |

- 포맷과 코드와 숫자 함꼐 사용하기
```python
# 숫자 바로 대입하기
print("I eat {0} apples".format(3))
# 문자 바로대입하기
print("I eat {0} apples".format("five"))
# 변수로 대입하기
a=3
print("I eat {0} apples".format(a))
# 2 개이상 값넣기
number=10
day="three"
print("I eat {0} apples and for {1} days".format(number,day))
# f 문자열 포맷팅
print(f"I eat {number+100} apples and for {day} days")


# 왼쪽 정렬
print("{0:<10}".format("hi"))
# 오른쪽 정렬
print("{0:>10}".format("hi"))
# 가운데 정렬
print("{0:^10}".format("hi"))
# 공백채우기
print("{0:+^10}".format("hi"))

```

> 문자열에 관련된 함수
>>count/find/join/upper/lower/strip/replace/strip
```python
# 문자열 관련 함수
# count
a="aabbddcda"
print(a.count("a"))
# find
a= "Python is..."
print(a.find("P"))
print(a.find("p")) #대소문자를 구분하고 값이 존재하지 않는다면 -1 을 반환한다.
# find
print(a.index('i')) # 문자열이 없으면 error가 난다 find와 차이점
# join
print("!".join(a)) # 문자열 사이에 !를 넣어준다.
# 대문자 변환 upper
print(a.upper())
# 소문자 변환 lower
print(a.lower())
# 양쪽 공백을 제거
print(a.strip())
# 문자열 바꾸기
print(a.replace("Python","Java"))
# 문자열 나누기
a="Life is too short"
print(a.split()) # 공백기준으로 문자열을 나눠줌

```
> 3. 리스트 자료형
- 어떠한 자료형도 포함시킬 수 있다.

> 리스트의 인덱싱과 슬라이싱
- 리스트도 문자열처럼 인덱싱과 슬라이싱이 가능하다.
- 리스트의 연산 및 함수
```python
# 리스트 자료형
a=[1,2,3,4,5]
print(a[0:2])
# 리스트의 연산
b= [2,3,4,5]
print(a+b)
# 리스트 반복하기
print(a*2)
# list의 길이
print(len(a))

# 리스트의 수정과 삭제
del a[1] # 삭제 del 객체
print(a)

# 리스트 관련함수 
# 리스트에 요소 추가
a.append(100)
print(a)

# 리스트의 정렬
a.sort()
print(a)

# 리스트의 역순 reverse
a.reverse()
print(a)

# 위치 변환
a=[1,2,3]
print(a.index(2)) # 2는 a의 1번째 요소

# 리스트의 요소 삽입
a.insert(0,4) # 0 위치에 4를 넣는다
print(a)

# 리스트의 요소 제거
a=[1,2,3,4,5,6,3]
a.remove(3) # 가장먼저의 3 을 제거해준다.
print(a)

# 리스트의 요소 끄집어내기
a=[1,2,3,4]
print(a.pop()) # 마지막 값을 주고 제거해준다.
print(a)
print(a.pop(2)) # index 2 값을 주고 제거해준다.
a.count(1) # 1의 갯수를 찾고 돌려준다
# 리스트의 확장
b=[100,2,3,4]
a.extend(b)
print(a)

```
> 4 튜플 자료형
- 튜플은 리스트와 거의 비슷하다
- 차이점 : 리스트 [] 튜플 () , 그값의 생성 삭제 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
- 인덱싱 슬라이싱 모두 가능하다.

> 5 딕셔너리 자료형
- 딕셔너리는 리스트나 튜플처럼 순차적으로 해당하는 요소값을 구하지 않고 key값에 대한 value값을 얻는것이다.
- 주의사항 key는 고유의 값이므로 중복되는 값이 생기는경우 하나를 제외하고 나머지 값들이 무시된다

```python
dic = {'name' : 'pay','phone' : '01110232130','birh':'0613'}
print(dic)
# 딕셔너리 추가
dic["add"] = 'addValue'
print(dic)
# 딕셔너리 요소 제거
del dic["add"] # key값을 넣어주면 관련 데이터를 모두 삭제한다.
print(dic)
# Value 불러오기
print(dic['name'])

# 딕셔너리 관련 함수들
print(dic.keys()) # key값들을 dict_keys로 변환해준다.
print(list(dic.keys()))# list형식으로 바꿔준다.
print(dic.values()) # value갑을 얻을 수 있다.
print(dic.items()) # key와 value의 쌍을 튜플로 묶은 값을 dict_item으로 돌려준다
print(dic.get('name')) # key에 대응되는 value를 돌려준다.
print(dic.get('monkey','name')) # monkey라는 key가 없으면 name값을 가지고오라고 해준다.
print(dic.clear()) # 관련된 쌍을 모두 제거해준다.
print('name' in dic) # 해당 key값이 있는지 조사해준다.

``` 
> 6. 집합 자료형
- 중복을 허용하지 않는다.
- 순서가 없다.
- unordered 이기 떄문에 인덱시으로 갑을 얻을 수 없다.
- list로 변형하여 index를 구하자
- 교집합, 차집한 합집합을 구할 수 있다.
```python
# 집합 자료구조
s1 = set([2,355,6,7,4])
print(s1)
s2 = list(s1)
print(s2)
s3 = set([2,3,4,5,6,7])

# 교집합
print(s1 & s3)
print(s1.intersection(s3))
# 합집합
print(s1|s3)
print(s1.union(s3))
# 차집합
print(s1-s3)
print(s1.difference(s3))

# 값 추가하기
s1.add(1000)
print(s1)
# 여러개 추가하기
s1.update([100,200,300])
print(s1)

# 특정값 제거하기
print(s1.remove(100))
```

> 파이썬에서 자료형의 값을 저장하는 공간,변수
- 파이썬의 변수에 저장된 값을 스스로 판단하여 자료형을 지정함
- 변수 > 객체를 가리키는것
- 객체 : 자료형과같은의미
```python
a=[1,2,3,4]
# [1,2,3,4] 의 값을 가지는 리스트 자료형이 자동으로 메모리에 생성되고 변수 a는 리스트가 저장된 메모리의 주소를 가르키게 된다.
a=[1,2,3,4]
print(id(a))
b=a
print(id(b))  # a 와 동일한 주소를 가르킨다. 즉 복사할 경우 가르키는 대상이 동일하다는 것을 알 수 있다


```
- 두변수가 서로다른 객체를 가르킬때는 copy를 사용해서 한다.

- 변수를 만드는 여러가지 방법
```python
# 튜플 만들기
a,b=('life','is good')
(a,b) = 'python','good'
# 리스트 만들기
[c,d] = ['python','very']
a=1
b=2
a,b=b,a # 간단하게 값교환을 바꿈
# 메모리 위치의 같음을 확인할 때에는 is를 사용한다
a=[1,2,3]
b=[1,2,3]
print( a is b)
```
# 파이썬 기본_2
## 제어문
>비교연산자
|비교연산지|설명|
|---|---|
|x>y|x가 y보다 작다|
|x<y |x가 y보다 크다 |
|x==y| x와y가 같다|
|x!=y| x와 y가 같지않다|
|x>=y| x가 y보다 크거나 같다|
|x<=y| x가 y보다 작거나 같다|
- 결과값은 boolean값 을 갖는다.

- 조건 판단을 하기위한 연산자
|연산자|설명|
|---|---|
|x or y|x와 y둘중에 하나만 참이면 참이다.|
|x and y|x와 y모두 참이어야 한다|
|not x|x가 거짓이면 참이다.|
```python
money = 2000
card = True
if money>3000 or card:
    print("텍시를 탈 수 있습니다.")
else:
    print('택시를 탈 수 없습니다.')
```
- 파이썬의 새로운 문자 특징
|in|not in|
|---|---|
|x in 리스트| x not in 리스트|
|x in 튜플| x not in 튜플|
|x in 문자열|x not in 문자열|

```python
money = 2000
card = True
if money>3000 or card:
    print("텍시를 탈 수 있습니다.")
else:
    print('택시를 탈 수 없습니다.')
    
print(1 in [1,2,3,4]) # True
print(1 not in [1,2,3,4]) #False

print('p' in "python") # True

pocket = ['paper','cellphone']
if 'money' in pocket:
    print("money가 있습니다.")
elif 'paper' in pocket:
    print("paper가 있습니다")
else:
    print("둘다 없습니다")

# 직관적으로 쓰기
score=80
message = "success" if score>=60 else "fail"
print(message)
```



## 반복문
> while 문
```python
treeHit = 0
while treeHit<10:
    treeHit+=1
    print(f"{treeHit}번 돌아가는 중입니다")
```

- 여러 가지 선택지중 하나를 선택해서 입력받는예제
```python
prompt = '''
1. ADD
2. DEL
3. List
4. Quit
'''
number =0
while number !=4:
    print(prompt)
    number=int(input())
```
- 강제로 while문 빠져나가기 break
- while문의 맨 처음으로 돌아가기 continue
```python
a=0
while a<10:
    a+=1
    if a%2 ==0:continue
    print(a) # a를 2로 나누었을때 나머지가0이면 맨앞으로돌아간다
# 1,3,5,7,9
```

> for문

- list를 이용한 for문
```python
text_list=['one','two','three']

for i in text_list:
    print(i)
```

- tuple을 이용한 for문
```python
a= [(1,2),(3,4),(5,6)]
for (first,second) in a:
    print(first,second)
```
- continue 사용하기

```python
marks = [10,20,30,40,50]
number= 0
for mark in marks:
    number+=1
    if mark<30:continue
    print(f'{number}번 학생은 합격이니다')
```
- for문과 range이용하기
```python
add = 0
for i in range(1,11):
    add+=i

print(add)

```
- list에 for문 조건문 이용하기
```python
# 리스트 내포하기
a=[1,2,3,4,5]
result = []
for num in a:
    result.append(num*3)
    
print(result)
result = [num*3 for num in a]
print(result)
result = [num*3 for num in a  if num<3]
print(result)
```
> 함수
- 매개변수(parameter)와 인수(arguments)
- 매개변수 : 함수에 입력으로 전달된 값을 받는 변수
- 인수 : 함수를 호출할 때 전달하는 입력값

> 함수의 결과값은 언제나 하나다.


# 파이썬 기본_3
- 1. 클래스
- 2. 모듈
- 3. 패키지
- 4. 예외처리
- 5. 내장함수
- 6. 외장함수

## 1. 클래스
> 클래스
- Class가 필요한 이유 : 메모리 관리를 위해서
- 같은 함수를 계속 사용하고, 변수들을 따로따로 관리하기 위해서
- 클래스(Class) 란 똑가은 무언가를 계속해서 만들어 낼 수 있는 설계도면
- 객체(Object) 란 클래스로 만든 피조물이다
- 클래스로 만든 객체에 가장 중요한 속성
    - 객체마다 고유한 성격을 가진다.
    - 즉, 독립적인 객체를 생성에 서로 영항을 주지 않는다.
- 인스턴스(Instance)
```python

class Cookie:
    def setdata(self, first, second): # 메서드의 매개변수
        # 메서드의 수행문
        self.first=first
        self.second=second
        

a = Cookie(4,2)
Cookie.setdata(a,4,2)

print(a.first)
print(a.second)
```
- a객체는 Cookie의 인스턴스이다.
- a의 객채변수는 다음과 같이 불러온다.
- 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.

> 생성자(Constructor)
- 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.
- 객체에 초깃값을 설정해야 할 필요가 있을때 같은 메서드를 호출하여 초깃값을 설정하기 보다는 생성자를 구현하는것이 안전한 방법이다.

- 파이썬 메서드 이름으로  \_\_init\_\_ 를 사용하면 이 메서드가 생상자가 된다. 
- setdata 메서드와 이름만 다르고 모든게 동일
- \_\_init\_\_으로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다는 차이가 있다.
```python
class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    
    def add(self):
        result = self.first+self.second
        return result
    
    def sub(self):
        result = self.first-self.second
        return result
    
    def mul(self):
        result =  self.first*self.second
        return result
        
    def div(self):
        result = self.first/self.second
        return result
    
a=FourCal(4,2)
print(a.first)
print(a.second)
```
- self => 생성되는 객체 first => 4 second => 2

> 클래스의 상속(Inheritance)
- 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는것
- FourCal 클래스에 a의 b승을 추가해보자
- class  MoreCal(FourCal) => class 클래스 이름(상속할 클래스 이름)
```python
class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    
    def add(self):
        result = self.first+self.second
        return result
    
    def sub(self):
        result = self.first-self.second
        return result
    
    def mul(self):
        result =  self.first*self.second
        return result
        
    def div(self):
        result = self.first/self.second
        return result
    
class MoreCal(FourCal):
    def pow(self):
        result = self.first**self.second
        return result
    
a=MoreCal(4,2)

print(a.pow())
print(a.mul())


```

> 메서드 오버라이딩(Overriding, 덮어쓰기)
- 부모클래스에 있는 메서드를 동일한 이름으로 다시 만드는것

```python
class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    
    def add(self):
        result = self.first+self.second
        return result
    
    def sub(self):
        result = self.first-self.second
        return result
    
    def mul(self):
        result =  self.first*self.second
        return result
        
    def div(self):
        result = self.first/self.second
        return result
    
class MoreCal(FourCal):
    def div(self):
        if self.seond==0:
            return 0
        else:
            result = self.first**self.second
        return result
    
a=MoreCal(4,2)

print(a.div())
```

> 클래스 변수
- 객체변수는 다른 객체들에 영향을 받지 않고 독립적으로 그값을 유지한다
- 객체변수와 다른 클래스변수
``` python
class Family:
    lastname="김"
    
a=Family()
print(a.lastname)

Family.lastname="박"
print(a.lastname)

```
- 클래스 변수 값을 변경했더니 클래스로 만든 객체의 lastname 값이 모두 변경됨
- 즉, 클래스 변수는 공유가 된다는 사실을 증명
- 클래스변수보다는 객체변수가 훨씬 중요하다.

## 5.2 모듈

- 모듈 :  함수나 변수 또는 클래스를 모아 놓은 파일
- 모듈을 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일
- 모듈 만들기
- 클래스 , 함수로 구성된 py 만들기
- import로 불러오기
- 함수를 일부만 불러오려면 from 모듈 이름 import 모듈함수 (전체 불러오려면 *)

> if __name__="__main__":의 의미
- 직접 파일을 실행했을 떄는 __name__=="__main__"이 참이된다
- 반대로 대화형 인터프리터나 다른 파일에서 이모듈을 사용하면 다음 문장이 수행되지 않는다.
- 파이썬의 __name__변수는 내부적으로 사용하는 특별한 변수 이름이다
- ex mo1.py처럼 직접 mod1.py 파일을 실행할 경우 __name__ 변수에는 __main__값이 저장된다. 하지만 파이썬 쎌이나 다름 파이썬 모듈에서는 mod1을 import 할경우 mod1.py의 __name__변수에는 mod1.py의 모듈이름 값 mo1이 저장된다.

- 위치가 다른 파일에 있을경우 모듈사용하기
``` python
import sys
sys.path # 여기서 구한 값을
sys.path.append("모듈을 저장한 디렉터 사용하기")
```

## 5.3 패키지
> 페키지(Package)는 도트를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)로 관리할 수있게 해준다.

> __init__ .py의 용도
- __init__ 파일은 해당 디렉토리가 패키지의 일부임을 알려주는 역활을한다.
- 이 파일이 없으면 페키지로 인식하지 않는다.

## 5.4 예외처리
- try,excpet문
- except [발생하는 오류 [as 오류 메시지 변수]]
```python
try:
    5/0
except ZeroDivisionError as e :
    print(e)
```

- 오류가 발생하더라도 그냥 통과시켜야할 경우 
except 안에 pass를 넣어준다.

# 5.5 내장함수 (따로 정리)
- 기본적인 자료형에 따른 내장함수들이 정리되어있음
# 5.6 외장함수
- 목적에 맞는 라이브러리를 사용하기
- 어떤 라이브러리가 존재하고 어떻게 사용할지 알아보자
>sys
- 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
>pickle
- 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
>OS
- OS모듈은 환경 변수나 디렉터리,파일 등의 OS를 제어할 수 있게 헤주는 모듈
>shutil
- 파일을 복사해 주는 파이썬 모듈
>glob
- 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름 모두알아야할 떄 사용하는 모듈
>Tempfile
- 파일을 임시로 만들어서 사용할 때 유용할 모듈
>Time
- 시간과 관련된 모듈
> random
- 난수를 발생시키는 모듈
>webbrowser
- 자신의 시스템에서 사용자는 기본 웹브라우저를 자동으로 실행하는 모듈

# 이것이 코딩테스트다 브록
