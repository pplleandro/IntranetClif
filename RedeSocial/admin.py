from django.contrib import admin

# Register your models here.
from RedeSocial.models import Rede, Banner, Banner2, Banner3, Institucional, Aniversario

admin.site.register(Rede)
admin.site.register(Banner)
admin.site.register(Banner2)
admin.site.register(Banner3)
admin.site.register(Institucional)
admin.site.register(Aniversario)