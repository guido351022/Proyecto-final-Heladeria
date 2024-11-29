from django.db import models
from django.utils import timezone

class Sabor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)  # Nuevo campo para apellido
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'  # Muestra el nombre completo

class Helado(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    sabor = models.ForeignKey(Sabor, on_delete=models.CASCADE, related_name='helados')  # Relación con sabor

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido de {self.cliente.nombre} - {self.fecha}'


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Mensaje de {self.nombre} - {self.email}'