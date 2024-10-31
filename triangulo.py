x = float(input("Digite o primeiro lado: "))
y = float(input("Digite o segundo lado: "))
z = float(input("Digite o terceiro lado: "))

if x == y and y == z and x == z:
    print("Equilatero")
    
elif x != z and x != y and y != z:
    print("Escaleno")
    
else:
    print("Isoceles")

a = x ** 2
b = y ** 2
c = z ** 2

if a == (b + c) or b == (a + c) or c == (a + b):
    print("Retangulo")