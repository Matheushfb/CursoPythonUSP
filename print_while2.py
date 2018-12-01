altura = int(input("digite a altura"))
largura = int(input("digite a largura"))
y = 0
x = 0

while y < largura:
    y = y + 1
    while x < altura:
        if y == 1 or y == largura or x == 0 or x == altura - 1:
            print("#", end ="")
        else:
            print (end =" ")
        x = x + 1
    print()
    x=0
