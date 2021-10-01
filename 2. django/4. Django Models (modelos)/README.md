# 4. Django Models (modelos)

No Django, os nossos dados são estruturados em modelos (models), sendo que estes modelos são independentes do banco de dados, possibilitando você utilizar o mesmo modelo para qualquer banco que queira utilizar.

No modelo definimos quais campos aquele objeto terá, e também como será o relacionamento dessas informações, se algum campo é chave estrangeira (ForeignKey), se é a relação é ManyToManyField ou OneToOneField, por exemplo.

Para dar inicio aos modelos, antes de tudo iremos criar uma app chamada Curso, no qual será a nossa aplicação de cursos. Para isso rodemos o código abaixo no terminal:

``` python manage.py startapp cursos ```

Vá até a pasta cursos criada no seu projeto, e encontre o arquivo nomeado models.py dentro dela.

Inicialmente iremos criar um modelo base para o nossa aplicação de cursos.
```   
from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']

    def __str__(self):
        return self.titulo
```
Acima criamos uma base chamada Base que extende o models.Model do próprio Django, criamos um campo chamada criacao -  campo de data que é capturada no momento da criação do objeto, atualização - campo de data que é capturada tanto na criação quanto na modificação do objeto, e ativo - campo do tipo booleano, verdadeiro ou falso.

Utilizando a Base acima para criar o nosso modelo de curso:
```
class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
```
A classe Curso, extende a classe Base, herdando todos os campos  que a Base tem e herdando também todos os campos e métodos que a Base herda do models do Django. Assim, criamos um titulo - Campo de texto com no máximo 255 caracteres, e url - campo autodescritivo que salva a url de um determinado curso. A classe meta serve para descrever o nosso modelo, que neste caso é Curso e no plural Cursos.

Para iniciar o primeiro subtópico dessa seção clique aqui: [1. Introdução a templates HTML](https://github.com/nunescarol/es3/tree/main/2.%20django/3.%20Templates%20HTML%20e%20Django%20Template%20Language/1.%20Introdu%C3%A7%C3%A3o%20a%20templates%20HTML). Para ir para o segundo subtópico dessa seção clique aqui: [2. Introdução à django template language](https://github.com/nunescarol/es3/tree/main/2.%20django/3.%20Templates%20HTML%20e%20Django%20Template%20Language/2.%20Introdu%C3%A7%C3%A3o%20%C3%A0%20django%20template%20language). Para ir para a lição final, clique aqui: [2. HTML Template Language](https://github.com/nunescarol/es3/tree/main/2.%20django/3.%20Templates%20HTML%20e%20Django%20Template%20Language/3.%20Explorando%20a%20django%20template%20language).

Se desejar seguir para o próximo tópico, clique aqui: [4. Django Models (modelos)](https://github.com/nunescarol/es3/tree/main/2.%20django/4.%20Django%20Models%20(modelos))
