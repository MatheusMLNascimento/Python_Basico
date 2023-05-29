import json

fav_number = input("Qual o número favorito? ")
filename = "fav_number.json"
with open(filename, "w") as f_obj:
    json.dump(fav_number, f_obj)
print("Vamos lembrar de seu número quando você voltar\n Seu número é " + fav_number + "!")