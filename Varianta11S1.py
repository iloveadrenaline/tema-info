n = int(input("Introduceți un număr n: "))
k = int(input("Introduceți un număr k: "))

while n > 0 and k > 0:
    c = n % 10
    if c % 2 == 1:
        p = p * c

    n = n // 10
    k = k - 1

print(p)