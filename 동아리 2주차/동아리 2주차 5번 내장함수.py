#5번 문제
name = input("이름 : ")
major = input("학과 : ")
st_id = int(input("학번 : "))

myself = dict(이름 = name , 학과 = major , 학번 = st_id)

##5.1번

quiz1 = list(myself.keys())
print(quiz1)

##5.2번

quiz2 = list(myself.values())
print(quiz2)

##5.3번

quiz3 = list(myself.items())
print(quiz3)

##5.4번

my_self = dict(zip(quiz1,quiz2))
print(my_self)


