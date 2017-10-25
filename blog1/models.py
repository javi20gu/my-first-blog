from django.db import models
from django.utils import timezone

class Post(models.Model):
	autor = models.ForeignKey('auth.User')
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	dia_creado = models.DateTimeField(default=timezone.now)
	dia_publicado = models.DateTimeField(blank=True,null=True)

	def publicar(self):
		self.dia_publicado = timezone.now()
		self.save()
	
	def __str__(self):
		return self.titulo