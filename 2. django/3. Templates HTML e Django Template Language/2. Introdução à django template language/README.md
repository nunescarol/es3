# 3. Templates HTML e Django Template Language
## 3.2. Introdução à django template language

Para dar início a esse tópico, vamos adicionar uma página HTML ao nosso projeto e conectar com a primeira página feita através de uma tag a:

### Adicionando uma página à pasta de templates

- Crie um arquivo HTML na pasta meu_projeto/templates/ chamado "page2.html" e adicione o seguinte código nele:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Segunda página</title>
</head>
<body>
    
    <p>Parabéns, você chegou aqui através do index.html</p>
    <p>Se deseja voltar ao início, clique <a href="{% url 'meu_app1:index' %}">aqui.</a></p>

    
</body>
</html>
```

Perceba o uso do trecho "{% url 'meu_app1:segunda-pagina' %}". Essa é uma tag de template do tipo {% url %}, ela funciona pesquisando a URL indicada conforme especificado no arquivo "urls.py", nesse caso, do app "meu_app1". No exemplo dado, é especificado o app e o nome da URL especificada com o argumento "name".

- Agora vamos atualizar o arquivo "index.html". Seu conteúdo ficará assim:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Meu App</title>
</head>
<body>
    
    <h1>Olá, Mundo.</h1>
    <a href="{% url 'meu_app1:segunda-pagina' %}">Leve-me para a segunda página</a>
    
</body>
</html>
```

### Editando o arquivo views.py

Edite o arquivo meu_projeto/meu_app1/views.py com o seguinte conteúdo:

```python
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def segunda(request):
    return render(request, 'page2.html')
```

### Adicionando a nova URL no arquivo urls.py

Edite o arquivo meu_projeto/meu_app1/urls.py com o seguinte conteúdo:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('segunda/', views.segunda, name='segunda-pagina'),
]
```

### Testando

Para iniciar o servidor do seu projeto Django, execute o seguinte comando da pasta raiz do projeto:

        python manage.py runserver

E acesse [http://127.0.0.1:8000/meuapp](http://127.0.0.1:8000/meuapp) e teste os links entre as páginas.

#### Exemplo da estrutura de pastas e arquivos:

Um exemplo da estrutura de diretórios e arquivos pode ser encontrada [aqui.](./meu_projeto)

### Próximo passo

Agora você já pode seguir para o próximo tópico: [3. Explorando a django template language](https://github.com/nunescarol/es3/tree/main/2.%20django/3.%20Templates%20HTML%20e%20Django%20Template%20Language/3.%20Explorando%20a%20django%20template%20language)