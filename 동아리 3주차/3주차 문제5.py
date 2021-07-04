##문제 5

def calc(v1,v2,oper):
    if oper == "+" or oper == "덧셈":
        print("%d + %d = %d" %(v1,v2,v1+v2))
        
    elif oper == "-" or oper == "뺄셈" :
        print("%d - %d = %d" %(v1,v2,v1-v2))
        
    elif oper == "*" or oper == "곱셈":
        print("%d * %d = %d" %(v1,v2,v1*v2))
        
    elif oper == "/" or oper == "나눗셈" :
        print("%d / %d = %0.1f" %(v1,v2,v1/v2))
        
    else :
        print("오류 : 기호를 확인하세요")
        

try :
    num1,num2 = map(int,input("숫자 두 개를 입력하세요:").split())
    
    operator = input("산술 방식을 입력하세요:")
    
    calc(num1,num2,operator)
    
except ValueError :
    
    print("end of caculation")
