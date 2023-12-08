from django.contrib import admin

from galeria.models import Fotografia

class ListandoFotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)


# registrando o db Fotografia no admin do django
admin.site.register(Fotografia, ListandoFotografia)