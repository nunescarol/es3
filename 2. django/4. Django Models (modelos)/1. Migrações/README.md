# 4. Migrations (Migrações)

Após o modelo ser criado, estamos aptos a criar as tabelas no banco de dados que irão armazenas as informações. Assim, rodaremos o comando abaixo para criar o banco de dados e as migrations.

``` python manage.py makemigrations ```

Com esse comando você pode observar que um banco de dados db.sqlite3 foi criado na raiz do seu projeto, ao lado do manage.py e dentro da aplicação cursos foi criada uma pasta chamada migrations e um arquivo __init__.py.

Agora rodaremos o código abaixo para criar as nossas tabelas no banco:

``` python manage.py migrate ```

Você verá uma tela como esta abaixo:

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

Pronto, as migrações já foram feitas e já estamos aptos a criar novos cursos.


Após executar o migrate iremos para próximo subtópico dessa seção que pode ser encontrado no link a seguir: [2. CRUD](https://github.com/nunescarol/es3/tree/main/2.%20django/4.%20Django%20Models%20(modelos)/2.%20CRUD).