n = int(input("Introduceți un număr n: "))
k = int(input("Introduceți un număr k: "))
nr = 0
p = 1

while n != 0 and k != 0:
    if n%2 == 0:
        nr = nr + n%10 * p
        p = p * 10

    else:
        k = k - 1
    n = n // 10

print(nr)