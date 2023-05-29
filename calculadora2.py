print("Calculadora, escolha a operação:\n n1 - Soma\n n2 - divisão\n n3 - multiplicação\n n4 - subtração")
soma = "n1"
divi = "n2"
multi = "n3"
sub = "n4"
select = input("Opção desejada:")
print()
if select == soma:
    b = int(input("Primeiro número"))
    a = int(input("Segundo número"))
    print('{} + {} = '.format(b, a), (a + b))
elif select == divi:
        a = int(input("Primeiro número"))
        b = int(input("Segundo número"))
        print('{} / {} = '.format(a, b), (a / b))
elif select == multi:
    a = int(input("Primeiro número"))
    b = int(input("Segundo número"))
    print('{} x {} = '.format(a, b), (a * b))
elif select == sub:
    a = int(input("Primeiro número"))
    b = int(input("Segundo número"))
    print('{} - {} = '.format(a, b), (a - b))