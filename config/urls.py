"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('livros/', livros, name='livros'),
    path('livros/delete/<int:id>/', DeleteLivroView.as_view(), name='delete_livro'),

    path('autor/', autor, name='autor'),
    path('cidade/', cidade, name='cidade'),
    path('editora/', editora, name='editora'),
    path('reserva/', reserva, name='reserva'),
    path('leitor/', leitor, name='leitor'),
    path('genero/', genero, name='genero'),

    path('editar/<int:id>/', EditarLivroView.as_view(), name='editar'),
]