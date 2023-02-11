from django.contrib import admin

# Register your models here.
from GuruApp.models import user, Hamburguer

admin.site.register(user)
#admin.site.register(Hamburguer)

@admin.register(Hamburguer)
class HamburguerAdmin(admin.ModelAdmin):
    list_display = ("productName", "productLine")
    list_filter = ("productPrice", )
    search_fields = ("productName__startswith", )
