str = input()
l = [-1] * 26

for i in range(len(str)):
    if l[ord(str[i]) - ord('a')] == -1:
        l[ord(str[i]) - ord('a')] = i
for L in l :
    print(L , end = " ")