A , B = map(int , input().split())
basket = [0] * A

for _ in range(B) :
    i , j , k = map(int , input().split())
    basket[i - 1 : j] = [k] * (j + 1 - i)

for b in basket :
    print(b , end = " ")