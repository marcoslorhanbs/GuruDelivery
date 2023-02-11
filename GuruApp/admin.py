from django.contrib import admin

# Register your models here.
from GuruApp.models import user, Hamburguer

admin.site.register(user)
admin.site.register(Hamburguer)