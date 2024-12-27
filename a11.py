lst = [1, 2, 3, 4]
indices = [0, 1, 3]  
for i in range(len(lst)):
    if i == 0:
        print(lst[i], end=" ")
        print('a', end=" ")  
    elif i == 1 or i == 3:
        print(lst[i], end=" ")
