nu = [ ]
nu2 = [ ]
x = 0
b = -2
print("Digite os números das duas listas\n(Digite 0 quando precisar sair)")
while x > b:
    n = int(input("Número %d: " % (x + 1)))
    if n == 0:
        break
    nu.append(n)
    x += 1
x = 0
while x > b:
    n2 = int(input("Número %d: " % (x + 1)))
    if n2 == 0:
        break
    nu2.append(n2)
    x += 1
nu.extend(nu2)
print(nu)