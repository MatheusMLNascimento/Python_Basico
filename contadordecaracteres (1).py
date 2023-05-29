valor = int(input("Digite um número:"))
y = 0
soma = 0

while valor != 0:
    y = soma % 10
    soma = soma + y
    valor = valor // 10
print("Os números somados é %d"%soma)