from django.contrib import admin
from eleccion.models import Circunscripcion, Mesa, Partido, Resultado

# Register your models here.
admin.site.register(Circunscripcion)
admin.site.register(Mesa)
admin.site.register(Partido)
admin.site.register(Resultado)