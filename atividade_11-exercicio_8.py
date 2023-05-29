#25/03/2022
#Matheus M. 
#Python online

#Atividade 1 - Ele apenas iria retirar de onde não se tem, ou seja, vai começar a usar números negativos

#Atividade 2
# Simulação de uma fila de banco
último = 10
fila = list(range(1,último+1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação (F, A ou S):")
    x = 0
    while (len(operação)) < x:
        if (operação[0][x]) == "A":
            if (len(fila)) > 0:
                atendido = fila.pop(0)
                print("Cliente %d atendido" % atendido)
            else:
                print("Fila vazia! Ninguém para atender.")
        elif (operação[0][x]) == "F":
            último += 1 # Incrementa o ticket do novo cliente
            fila.append(último)
        elif (operação[0][x]) == "S":
            break
        x += 1
        
#Atividade 3
#Não entendi como fazer