from django.db import models

# Create your models here.

class Produto(models.Model):
  codigo = models.CharField (
    null = True,
    help_text = "Código do produto",
    unique = True,
    max_length = 100,
  )
  nome_produto = models.CharField(
    null = True,
    max_length = 100,)
  preco = models.FloatField()
  avaliacao_produto = models.CharField(
    max_length = 100
  ) 

  def save(self, *args, **kwargs):
    if self.pk is Nome:
      self.setor = self.name.upper()

    super(Produto, self).save(*args, **kwargs)