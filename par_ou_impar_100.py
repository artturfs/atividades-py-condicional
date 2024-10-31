x = float(input("Digite um valor: "))

if x % 2 == 0:
    print("O número é par!")
    if x > 100:
        print("O número é maior que 100")
    else:
        print("O número é menor que 100")

else:
    print("O número é impar")
    if x < 100:
        print("O número é menor que 100")