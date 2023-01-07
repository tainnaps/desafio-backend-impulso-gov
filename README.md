# Desafio Backend - Impulso Gov

Este repositório contém a resolução do Desafio Backend do processo seletivo da empresa **Impulso Gov**, na qual foi construída uma API para retornar dados dos estabelecimentos de saúde vinculados ao SUS.

## Sumário

- [Tecnologias](https://github.com/tainnaps/desafio-backend-impulso-gov#tecnologias)
- [Executando a API](https://github.com/tainnaps/desafio-backend-impulso-gov#executando-a-api)
- [Documentação da API](https://github.com/tainnaps/desafio-backend-impulso-gov#documenta%C3%A7%C3%A3o-da-api)
- [Executando os testes](https://github.com/tainnaps/desafio-backend-impulso-gov#executando-os-testes)

## Tecnologias

As tecnologias utilizadas para desenvolver a API foram:

- `Docker`: criação de container para desenvolvimento
- `FastAPI`: construção da API
- `Sqlite3`: acesso ao banco de dados
- `Pytest`: criação de testes

## Executando a API

### Pré-requisitos

⚠️ Para executar a API, é necessário:

- Ter o [Docker](https://docs.docker.com/get-docker/) e o [Docker Compose](https://docs.docker.com/compose/) instalados na sua máquina.
- Clonar este repositório.

### Passo a passo

Com os pré-requisitos atendidos, siga os seguintes passos para executar a API:

1 - Dentro raiz do projeto, execute o seguinte comando no terminal para iniciar o container da API:

``` bash
docker-compose up

ou inicie o container em segundo plano

docker-compose up -d
```

2 - Para acessar a API, abra o seguinte endereço em seu navegador web:

``` bash
http://127.0.0.1:8000
```

Caso tudo tenha corrido como esperado, você receberá a seguinte resposta ao acessar o endereço:

``` json
{
  "message": "Webservice OK"
}
```

Isso significa que a API está pronta para receber mais requisições.

## Documentação da API

Para conhecer os endpoints disponíveis na API e entender como fazer requisições para eles, acesse a [documentação da API](http://127.0.0.1:8000/docs).

⚠️ A documentação só estará disponível enquanto a API estiver em execução.

## Executando os testes

Foram desenvolvidos testes de integração para os endpoints da API usando `pytest` e o `TestClient` da `FastAPI`.

Para executar os testes, siga os seguintes passos:

1 - Acesse o terminal do container da API com o comando abaixo:

``` bash
docker exec -it impulso-gov-backend bash
```

2 - No terminal do container da API, execute o seguinte comando:

``` bash
pytest -v
```

Com isso, você verá o resultado de cada caso de teste.
