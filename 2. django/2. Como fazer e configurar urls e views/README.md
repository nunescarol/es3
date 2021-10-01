# 2. Como fazer e configurar urls e views

## Views

Vamos construir a primeira view do app meu_app1. Abra o arquivo meu_projeto/meu_app1/views.py e coloque o seguinte código no arquivo:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, mundo.")
```

## Urls

- Agora que temos nossa função 'index' no arquivo "views.py", é preciso configurar as urls do projeto. Então crie um arquivo chamado "urls.py" na pasta meu_projeto/meu_app1/ e adicione o seguinte código nele:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

- Agora é preciso adicionar as urls do meu_app1 no arquivo meu_projeto/meu_projeto/urls.py. Adicione o seguinte código nesse arquivo:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('meuapp/', include('meu_app1.urls')),
    path('admin/', admin.site.urls),
]
```

## Acessando a URL

Para iniciar o servidor do seu projeto Django, execute o seguinte comando dentro do diretório raiz do projeto:

        python manage.py runserver

E acesse [http://127.0.0.1:8000/meuapp](http://127.0.0.1:8000/meuapp). Se tudo tiver dado certo, a página encontrada nessa url será a seguinte: 
![Django Success](https://github.com/nunescarol/es3/blob/main/imagens/django-view-meuapp.png?raw=true)

### Exemplo da estrutura de pastas e arquivos:

Um exemplo da estrutura de diretórios e arquivos pode ser encontrada [aqui.](./meu_projeto)

### Próximo passo

Agora você já pode seguir para o próximo tópico: [3. Templates HTML e Django Template Language](https://github.com/nunescarol/es3/tree/main/2.%20django/3.%20Templates%20HTML%20e%20Django%20Template%20Language)
