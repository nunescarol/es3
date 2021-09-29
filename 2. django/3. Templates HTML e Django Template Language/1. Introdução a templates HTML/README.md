# 3. Templates HTML e Django Template Language
## 3.1. Introdução

Vamos dar início na aprendizagem dos conceitos básicos da manipulação de templates HTML com o Django.

### Templates

- Primeiro, é necessário organizar a pasta que ficará os templates HTML. Crie um diretório chamado "templates" na pasta raiz do projeto (no mesmo nível em que está o arquivo "manage.py")
- Nesse diretório criado, crie o arquivo "index.html" e adicione o seguinte código HTML:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Meu App</title>
</head>
<body>
    
    <h1>Olá, Mundo.</h1>
    
</body>
</html>
```

### View

Agora vamos escrever uma view que renderiza o template HTML recém criado. Vamos editar a função do arquivo meu_projeto/meuapp1/views.py que foi criada no tópico anterior:

```python
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
```

### Mapeando a pasta de templates

Agora é necessário adicionar a pasta de templates ao arquivo meu_projeto/meu_projeto/settings.py. Adicione o seguinte código na configuração de templates (linha 54):

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### Testando

Para iniciar o servidor do seu projeto Django, execute o seguinte comando da pasta raiz do projeto:

        python manage.py runserver

E acesse [http://127.0.0.1:8000/meuapp](http://127.0.0.1:8000/meuapp). Se tudo tiver dado certo, a página encontrada nessa url será a seguinte: 

<p align="center">
  <img src="https://github.com/nunescarol/es3/blob/main/imagens/django-html-meuapp.png?raw=true" alt="Sucesso HTML"/>
</p>

### Exemplo da estrutura de pastas e arquivos:

Um exemplo da estrutura de diretórios e arquivos pode ser encontrada [aqui.](./meu_projeto)

### Próximo passo

Agora você já pode seguir para o próximo tópico: [2. Introdução à django template language](https://github.com/nunescarol/es3/tree/main/2.%20django/3.%20Templates%20HTML%20e%20Django%20Template%20Language/2.%20Introdu%C3%A7%C3%A3o%20%C3%A0%20django%20template%20language)