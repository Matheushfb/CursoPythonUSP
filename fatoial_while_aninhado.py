n = int(input("Insira um numero para que se calcule o fatorial: "))
while n >= 0:
    fat = n
    i = 1
    while i < n:
        fat = fat * (n-i)
        i = i + 1
    print(fat)
    n = n - 1
    n = int(input("Insira um numero para que se calcule o fatorial: "))
