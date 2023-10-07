N , M = map(int , input().split())
num = [] # 1 2 3 4 5

for k in range(N) :# 0 1 2 3 4
    num.append(k + 1)

for k in range(M) :
    i , j = map(int , input().split()) # 1 2
    num[i - 1], num[j - 1] = num[j - 1], num[i - 1]

for n in num :
    print(n , end = " ")