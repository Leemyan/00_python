'''
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3) #덧셈
print(2*8) #곱셈
print(2/8) #나누기

print('풍선')
print("나비")
print("ㅋ"*9)
print(2*2)

''' 
    #주석처리 1번 (작은따옴표 3개)

# 주석처리 2번 (컨트롤 + / 또는 command + /)
# print(5 > 10)
# print(True)
# print(False)
# print(not True)
# print(not (5 > 10))



# animal = "강아지"
# name = "윈디"
# age = 7
# hobby = "사람만나기"
# is_adult = age >= 4

# print("우리집 " + animal + "의 이름은 " + name + " 에요")
# print(name + "는 "+str(age)+"살이며, "+hobby+"을/를 아주 좋아해요")
# print("우리 " + name + "는"+str(is_adult)+"어른이라서 나중에 무지개다리에서 만날거에요")

# animal = "기니피그"
# name = "반반이/노랑이"
# age = 4
# hobby = "밥먹기"
# is_adult = age >= 6

     # + 말고 , 로도 붙일 수 있음. 대신 ,(쉼표)는 띄어쓰기가 하나 자동으로 붙는다.

# print("우리집 " , animal , "의 이름은 " , name , " 에요")
# print(name , "는 "+str(age),"살이며, ",hobby,"을/를 아주 좋아해요")
# print("우리 " , name , "는",str(is_adult),"어른이라서 나중에 무지개다리에서 만날거에요")



# Quiz. 변수를 이용하여 다음 문장을 출력하시오.
# 변수명 : station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력문장 : xx 행 열차가 들어오고 있습니다.

# station = {"사당", "신도림", "인천공항"}

#print(station)

## 복잡하게 생각하지 말 것.
# station = "사당"
# print(station, "행 열차가 들어오고 있습니다.")

# station = "신도림"
# print(station, "행 열차가 들어오고 있습니다.")

# station = "인천공항"
# print(station, "행 열차가 들어오고 있습니다.")


# print(1+1) #2
# print(3-2) #1
# print(5*2) #10
# print(6/3) #2.0

# print(2**3) #2^3 = 8
# print(5%3) #나머지구하기 2
# print(10%3) #나머지구하기 1
# print(5//3) #몫 1
# print(10//3) #몫 3

# print(10 > 3) #True
# print(4 >= 7) #False
# print(10 < 3) #False
# print(5 <= 5) #True

# print(3 == 3) #True
# print(4 == 2) #False
# print(3 + 4 == 7) #True

# print(1 != 3) #True
# print(not(1 != 3 )) #False

# print((3 > 0) and (3 < 5)) #True
# print((3 > 0) & (3 < 5)) #True

# print((3 > 0) or (3 > 5)) #True
# print((3 > 0) | (3 > 5)) #True

# print(5 > 4 > 3) #True
# print(5 > 4 > 7) #False

# print(2 + 3 * 4) #14
# print((2 + 3) * 4) #20

# number = 2 + 3 * 4 #14
# print(number)

# number = number + 2 #16
# print(number)

# number += 2 #18
# print(number)

# number *= 2 #36
# print(number)

# number /= 2 #18
# print(number)

# number -= 2 #16
# print(number)

# # number %= 2 #0
# # print(number)

# number %= 5 #1
# print(number)


# print(abs(-5)) #5
# print(pow(4, 2)) #4^2 = 4*4 = 16
# print(max(5, 12)) #12
# print(min(5, 12)) #5
# print(round(3.14)) #3
# print(round(4.99)) #5

# from math import *
# print(floor(4.99)) #4 반올림
# print(ceil(3.14)) #4 올림
# print(sqrt(16)) #4 제곱근


# from random import *

# print(random()) #0.6413675117230072 랜덤(0.0 ~ 1.0 미만의 임의의 값 생성)
# print(random() * 10) #4.872338492594057 랜덤(0.0~10.0 미만의 임의의 값 생성)

# print(int(random() * 10)) #0~10 미만의 임의의값 생성
# print(int(random() * 10)) #0~10 미만의 임의의값 생성
# print(int(random() * 10)) #0~10 미만의 임의의값 생성

# print(int(random() * 10) + 1) #1~10 이하의 임의의 값 생성 
# print(int(random() * 10) + 1) #1~10 이하의 임의의 값 생성 
# print(int(random() * 10) + 1) #1~10 이하의 임의의 값 생성 
# print(int(random() * 10) + 1) #1~10 이하의 임의의 값 생성 
# print(int(random() * 10) + 1) #1~10 이하의 임의의 값 생성 
# print(int(random() * 10) + 1) #1~10 이하의 임의의 값 생성 

#로또값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의값 생성

# print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1~46 미만의 임의의 값 생성

# print(randint(1, 45)) # 1~45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1~45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1~45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1~45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1~45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1~45 이하의 임의의 값 생성

'''
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''

# # day = randint(4, 28) # 값을 감싸면 해결
# # print("오프라인 스터디 모임 날짜는 매월"+ day +" 일로 선정되었습니다.")
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월"+ str(date) +" 일로 선정되었습니다.")

'''문자열'''

# sentense = '나는 소년입니다'
# print(sentense)
# sentense2 = '파이썬은 쉬워요'
# print(sentense2)
# sentense3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentense3)

'''슬라이싱'''

jumin = "990120-1234567"

print("성별 : " + jumin[7]) # 1
print("연도 : " + jumin[0:2]) # 0번째부터 2번째 직전까지
print("월 : " + jumin[2:4]) # 01
print("일자 : " + jumin[4:6]) # 20

print("생년월일 : " + jumin[:6]) # 990120
print("뒤 7자리 : " + jumin[7:]) # 1234567