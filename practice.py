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

''' #주석처리 1번 (작은따옴표 3개)

# 주석처리 2번 (컨트롤 + / 또는 command + /)
# print(5 > 10)
# print(True)
# print(False)
# print(not True)
# print(not (5 > 10))



animal = "강아지"
name = "윈디"
age = 7
hobby = "사람만나기"
is_adult = age >= 4

print("우리집 " + animal + "의 이름은 " + name + " 에요")
print(name + "는 "+str(age)+"살이며, "+hobby+"을/를 아주 좋아해요")
print("우리 " + name + "는"+str(is_adult)+"어른이라서 나중에 무지개다리에서 만날거에요")

animal = "기니피그"
name = "반반이/노랑이"
age = 4
hobby = "밥먹기"
is_adult = age >= 6

# + 말고 , 로도 붙일 수 있음. 대신 ,(쉼표)는 띄어쓰기가 하나 자동으로 붙는다.

print("우리집 " , animal , "의 이름은 " , name , " 에요")
print(name , "는 "+str(age),"살이며, ",hobby,"을/를 아주 좋아해요")
print("우리 " , name , "는",str(is_adult),"어른이라서 나중에 무지개다리에서 만날거에요")