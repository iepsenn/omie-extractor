# omie-extractor
Extrator de dados para o ERP [Omie](https://www.omie.com.br/).

## Prerequisites
O único prerequisito pode ser instalado com o seguinte comando:
```
pip install PyYAML
```

## Arquivos de configuração
* `keys.yaml`
    Lista de chaves da API a serem usadas no extrator. O formato dos itens da lista é: [`app_key`, `app_secret`].
* `routes.yaml`
    Lista de rotas e métodos a serem acessados.

## Execução
Basta mudar os parâmetros nos arquivos de configuração e rodar o script `extractor.py`

## License
This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details