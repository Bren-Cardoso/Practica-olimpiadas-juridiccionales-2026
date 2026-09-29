cant = int(input())
peso = input().split()
peso.sort()

if cant%2 == 0:
    if cant >= 4:
        if peso[0] == peso[1] and peso[2] == peso[3]:
            print("YES")
        if peso[0] != peso[1] or peso[2] != peso[3]:
            print("NO")
    if cant == 2:
        if peso[0] == peso[1]:
            print("YES")
        if peso[0] != peso[1]:
            print("NO")
else:
    print("NO")