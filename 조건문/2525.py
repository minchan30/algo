H , M = map(int , input().split())
T = int(input())

X = T // 60
Y = T % 60

H = H + X
M = M + Y

if M >= 60:
    H = H + 1
    M = M - 60

if H >= 24:
    H = H - 24

print(H, M)



# M + T =  몇시간 몇분 3시간 30분
# H = H + 3
# # pirnt(H,30분)
# H == 26시
# H = H % 24  => 2시