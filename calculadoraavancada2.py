print("Calculadora, escolha a operação:\n+ = Soma\n/ = divisão\nx = multiplicação\n- = subtração\nn5 - potência")
soma = "+"
divi = "/"
multi = "x"
sub = "-"
poten = "n5"
select = input("Opção desejada:")
print()
if select == soma:
        num = int(input("Quantos números você quer somar?(De 2-5 números)"))
        if num == 2:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))    
            print('{} + {} = '.format(a, b), (a + b))
        elif num == 3:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            print('{} + {} + {} = '.format(a, b, c), (a + b + c))
        elif num == 4:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            print('{} + {} + {} + {} = '.format(a, b, c, d), (a + b + c + d))
        elif num == 5:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            e = int(input("Quinto número"))
            print('{} + {} + {} + {} + {} = '.format(a, b, c, d, e), (a + b + c + d + e))
elif select == poten:
    print("Potência")
    print()
    a = int(input("Primeiro número"))
    b = int(input("Segundo número"))    
    print('{} ^ {} = '.format(a, b), (a ** b))
elif select == divi:
        num = int(input("Quantos números você quer dividir?(Até 5 números)"))
        if num == 2:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))    
            print('{} / {} = '.format(a, b), (a / b))
        elif num == 3:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            print('{} / {} / {} = '.format(a, b, c), (a / b / c))
        elif num == 4:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            print('{} / {} / {} / {} = '.format(a, b, c, d), (a / b / c / d))
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
            print('{} x {} = '.format(a, b), (a * b))
        elif num == 3:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            print('{} x {} x {} = '.format(a, b, c), (a * b * c))
        elif num == 4:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            print('{} x {} x {} x {} = '.format(a, b, c, d), (a * b * c * d))
        elif num == 5:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            e = int(input("Quinto número"))
            print('{} x {} x {} x {} x {} = '.format(a, b, c, d, e), (a * b * c * d * e))
elif select == sub:
        num = int(input("Quantos números você quer subtrair?(Até 5 números)"))
        if num == 2:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))    
            print('{} - {} = '.format(a, b), (a - b))
        elif num == 3:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            print('{} - {} - {} = '.format(a, b, c), (a - b - c))
        elif num == 4:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            print('{} - {} - {} - {} = '.format(a, b, c, d), (a - b - c - d))
        elif num == 5:
            a = int(input("Primeiro número"))
            b = int(input("Segundo número"))
            c = int(input("Terceiro número"))
            d = int(input("Quarto número"))
            e = int(input("Quinto número"))
            print('{} - {} - {} - {} - {} = '.format(a, b, c, d, e), (a - b - c - d - e))