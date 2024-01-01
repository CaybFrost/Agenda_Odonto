from django.db import models


class Todo(models.Model):
    nome = models.CharField(max_length=100 , null=False, blank=False)
    data_consulta = models.DateField(null=False, blank=False)
    hora_consulta = models.TimeField(null=True)
    dentista = models.CharField(max_length=100 , null=False, blank=False)

    class Meta:
        ordering = ['data_consulta']