from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('api/v1/', include('cursos.urls')),
    path('meuapp/', include('meu_app1.urls')),
    path('admin/', admin.site.urls),
]