import requests
import json
import yaml
from time import sleep
import time

start_time = time.time()

url = 'https://app.omie.com.br/api/v1/'

# Lendo arquivos de configuração
with open('./keys.yaml') as file:
    keys = yaml.load(file, Loader=yaml.FullLoader)

with open('./routes.yaml') as file:
    routes = yaml.load(file, Loader=yaml.FullLoader)

# Usa todas as chaves passadas para conectar e extrair
for app_key, app_secret in keys['keys']:

    # Extrai de todas as rotas passadas
    for route, call in routes['routes']:

        print("Extracting from {} method...".format(call))

        # Nome para salvar arquivos com os dados coletados
        filename = '{}_{}.json'.format(app_key, call)

        # Parâmetros padrão para requisição
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
                route,
                str(params).replace('\'', "\"")
            )

            # Fazendo a request pra página
            response = requests.get(url_api)

            if response.status_code == 200:
                content = response.json()[list(response.json().keys())[-1]]
                data += list(content)
                page += 1

                break

                sleep(3)
            else:
                print('Found {} pages from {} route!!'.format(page, call))
                break

        # Salva o resultado em um arquivo json
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)

print('--- {} minutes ---'.format(
    round((time.time() - start_time) / 60, 2))
)
