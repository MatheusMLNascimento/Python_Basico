f = [ ]
g = [ ]
x = 0
b = 3
while b > x:
    a = int(input("Digite o número %d"% (x + 1)))
    f.append(a)
    x += 1
    if x == 3:
        b = 6
        while b > x:
            c = int(input("Digite o número %d" %(x + 1)))
            g.append(c)
            x += 1
f.extend(g)
print(f)