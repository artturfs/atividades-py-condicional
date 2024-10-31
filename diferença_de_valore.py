a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if c != a:
    print("A é diferente de C")
    if b != a:
        print("A é diferente de B")

elif a == c:
    print("A é igual a C")
    if a == b:
        print("A é igual a B")
    elif a != b:
        print("A é diferente de B")

if b == c:
    print("B é igual a C")

else:
    print("B é diferente de C")