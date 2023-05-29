import json

filename = "fav_number.json"

try:
    with open(filename) as f_obj:
        fav_number = json.load(f_obj)

except FileNotFoundError:
    fav_number = input("Qual é seu número favorito? ")
    with open(filename, "w") as f_obj:
        json.dump(fav_number, f_obj)
        print("Vamos lembrar de seu número quando você voltar\n Seu número é " + fav_number + "!")
else:
    print("Bem vindo de volta, " + fav_number + "!")