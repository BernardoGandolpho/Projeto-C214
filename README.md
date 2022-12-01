# API Pokemon (Projeto Laboratório C214)
![Python tests](https://github.com/BernardoGandolpho/Projeto-C214/actions/workflows/python-app.yml/badge.svg) ![Linter](https://github.com/BernardoGandolpho/Projeto-C214/actions/workflows/linter.yml/badge.svg)

Este repositório contém o código para a aplicação API Pokemon, criado para o projeto do laboratório dadisciplina C214 (Engenharia de Software).

Para a API foi utilizada a biblioteca FastAPI do Python e Pytest para realizar os testes unitários. O Front foi feito com React utilizando a ferramenta ViteJS como base do projeto. O GitHub Actions foi escolhido para executar os testes e executar o linter sobre o código em Python para manter de acordo com as normas da PEP-8.

## Executando a API

Antes de executar a aplicação, é necessário criar o arquivo **.env** na pasta raíz do projeto. O conteúdo dele deve seguir o padrão do arquivo **.env.example**.

A execução da aplicação foi estruturada utilizando o Docker Compose. Sendo assim, o frontend, o backend e o banco de dados (MongoDB) são executados em containeres que podem ser executados a partir da pasta raíz com o comando abaixo:

```
docker-compose build
docker-compose up
```

Para simplificar ainda mais, utilizamos o arquivo Makefile, que permite executar o docker com o comando ```make run```.

Com os containeres em execução, basta acessar o link <http://localhost:5173> para visualizar o frontend da aplicação. Caso queira fazer requisições diretas na API, é possível fazer requisições HTTP para a URL <http://localhost:8088/pokemons>.


### Populando o Banco de Dados

Como a aplicação precisa de dados para ser utilizada, criamos um script que preenche o Mongo com dados vindo de outra API de pokemon disponível online.

Como o processo de preencher o banco é um pouco lento, na função main, está definido que serão preenchidos os Pokemons até o número 151 (1ª geração) e serão preenchidos com apenas 100 ataques diferentes. Esse número pode ser alterado, porém, não recomendamos colocar um número muito grande pois o frontend não possui paginação e pode acabar atrapalhando o uso.

Para executar o script, com a aplicação sendo executada, execute o seguinte comando em outro terminal: ```python script_db.py```

Uma vez preenchido, os dados ficaram armazenados localmente na pasta /db.

## Testes de Backend

Os testes estão escritos na pasta /backend/tests. Os testes são testes unitários feitos em cima das funções de busca da API. As funções de CREATE, UPDATE e DELETE não estão cobertas por testes.

Para executar a bateria de testes, é necessário executar o seguinte comando a partir da pasta raíz:
```
python -m pytest backend
```

Para gerar um artefato dos testes, é possível utilizar o comando abaixo:
```
python3 -m pytest backend --html artefato.html
```

## Workflows

A pasta .github/workflows possui os arquivos .yml que configuram os Jobs que são realizados pelo GitHub Actions. O Jobs de linter executa em todos os Pull Requests criados e os testes, por serem mais demorados, executam em Pull Requests e Pushes apenas para a branch main.
