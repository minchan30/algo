LY = int(input())
if LY % 4 == 0 and (LY % 100 != 0 or LY % 400 == 0):
    print(1)
else :
    print(0)