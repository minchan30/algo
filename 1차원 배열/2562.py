num =[]
for p in range(9) :
    a = int(input())
    num.append(a)
num_max = 0
num_index = 0
for i in range(len(num)):
    if num_max < num[i]:
        num_max = num[i]
        num_index = i
print(num_max)
print(num_index + 1)