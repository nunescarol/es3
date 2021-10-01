from django.urls import path

from rest_framework.routers import SimpleRouter

from cursos.views import (CursoAPIView,
                          CursosAPIView,
                         )

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
]