# Desafio Backend - Impulso Gov

Este repositório contém a resolução do Desafio Backend do processo seletivo da empresa **Impulso Gov**.

Para solucionar o desafio, foi desenvolvida uma API em `Python` para consultar dados dos estabelecimentos de saúde vinculados ao SUS.

> O arquivo `dados.db` foi disponibilizado pela **Impulso Gov** para a realização do desafio.

## Sumário

- [Container](https://github.com/tainnaps/desafio-backend-impulso-gov#container)
- [Tecnologias](https://github.com/tainnaps/desafio-backend-impulso-gov#tecnologias)
- [Executando a API](https://github.com/tainnaps/desafio-backend-impulso-gov#executando-a-api)
- [Documentação](https://github.com/tainnaps/desafio-backend-impulso-gov#documenta%C3%A7%C3%A3o)
- [Executando os testes](https://github.com/tainnaps/desafio-backend-impulso-gov#executando-os-testes)

## Container

A API foi desenvolvida num container Docker contendo o Linux como Sistema Operacional e a linguagem `Python` na versão 3.11.1.

O objetivo de criar um container para a API é garantir que quem executá-la a partir deste repositório estará com o mesmo ambiente usado durante sua criação. Dessa forma, não haverá conflitos de versão da linguagem ou incompatibilidade de Sistema Operacional.

## Tecnologias

As tecnologias utilizadas para desenvolver a API foram:

- `Docker`: criação de container para desenvolvimento
- `FastAPI`: construção da API
- `Sqlite3`: acesso ao banco de dados
- `Pytest`: criação de testes

## Executando a API

Para executar a API, é necessário ter o [Docker](https://docs.docker.com/get-docker/) e o [Docker Compose](https://docs.docker.com/compose/) instalados na sua máquina. Com este pré-requisito atendido, siga os passos abaixo para executá-la:

1 - Clone este repositório

``` bash
git clone https://github.com/tainnaps/desafio-backend-impulso-gov.git
```

2 - Entre no diretório raiz do repositório clonado

``` bash
cd desafio-backend-impulso-gov
```

3 - Dentro do diretório raiz (onde se encontra o arquivo `docker-compose.yml`), inicie o container da API

``` bash
docker-compose up

# ou inicie o container em segundo plano

docker-compose up -d
```

4 - Acesse a API inserindo o endereço abaixo em seu navegador web

``` bash
http://127.0.0.1:8000
```

Caso tudo tenha ocorrido como esperado, a seguinte resposta será exibida pelo navegador:

``` json
{
  "message": "Webservice OK"
}
```

Isso significa que a API está pronta para receber mais requisições.

## Documentação

Para conhecer os endpoints disponíveis na API e entender como fazer requisições para eles, acesse a [documentação da API](http://127.0.0.1:8000/docs).

⚠️ A documentação é disponibilizada através de um endpoint da API, portanto ela só pode ser acessada enquanto a API estiver em execução.

## Executando os testes

Foram desenvolvidos testes de integração para os endpoints da API usando `pytest` e o `TestClient` da `FastAPI`.

Para executar os testes, siga os seguintes passos:

1 - Acesse o terminal do container da API

``` bash
docker exec -it impulso-gov-backend bash
```

2 - No terminal do container da API, execute o comando de teste

``` bash
pytest -v
```

**OBSERVAÇÃO**: por se tratar de uma API que apenas consulta o banco de dados, sem alterá-lo, não criei um banco de teste, mas sei que, num caso real, o ideal seria criá-lo para o ambiente de testes.
