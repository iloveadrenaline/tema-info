a = int(input("Introduceți un număr a: "))
b = int(input("Introduceți un număr b: "))
k = 0

for i in range(a, b):
    n = i
    c = 0
    while n > 0:
        if n % 2 == 1:
            c = c + 1

        n = n // 10

    if c > 0:
        k = k + 1


print(k)