L = [3,4,5,6,4,5,7,56,8,6,89,6,4,56,7,2,5,4,6,8,57,4,5,21,3,2,5,4,8,96,5,7]
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