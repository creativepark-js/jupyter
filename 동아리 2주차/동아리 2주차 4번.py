place = input('식당을 입력하세요."금정/학생/교직원" :')
menu = input('메뉴를 입력하세요."아침/정식/특정식" :')

if place == "금정":
    if menu == "아침":
        print("1,000원입니다.")
    elif menu == "정식":
        print("3,500원입니다.")
    else:
        print("존재하지 않는 메뉴입니다")
elif place == "학생":
    if menu == "특정식":
        print("4,500원입니다.")
    elif menu == "정식":
        print("3,500원입니다.")
    else:
        print("존재하지 않는 메뉴입니다")
elif place == "교직원":
    if menu == "정식":
        print("4,500원입니다.")
    else:
        print("존재하지 않는 메뉴입니다")
else:
    print("존재하지 않는 식당입니다")
