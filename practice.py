# 문자열
'''
print("ㅋㅋㅋㅋㅋ")
print('ㅋㅋㅋㅋㅋ')
print("ㅋ"*8)
'''
# 참 / 거짓
'''
print( 5 > 10)
print(5<10)
print(True)
print(False)
print(not True)
print(not ( 5 > 10))
'''
# 변수
# * 애완동물을 소개해 주세요~
'''
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+animal+"의 이름은 "+name+"이예요")
hobby = "공놀이"
#print(name+"는 "+ str(age)+ "살이며, "+hobby+"을 아주 좋아해요")
print(name,"는 ",age,"살이며, ",hobby,"을 아주 좋아해요")
# + 뿐만 아니라 " , " 도 문장을 합칠 때 사용 가능하나 +와 달리 str() 자료형 변형을 안해도 된다.
print("연탄이는 어른일까요? "+ str(is_adult))
'''
# 주석
''' 내용 문장 주석 '''
   # 한줄 주석
   #  특정 구간만 주석 처리를 진행 하고 싶다면 "ctrl + /" 로 주석 처리한다.

# 퀴즈 01
'''statin = "사당"
print(statin,"행 열차가 들어오고 있습니다.")
statin="신도림"
print(statin,"행 열차가 들어오고 있습니다.")
statin="인천공항"
print(statin,"행 열차가 들어오고 있습니다.")
'''
# 숫자열(계산)
'''
print( 2**3 ) # 2^3=8
print( 5%3) #나머지 값 추출 2
print(10%3) #나머지 값 추출 1
print(5//3) # 나눗샘의 목 값 추출 1

print(10 > 3) #True
print(4>= 7) # False
print(10< 3) # False
print(5<=5) # True

print (3==3) # True
print(4==2) # False
print(3+4 == 7 ) # True

print(1 != 3) #True
print(not(1 != 3)) #False
'''
'''
print((3>0) and (3<5)) # True
print((3>0) & (3<5)) # True

print((3>0) or (3<5)) # True
print((3>0) | (3<5))  # True

print(5>4>3)# True
print(5>4>7) #False
'''
# 숫자열 (변수 더하기)
'''
number=2+3*4 # 14
print(number)
number=number+2 # 16
print(number)
number+=2 # 18
print(number)
number*=2 # 36
print(number)
number/=2 # 18
print(number)
number-=2 # 16
print(number)
number%=2 # 0 ( 나머지 )
print(number)
'''
# 숫자열( 절대값, 제곱값 등 )
'''
print(abs(-5)) # 절대값 5
print(pow(4,2)) # 4^2 =4*4=16
print(max(5,12,20)) # 큰 값 출력
print(min(5,12)) # 작은 값 출력
print(round(3.14))#3  소숫잠 첫째자리
print(round(4.99))#5 

from math import * # python의  math 라이브러리 사용 할 것인데 모두 ( * ) 사용한다
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4
'''
# 랜덤 변수
'''
#from random import *
# print(random()) # 0.0~1.0 미만의 임의의 값 생성
# print(random()*10) # 0.0. ~ 10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0~10 미만의 임의의 값 생성
# print(int(random()*10)) # 0~10 미만의 임의의 값 생성
# print(int(random()*10)) # 0~10 미만의 임의의 값 생성
# print(int(random()*10)+1) # 1~10 이하의 임의의 값 생성
# print(int(random()*10)+1) # 1~10 이하의 임의의 값 생성
# print(int(random()*10)+1) # 1~10 이하의 임의의 값 생성
# print(int(random()*10)+1) # 1~10 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1~45 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1~45 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1~45 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1~45 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1~45 이하의 임의의 값 생성
# print(randrange(1,46))#1~46 미만의 임의의 값 생성
# print(randrange(1,46))#1~46 미만의 임의의 값 생성
# print(randrange(1,46))#1~46 미만의 임의의 값 생성
# print(randrange(1,46))#1~46 미만의 임의의 값 생성
# print(randrange(1,46))#1~46 미만의 임의의 값 생성
# print(randint(1,45))# 1~45 이하의 임의의 값 생성
# print(randint(1,45))# 1~45 이하의 임의의 값 생성
# print(randint(1,45))# 1~45 이하의 임의의 값 생성
# print(randint(1,45))# 1~45 이하의 임의의 값 생성
# print(randint(1,45))# 1~45 이하의 임의의 값 생성
# print(randint(1,45))# 1~45 이하의 임의의 값 생성
'''
# 퀴즈02
'''
from random import *
study_off=int((random()*25)+4) # 1~3일까지는 스터디 준비 -> 제외 // 28일 이내의 값
print("오프라인 스터미 모임 날짜는 매월"+str(study_off ))
study_off=randrange(4,29)#4~28일까자의 날짜
print("오프라인 스터미 모임 날짜는 매월"+str(study_off ))
study_off=randint(4,28)#4~28일까자의 날짜
print("오프라인 스터미 모임 날짜는 매월"+str(study_off ))
'''

# 문자열
'''
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = '나는 파이썬이 쉬워요' 
print(sentence2)
sentence3= """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)
'''

#슬라이싱 
'''
jumin = '940917-1234567'

print("성별 : " +jumin[7])
print("연 :"+ jumin[0:2] ) # 0~2 직적의 인덱스 까지 즉 0,1 인덱스 값을 가져옵니다.
print("월 : "+ jumin[2:4])
print("일 : "+jumin[4:6])

print("생년월일 : "+jumin[:6]) # 처움부터 6 직전까지
print("뒤 7자리 : "+jumin[7:]) # 7부터 끝까지 
print(" 뒤 7자리 (뒤에부터)" + jumin[-7:]) # 맨 뒤에서 7번째 부터 끝까지
'''
# 문자열 처리함수
'''python= "Python is Amazing"
print(python.lower()) #소문자로 변화
print(python.upper()) #대문자로 변화
print(python[0].isupper()) #0인덱스가 대문자인지 blood
print(len(python)) # 문자열 개수
print(python.replace("Python","Java")) # 문자열 

index = python.index('n') # python 변수에서 "n"이 있는 인덱스 위치
print(index) #5번째

index= python.index('n', index +1) # python 변수에서 처음 n 다음부터 찾음
print(index)

print(python.find("Java")) # 원하는 값이 없는 경우 -1을 반환
#print(python.index("Java")) # 오류가 발생하면서 프로그램 오류로 다음 코딩 내용 안내려옴

print(python.count("n"))
'''
