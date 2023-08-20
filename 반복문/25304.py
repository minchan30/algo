Money = int(input())
Count = int(input())

sum = 0

for i in range(Count) :
    A , B = map(int,input().split())
    sum = sum + (A * B)
if sum == Money :
    print('Yes')
else :
    print('No')