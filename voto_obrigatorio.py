idade = int(input("Qual sua idade?: "))

if idade == 16 or idade == 17 or idade >= 70:
    print("Na sua idade, o voto é opcional")
    
elif idade >= 18 and idade <= 69:
    print("Na sua idade, o voto é obrigatóro")
    
elif idade < 16:
    print("Na sua idade, o voto é proibido")