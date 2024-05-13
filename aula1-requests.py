import requests

#Buscar informações- GET(link para acessar o CEP)
r = requests.get('https://cep.awesomeapi.com.br/json/20541100')
print(r)
print(r.json())

#Buscar informações- GET(Banco de dados)
r = requests.get('https://teste-3dd91-default-rtdb.firebaseio.com/.json')
print(r)
print(r.json())

#Criar informações- POST(Banco de dados)
informaçoes = '{"Nome": "Sara", "idade": "14"}'
r = requests.post("https://teste-3dd91-default-rtdb.firebaseio.com/.json", data=informaçoes)
print(r)
print(r.json())

#Editar informação- PATCH(Banco de dados)
informaçoes = '{"Nome": "Carla", "idade": 23}'
r = requests.patch("https://teste-3dd91-default-rtdb.firebaseio.com/-NxYSLPTf9LuERsFgC3v.json", data=informaçoes)
print(r)
print(r.json())

#Deletar informações- DELETE(Banco de dados)
r = requests.delete("https://teste-3dd91-default-rtdb.firebaseio.com/-NxYS_hG4fbHzX6wIPra.json")
print(r)
print(r.json())