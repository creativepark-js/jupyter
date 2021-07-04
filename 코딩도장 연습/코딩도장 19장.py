height = int(input())
for i in range(height):
    for j in reversed(range(height)):
        if j > i :
            print('',end='')
        else:
            print('*', end='') 
    print()
    
