from django.db import models

# null=False --> Não pode ser nula
class Fotografia(models.Model):
    
    OPCOES_CATEGORIAS = [
        ("NEBULOSA", "nebulosa"), ("ESTRELA", "estrela"), ("GALAXIA", "galaxia"), ("PLANETA", "planeta")
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAS, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    
    # Retorna a string nome
    def __str__(self):
        return f"Fotografia {self.nome}"