x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))
z = int(input("Digite um valor para z: "))

if x > y and x > z:
    print("X é o maior número")
    
elif y > x and y > z:
    print("Y é o maior número")
    
elif z > x and z > y:
    print("Z é o maior número")

else:
    print("O valor provavelmente não é um número")