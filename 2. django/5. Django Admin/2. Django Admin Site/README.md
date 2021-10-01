# 5. Django Admin
## 5.2. Django Admin Site

Agora que temos um super usuário, podemos entrar no nosso painel do Administrador. Comece iniciando o servidor com o comando abaixo:

```python
python manage.py runserver
``` 

Após o servidor iniciar, iremos até o navegador e entraremos no link abaixo:
``` http://localhost:8000 ```

Uma tela como a abaixo será mostrada, entraremos com o login e senha do superuser criado anteriormente:
![Django Admin Login](https://github.com/nunescarol/es3/blob/main/imagens/login_admin.png?raw=true)


Após o login ser realizado, outra tela como a abaixo será exibida:
![Django Admin Site](https://github.com/nunescarol/es3/blob/main/imagens/admin_index.png?raw=true)

Perceba que ainda não há  como modificar, inserir ou fazer qualquer operação com o model Curso criado na seção 4, apenas como modificar, inserir ou manipular usuários e grupos.

Na próxima subseção iremos fazer com que seja possivel inserir, modificar e excluir cursos pelo painel do django admin, veja em: [3. Manipulando models no Django Admin Site](https://github.com/nunescarol/es3/tree/main/2.%20django/5.%20Django%20Admin/3.%20Manipulando%20models%20no%20Django%20Admin%20Site).
