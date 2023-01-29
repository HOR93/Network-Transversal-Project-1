import json

def load_json(file): # load do json com o dicionario
    with open(file) as respostas_pris:
        return json.load(respostas_pris)


dicionario_pris = load_json("intents.json")
bot_name = "> 🤖"
