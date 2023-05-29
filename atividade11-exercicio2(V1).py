import random
L = random.randint(1,52, (130))
p = int(input("Digite o procurado:"))
x = 0
f = [ ]
achou = False
while x < len(L):
    if L[x] == p:
        achou = True
        f.append(x)
    x += 1
if achou:
    print("%d achado na posição {}".format(f) % (p))
else:
    print("%d não encontrado" % p)