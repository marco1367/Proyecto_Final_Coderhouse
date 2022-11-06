from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Messages(models.Model):
    
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="destinatario")
    mensaje = models.CharField(max_length=100)
        
    def __str__(self):
        return f"de: {self.remitente} - para: {self.destinatario} / mensaje: {self.mensaje} "