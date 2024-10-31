b = float(input("Digite a base do retângulo: "))
h = float(input("Digite a altura do retângulo: "))

area = b * h
perimetro = 2 * (b + h)

print("\nUsando a fórmula para área: b * h, \nconseguimos o resultado: {:.2f}".format(area)) 
print("Usando a fórmula para perimetro: 2 * (b + h), \nconseguimos o resultado: {:.2f}".format(perimetro))