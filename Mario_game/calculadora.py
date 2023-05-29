print("Calculadora, escolha a operação:")
select = int(input(" 1 - Multiplicação\n 2 - Divisão\n 3 - Soma\n 4 - Subtração\n"))

print()
if select == 3:
    print("Soma -\n")
    b = int(input("Primeiro número: "))
    a = int(input("Segundo número: "))
    print(f"{a} + {b} =", (a + b))
elif select == 2:
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))
        print(f"{a} / {b} =", (a / b))
elif select == 1:
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    print(f"{a} x {b} =", (a * b))
elif select == 4:
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    print(f"{a} - {b} =", (a - b))
else:
    print("Escolha apenas entre as 4 opções!")