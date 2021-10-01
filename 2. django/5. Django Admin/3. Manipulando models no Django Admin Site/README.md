# 5. Django Admin
## 5.3. Django Admin Site

Para mostrar um model no painel do admin, devemos ir até a pasta da aplicação, mo arquivo admin.py, ex: meus_projeto\cursos\admin.py .

iremos inserir no arquivo o seguinte:

```python
from django.contrib import admin
# Register your models here.
from cursos.models import Curso

admin.site.register(Curso)
``` 
Com o código acima, estamos registrando o model Curso no nosso painel do admin possibilitando, agora, que façamos operações de CRUD pelo próprio painel.

![Django Admin Site](https://github.com/nunescarol/es3/blob/main/imagens/admin_index2.png?raw=true)

Ao clicar em adicionar (add) um curso a seguinte tela será exibida, solicitando informações para o novo curso:

![Django Admin Site 3](https://github.com/nunescarol/es3/blob/main/imagens/admin insert curso.png?raw=true)

Ao salvar uma lista de cursos será exibida, nesta lista podemos escolher qualquer curso para editar, veja que podemos editar os campos como também excluir o curso:

![Django Admin Site 4](https://github.com/nunescarol/es3/blob/main/imagens/admin update curso.png?raw=true)

Na próxima seção criar uma API REST para fornecer nossos cursos na web: [6. API REST](https://github.com/nunescarol/es3/tree/main/2.%20django/6.%20API%20REST).
