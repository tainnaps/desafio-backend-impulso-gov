# Desafio Backend - Impulso Gov

## Executando o webservice

### Pré-requisitos

⚠️ Para executar o *webservice*, é necessário:

- Ter o [Docker](https://docs.docker.com/get-docker/) e o [Docker Compose](https://docs.docker.com/compose/) instalados na sua máquina.
- Clonar o este repositório.

### Passo a passo

Com os pré-requisitos atendidos, siga os seguintes passos para executar o *webservice*:

1 - Dentro raiz do projeto, execute o seguinte comando no terminal para iniciar o container do *webservice*:

``` bash
docker-compose up

ou inicie o container em segundo plano

docker-compose up -d
```

2 - Para acessar o *webservice*, abra o seguinte endereço em seu navegador web:

``` bash
http://127.0.0.1:8000
```

Caso tudo tenha corrido como esperado, você receberá a seguinte resposta ao acessar o endereço:

``` json
{
  "message": "Webservice OK"
}
```

Isso significa que o *webservice* está pronto para receber mais requisições.

## Documentação do webservice

Para conhecer os endpoints disponíveis no *webservice* e entender como fazer requisições para eles, acesse a [documentação do webservice](http://127.0.0.1:8000/docs).

⚠️ A documentação só estará disponível enquanto o webservice estiver em execução.

## Executando os testes

Foram desenvolvidos testes de integração os endpoints do *webservice* usando `pytest` e o `TestClient` da `FastAPI`.

Para executar os testes, siga os seguintes passos:

1 - Acesse o terminal do container do *webservice* com o comando abaixo:

``` bash
docker exec -it impulso-gov-backend bash
```

2 - No terminal do container do *webservice*, execute o seguinte comando:

``` bash
pytest -v
```
