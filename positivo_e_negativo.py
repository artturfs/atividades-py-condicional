x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))

if x > 0:
    print("X é positivo")
    if y > 0:
        print("Y é positivo")
    else:
        print("Y é impar")
    
elif x < 0:
    print("X é negativo")
    if y > 0:
        print("Y é positivo")
    else:
        print("Y é negativo")