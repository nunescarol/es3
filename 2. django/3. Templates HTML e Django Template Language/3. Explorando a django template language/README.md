# 3. Templates HTML e Django Template Language
## 3.3. Explorando a django template language

Vamos dar continuidade a exploração da linguagem de template Django. Dessa vez, vamos usar as tags {% if %} e {% for %}, além do conceito da {{ variável }}

### Editando o arquivo views.py

Para ajudar a exemplificar o uso das tags mostradas acima, vamos editar a função "index" do arquivo meu_projeto/meu_app1/views.py. Vamos declarar uma lista com várias frutas e a retornar junto do "request" e do "index.html" por meio de um dicionário:

```python
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    frutas = ["maçã", "banana", "morango", "abacaxi", "kiwi"]
    flag = True

    dicionario = {"frutas": frutas, "flag": flag}

    return render(request, 'index.html', dicionario)

def segunda(request):
    return render(request, 'page2.html')
```

### Fazendo uso das tags

Agora vamos editar nosso arquivo "index.html". Vamos dizer que, dada a lista fornecida pela função de view, nós queremos mostrar seus itens apenas se há uma indicação que devemos mostrar (uma flag, por exemplo). Então, o conteúdo do arquivo meu_projeto/templates/index.html ficará da seguinte forma:

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

    {% for item in frutas %}
    <ul>
        {% if flag %}

        <li>{{item}}</li>
        
        {% endif %}
    </ul>
    {% endfor %}
    
</body>
</html>
``` 

Perceba o uso da tag {% for %}, aqui ela serve para automatizar a criação de items de nossa lista não ordenada, desse modo não é necessário escrever um elemento para cada item. O uso do {% if %} condiciona a exibição dos items da lista "frutas", se for verdadeiro a lista é exibida, se for falso, a lista não é exibida. Há também o {{ item }}, o qual possibilita o acesso da variável "item" em questão, sem as chaves seria exibido apenas a string "item".

### Testando

Para iniciar o servidor do seu projeto Django, execute o seguinte comando da pasta raiz do projeto:

        python manage.py runserver

E acesse [http://127.0.0.1:8000/meuapp](http://127.0.0.1:8000/meuapp) e teste a exibição da lista. No arquivo meu_projeto/meu_app1/views.py mude o valor da flag de "True" para "False" e veja o que acontece na página HTML carregada.

#### Exemplo da estrutura de pastas e arquivos:

Um exemplo da estrutura de diretórios e arquivos pode ser encontrada [aqui.](./meu_projeto)

### Próximo passo

Agora que você já sabe o básico sobre como templates HTML funcionam e como usar a django template language, pode seguir para o próximo tópico: [4. Django Models (modelos)](https://github.com/nunescarol/es3/tree/main/2.%20django/4.%20Django%20Models%20(modelos))