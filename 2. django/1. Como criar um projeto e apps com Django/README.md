# 1. Como criar um projeto e apps com Django

## O que é um projeto Django e o que é um app?

Blabla

## Criação de um projeto

Para criar um projeto django, navegue até o diretório desejado e execute o comando:

```django-admin startproject meu_projeto```

Desse modo, o Django se certifica de criar todos os arquivos necessários para se ter um projeto funcional.

## Criação de um app

Com o projeto já criado, entre na pasta do projeto com:

```cd meu_projeto```

E execute o comando:

```django-admin startapp meu-app1```

Desse modo, o Django se certifica de criar todos os arquivos necessários para se ter um app contido no seu projeto. Um exemplo da estrutura de diretórios e arquivos pode ser encontrada [aqui.](./meu_projeto)

## Iniciando o servidor

Para iniciar o servidor do seu projeto Django, execute o comando:

```python manage.py runserver```

E acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Se tudo tiver dado certo, a página encontrada nessa url será a seguinte: 
![Django Success](https://github.com/nunescarol/es3/blob/main/imagens/django-success.png?raw=true)