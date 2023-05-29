import random
import numpy as np
t = int(input("Digite quantos números seram usados: "))
L = np.random.randint(1,100, (t,1))
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