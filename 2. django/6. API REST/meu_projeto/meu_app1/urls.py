from django.urls import path

from . import views

app_name = 'meu_app1'

urlpatterns = [
    path('', views.index, name='index'),
    path('segunda/', views.segunda, name='segunda-pagina'),
]