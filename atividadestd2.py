x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
z = float(input("Digite o terceiro número: "))

print("\nO triângulo equilátero é um tipo de triângulo que possui os três lados congruentes")
print("Triângulo isósceles é um polígono que apresenta três lados, sendo, pelo menos, dois deles congruentes")
print("Triângulo escaleno tem todos os lados com medidas diferentes.")
print("O triângulo retângulo é um polígono que possui três lados e três ângulos, e um desses ângulos é reto, ou seja, possui 90º.")

if x == y == z:
    print("\nO triângulo é equilátero")

elif x == y or y == z or x == z:
    if x != z or y != z or x != y:
        print("\nO triângulo é isóceles")

elif x != z and x != y and z != y:
    print("\nO triângulo é escaleno")

else:
    print("\nO triângulo é retângulo")

    