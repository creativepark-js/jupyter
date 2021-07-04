#5번 문제
name = input("이름을 입력하세요: ")
major = input("학과를 입력하세요: ")
st_id = int(input("학번을 입력하세요: "))

myself = dict(이름 = name , 학과 = major , 학번 = st_id)

##5.1번

quiz1 = myself.keys()
print(myself.keys())

##5.2번

quiz2 = myself.values()
print(quiz2)

##5.3번

quiz3 = myself.items()
print(quiz3)

##5.4번

my_self = dict(zip(quiz1,quiz2))
print(my_self)
