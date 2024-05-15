import requests

#Buscar informações- GET(link para acessar o CEP)
response = requests.get('https://cep.awesomeapi.com.br/json/20541100')
print('Status code:', response.status_code) 
#Os códigos de status de resposta HTTP indicam se uma solicitação foi concluída com êxito ou se teve algum erro.

print('Header') #Cabeçalho
print(response.headers)

print('Content') #Conteúdo
print(response.content)