book = [0] * 30

for _ in range(28):
    book[int(input())-1] = 1

for i in range(30):
    if book[i] == 0:
        print(i + 1)