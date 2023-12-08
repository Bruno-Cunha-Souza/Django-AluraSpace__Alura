from django.contrib import admin

from galeria.models import Fotografia

class ListandoFotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id", "nome")
    #Pesquisar pelo nome
    search_fields = ("nome",)
    #Filtrar por categoria
    list_filter = ("categoria",)
    
# registrando o db Fotografia no admin do django
admin.site.register(Fotografia, ListandoFotografia)