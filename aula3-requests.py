import requests
from bs4 import BeautifulSoup
'''
Beautiful Soup é uma biblioteca que facilita a extração de informações de páginas da web. 
Ele fica sobre um analisador HTML ou XML, fornecendo expressões idiomáticas Python para iterar, 
pesquisar e modificar a árvore de análise.
'''

#Buscar informações- GET(link para acessar o CEP)
response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

print(type(site))
post =  site.find('div', attrs={'class': "_evt"})
print(post.prettify())