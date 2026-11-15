x = int(input("Introduceți un număr x: "))
y = 0 

while x != 0:
    while x > 9:
        x = x // 10

    y = y * 10 + x
    x = int(input("Introduceți un număr x: "))

print(y)