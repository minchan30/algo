num = int(input())
num2 = input() #   '54321'
a = 0
# num2[0] ==>'5'
# num2[1] ==>4
# num2[2] ==>3
# num2[3] ==>2
# num2[4] ==>1

for i in range(num) :
    a += int(num2[i])

print(a)