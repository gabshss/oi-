from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Genero, Livro, Reserva


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    list_filter = ('uf',)
    search_fields = ('nome',)

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1 
    
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome',)
    inlines = [LivroInline]

admin.site.register(Livro)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site', 'cidade')
    list_filter = ('cidade',)
    search_fields = ('nome',)


@admin.register(Leitor)
class LeitorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf')
    search_fields = ('nome', 'cpf')


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('livro', 'leitor', 'data_reserva', 'status')
    list_filter = ('status', 'data_reserva')



