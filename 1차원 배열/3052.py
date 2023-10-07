l = [0] * 42

for _ in range(10):
    n = int(input())
    l[n % 42] += 1

print(l)