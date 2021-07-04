## 문제 2.1
lst1 = []
for i in range(-25,26) :
    lst1.append(i)

print(lst1)


## 문제 2.2

lst2 = []
lst3 = []
for i in range(0,len(lst1)):
    a = lst1[i]
    if a < 0 :
        lst2.append(a)
    elif a > 0 :
        lst3.append(a)
print(lst2)
print(lst3)
