import json

filename = 'fav_number.json'
with open(filename) as f_obj:
    fav_number = json.load(f_obj)
print("“Eu sei qual é o seu número favorito! É, " + fav_number + "!")