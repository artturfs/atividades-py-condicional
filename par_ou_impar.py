x = int(input("Digite um valor para x: "))
y = int(input("Digite um valor para y: "))

if x % 2 == 0:
    print("X é par")
    if y % 2 == 0:
        print("Y é par")
    else:
        print("Y é impar")
    
elif x % 2 == 1:
    print("X é impar")
    if y % 2 == 0:
        print("Y é par")
    else:
        print("Y é impar")