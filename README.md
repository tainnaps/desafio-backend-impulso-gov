# Desafio Backend - Impulso Gov

## Executando o webservice

Para iniciar o *webservice*, execute o seguinte comando no terminal, dentro da pasta raiz:

``` bash
docker-compose up
```

Para acessar o *webservice*, abra o seguinte endereço em seu navegador web:

``` bash
http://127.0.0.1:8000
```

Caso tudo tenha corrido como esperado, você receberá a seguinte resposta ao acessar o endereço:

``` json
{
  "message": "Webservice OK"
}
```

Isso significa que o *webservice* está pronto para receber requisições.

## Documentação do webservice

Para conhecer os endpoints disponíveis no *webservice* e entender como fazer requisições para eles, acesse a [documentação do webservice](http://127.0.0.1:8000/docs).

⚠️ A documentação só estará disponível enquanto o webservice estiver em execução.

## Executando os testes

Para executar os testes, acesse o container executando o seguinte comando no terminal, dentro da pasta raiz:

``` bash
docker exec -it impulso-gov-backend bash
```

Dentro do container, execute o `pytest` como seguinte comando:

``` bash
pytest -v
```
