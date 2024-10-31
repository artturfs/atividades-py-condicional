x = float(input("Digite quantos dias tem o ano: "))

if 0 < x and x == 365 and x == 366:
    if (x / 4) == 0:
        print("o ano é bissexto")
    else:
        print("O ano não é bissexto")
else:
    print("Não é válido")
