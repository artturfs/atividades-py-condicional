a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

primeiro = segundo = terceiro = 0

if a <= b and a <= c:
    primeiro = a
    if b <= c:
        segundo = b
        terceiro = c

    else:
        segundo = c
        terceiro = b

elif b <= a and b <= c:
    primeiro = b
    if a <= c:
        segundo = a
        terceiro = c

    else:
        segundo = c
        terceiro = a

else:
    primeiro = c
    if a <= b:
        segundo = a
        terceiro = b

    else:
        segundo = b
        terceiro = a

print("Os valores em ordem crescente são:", primeiro, segundo, terceiro)