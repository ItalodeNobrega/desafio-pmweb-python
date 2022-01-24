# API para consulta de CPF (PMWEB challenge)

A aplicação consiste, de uma forma geral, verificar se um determinado número de CPF está em uma Blacklist, caso esteja, a aplicação retorna que o cpf em questão está liberado com a mensagem `FREE`, caso contrário, rejeita com a mensagem `BLOCKED`.


## Overview técnico

Visando apenas construir a aplicação para ser consumida, seja por WEB ou Mobile, resolvi utilizar a interface como RESTful, no qual construí utilizando o microframework **Flask**.
Tentei ser o mais objetivo e simplório na execução reduzindo ao máximo a lógica para menor complexidade possível.

**Tecnologias utilizadas:**

- Python;
- Flask;

**Rodando a aplicação**
Para rodar a aplicação, disponibilizei uma forma.

Rodando com Flask:

1. Rodar o comando `pip install Flask` e aguardar sua instalação;
2. Após a instalação, rode o comando `flask run`.

Após rodar o método de acesso, a aplicação estará rodando no link: **http://localhost:5000/**

## Rotas

Como o objetivo da aplicação é bem simples, ela possuí apenas um único endpoint, recebendo o CPF por parâmentro na URL, dessa forma:

```http
http://localhost:5000/SEU_CPF

```

E então, o retorno deverá vim a partir de um JSON, sendo a valor o status do CPF.
```json
{
  "status": "FREE"
}
```
