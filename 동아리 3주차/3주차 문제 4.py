##문제4

import random

r = random.randrange(1,101,1)

count = 0


while True:
    num = int(input("1부터 100까지의 숫자를 입력하세요: "))
    count += 1
    if r == num:
        print("정답입니다 시도횟수 : %d" %count)
        break
    elif r < num :
        print("더 작은 값을 입력하세요")
        continue
    elif r > num :
        print("더 큰 값을 입력하세요")
        continue
