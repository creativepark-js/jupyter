## 3번 문제

n1,n2 = map(int,input("두 자리 정수를 2개를 입력하시오 : ").split(','))

if n1 != n2 :
    if n1//10 == n2//10 or n1%10 == n2%10:
        print(f"{n1},{n2}: 일의 자리 혹은 십의 자리 수가 일치함")
    elif n1//10 == n2%10 or n1%10 == n2//10:
        print(f"{n1},{n2}: 일치하는 숫자가 존재하나 두 수에서의 자리값이 서로 다름")
    else:
        print(f"{n1},{n2}: 일치하는 숫자가 없음")
else:
    print(f"{n1},{n2}: 두 수는 동일함")
