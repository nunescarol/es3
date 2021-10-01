# 6. API REST 

Agora iremos disponibilizar nossos dados na web através de uma API REST!

O primeiro passo para isso é instalar o pacote do Django Rest Framework (DRF) pelo pip:
```python
pip install djangorestframework 
```

Após instalar o DRF, precisamos adicioná-lo no arquivo SETTINGS.py:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    #apps
    'cursos',
]
```

Agora iremos até a pasta da nossa aplicação cursos e iremos criar um arquivo chamado serializers.py, nele iremos escrever o seguinte:

```python
from rest_framework import serializers
from .models import Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
        )

```

Após serializar a nossa aplicação, vamos até o arquivo de views para criá-las:

```python
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Curso
from .serializers import CursoSerializer


"""
API V1
"""


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
```

Agora que já criamos as views, iremos criar as urls, crie um arquivo chamado urls.py da seguinte forma:

```python
from django.urls import path

from rest_framework.routers import SimpleRouter

from cursos.views import (CursoAPIView,
                          CursosAPIView,
                         )

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
]
```
Agora no arquivo urls do seu projeto, deve ficar assim:

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('api/v1/', include('cursos.urls')),
    path('meuapp/', include('meu_app1.urls')),
    path('admin/', admin.site.urls),
]
```
PRONTO!!!

Agora podemos iniciar nosso servidor com o comando python manage.py runserver e ir até a url da nossa api:

```
http://localhost:8000/api/v1/cursos
```

Ao acessar o link, uma tela como a abaixo será exibida com todos os cursos já cadastrados:
![Django API](https://github.com/nunescarol/es3/blob/main/imagens/apirest.jpeg?raw=true)

Fica como desafio você adicionar novos cursos pelo formulário que fica na parte inferior da imagem.

Para acessar um curso específico, devemos seguir o link com o id do curso, por exemplo, queremos acessar o curso com id = 2, então acessaremos o seguinte link:

```
http://localhost:8000/api/v1/cursos/2
```

Uma imagem como a abaixo será exibida:

![Django API2](https://github.com/nunescarol/es3/blob/main/imagens/apirest2.jpeg?raw=true)

# Parabéns
Agora você já tem noção dos conceitos básicos de Python e Django e já é capaz de desenvolver projetos em django capazes de fornecer API's rest.

