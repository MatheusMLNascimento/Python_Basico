#24/02/2022
#Os "Print()" vazio que eu coloco nos finais são para pular linha
#Atividade 1
print("Calculadora, escolha a operação:\n+ = Soma\n/ = divisão\nx = multiplicação\n- = subtração")
soma = "+"
divi = "/"
multi = "x"
sub = "-"
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
print()

#Atividade 2
mes = int(input("Digite o número do mês(1-12)"))
if mes == 1:
    print("Mês de Janeiro")
elif mes == 2:
    print("Mês de Fevereiro")
elif mes == 3:
    print("Mês de Março")
elif mes == 4:
    print("Mês de Abril")
elif mes == 5:
    print("Mês de Maio")
elif mes == 6:
    print("Mês de Junho")
elif mes == 7:
    print("Mês de Julho")
elif mes == 8:
    print("Mês de Agosto")
elif mes == 9:
    print("Mês de Setembro")
elif mes == 10:
    print("Mês de Outubro")
elif mes == 11:
    print("Mês de Novembro")
elif mes == 12:
    print("Mês de Dezembro")
else:
    print("Só temos 12 meses num ano!")
print()
#Atividade 3
me = float(input("Digite a quantidade de metros que quer que seja convertido em milímetros:"))
print("Resultado:", me * 1000, "mm")
print()

#Atividade 4
print("Dias, horas e minutos para segundo")
di = int(input("Dias:"))
ho = int(input("Horas:"))
minn = int(input("Minutos:"))
dih = (((di * 24) * 60) * 60 )
hor = ((ho * 60) * 60)
mini = minn * 60
print("Sua quantidade de segundos são:", (dih + hor + mini))
print()

#Atividade 5
sal = float(input("Digite seu salário:"))
per = int(input("Digite o aumento a receber:"))
dess = per / 100
dess2 = sal * dess
to = sal + dess2
print("Valor do aumento: R$ %1.2f" %dess2)
print("Novo salário: R$ %1.2f" %to)
print()

#Atividade 6
val = float(input("Preço original da mercadoria: R$"))
per1 = int(input("Porcentagem de desconto:"))
des = per1 / 100
valdes = val * des
valto = val - valdes
print("Valor original: R$", val )
print("Valor descontado: R$", valdes)
print("Valor total: R$", valto)
print()

#Atividade 7
#Vm = delta S / delta t
km = float(input("Distância até o destino(km):"))
vm = float(input("Velocidade média esperada(km/h):"))
dS = km - 0
T = dS / vm
print("Tempo total: %1.2f horas" % T)
print()

#Atividade 8
#F = (9 x C)/5 + 32
C = int(input("Graus Celsius para Fahrenheith:"))
print("F° =",((9 * C) /5 + 32 ))
print()

#Atividade 9
kmper = float(input("Kilometro percorrido:"))
dias = int(input("Dias alugados:"))
print("R$", (kmper * 0.25) + (dias * 60))
print()

#Atividade 10
cigdia = int(input("Quantos cigarros por dia"))
anofum = int(input("Quantos anos de fumante"))
tocig = ((cigdia * 365) * anofum)
arkcig = (((tocig * 10) /60) /24)
print("Dias de vida a menos: %8.2f" % arkcig)