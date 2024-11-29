from django.contrib import admin
from .models import Cliente, Helado, Pedido, Sabor

admin.site.register(Cliente)
admin.site.register(Sabor)
admin.site.register(Helado)
admin.site.register(Pedido)
