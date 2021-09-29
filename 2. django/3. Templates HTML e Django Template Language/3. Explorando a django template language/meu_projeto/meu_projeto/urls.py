from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('meuapp/', include('meu_app1.urls')),
    path('admin/', admin.site.urls),
]