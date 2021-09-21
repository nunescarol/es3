# 1. Como criar um projeto e apps com Django

## O que é um projeto Django e o que é um app?

Um projeto é um pacote Python – isto é. um diretório de código – que contém todas as configurações para uma instância do Django. Isto pode incluir configuração de banco de dados, opções específicas do Django e configurações específicas da aplicação. Cada aplicação que você escreve no Django consiste de um pacote Python que segue uma certa convenção. O Django gera automaticamente a estrutura básica de diretório de uma aplicação, assim como faz com a do projeto.

Em resumo, um projeto é uma coleção de configurações e aplicações para um website específico. Uma aplicação é um conjunto de elementos web que faz alguma coisa (por exemplo, um sistema de blog ou um app de enquetes básico). Um projeto pode conter múltiplas aplicações. Uma aplicação pode estar em múltiplos projetos.

Fonte: [Documentação Django](https://docs.djangoproject.com/pt-br/3.2/intro/tutorial01/#creating-the-polls-app)

## Criação de um projeto

Para criar um projeto django, navegue até o diretório desejado e execute o seguinte comando no terminal (ou Powershell ou Prompt de Comando):

        django-admin startproject meu_projeto

Desse modo, o Django se certifica de criar todos os arquivos necessários para se ter um projeto funcional.

## Criação de um app

Com o projeto já criado, entre na pasta do projeto com:

        cd meu_projeto

E execute o comando:

        django-admin startapp meu-app1

Desse modo, o Django se certifica de criar todos os arquivos necessários para se ter um app contido no seu projeto. Um exemplo da estrutura de diretórios e arquivos pode ser encontrada [aqui.](./meu_projeto)

## Iniciando o servidor

Para iniciar o servidor do seu projeto Django, execute o comando:

        python manage.py runserver

E acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Se tudo tiver dado certo, a página encontrada nessa url será a seguinte: 
![Django Success](https://github.com/nunescarol/es3/blob/main/imagens/django-success.png?raw=true)

## Próximo passo

Agora que você já tem seu projeto e app criado, siga para o próximo tópico: [2. Como fazer e configurar urls e views](https://github.com/nunescarol/es3/tree/main/2.%20django/2.%20Como%20fazer%20e%20configurar%20urls%20e%20views)