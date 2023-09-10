num = int(input())
for i in range(1 , num + 1) :
    print(' '*(-i + num), end='')
    print('*'*(i))
               
# N = 5
# *의 개수
# 1 1
# 2 2
# 3 3
# i i

# ' '의 개수
# 1 4
# 2 3
# y = -x + k

#    *
#   **
#  ***
# ****

# N = 4
# ' '의 개수
# 1 3
# 2 2
# y = -x + k

# N K
# 5 5
# 4 4
# y = N