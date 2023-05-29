# Arquivo base para o código, aqui eu apenas transformei todas as etapas em funções
def soma():
    print("Soma -\n")
    b = int(input("Primeiro número: "))
    a = int(input("Segundo número: "))
    print(f"{a} + {b} =", (a + b))

def divisao():
    print("Divisão -\n")
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    print(f"{a} / {b} =", (a / b))

def multiplicacao():
    print("Multiplicação -\n")
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    print(f"{a} x {b} =", (a * b))

def subtracao():
    print("Subtração -\n")
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    print(f"{a} - {b} =", (a - b))
