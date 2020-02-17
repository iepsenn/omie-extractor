import requests
import json
import yaml
# import sys
from time import sleep

url = 'https://app.omie.com.br/api/v1/'

with open('./keys.yaml') as file:
    keys = yaml.load(file, Loader=yaml.FullLoader)

with open('./routes.yaml') as file:
    routes = yaml.load(file, Loader=yaml.FullLoader)

app_key = keys['app_key']
app_secret = keys['app_secret']


# api = 'estoque/movestoque/'
# call = 'ListarMovimentos'

api = routes['route']
call = routes['call']

filename = '{}.json'.format(call)

params = {
    "call": "{}".format(call),
    "app_key": "{}".format(app_key),
    "app_secret": "{}".format(app_secret),
    "param": [
        {
            "pagina": 0,
            "registros_por_pagina": 100,
            "apenas_importado_api": "N"
        }
    ]
}

data = []
page = 1

# Busca dados de todas as páginas
while True:

    params['page'] = page

    # Formata o url para pegar dados da página atual
    url_api = '{}{}?JSON={}'.format(
        url,
        api,
        str(params).replace('\'', "\"")
    )

    # Fazendo a request pra página
    response = requests.get(url_api)

    # Testa se deu tudo certo
    if response.status_code == 200:
        print('ok')
        content = response.json()

        data += list(content)
        page += 1

        sleep(3)
    else:
        print('ERROR {}'.format(response.status_code))
        print('Found {} pages!!'.format(page))
        break

# Salva o resultado em um arquivo json
with open(filename, 'w') as json_file:
    json.dump(data, json_file)
