from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View

from .models import Livro, Autor, Cidade, Editora, Reserva, Leitor, Genero
from .forms import LivroForm


def index(request):
    livros = Livro.objects.all().order_by('nome')[:5]
    return render(request, 'index.html', {'livros': livros})


def livros(request):
    lista_livros = Livro.objects.all().order_by('nome')
    return render(request, 'livros.html', {'livros': lista_livros})


def autor(request):
    lista_autores = Autor.objects.all().order_by('nome')
    return render(request, 'autor.html', {'autores': lista_autores})


def cidade(request):
    lista_cidades = Cidade.objects.all().order_by('nome')
    return render(request, 'cidade.html', {'cidades': lista_cidades})


def editora(request):
    lista_editoras = Editora.objects.all().order_by('nome')
    return render(request, 'editora.html', {'editoras': lista_editoras})


def reserva(request):
    lista_reservas = Reserva.objects.all().order_by('-data_reserva')
    return render(request, 'reserva.html', {'reservas': lista_reservas})


def leitor(request):
    lista_leitores = Leitor.objects.all().order_by('nome')
    return render(request, 'leitor.html', {'leitores': lista_leitores})


def genero(request):
    lista_generos = Genero.objects.all().order_by('nome')
    return render(request, 'genero.html', {'generos': lista_generos})


class DeleteLivroView(View):
    def get(self, request, id, *args, **kwargs):
        livro = get_object_or_404(Livro, id=id)
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('livros')


class EditarLivroView(View):
    template_name = 'editar_livro.html'

    def get(self, request, id, *args, **kwargs):
        livro = get_object_or_404(Livro, id=id)
        form = LivroForm(instance=livro)
        return render(request, self.template_name, {
            'livro': livro,
            'form': form
        })

    def post(self, request, id, *args, **kwargs):
        livro = get_object_or_404(Livro, id=id)
        form = LivroForm(request.POST, instance=livro)

        if form.is_valid():
            form.save()
            messages.success(request, 'Livro atualizado com sucesso!')
            return redirect('editar', id=id)

        return render(request, self.template_name, {
            'livro': livro,
            'form': form
        })