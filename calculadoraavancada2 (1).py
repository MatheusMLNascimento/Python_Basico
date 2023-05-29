print("Calculadora, escolha a operação:\n n1 - Soma\n n2 - divisão\n n3 - multiplicação\n n4 - subtração\n n5 - potência")
soma = "n1"
divi = "n2"
multi = "n3"
sub = "n4"
poten = "n5"
select = input("Opção desejada:")
print()
if select == soma:
        num = int(input("Quantos números você quer somar?(De 2-5 números)"))
        if num == 2:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))    
            print("resultado: ", a + b)
        elif num == 3:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            print("resultado: ", a + b + c)
        elif num == 4:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            print("resultado: ", a + b + c + d)
        elif num == 5:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            e = int(input("Quinto número"))
            print("resultado: ", a + b + c + d + e)
elif select == poten:
    print("Potência")
    print()
    a = int(input("Primeiro número"))
    b = int(input("Segundo número"))    
    print("resultado: ", a ** b)
elif select == divi:
        num = int(input("Quantos números você quer dividir?(Até 5 números)"))
        if num == 2:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))    
            print("resultado: ", a / b)
        elif num == 3:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            print("resultado: ", a / b / c)
        elif num == 4:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            print("resultado: ", a / b / c / d)
        elif num == 5:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            e = int(input("Quinto número"))
            print("resultado: ", a / b / c / d / e)
elif select == multi:
        num = int(input("Quantos números você quer multiplicar?(Até 5 números)"))
        if num == 2:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))    
            print("resultado: ", a * b)
        elif num == 3:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            print("resultado: ", a * b * c)
        elif num == 4:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            print("resultado: ", a * b * c * d)
        elif num == 5:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            e = int(input("Quinto número"))
            print("resultado: ", a * b * c * d * e)
elif select == sub:
        num = int(input("Quantos números você quer subtrair?(Até 5 números)"))
        if num == 2:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))    
            print("resultado: ", a - b)
        elif num == 3:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            print("resultado: ", a - b - c)
        elif num == 4:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            print("resultado: ", a - b - c - d)
        elif num == 5:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            e = int(input("Quinto número"))
            print("resultado: ", a - b - c - d - e)