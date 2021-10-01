# 4. Django Models
## 4.2. CRUD (create, read, update, delete)

Como já criamos o banco de dados e criamos as tabelas com o migrate, agora já podemos realizar as operações de CRUD, a criação, leitura, atualização e exclusão de um objeto no banco.

O primeiro passo para é abrir o shell

```python
python manage.py shell
```

Após o shell, iremos importa o objeto Curso pelo seguinte comando:

```python
 from cursos.models import Curso
```

Agora que já importamos o objeto, podemos finalmente criar um curso:

```python
curso = Curso(titulo="Curso de Django", url="https://github.com/nunescarol/es3")       
curso.save()
```
Para checar se o curso realmente foi criado podemos buscar todos os cursos com o comando:
```python
Curso.objects.all()
```

Agora vamos ler e alterar o curso criado:
```python
curso = Curso.objects.get(pk=1)
curso.titulo = "Curso de Django 3"
curso.save()
```
Acima fizemos um get com a primary key igual a 1 devido a este curso ter sido o primeiro e único curso a ser criado.

Para apagar o curso, basta:
```python
curso.delete()
```

Agora que você já sabe o básico sobre como criar modelos e realizar ações de CRUD, podemos então prosseguir para a próxima etapa: [5. Django Admin](https://github.com/nunescarol/es3/tree/main/2.%20django/5.%20Django%20Admin)