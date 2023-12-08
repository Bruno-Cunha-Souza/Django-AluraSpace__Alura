from django.contrib import admin

from galeria.models import Fotografia

class ListandoFotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome")
    #Pesquisar pelo nome
    search_fields = ("nome",)
    #Filtrar por categoria
    list_filter = ("categoria",)
    #Pode publicar sem entrar no item
    list_editable = ("publicada",)
    #Numero de itens por pagina
    list_per_page = 10
    
# registrando o db Fotografia no admin do django
admin.site.register(Fotografia, ListandoFotografia)