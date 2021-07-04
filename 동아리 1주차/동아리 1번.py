
##1번 문제
name1,name2 = input("이름을 입력하세요: ").split(',')
age1,age2 = map(int,input("나이를 입력하세요: ").split(','))
print(name1,"의 나이는 ",age1,"살입니다",sep = '')
print(name2,"의 나이는 ", age2, "살입니다",sep = '')
print("엄마의 나이는 ",((age1+age2)-2), "살입니다",sep ='')
print("아빠의 나이는 ",(age2*2),"살입니다",sep ='')


