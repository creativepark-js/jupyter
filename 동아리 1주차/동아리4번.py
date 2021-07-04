##4.1번
print("a","b",1,2,"[c,d,3]","(1,2,3)",sep = ',')

##4.2번
x =list(range(1,100,2))
print(x)

##4.3번

a,b = map(int,input("나누는 수와 나누어지는 수를 입력하세요:").split())
c = [a,b,int(b/a),int(b%a)]
print(c)

##4.4번

y = ["안녕하세요","공백","저는"]
y.remove("공백")
y.append("박재성입니다")
print(y)
